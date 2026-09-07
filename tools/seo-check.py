#!/usr/bin/env python3
"""Controle SEO du site — a lancer a chaque routine mensuelle.

Verifie :
  1. presence des fichiers SEO critiques
  2. balises par page (canonical, OG, H1 unique, JSON-LD)
  3. validite JSON des blocs JSON-LD
  4. coherence schema FAQ / contenu visible (exigence Google)
  5. coherence sitemap / pages reellement presentes

Usage : python3 tools/seo-check.py
"""
import re, json, glob, sys, os
import html as H

os.chdir(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
errors, warnings = [], []

def norm(s):
    """Normalise apostrophes et espaces pour comparer schema et contenu."""
    s = s.replace('’', "'").replace('‘', "'")
    s = s.replace(' ', ' ').replace(' ', ' ')
    return re.sub(r'\s+', ' ', s).strip()

def strip_tags(s):
    return norm(H.unescape(re.sub(r'<[^>]+>', ' ', s)))

print('=' * 62)
print('1. FICHIERS SEO CRITIQUES')
print('=' * 62)
for f in ['robots.txt', 'sitemap.xml', 'favicon.ico',
          'favicon-48.png', 'favicon-96.png', 'favicon-192.png',
          'apple-touch-icon.png']:
    if os.path.exists(f):
        print(f'  OK        {f:24} {os.path.getsize(f)} o')
    else:
        errors.append(f'fichier manquant : {f}')
        print(f'  MANQUANT  {f}')

print()
print('=' * 62)
print('2. BALISES PAR PAGE')
print('=' * 62)
print(f'  {"PAGE":<38}{"CANON":<7}{"OG":<5}{"H1":<5}{"LD"}')
def is_redirect_stub(path):
    return 'http-equiv="refresh"' in open(path, encoding='utf-8').read()

all_html = sorted(glob.glob('*.html') + glob.glob('*/index.html'))
stubs = [f for f in all_html if is_redirect_stub(f)]
pages = [f for f in all_html if f not in stubs]
if stubs:
    print(f'  ({len(stubs)} redirections ignorees : ' + ', '.join(s.split("/")[0] for s in stubs) + ')')
for f in pages:
    src = open(f, encoding='utf-8').read()
    canon = len(re.findall(r'rel="canonical"', src))
    og    = len(re.findall(r'property="og:', src))
    h1    = len(re.findall(r'<h1\b', src))
    ld    = len(re.findall(r'application/ld\+json', src))
    print(f'  {f:<38}{canon:<7}{og:<5}{h1:<5}{ld}')
    if canon != 1: errors.append(f'{f} : {canon} canonical (attendu 1)')
    if og < 5:     warnings.append(f'{f} : seulement {og} balises Open Graph')
    if h1 != 1:    errors.append(f'{f} : {h1} balises H1 (attendu 1)')

print()
print('=' * 62)
print('3. VALIDITE JSON-LD')
print('=' * 62)
faq_pages = 0
for f in pages:
    src = open(f, encoding='utf-8').read()
    for b in re.findall(r'<script type="application/ld\+json">(.*?)</script>', src, re.S):
        try:
            json.loads(b)
            print(f'  OK        {f}')
        except Exception as e:
            errors.append(f'{f} : JSON-LD invalide -> {e}')
            print(f'  INVALIDE  {f} -> {e}')

print()
print('=' * 62)
print('4. SCHEMA FAQ vs CONTENU VISIBLE')
print('=' * 62)
for f in pages:
    src = open(f, encoding='utf-8').read()
    blocks = re.findall(r'<script type="application/ld\+json">(.*?)</script>', src, re.S)
    if not blocks:
        continue
    body = strip_tags(re.sub(r'<script type="application/ld\+json">.*?</script>', '', src, flags=re.S))
    for b in blocks:
        try:
            data = json.loads(b)
        except Exception:
            continue
        for n in data.get('@graph', [data]):
            if n.get('@type') != 'FAQPage':
                continue
            faq_pages += 1
            for q in n.get('mainEntity', []):
                probe = norm(q['name'])[:45]
                if probe in body:
                    print(f'  OK        {f} : {q["name"][:48]}')
                else:
                    errors.append(f'{f} : question du schema absente de la page -> {q["name"][:60]}')
                    print(f'  ABSENTE   {f} : {q["name"][:48]}')
if faq_pages == 0:
    print('  (aucun FAQPage)')

print()
print('=' * 62)
print('5. SITEMAP')
print('=' * 62)
sm = open('sitemap.xml', encoding='utf-8').read()
listed = set(re.findall(r'<loc>https://pierrehamoumou-avocat\.fr/([^<]*)</loc>', sm))
listed.discard('')
def url_to_file(u):
    return (u.rstrip('/') + '/index.html') if u.endswith('/') else u
listed = {url_to_file(u) for u in listed}
on_disk = set(pages) - {'index.html'}
for miss in sorted(on_disk - listed):
    warnings.append(f'page absente du sitemap : {miss}')
    print(f'  ABSENTE DU SITEMAP  {miss}')
for ghost in sorted(listed - on_disk):
    errors.append(f'sitemap : URL sans fichier -> {ghost}')
    print(f'  URL FANTOME         {ghost}')
if not (on_disk - listed) and not (listed - on_disk):
    print(f'  OK        {len(listed) + 1} URL, toutes correspondent a un fichier')

print()
print('=' * 62)
print('6. CHAMPS A COMPLETER')
print('=' * 62)
todo = 0
for f in pages:
    n = open(f, encoding='utf-8').read().count('A COMPLETER') + open(f, encoding='utf-8').read().count('\u00c0 COMPL\u00c9TER')
    if n:
        todo += n
        warnings.append(f'{f} : {n} champ(s) a completer avant mise en ligne')
        print(f'  {n} champ(s)  {f}')
if not todo:
    print('  aucun')

print()
print('=' * 62)
if errors:
    print(f'ERREURS ({len(errors)})')
    for e in errors:
        print('  -', e)
if warnings:
    print(f'AVERTISSEMENTS ({len(warnings)})')
    for w in warnings:
        print('  -', w)
if not errors and not warnings:
    print('AUCUN PROBLEME DETECTE')
print('=' * 62)
sys.exit(1 if errors else 0)
