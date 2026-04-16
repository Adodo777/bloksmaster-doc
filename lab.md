# Le Lab Blocks Master

Le **Lab** est le cœur de developpement de votre environnement. Il vous permet de coder vos propres composants Gutenberg utilisables partout dans WordPress.

## Comment ça marche ?

A chaque fois que vous creez un "Bloc" via l'interface du Lab, le code que vous ecrivez est compile et enregistre physiquement sous forme de bloc natif Gutenberg. 
Plus besoin de React, de JSX ou d'outils complexes de compilation.

## Exemple d'utilisation

Dans l'onglet "Creer un bloc", rentrez les informations suivantes : 
1. **Nom** : "Mon Bloc de Test"
2. **Editeur de code** :

```html
<div class="tw-bg-gray-100 tw-p-8 tw-rounded-xl">
    <h2 class="tw-text-3xl tw-font-bold tw-text-indigo-600">
        Ceci est mon premier bloc
    </h2>
    <p class="tw-mt-4 tw-text-gray-700">
        Entierement genere via Blocks Master avec Tailwind CSS natif.
    </p>
</div>
```

Cliquez sur **Enregistrer le bloc**.
C'est tout. Le bloc est maintenant disponible dans Gutenberg sous le nom "Mon Bloc de Test" de n'importe quelle page.

## Support Tailwind CSS
Le plugin embarque en local la derniere version compilable de Tailwind CSS et la configure automatiquement.

> [!WARNING]
> Respect strict des prefix : Pour eviter tout type de conflit avec les classes de votre theme de base (ex: Astra, OceanWP), TOUTES les classes Tailwind de ce plugin sont obligatoirement prefixees par `tw-`.

* **Mauvais** : `class="bg-red-500 rounded p-4"`
* **Bon** : `class="tw-bg-red-500 tw-rounded tw-p-4"`
