# Taxis de l'Essonne : site vitrine

Site vitrine d'un artisan taxi basé à Athis-Mons (Essonne, 91) : taxi privé, transport médical conventionné CPAM et transport PMR (Handy Essonne).

**Aperçu en ligne** : https://salasss.github.io/taxis-essonne/
C'est une version de travail, non référencée par Google tant que le client ne l'a pas validée.

## Structure

```
├── index.html              Le site (page unique, publiée par GitHub Pages)
├── assets/
│   ├── logo/               Logo et icônes utilisés par le site
│   │   ├── logo.png            logo complet (fond clair)
│   │   ├── logo-blanc.png      logo complet (fond foncé, pied de page)
│   │   ├── logo-icone.png      le van seul
│   │   ├── favicon.png         icône de l'onglet du navigateur
│   │   └── apple-touch-icon.png icône d'écran d'accueil iPhone
│   └── photos/             Photos du véhicule (à fournir par le client)
├── design/                 Fichiers de travail (non utilisés par le site)
│   ├── logo-source.jpg         logo d'origine généré par IA
│   ├── detourer-logo.py        génère assets/logo/ à partir du logo d'origine
│   └── prompts-logo.md         prompts utilisés pour générer le logo
└── client/                 Documents privés du client (exclus de Git)
```

## Mettre à jour l'aperçu

Après une modification :

```
git add -A
git commit -m "Description du changement"
git push
```

Le lien d'aperçu se met à jour tout seul en 1 à 2 minutes.

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

- [ ] Photos du véhicule et de la rampe PMR : originaux reçus (dans `client/`), à retoucher puis déposer dans `assets/photos/`
- [ ] Logo officiel de l'Assurance Maladie (fichier fourni par la CPAM)
- [ ] Faire confirmer par le client l'arrimage du fauteuil et le type de licence (espèces : confirmé ; rampe : visible sur les photos)
- [ ] SIRET et page de mentions légales (obligatoire)
- [ ] Nom de domaine (mettre à jour la balise `canonical`)
- [ ] Retirer la balise `noindex` de `index.html`
- [ ] Logo en vectoriel (SVG) pour l'impression
- [ ] Remplacer le CDN Tailwind par une feuille de style compilée
