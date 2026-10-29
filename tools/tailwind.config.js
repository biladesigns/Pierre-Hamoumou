// Configuration de compilation du CSS du site (Tailwind v3, reglages par defaut).
// Compiler : npx tailwindcss@3.4.17 -c tools/tailwind.config.js -i tools/input.css -o tailwind.css --minify
// Puis remplacer ?v= dans les pages par les 8 premiers caracteres du md5 (seo-check.py le verifie).
module.exports = {
  content: ['./*.html', './*/*.html', './*.js'],
  theme: { extend: {} },
  plugins: [],
}
