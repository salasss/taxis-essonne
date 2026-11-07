# Taxis de l'Essonne : site vitrine

Site vitrine d'un artisan taxi basé à Athis-Mons (Essonne, 91) : taxi privé, transport médical conventionné CPAM et transport PMR (Handy Essonne).

**Adresse du site** : https://www.taxisdelessonne.fr/ (le nom de domaine sans www redirige vers celle-ci)

- **Nom de domaine** : chez OVH (3 ans, renouvellement novembre 2029), propriétaire BOAAS
- **Hébergement** : Netlify (gratuit), relié à ce dépôt GitHub : chaque `git push` met le site à jour
- **Adresse Netlify** : https://candid-semifreddo-9abb3f.netlify.app

## Structure

```
├── index.html              Le site (page unique)
├── mentions-legales.html   Mentions légales (obligatoires)
├── 404.html                Page « introuvable »
├── robots.txt, sitemap.xml Indications pour Google
├── netlify.toml            Réglages Netlify (sécurité, fichiers de travail non publiés)
├── assets/
│   ├── logo/               Logo et icônes utilisés par le site
│   │   ├── logo.png            logo complet (fond clair)
│   │   ├── logo-blanc.png      logo complet (fond foncé, pied de page)
│   │   ├── logo-icone.png      le van seul
│   │   ├── favicon.png         icône de l'onglet du navigateur
│   │   └── apple-touch-icon.png icône d'écran d'accueil iPhone
│   └── photos/             Photos du véhicule retouchées (plaque masquée)
├── design/                 Fichiers de travail (bloqués sur le site par netlify.toml)
│   ├── logo-source.jpg         logo d'origine généré par IA
│   ├── detourer-logo.py        génère assets/logo/ à partir du logo d'origine
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

Netlify met le site à jour tout seul en moins d'une minute.

## Changer le logo

Remplacer `design/logo-source.jpg` par le nouveau logo (fond clair uni), puis lancer :

```
python design/detourer-logo.py design/logo-source.jpg assets/logo
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

## Reste à faire avant la mise en ligne définitive

- [x] Photos du véhicule et de la rampe PMR (retouchées, plaque masquée ; originaux dans `client/photos/`)
- [x] Badge « Taxi conventionné CPAM » (badge maison : le logo officiel de l'Assurance Maladie est une marque protégée)
- [ ] Faire confirmer par le client l'arrimage du fauteuil et le type de licence (espèces : confirmé ; rampe : visible sur les photos)
- [x] SIRET et page de mentions légales (`mentions-legales.html`)
- [ ] Mentions légales : ajouter le capital social, confirmer le RCS et l'adresse du siège (Kbis)
- [ ] Mettre à jour l'hébergeur dans les mentions légales en cas de changement
- [ ] Nom de domaine (mettre à jour la balise `canonical`)
- [ ] Retirer la balise `noindex` de `index.html`
- [ ] Logo en vectoriel (SVG) pour l'impression
- [ ] Remplacer le CDN Tailwind par une feuille de style compilée
