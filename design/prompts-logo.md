# Prompts logo : Taxis de l'Essonne / Handy Essonne

Prompts à copier-coller dans un générateur d'images IA pour créer le logo du client.
Les prompts sont en anglais, car les générateurs donnent de meilleurs résultats ainsi. ChatGPT et Ideogram comprennent aussi le français.

---

## 1. Rappel de la marque

| Élément | Valeur |
|---|---|
| Marque principale | **Taxis de l'Essonne** (taxi privé + transport conventionné) |
| Sous-marque | **Handy Essonne** (transport PMR, fauteuil roulant) |
| Lieu | Athis-Mons, Essonne (91) |
| Bleu marine | `#0A2463` |
| Bleu vif | `#1D4ED8` |
| Blanc | `#FFFFFF` |
| Rouge | `#E1000F` |
| Police du site | Bricolage Grotesque, ExtraBold |
| Ton | Premium, moderne, rassurant, « French touch » |

**À éviter** : effet drapeau, damier de taxi, voiture réaliste ou style clip-art (une voiture stylisée en quelques traits, oui : voir les prompts 6 à 8), dégradés, 3D, ombres, logo de l'Assurance Maladie dans le logo (il est réglementé et doit rester à part).

---

## 2. Quel outil utiliser

- **ChatGPT (génération d'images)** ou **Ideogram** : les meilleurs pour écrire correctement le nom « Taxis de l'Essonne ». À utiliser pour les prompts 1, 4, 5 et 7.
- **Midjourney** : le plus esthétique, mais il écrit mal les textes. À utiliser pour le **symbole seul** (prompts 2, 3, 6 et 8) ; le nom s'ajoute ensuite dans Figma ou Canva avec la police Bricolage Grotesque.

> L'IA produit une image (PNG). Pour un vrai logo, il faudra le **redessiner en vectoriel (SVG)** dans Figma ou Illustrator, ou le vectoriser, avant de le livrer au client.

---

## 3. Les prompts

### Prompt 1 : Le « i » rouge (logotype, recommandé)

Idée : le point du « i » de *Taxis* devient rouge, comme le voyant lumineux d'un taxi. Simple, mémorable, cohérent avec le site.

```
Minimalist wordmark logo for a premium French taxi company. The text reads exactly "Taxis de l'Essonne" in a heavy modern grotesque sans-serif typeface (similar to Bricolage Grotesque ExtraBold), tight letter spacing, deep navy blue color #0A2463. The dot of the letter "i" in "Taxis" is a perfect red circle #E1000F, like the glowing roof light of a taxi. Below, in small wide-spaced uppercase letters: "PRIVÉ · CONVENTIONNÉ · PMR". Flat vector design, no gradient, no shadow, no 3D, plain white background #FFFFFF, centered, generous margins, luxury Swiss-style brand identity.
```

### Prompt 2 : Monogramme « E » (icône, favicon, réseaux sociaux)

Idée : reprend le monogramme provisoire du site (carré arrondi + E + point rouge).

```
Minimalist logo mark: a bold geometric capital letter "E" made of thick strokes with slightly rounded ends, in white #FFFFFF, centered inside a softly rounded square in deep navy blue #0A2463. A small red dot #E1000F sits in the top right corner of the square, like a taxi roof light. Flat vector, perfectly symmetrical, crisp edges, no gradient, no shadow, no 3D, plain white background, modern premium French brand, app icon style.
```

Paramètres Midjourney à ajouter à la fin :

```
--ar 1:1 --style raw --no gradient, shadow, 3d, photo, car, checkered pattern, text
```

### Prompt 3 : « De porte à porte » (symbole trajet)

Idée : une ligne continue forme un trajet qui dessine la lettre E et finit sur un point rouge (la destination).

```
Minimalist logo symbol: one single continuous bold line in deep navy #0A2463 that draws a winding road and subtly forms the capital letter "E", the line ends on a solid red dot #E1000F representing the destination. Geometric, thick uniform stroke, rounded line caps, flat vector, no gradient, no shadow, no 3D, plain white background #FFFFFF, centered, modern premium transport brand, Awwwards style.
```

Paramètres Midjourney :

```
--ar 1:1 --style raw --no gradient, shadow, 3d, photo, car, map, text
```

### Prompt 4 : Signature tricolore discrète (logotype + détail)

Idée : le bleu-blanc-rouge du client, traité comme une marque de luxe et non comme un drapeau.

```
Minimalist logo lockup for a premium French taxi company. The text reads exactly "Taxis de l'Essonne" in a heavy modern grotesque sans-serif, tight letter spacing, deep navy #0A2463. To the left of the text, a tiny signature mark made of two short horizontal bars: one blue #1D4ED8 and one red #E1000F, separated by an empty gap where the white background itself plays the role of the white stripe. Elegant, restrained, not a flag. Flat vector, no gradient, no shadow, plain white background #FFFFFF, centered, luxury brand identity.
```

### Prompt 5 : Sous-marque « Handy Essonne » (PMR)

Idée : même univers que la marque principale, avec un pictogramme d'accessibilité moderne, dans sa version dynamique où la personne est en mouvement.

```
Minimalist sub-brand logo for "Handy Essonne", an accessible taxi service for wheelchair users. A modern dynamic accessibility icon (a person in a wheelchair leaning forward, in motion) simplified into bold geometric shapes, white #FFFFFF, inside a softly rounded square in navy blue #1D4ED8, with a small red dot #E1000F in the top right corner. To the right, the text reads exactly "Handy Essonne" in a heavy modern grotesque sans-serif, deep navy #0A2463. Flat vector, friendly but premium, no gradient, no shadow, no 3D, plain white background, centered.
```

### Avec une voiture

Le véhicule du client est un monospace / van adapté PMR : il vaut mieux le représenter lui plutôt qu'une berline. Pour rester haut de gamme, la voiture doit être **stylisée en quelques traits**, jamais réaliste.

### Prompt 6 : La voiture en un seul trait (version voiture du prompt 3)

Idée : la route arrive, dessine la silhouette du van, puis repart vers un point rouge, la destination. C'est le « de porte à porte » en image.

```
Minimalist logo symbol: a modern minivan seen from the side, drawn with one single continuous bold line in deep navy #0A2463. The line starts as a flat road on the left, rises to draw the vehicle silhouette (roof, windows, two perfectly round wheels), then continues forward as a road and ends on a solid red dot #E1000F representing the destination. Thick uniform stroke, rounded line caps, geometric, flat vector, no gradient, no shadow, no 3D, plain white background #FFFFFF, centered, modern premium transport brand, Awwwards style.
```

Paramètres Midjourney :

```
--ar 1:1 --style raw --no gradient, shadow, 3d, photo, realistic, checkered pattern, text
```

### Prompt 7 : Le van et son voyant taxi (logo complet avec le nom)

Idée : une silhouette pleine et simple du van, avec le voyant taxi rouge sur le toit. On reconnaît tout de suite un taxi, sans damier.

```
Minimalist logo lockup for a premium French taxi company. On the left, a simplified side-view silhouette of a modern minivan in solid deep navy #0A2463, made of clean geometric shapes, windows cut out in white, two round wheels, and a small glowing red rounded light #E1000F on the roof like a taxi sign. On the right, the text reads exactly "Taxis de l'Essonne" in a heavy modern grotesque sans-serif (similar to Bricolage Grotesque ExtraBold), tight letter spacing, deep navy. Flat vector, no gradient, no shadow, no 3D, plain white background #FFFFFF, centered, generous margins, luxury Swiss-style brand identity.
```

### Prompt 8 : Handy Essonne, le van à rampe (sous-marque PMR)

Idée : le même van vu de dos, rampe dépliée, avec un pictogramme fauteuil qui monte. On comprend tout de suite que le véhicule est accessible.

```
Minimalist logo symbol for an accessible taxi service: a modern minivan seen from the rear three-quarter view, simplified into bold geometric shapes in navy blue #1D4ED8, rear door open with a ramp deployed to the ground, and a simplified dynamic wheelchair user icon in red #E1000F rolling up the ramp. Friendly but premium, thick clean shapes, flat vector, no gradient, no shadow, no 3D, plain white background #FFFFFF, centered, app icon style.
```

Paramètres Midjourney :

```
--ar 1:1 --style raw --no gradient, shadow, 3d, photo, realistic, text
```

---

## 4. Variantes à demander ensuite

Une fois la bonne piste trouvée, relancer le même prompt en ajoutant à la fin :

- **Version fond sombre** : `on a deep navy blue background #0A2463, logo in white`
- **Version une couleur** : `single color version, all navy #0A2463, no red`
- **Plusieurs propositions** : `show 4 variations on a grid`

---

## 5. Checklist avant de montrer au client

- [ ] Le nom est écrit **sans faute** (apostrophe et accents compris).
- [ ] Le logo reste lisible **en tout petit** (favicon de 32 px).
- [ ] Il fonctionne **en une seule couleur** et **sur fond sombre**.
- [ ] Il a été **redessiné en vectoriel (SVG)**.
- [ ] Il ne ressemble pas à une marque existante (vérifier sur la base des marques de l'INPI, data.inpi.fr).
- [ ] Le logo de l'Assurance Maladie n'apparaît **pas** dans le logo.
