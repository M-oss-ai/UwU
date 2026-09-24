# UwU Script

UwU Script est un langage de programmation qui utilise **uniquement** des
emojis comme syntaxe. Il est fortement inspiré de Python.

> **Remarque sur ce document.** Ce fichier corrige le `README.md`
> d'origine et reste synchronisé avec l'interpréteur réel (`b.py` /
> `c.py`). Chaque exemple ci-dessous a été exécuté contre le code actuel,
> pas seulement déduit à la main — y compris les parties sur `🤙`
> (références de fonction) et les ajouts ponctuation/aléatoire/attributs
> fusionnés depuis `main`.

## Documentation

### Commentaires
Tout caractère qui n'est pas un emoji est ignoré par l'interpréteur.
Les espaces et les tabulations ne font pas partie de la syntaxe.

Si vous voulez utiliser des emojis dans un commentaire sans qu'ils soient
interprétés, commencez le commentaire par 😶. Tout emoji trouvé après 😶
sur cette ligne est ignoré.

#### Exemple
```
Les lettres sont ignorées 😶 ❤️🌷 ces emojis sont ignorés aussi 🌷❤️
```

### Hello World
Le premier programme traditionnel consiste à afficher "Hello world!"
dans la console. La fonction `print` est 🪶. Comme expliqué dans
« Fonctions » ci-dessous, un emoji de fonction ne s'exécute que si 🤙 le
suit directement.

```
🪶🤙♓🔱🛴🛴🅾️⚰️〰️🅾️®️🛴🆔📦
```
Résultat :

`hello world`

### Table de conversion

