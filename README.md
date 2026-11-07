# Taxis de l'Essonne : site vitrine

Site vitrine d'un artisan taxi basé à Athis-Mons (Essonne, 91) : taxi privé, transport médical conventionné CPAM et transport PMR (Handy Essonne).

**Adresse du site** : https://taxisdelessonne.fr/ (l'adresse avec www redirige vers celle-ci)

- **Nom de domaine** : chez OVH (3 ans, renouvellement novembre 2029), propriétaire BOAAS
- **Hébergement** : Netlify (gratuit), relié à ce dépôt GitHub : chaque `git push` met le site à jour. Seul le dossier `site/` est publié.
- **Adresse Netlify** : https://taxisdelessonne.netlify.app
- **DNS chez OVH** : A (sous-domaine vide) → `75.2.60.5` ; CNAME `www` → `taxisdelessonne.netlify.app.`

## Structure

```
├── site/                   Le site publié (et rien d'autre)
│   ├── index.html              page unique
│   ├── mentions-legales.html   mentions légales (obligatoires)
│   ├── 404.html                page « introuvable »
│   ├── robots.txt, sitemap.xml indications pour Google
│   ├── _headers                en-têtes de sécurité et de cache (Netlify / Cloudflare Pages)
│   └── assets/
│       ├── logo/               logo et icônes
│       │   ├── logo.png            logo complet (fond clair)
│       │   ├── logo-blanc.png      logo complet (fond foncé, pied de page)
│       │   ├── logo-icone.png      le van seul
│       │   ├── favicon.png         icône de l'onglet du navigateur
│       │   └── apple-touch-icon.png icône d'écran d'accueil iPhone
│       └── photos/             photos du véhicule retouchées (plaque masquée)
├── netlify.toml            Réglage Netlify : publier le dossier site/
├── design/                 Fichiers de travail (jamais publiés)
│   ├── logo-source.jpg         logo d'origine généré par IA
│   ├── detourer-logo.py        génère site/assets/logo/ à partir du logo d'origine
│   └── prompts-logo.md         prompts utilisés pour générer le logo
└── client/                 Documents privés du client (exclus de Git)
```

## Mettre à jour le site

Après une modification :

```
git add -A
git commit -m "Description du changement"
git push
```

L'hébergeur met le site à jour tout seul en moins d'une minute.

## Changer le logo

Remplacer `design/logo-source.jpg` par le nouveau logo (fond clair uni), puis lancer :

```
python design/detourer-logo.py design/logo-source.jpg site/assets/logo
```

Le script retire le fond, recadre le logo et le recolore aux couleurs du site : bleu `#0A2463`, rouge `#E1000F`, blanc. Il régénère aussi les icônes. Il nécessite Python avec `numpy` et `Pillow`.

## Charte

| | |
|---|---|
| Police | Bricolage Grotesque (Google Fonts) |
| Bleu marine | `#0A2463` |
| Bleu vif | `#1D4ED8` |
| Blanc | `#FFFFFF` |
| Rouge | `#E1000F` |

## Reste à faire

- [x] Photos du véhicule et de la rampe PMR (retouchées, plaque masquée ; originaux dans `client/photos/`)
- [x] Badge « Taxi conventionné CPAM » (badge maison : le logo officiel de l'Assurance Maladie est une marque protégée)
- [x] SIRET et page de mentions légales (`site/mentions-legales.html`)
- [x] Nom de domaine taxisdelessonne.fr (OVH), https actif
- [x] Balise `noindex` retirée : site ouvert à Google (7/11/2026)
- [ ] Quitter Netlify (badge « Powered by Netlify » imposé en compte gratuit) pour Cloudflare Pages, puis mettre à jour l'hébergeur dans les mentions légales
- [ ] Passer le propriétaire du domaine au nom de BOAAS (OVH → Changer de propriétaire)
- [ ] Mentions légales : ajouter le capital social, confirmer le RCS et l'adresse du siège (Kbis)
- [ ] Faire confirmer par le client l'arrimage du fauteuil et le type de licence (espèces : confirmé ; rampe : visible sur les photos)
- [ ] Désactiver l'ancien aperçu GitHub Pages
- [ ] Déclarer le site dans Google Search Console et créer la fiche Google Maps
- [ ] Logo en vectoriel (SVG) pour l'impression
- [ ] Remplacer le CDN Tailwind par une feuille de style compilée
