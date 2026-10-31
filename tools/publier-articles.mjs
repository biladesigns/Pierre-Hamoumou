// Prepare la diffusion des articles sur LinkedIn.
//
// A lancer apres chaque ajout ou modification d'article dans articles/ :
//   cd tools && npm install   (une seule fois)
//   node tools/publier-articles.mjs
//
// Pour chaque article :
//  1. genere l'image d'apercu LinkedIn og/<slug>.png (1200 x 627, polices du site)
//     si elle n'existe pas encore (--force pour tout regenerer) ;
//  2. fait pointer og:image de l'article vers cette image ;
//  3. reconstruit le flux articles/feed.xml, que Zapier surveille pour publier
//     un post LinkedIn a chaque nouvel article.
//
// Texte du post : la balise <meta name="linkedin-post" content="..."> de l'article
// si elle existe, sinon sa meta description.

import fs from 'node:fs'
import path from 'node:path'
import { createRequire } from 'node:module'

const ROOT = path.resolve(path.dirname(new URL(import.meta.url).pathname), '..')
const require = createRequire(path.join(ROOT, 'tools') + '/')
const BASE = 'https://pierrehamoumou-avocat.fr'
const CHROME = process.env.CHROME_PATH || '/Applications/Google Chrome.app/Contents/MacOS/Google Chrome'
const FORCE = process.argv.includes('--force')

const esc = s => s.replace(/&/g, '&amp;').replace(/</g, '&lt;').replace(/>/g, '&gt;').replace(/"/g, '&quot;')
const unesc = s => s.replace(/&quot;/g, '"').replace(/&#39;/g, "'").replace(/&lt;/g, '<').replace(/&gt;/g, '>').replace(/&amp;/g, '&')
const meta = (html, re) => { const m = html.match(re); return m ? unesc(m[1]) : null }

// --- 1. Lecture des articles -------------------------------------------------
const dir = path.join(ROOT, 'articles')
const articles = fs.readdirSync(dir)
  .filter(f => f.endsWith('.html') && f !== 'index.html')
  .map(f => {
    const html = fs.readFileSync(path.join(dir, f), 'utf8')
    const ld = JSON.parse(html.match(/<script type="application\/ld\+json">([\s\S]*?)<\/script>/)[1])
    const art = (ld['@graph'] || [ld]).find(n => n['@type'] === 'Article')
    if (!art) throw new Error(`${f} : pas de schema Article`)
    const slug = f.replace(/\.html$/, '')
    return {
      file: f, slug,
      url: `${BASE}/articles/${f}`,
      titre: art.headline,
      date: art.datePublished,
      description: meta(html, /<meta name="description" content="([^"]*)"/),
      post: meta(html, /<meta name="linkedin-post" content="([^"]*)"/),
      rubrique: meta(html, /<span class="inline-block[^"]*">\s*([^<]+?)\s*<\/span>/) || 'Actualités',
    }
  })
  .sort((a, b) => b.date.localeCompare(a.date))

// --- 2. Images d'apercu ------------------------------------------------------
const ogDir = path.join(ROOT, 'og')
fs.mkdirSync(ogDir, { recursive: true })
const aGenerer = articles.filter(a => FORCE || !fs.existsSync(path.join(ogDir, a.slug + '.png')))

