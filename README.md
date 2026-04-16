# Blocks Master / SiteMaster

Bienvenue dans la documentation officielle de la suite **Blocks Master**.

Cette suite outillegere et entierement native a WordPress (Custom Post Types et Gutenberg) se compose de deux modules interactifs :

1. **Blocks Master Lab** : Un environnement de developpement integre (IDE) pour concevoir vos propres composants visuels (blocs) directement en HTML/PHP avec le support natif de **Tailwind CSS**.
2. **SiteMaster** : Un gestionnaire de structure de donnees robuste permettant de creer des "Groupes" (Collections), d'y ajouter des champs personnalises complets, et d'editer vos enregistrements via une interface standard couplee a Gutenberg.

---

## Pourquoi ce plugin ?

- **Fini les usines a gaz** : Pas de constructeurs lents ou de stockage opaque. Vos donnees sont stockees sous forme de *Custom Post Types* natifs et de `post_meta`.
- **Visuel de developpement immediat** : Codez en direct avec vos classes Tailwind pre-configurees (prefixees par `tw-`) sans jamais rouvrir votre IDE local ni relancer de build.
- **Routage Naturel** : Definissez un "Chemin de listing" (ex: `/services`) et selectionnez une page modele. Tout visiteur se rendant sur `/services/nettoyage` verra votre interface dynamique avec les donnees correctes.

## Pre-requis
- **WordPress 6.0 ou superieur** avec l'editeur Gutenberg actif.
- Pas de base de donnees personnalisee requise (architecture 100% native).

---

> [!TIP]
> Naviguez dans le menu lateral pour apprendre a utiliser le Lab, creer vos premieres pages dynamiques, ou explorer l'API PHP `sm_get_current_*`.
