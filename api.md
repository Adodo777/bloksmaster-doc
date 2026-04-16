# Reference API (PHP)

Lorsque vous concevez de nouveaux blocs sous **Blocks Master Lab**, une série de fonctions (`helpers`) vous a été préparée dans `includes/sm-db.php`.
Elles vous permettent d'aspirer la data depuis l'interface Gutenberg dans votre code HTML/PHP.

## Contexte Global

Toutes ces fonctions prennent en source `$GLOBALS['sm_current_term']`.
Vous n'avez pas besoin de spécifier un ID. Lors de l'affichage d'un Element via le listing, la page saura exactement que les requêtes se destinent à cet endroit précis.

## Les Helpers disponibles

### `sm_get_current_term_name()`
Retourne le **Titre** de l'élément en cours de lecture.
```php
<h1 class="tw-font-bold tw-text-xl">
    <?= sm_get_current_term_name() ?>
</h1>
```

### `sm_get_current_content()`
Retourne le contenu **Riche global de l'éditeur classique** généré par Gutenberg (images, textes, styles inclus).
```php
<div class="tw-prose">
    <?= sm_get_current_content() ?>
</div>
```

### `sm_get_current_value( $key )`
C'est la fonction reine du framework SiteMaster ! Elle vous donnera **la valeur rattachée à la clé spécifique de Meta Box**.

`$key` correspond exactement à ce qui a été auto-généré dans "Clé unique" lors de la configuration du champ dans "Groupes de champs".

```php
<div class="tw-flex tw-justify-between">
    <span>Tarification à partir de</span>
    <span class="tw-font-bold">
        <?= sm_get_current_value("prix_fixe") ?> €
    </span>
</div>
```

**Spécificité sur les images**
Un champ de type "Image" retourne nativement l'URL source de votre WordPress Media (upload). C'est pourquoi vous devez directement l'injecter au milieu d'un tag `<img src="...">` pour qu'il soit affiché à l'écran.

```php
<?php if (sm_get_current_value("photo_profil")) : ?>
    <img src="<?= sm_get_current_value("photo_profil") ?>" 
         class="tw-rounded-full tw-w-32 tw-h-32" />
<?php else: ?>
    <!-- Avatar par défaut de substitution -->
    <div class="tw-bg-gray-300 tw-rounded-full tw-w-32 tw-h-32"></div>
<?php endif; ?>
```

---

> [!CAUTION]
> N'utilisez pas de fonction d'echo basique avec ces variables d'environnement sur des valeurs non controlables par l'identite des webmasters, car elles ne sont pas pre-sanitized par la couche visuelle de `sm_get_current_value()`. Mettez un `esc_html()` autour si vous n'etes pas absolument sur.