if (aGenerer.length) {
  const puppeteer = require('puppeteer-core')
  const font = f => fs.readFileSync(path.join(ROOT, 'fonts', f)).toString('base64')
  const fonts = `
    @font-face{font-family:'Cormorant';font-weight:300 700;src:url(data:font/woff2;base64,${font('cormorant-garamond.woff2')}) format('woff2')}
    @font-face{font-family:'DM';font-weight:100 1000;src:url(data:font/woff2;base64,${font('dm-sans.woff2')}) format('woff2')}`
  const browser = await puppeteer.launch({ executablePath: CHROME, headless: true })
  const page = await browser.newPage()
  await page.setViewport({ width: 1200, height: 627, deviceScaleFactor: 1 })
  for (const a of aGenerer) {
    await page.setContent(`<!doctype html><html lang="fr"><meta charset="utf-8"><style>${fonts}
      *{box-sizing:border-box;margin:0}
      body{width:1200px;height:627px;background:#2C6E68;color:#fff;font-family:'DM';overflow:hidden}
      .c{position:absolute;inset:0;padding:68px 84px 64px;display:flex;flex-direction:column}
      .k{font-weight:500;font-size:19px;letter-spacing:.16em;text-transform:uppercase;color:#AED18E}
      h1{font-family:'Cormorant';font-weight:500;font-size:64px;line-height:1.1;margin-top:34px;max-width:1000px;
         font-variant-numeric:lining-nums;letter-spacing:-.005em;hyphens:none}
      .s{margin-top:auto;display:flex;align-items:center;gap:22px}
      .r{width:56px;height:2px;background:#AED18E}
      .n{font-family:'Cormorant';font-weight:500;font-size:31px;line-height:1}
      .q{font-size:18px;color:rgba(255,255,255,.75);margin-top:6px}
      </style><div class="c"><div class="k">${esc(a.rubrique)}</div><h1 id="t">${esc(a.titre)}</h1>
      <div class="s"><div class="r"></div><div><div class="n">Maître Pierre Hamoumou</div>
      <div class="q">Avocat au Barreau de Lyon · Droit de la sécurité sociale</div></div></div></div></html>`)
    await page.evaluate(async () => {
      await document.fonts.ready
      // Le titre tient en 4 lignes au plus : on reduit la taille si besoin.
      const t = document.getElementById('t')
      let size = 64
      while (t.getBoundingClientRect().height > size * 1.1 * 4 + 2 && size > 40) { size -= 2; t.style.fontSize = size + 'px' }
    })
    await page.screenshot({ path: path.join(ogDir, a.slug + '.png') })
    console.log('image   og/' + a.slug + '.png')
  }
  await browser.close()
}

// --- 3. og:image et lien vers le flux dans chaque article --------------------
const FEED_LINK = '<link rel="alternate" type="application/rss+xml" title="Actualités du Cabinet Hamoumou" href="/articles/feed.xml">'
for (const a of articles) {
  const p = path.join(dir, a.file)
  let html = fs.readFileSync(p, 'utf8')
  const avant = html
  const img = `${BASE}/og/${a.slug}.png`
  html = html.replace(/<meta property="og:image" content="[^"]*">(\n<meta property="og:image:(width|height|alt)" content="[^"]*">)*/,
    `<meta property="og:image" content="${img}">\n<meta property="og:image:width" content="1200">\n<meta property="og:image:height" content="627">\n<meta property="og:image:alt" content="${esc(a.titre)}">`)
  if (!html.includes('application/rss+xml')) html = html.replace('<link rel="canonical"', FEED_LINK + '\n<link rel="canonical"')
  if (html !== avant) { fs.writeFileSync(p, html); console.log('maj     articles/' + a.file) }
}
const idx = path.join(dir, 'index.html')
let ih = fs.readFileSync(idx, 'utf8')
if (!ih.includes('application/rss+xml')) { fs.writeFileSync(idx, ih.replace('<link rel="canonical"', FEED_LINK + '\n<link rel="canonical"')); console.log('maj     articles/index.html') }

// --- 4. Flux RSS ------------------------------------------------------------
const rfc822 = d => new Date(d + 'T08:00:00+01:00').toUTCString()
const items = articles.map(a => {
  const png = path.join(ogDir, a.slug + '.png')
  return `    <item>
      <title>${esc(a.titre)}</title>
      <link>${a.url}</link>
      <guid isPermaLink="true">${a.url}</guid>
      <pubDate>${rfc822(a.date)}</pubDate>
      <description>${esc(a.post || a.description || '')}</description>
      <enclosure url="${BASE}/og/${a.slug}.png" length="${fs.statSync(png).size}" type="image/png"/>
    </item>`
}).join('\n')
const feed = `<?xml version="1.0" encoding="UTF-8"?>
<rss version="2.0" xmlns:atom="http://www.w3.org/2005/Atom">
  <channel>
    <title>Actualités du Cabinet Maître Pierre Hamoumou</title>
    <link>${BASE}/articles/</link>
    <atom:link href="${BASE}/articles/feed.xml" rel="self" type="application/rss+xml"/>
    <description>Analyses de jurisprudence et de réglementation en droit de la sécurité sociale et en contentieux URSSAF, par Maître Pierre Hamoumou, avocat au Barreau de Lyon.</description>
    <language>fr-FR</language>
    <lastBuildDate>${rfc822(articles[0].date)}</lastBuildDate>
${items}
  </channel>
</rss>
`
fs.writeFileSync(path.join(dir, 'feed.xml'), feed)
console.log(`flux    articles/feed.xml (${articles.length} articles)`)
const sansPost = articles.filter(a => !a.post).map(a => a.file)
if (sansPost.length) console.log('note    sans <meta name="linkedin-post"> (la meta description servira de texte) : ' + sansPost.join(', '))
