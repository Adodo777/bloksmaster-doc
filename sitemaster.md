# SiteMaster : Modeles et Donnees

Le module **SiteMaster** gere toute l'infrastructure de donnees avancees.

## Creer un Groupe (Interface de Donnees)

1. Rendez-vous dans **Blocks Master Lab > Groupes de champs**.
2. Remplissez le nom de la collection (ex: "Services", "Projets", "Equipe").
3. Un groupe peut etre vu comme un type de contenu precis. Vous pourrez lui ajouter autant de champs personnalises que vous le souhaitez : Image, Texte long, Nombre, URL, etc.

> [!NOTE]
> Automatiquement, chaque fois qu'un champ est cree, il est lie a son element via le systeme standard WordPress (les Meta Box) et affiche dynamiquement dans Gutenberg.

## Creer un Modele (Gabarit dynamique)

La puissance de SiteMaster reside dans sa liaison des pages modeles.

1. Allez dans **Blocks Master Lab > Pages Modeles**.
2. Creez votre nouveau design de page entierement depuis l'editeur standard de WordPress.
3. Retournez dans les reglages de votre Groupe, puis assignez-lui cette **Page Modele**, ainsi qu'un **Chemin de listing** (ex: `services`).

## Explication du Routage

Lorsque SiteMaster detecte un chemin `/path-listing/mon-element`:
- Le systeme verifie que le groupe associe a `path-listing` correspond.
- Il verifie que `mon-element` existe bien dans ce groupe.
- Le plugin force alors WordPress a afficher la **Page Modele** de maniere globale en arriere-plan.
- Toutes les balises et developpements crees dans vos Blocs recupèrent les details de "*mon-element*" specifiquement pour ce visiteur !

## Securite Native

Tout est fonde sur **Custom Post Types** (CPT).
- Les Modeles sont des `$post_type = 'sm_template'`.
- Les Elements sont des `$post_type = 'sm_item'`.

Et bien que caches de maniere intempestive avec `show_in_menu = false` pour garder une zone de travail saine, ils restent modifiables par vos administrateurs via un controleur des requetes strict et securise par nonce.