| Emoji | Valeur |
|----|-----|
| 🅰️ | `"a"` |
| 🅱️ | `"b"` |
| ©️ | `"c"` |
| 🆔 | `"d"` |
| 🔱 | `"e"` |
| 🎏 | `"f"` |
| 🐍 | `"g"` |
| ♓ | `"h"` |
| ℹ️ | `"i"` |
| 🎷 | `"j"` |
| 🔑 | `"k"` |
| 🛴 | `"l"` |
| Ⓜ️ | `"m"` |
| 🆖 | `"n"` |
| 🅾️ | `"o"` |
| 🅿️ | `"p"` |
| 🔍 | `"q"` |
| ®️ | `"r"` |
| 💲 | `"s"` |
| ™️ | `"t"` |
| ⛎ | `"u"` |
| ♈ | `"v"` |
| 〰️ | `"w"` |
| ❌ | `"x"` |
| 🩺 | `"y"` |
| 💤 | `"z"` |
| ⚰️ | `" "` |
| ❗ | `"!"` |
| ❓ | `"!"` (actuellement mappé sur `!` également, pas `?` — cela ressemble à un bug de l'interpréteur, documenté tel quel) |
| 🗨️ | `""` |
| ⤵️ | `"\n"` |
| 0️⃣ | `0` |
| 1️⃣ | `1` |
| 2️⃣ | `2` |
| 3️⃣ | `3` |
| 4️⃣ | `4` |
| 5️⃣ | `5` |
| 6️⃣ | `6` |
| 7️⃣ | `7` |
| 8️⃣ | `8` |
| 9️⃣ | `9` |
| 🟢 | `True` |
| 🔴 | `False` |
| 🕳️ | `None` |

Ponctuation et autres caractères spéciaux :

| Emoji | Valeur | Emoji | Valeur |
|----|-----|----|-----|
| 📞 | `"\"` | 🌘 | `"("` |
| 🚥 | `"-"` | 🌒 | `")"` |
| ✴️ | `"*"` | 🫳 | `"~"` |
| 🔘 | `"•"` | ✨ | `"+"` |
| 💵 | `"$"` | 🫐 | `":"` |
| 💶 | `"€"` | 🏒 | `";"` |
| ❤️ | `"♥"` | ⤴️ | `","` |
| 🦯 | `"/"` | 🍺 | `"'"` |
| 💴 | `"¥"` | 🍻 | `"\""` |
| 💷 | `"£"` | 📎 | `"&"` |
| 🥿 | `"_"` | 🎓 | `"^"` |
| ⚫️ | `"."` | 🐌 | `"@"` |
| 🚦 | `"\|"` | 💯 | `"%"` |
| #️⃣ | `"#"` | 👉 | `"{"` |
| ▶️ | `">"` | 👈 | `"}"` |
| ◀️ | `"<"` | 🫸 | `"["` |
| 🥓 | `"="` | 🫷 | `"]"` |

### Types
Vous pouvez obtenir le type d'une valeur avec 🏷️.

Pour convertir entre les types, utilisez :

| Emoji | Type |
|----|-------|
| 🔤 | `str` |
| 🔢 | `int` |
| ⚖️ | `bool` |
| 📋 | `list` |

Quand deux valeurs consécutives n'ont pas le même type, ou sont de type
`bool`/`None`, elles restent séparées et sont affichées avec un simple
espace entre elles (séparateur par défaut de `print` en Python) :

```
🪶🤙🅰️1️⃣📦
🪶🤙🟢🔴📦
🪶🤙🕳️🕳️📦
```
Résultat :

`a 1`

`True False`

`None None`

Quand deux valeurs consécutives sont toutes les deux de type `str` ou
`int`, elles sont fusionnées :

```
🪶🤙🅰️🅱️📦
🪶🤙0️⃣1️⃣0️⃣📦
```
Résultat :

`ab`

`10`

Vous pouvez utiliser ⛓️‍💥 pour forcer deux valeurs à rester séparées
(elles sont quand même affichées avec un simple espace entre elles) :

```
🪶🤙🅰️⛓️‍💥🅱️📦
🪶🤙0️⃣⛓️‍💥1️⃣0️⃣📦
```
Résultat :

`a b`

`0 10`

#### Liste
Utilisez 🌜🌛 pour créer une liste. Les listes ont une taille variable et
peuvent contenir d'autres listes. Afficher une liste utilise la
représentation propre à Python, donc les chaînes à l'intérieur sont
affichées avec des guillemets :

```
🪶🤙🌜🅰️⛓️‍💥🅱️0️⃣⛓️‍💥1️⃣0️⃣🟢🔴🕳️🌜🌛🌛📦
```
Résultat :

`['a', 'b', 0, 10, True, False, None, []]`

Utilisez 👀 pour indexer ou découper une liste — un index renvoie un
élément, deux index renvoient une tranche :

```
🪶🤙👀🤙🌜🅰️⛓️‍💥🅱️⛓️‍💥©️🌛1️⃣📦📦
```
Résultat :

`b`

### Fonctions

| Emoji | Fonction | Description |
|----|---------|-----------------|
| 🪶 | `print` | Identique à Python |
| 🔠 | `str.upper` | Identique à Python |
| 🏷️ | `type` | Identique à Python |
| 🔢 | `int` | Identique à Python |
| 🔤 | `str` | Identique à Python |
| ⚖️ | `bool` | Identique à Python |
| 📋 | `list` | Identique à Python |
| 🧮 | `len` | Identique à Python |
| 📏 | `range` | Identique à Python |
| 🔽 | `min` | Identique à Python |
| 🔼 | `max` | Identique à Python |
| 🗃️ | `sum` | Identique à Python |
| 🗂️ | `sorted` | Identique à Python |
| 🙅 | `not` | Inverse `True`/`False` |
| 🏁 | `end` | Termine le programme |
| 🔣 | `chr` | Identique à Python |
| 🔎 | `find` | Recherche dynamiquement une fonction native ou d'un module par son nom et renvoie une **référence** vers elle (ne l'appelle pas) |
| 🐙 | `find_attribut` | Recherche dynamiquement un attribut/une méthode par son nom sur une valeur et le renvoie — une référence si c'est appelable, la valeur brute sinon (ne l'appelle pas) |
| 🪞 | `list.copy` | Identique à Python |
| 📨 | `list.append` | Identique à Python |
| 🎞️ | `list.extend` | Identique à Python |
| 🗑️ | `list.remove` | Identique à Python |
| 🍿 | `list.pop` | Identique à Python |
| 👀 | `select_in_list` | Indexe (`l[i]`) ou découpe (`l[i:j]`) une liste |
| ⁉️ | `input` | Identique à Python |
| 🎲 | `random.randint` | Identique à Python |
| 🎰 | `random.random` | Identique à Python |
| 🎁 | `random.choice` | Identique à Python |
| ⏳ | `time.sleep` | Identique à Python |

