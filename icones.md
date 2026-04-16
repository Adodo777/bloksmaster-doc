# Utilisation des Icones (Lucide)

Le plugin embarque en local la librairie Open Source d'icones vectorielles **Lucide Icons** (version v1.8.0), pre-configuree pour se declencher sans aucune action externe.

## Principe

Tous vos developpements dans les blocs du Lab peuvent immediatement se servir des balises `<i>`. Le script interne se chargera de traquer le site Web ou vos modeles en temps reel pour generer les SVG a l'ecran.

## La Structure

Pour appeler une icone, il suffit d'utiliser la syntaxe standard des balises `i` avec un set d'attributs `data-lucide` :

```html
<i data-lucide="nom-de-licone"></i>
```

## Combiner Lucide et Tailwind

La puissance reelle de notre environnement vient lors du croisement de Lucide avec Tailwind CSS (`tw-`).

Etant donne que Lucide genere du SVG vectoriel sous la couverte, vous pouvez utiliser des classes de taille (`tw-w-X`, `tw-h-X`) et des couleurs de texte (`tw-text-`) standard pour en changer la disposition :

```html
<div class="tw-p-4 tw-rounded tw-bg-gray-100 tw-flex tw-items-center tw-gap-3">

    <!-- Une icone avec une couleur violette et une taille Moyenne -->
    <i data-lucide="sparkles" class="tw-w-6 tw-h-6 tw-text-purple-600"></i>
    
    <p class="tw-font-bold tw-text-gray-800">Ceci est mon titre eclairant</p>
    
</div>
```

## Catalogue des Icones

Pour connaitre les valeurs exactes a rentrer dans votre balise `data-lucide`, consultez directement le catalogue en ligne :

[Voir les 1400+ icones de Lucide](https://lucide.dev/icons)

> [!TIP]
> Lorsque vous cliquez sur une icone particuliere sur leur site, recopiez tout simplement le petit nom en minuscule qui apparait (exple: `arrow-right`).
