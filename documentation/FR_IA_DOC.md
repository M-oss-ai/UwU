# UwU Script

UwU Script est un langage de programmation qui utilise **uniquement** des
emojis comme syntaxe. Il est fortement inspiré de Python.

> **Remarque sur ce document.** Ce fichier corrige le `README.md`
> d'origine : il corrige les fautes d'orthographe/grammaire et, surtout,
> réaligne chaque référence d'emoji avec ce qui est réellement implémenté
> dans `b.py` / `c.py`. La documentation d'origine n'était plus synchronisée
> avec l'interpréteur (elle référençait par exemple des emojis pour `e`,
> `f`, `g`, `t`, `v`, `x`, `y`, `!`, `\n`, `upper` et la fin de bloc `if`
> qui n'existent plus dans le code).

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
dans la console. La fonction `print` est 🪶.

```
🪶♓🔱🛴🛴🅾️⚰️〰️🅾️®️🛴🆔📦
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

Aucun emoji n'est actuellement associé au `"."` (point) dans l'interpréteur.

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
`bool`/`None`, elles restent séparées (jointes par `", "` à l'affichage) :

```
🪶🅰️1️⃣📦
🪶🟢🔴📦
🪶🕳️🕳️📦
```
Résultat :

`a 1`

`True False`

`None None`

Quand deux valeurs consécutives sont toutes les deux de type `str` ou
`int`, elles sont fusionnées :

```
🪶🅰️🅱️📦
🪶0️⃣1️⃣0️⃣📦
```
Résultat :

`ab`

`10`

Vous pouvez utiliser ⛓️‍💥 pour forcer deux valeurs à rester séparées
(jointes par `", "`) :

```
🪶🅰️⛓️‍💥🅱️📦
🪶0️⃣⛓️‍💥1️⃣0️⃣📦
```
Résultat :

`a b`

`0 10`

#### Liste
Utilisez 🌜🌛 pour créer une liste. Les listes ont une taille variable et
peuvent contenir d'autres listes.

```
🪶🌜🅰️⛓️‍💥🅱️0️⃣⛓️‍💥1️⃣0️⃣🟢🔴🕳️🌜🌛🌛📦
```
Résultat :

`[a, b, 0, 10, True, False, None, []]`

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
| 🔎 | `find` | Recherche et appelle dynamiquement une fonction native ou d'un module par son nom |
| 🪞 | `list.copy` | Identique à Python |
| 📨 | `list.append` | Identique à Python |
| 🎞️ | `list.extend` | Identique à Python |
| 🗑️ | `list.remove` | Identique à Python |
| 🍿 | `list.pop` | Identique à Python |
| ⁉️ | `input` | Identique à Python |

Utilisez 📦 pour marquer la fin des paramètres d'une fonction.
Vous pouvez imbriquer des appels de fonction :

```
🪶🅰️🔠🅱️📦©️📦
```
Résultat :

`aBc`

### Opérateurs

| Emoji | Python | Action |
|----|-------|------|
| ➕ | `+` | Addition |
| ➖ | `-` | Soustraction |
| ➗ | `/` | Division |
| 🪵 | `//` | Division entière |
| 🪙 | `%` | Modulo |
| ✳️ | `*` | Multiplication |
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
| ⚪️ | N/A | Réservé / pas encore implémenté (actuellement un opérateur sans effet) |

Pour utiliser un opérateur, placez-le entre deux valeurs :

```
🪶1️⃣➕2️⃣📦
🪶🔴🤝🟢📦
```
Résultat :

`3`

`False`

Il n'y a pas de priorité d'opérateurs en UwU Script : toutes les
opérations sont évaluées de gauche à droite.

```
🪶1️⃣➕2️⃣✳️3️⃣📦
```
Résultat :

`9`

À l'intérieur de 🌜🌛, si le contenu ne comporte que des opérateurs et
produit une seule valeur, ce n'est pas traité comme une liste mais comme
cette valeur seule. Cela permet de contrôler l'ordre d'évaluation :

```
🪶🌜1️⃣➕🌜2️⃣✳️3️⃣🌛🌛📦
🪶🌜🌜1️⃣➕2️⃣🌛🌛📦
🪶🌜1️⃣➕2️⃣🅰️🌛📦
```
Résultat :

`7`

`[3]`

`[3, a]`

### Variables

UwU Script n'a pas d'affectation `=`. Il suffit de placer un emoji
inconnu (ou une variable existante) en début de ligne, suivi de sa
nouvelle valeur.

```
😀5️⃣0️⃣
🪶😀📦

😀1️⃣0️⃣
🪶😀📦
```
Résultat :

`50`

`10`

Vous pouvez assigner plusieurs variables sur la même ligne :

```
😀😛5️⃣⛓️‍💥0️⃣
🪶😀📦

😀😇8️⃣⛓️‍💥3️⃣
🪶😀😛😇📦
```
Résultat :

`5 0`

`8 0 3`

### If (condition)
Le mot-clé `if` est 🤔, une valeur booléenne doit le suivre directement.
Le bloc `if` continue jusqu'au prochain 🔚. Tout ce qui se trouve entre
🤔 et 🔚 n'est exécuté que si le booléen vaut `True`.

```
😀8️⃣💪2️⃣
🪶😀📦

🤔😀
🪶🔠®️📦ℹ️🐍♓™️📦
🔚
```
Résultat :

`True`

`Right`

Pour exécuter quelque chose quand le booléen vaut `False`, utilisez 😌.
Ne mettez pas de 🔚 avant 😌 :

```
😀8️⃣🤏2️⃣
🪶😀📦

🤔😀
🪶🔠®️📦ℹ️🐍♓™️📦

😌
🪶🔠🆖📦🅾️™️⚰️🔠®️📦ℹ️🐍♓™️📦
🔚
```
Résultat :

`False`

`Not Right`

Vous pouvez utiliser 😏 pour vérifier une seconde condition si la
première vaut `False`, puis une troisième, et ainsi de suite :

```
🤔🔴
🪶1️⃣⛓️‍💥🔠®️📦ℹ️🐍♓™️📦

😏🔴
🪶2️⃣⛓️‍💥🔠®️📦ℹ️🐍♓™️📦

😏🟢
🪶3️⃣⛓️‍💥🔠®️📦ℹ️🐍♓™️📦

😌
🪶🔠🅰️📦🛴🛴⚰️🔠🆖📦🅾️™️⚰️🔠®️📦ℹ️🐍♓™️📦
🔚
```
Résultat :

`3 Right`

Vous pouvez aussi utiliser 😏 sans 😌 final :

```
🤔🔴
🪶1️⃣⛓️‍💥🔠®️📦ℹ️🐍♓™️📦

😏🟢
🪶2️⃣⛓️‍💥🔠®️📦ℹ️🐍♓™️📦
🔚
```
Résultat :

`2 Right`

### Feuille de route (pas encore implémenté)
Le code source de l'interpréteur (`b.py`) contient des commentaires
décrivant des fonctionnalités prévues mais **pas encore disponibles** :
aucun emoji ne leur est actuellement associé dans la table de conversion.

- Boucles `for` (emoji prévu : 🌀)
- Boucles `while` (emoji prévu : 🤗)
- Fonctions définies par l'utilisateur avec paramètres et `return`
  (emojis prévus : 🌏, 👉, 👈, 🙏, 🔃)
- Support des nombres aléatoires
- Appels de fonction de type objet/méthode
- Caractères spéciaux supplémentaires

Ne comptez pas dessus : utiliser ces emojis aujourd'hui échouera, car ils
ne sont pas encore enregistrés dans la table de conversion.