**Un emoji de fonction ne s'exécute pas tout seul.** Le rencontrer
produit une **référence** vers cette fonction — voir « Références de
fonction » ci-dessous. Pour réellement l'appeler, placez 🤙 juste après
son emoji ; la fonction s'exécute alors avec ce qui suit, jusqu'au
prochain 📦, comme paramètres. Vous pouvez imbriquer des appels en
mettant 🤙 après chaque fonction à exécuter :

```
🪶🤙🅰️🔠🤙🅱️📦©️📦
```
Résultat :

`aBc`

**Au niveau supérieur (premier emoji d'une ligne), une fonction doit
être appelée.** La laisser comme référence non appelée sans rien qui la
consomme est une erreur — l'interpréteur considère qu'une instruction
qui ne fait que construire une référence inutilisée est une erreur de
frappe :

```
🪶🔠📦
```
Résultat :

`🚫 🤷 🪶 🤷 🤙 🫵 🖕` (erreur, le programme s'arrête)

Cette restriction ne s'applique qu'au début d'une ligne de premier
niveau. Une référence brute est parfaitement valide — et c'est tout
l'intérêt — quand elle est utilisée comme valeur : passée en argument,
affichée au sein d'un appel plus large, ou stockée dans une variable
(voir ci-dessous).

### Références de fonction
Rencontrer un emoji de fonction ne l'appelle pas — cela produit une
**référence** vers cette fonction, la fonction elle-même, non exécutée.
Utilisée comme donnée brute (par exemple affichée seule), une référence
s'affiche sous la forme `<fonction NOM>` :

```
🪶🤙🔠📦
```
Résultat :

`<fonction str.upper>`

Une référence n'est pas du même type qu'une chaîne de caractères, donc —
comme deux valeurs de types différents (voir « Types » plus haut) —
elle ne fusionne pas avec une chaîne adjacente ; elle est affichée avec
un espace à la place :

```
🪶🤙🔠Ⓜ️📦
```
Résultat :

`<fonction str.upper> m`

Pour réellement **appeler** une fonction, placez 🤙 juste *après* son
emoji — les valeurs qui suivent (jusqu'à 📦) deviennent ses paramètres :

```
🪶🤙Ⓜ️📦
```
Résultat :

`m`

Une référence peut aussi être stockée dans une variable et appelée plus
tard : `🤙` placé directement devant une variable qui contient une
référence l'appelle, avec ce qui suit la variable (jusqu'à 📦) comme
paramètres :

```
😀🪶
🪶🤙😀📦
```
Résultat :

`<fonction print>`

Ici, 😀 stocke la référence vers `print` (jamais appelée sur cette
ligne), et la seconde ligne affiche cette référence comme donnée brute.

```
😀🔠
🪶🤙😀🤙Ⓜ️📦
```
Résultat :

`M`

Ici, 😀 stocke la référence vers `str.upper`, et `🤙😀🤙Ⓜ️` l'appelle avec
`"m"` comme argument.

### Recherche dynamique (find / find_attribut)
🔎 (`find`) et 🐙 (`find_attribut`) récupèrent des fonctions et des
attributs qui n'ont pas leur propre emoji, par leur nom. Comme toute
fonction, elles ne renvoient jamais qu'une **référence** — elles
n'appellent jamais ce qu'elles trouvent. Pour utiliser le résultat,
stockez-le dans une variable et appelez la variable avec 🤙, exactement
comme dans « Références de fonction » ci-dessus.

`find` prend un nom (une chaîne) et le cherche d'abord parmi les
fonctions natives de Python :

```
😀🔎🤙🛴🔱🆖📦
🪶🤙😀🤙♓ℹ️📦📦
```
Résultat :

`2`

Ici, 😀 stocke une référence vers la fonction native `len` (recherchée
via la chaîne `"len"`, épelée lettre par lettre), et la seconde ligne
l'appelle sur `"hi"`.

Donnez un second nom à `find` — un module — pour atteindre une fonction
de n'importe quel module importable, pas seulement celles de la table :

```
🥑🔎🤙®️🅰️🆖🆔ℹ️🆖™️⛓️‍💥®️🅰️🆖🆔🅾️Ⓜ️📦
🪶🤙🥑🤙1️⃣⛓️‍💥1️⃣0️⃣📦📦
```
Résultat : un entier aléatoire entre `1` et `10` (`random.randint(1, 10)`).

Notez le ⛓️‍💥 entre les deux noms : sans lui, les chaînes adjacentes
`"randint"` et `"random"` fusionneraient en une seule (voir « Types »
plus haut).

`find_attribut` prend une valeur et un nom d'attribut, et renvoie ce que
renverrait `getattr` — une référence vers une méthode liée si
l'attribut est appelable, ou la valeur brute sinon :

```
💚🐙🤙♓ℹ️⛓️‍💥⛎🅿️🅿️🔱®️📦
🪶🤙💚🤙📦📦
```
Résultat :

`HI`

Ici, 💚 stocke une référence vers `"hi".upper`, et la seconde ligne
l'appelle sans argument.

```
🥝🐙🤙5️⃣⛓️‍💥®️🔱🅰️🛴📦
🪶🤙🥝📦
```
Résultat :

`5`

Ici, `"real"` nomme un attribut brut (non appelable) de `5`, donc 🥝
contient la valeur elle-même, pas une référence — l'afficher ne
nécessite pas de 🤙.

### Opérateurs

| Emoji | Python | Action |
|----|-------|------|
| ➕ | `+` | Addition |
| ➖ | `-` | Soustraction |
| ➗ | `/` | Division |
| 🪵 | `//` | Division entière |
| 🪙 | `%` | Modulo |
| *️⃣ | `*` | Multiplication |
| ⚡️ | `**` | Exponentiation |
| 🟥 | N/A | Racine (`avant ** (1 / après)`, ex. `après = 2` donne une racine carrée) |
| 🟰 | `==` | Égalité |
| 🚫 | `!=` | Différence |
| 💪 | `>` | Supérieur à |
| 🤏 | `<` | Inférieur à |
| 🤝 | `and` | ET logique |
| 🔀 | `or` | OU logique |
| 📥 | `in` | Test d'appartenance |
| 📤 | `not in` | Test de non-appartenance |
| ⚪️ | N/A | Assemble deux entiers en un nombre décimal : `float(str(avant) + "." + str(après))` |

Pour utiliser un opérateur, placez-le entre deux valeurs :

```
🪶🤙1️⃣➕2️⃣📦
🪶🤙🔴🤝🟢📦
```
Résultat :

`3`

`False`

L'opérateur d'assemblage décimal :

```
🪶🤙1️⃣⚪️2️⃣📦
```
Résultat :

`1.2`

Il n'y a pas de priorité d'opérateurs en UwU Script : toutes les
opérations sont évaluées de gauche à droite.

```
🪶🤙1️⃣➕2️⃣*️⃣3️⃣📦
```
Résultat :

`9`

À l'intérieur de 🌜🌛, si le contenu ne comporte que des opérateurs et
produit une seule valeur, ce n'est pas traité comme une liste mais comme
cette valeur seule. Cela permet de contrôler l'ordre d'évaluation :

```
🪶🤙🌜1️⃣➕🌜2️⃣*️⃣3️⃣🌛🌛📦
🪶🤙🌜🌜1️⃣➕2️⃣🌛🌛📦
🪶🤙🌜1️⃣➕2️⃣🅰️🌛📦
```
Résultat :

`7`

`[3]`

`[3, 'a']`

### Variables

UwU Script n'a pas d'affectation `=`. Il suffit de placer un emoji
inconnu (ou une variable existante) en début de ligne, suivi de sa
nouvelle valeur.

```
😀5️⃣0️⃣
🪶🤙😀📦

😀1️⃣0️⃣
🪶🤙😀📦
```
Résultat :

`50`

`10`

Vous pouvez assigner plusieurs variables sur la même ligne. Notez que,
selon la règle de fusion de « Types » ci-dessus, les afficher l'une
après l'autre sans rien entre elles fusionne les valeurs de même type —
utilisez ⛓️‍💥 dans l'appel `print` aussi si vous voulez qu'elles restent
séparées :

```
😀😛5️⃣⛓️‍💥0️⃣
🪶🤙😀⛓️‍💥😛📦

😀😇8️⃣⛓️‍💥3️⃣
🪶🤙😀⛓️‍💥😛⛓️‍💥😇📦
```
Résultat :

`5 0`

`8 0 3`

### If (condition)
Le mot-clé `if` est 🤔, une valeur booléenne doit le suivre directement.
Le bloc `if` continue jusqu'au prochain 🔚. Tout ce qui se trouve entre
🤔 et 🔚 n'est exécuté que si le booléen vaut `True`.

Assigner directement une variable au résultat d'une comparaison (ex.
`8️⃣💪2️⃣` seul sur la ligne) fait actuellement planter l'interpréteur —
un bug préexistant, sans rapport avec `🤙`. Entourer la comparaison de
🌜🌛 l'évite, donc les exemples ci-dessous font ainsi :

```
😀🌜8️⃣💪2️⃣🌛
🪶🤙😀📦

🤔😀
🪶🤙🔠🤙®️📦ℹ️🐍♓™️📦
🔚
```
Résultat :

`True`

`Right`

Pour exécuter quelque chose quand le booléen vaut `False`, utilisez 😌.
Ne mettez pas de 🔚 avant 😌 :

```
😀🌜8️⃣🤏2️⃣🌛
🪶🤙😀📦

🤔😀
🪶🤙🔠🤙®️📦ℹ️🐍♓™️📦

😌
🪶🤙🔠🤙🆖📦🅾️™️⚰️🔠🤙®️📦ℹ️🐍♓™️📦
🔚
```
Résultat :

`False`

`Not Right`

Vous pouvez utiliser 😏 pour vérifier une seconde condition si la
première vaut `False`, puis une troisième, et ainsi de suite :

```
🤔🔴
🪶🤙1️⃣⛓️‍💥🔠🤙®️📦ℹ️🐍♓™️📦

😏🔴
🪶🤙2️⃣⛓️‍💥🔠🤙®️📦ℹ️🐍♓™️📦

😏🟢
🪶🤙3️⃣⛓️‍💥🔠🤙®️📦ℹ️🐍♓™️📦

😌
🪶🤙🔠🤙🅰️📦🛴🛴⚰️🔠🤙🆖📦🅾️™️⚰️🔠🤙®️📦ℹ️🐍♓™️📦
🔚
```
Résultat :

`3 Right`

Vous pouvez aussi utiliser 😏 sans 😌 final :

```
🤔🔴
🪶🤙1️⃣⛓️‍💥🔠🤙®️📦ℹ️🐍♓™️📦

😏🟢
🪶🤙2️⃣⛓️‍💥🔠🤙®️📦ℹ️🐍♓™️📦
🔚
```
Résultat :

`2 Right`

### Feuille de route (pas encore implémenté)
Le code source de l'interpréteur (`b.py`) contient des commentaires
décrivant des fonctionnalités toujours prévues mais **pas encore
disponibles** :

- Boucles `for` (emoji prévu : 🌀)
- Boucles `while` (emoji prévu : 🤗)
- Fonctions définies par l'utilisateur avec paramètres et `return`
  (emojis prévus : 🌏, 🙏, 🔃 — 👉/👈 avaient aussi été envisagés pour
  ça, mais sont désormais réutilisés pour `{`/`}`)

Le support des nombres aléatoires, les appels façon objet/attribut, et
un grand nombre de caractères spéciaux figuraient auparavant ici comme
prévus — ils sont maintenant implémentés (🎲/🎰/🎁/⏳, 🐙, et la table de
ponctuation ci-dessus).

Ne comptez pas sur ce qu'il reste ci-dessus : les utiliser aujourd'hui
échouera, car ils ne sont pas encore enregistrés dans la table de
conversion.
