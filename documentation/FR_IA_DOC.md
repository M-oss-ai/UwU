# UwU Script

UwU Script est un langage de programmation qui utilise **uniquement** des
emojis comme syntaxe. Il est fortement inspiré de Python.

> **Remarque sur ce document.** Ce fichier corrige le `README.md`
> d'origine et reste synchronisé avec l'interpréteur réel (`b.py` /
> `c.py`). Chaque exemple ci-dessous a été exécuté contre le code actuel,
> pas seulement déduit à la main.

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

#### Récupérer un élément (🎯)
Placez 🎯 entre une liste (ou une chaîne) et un index pour obtenir cet
élément — l'équivalent du `("a", "b")[1]` de Python. Le premier élément a
pour index `0` :

```
🪶🤙🌜🅰️⛓️‍💥🅱️🌛🎯1️⃣📦
🪶🤙🅰️🅱️©️🎯1️⃣📦
```
Résultat :

`b`

`b`

La liste peut être une variable ou le résultat d'une fonction, l'index
peut être n'importe quelle valeur, et 🎯 peut être enchaîné pour entrer
dans des listes imbriquées. Quand l'élément est lui-même une liste, il
est conservé entier :

```
😀🌜🌜1️⃣⛓️‍💥2️⃣🌛⛓️‍💥3️⃣🌛
🪶🤙😀🎯0️⃣📦
🪶🤙😀🎯0️⃣🎯1️⃣📦
```
Résultat :

`[1, 2]`

`2`

Contrairement aux autres opérateurs (voir « Opérateurs » plus bas), 🎯
est toujours appliqué en premier, il n'a donc pas besoin d'être groupé.
Un index peut être calculé avec 🌜🌛, ce qui est aussi la façon d'écrire
un index négatif (il n'y a pas de signe moins dans les nombres) :

```
😀🌜5️⃣⛓️‍💥6️⃣🌛
🪶🤙1️⃣0️⃣➕😀🎯1️⃣📦
🪶🤙😀🎯🌜0️⃣➖1️⃣🌛📦
```
Résultat :

`16`

`6`

Un index hors de la liste arrête le programme avec l'`IndexError` de
Python. 👀 (ci-dessus) fait le même travail sous forme de fonction, et
découpe aussi des tranches.

### Emoji littéraux (🎭)
Les emojis ont normalement un sens : 🅰️ est la lettre `"a"`, ➕ est un
opérateur, et un emoji que le langage ne connaît pas est une erreur. 🎭
transforme les emojis qui suivent en texte brut, tels que tapés, jusqu'au
prochain 📦. C'est ainsi que l'on affiche un emoji ou qu'on en garde un
comme donnée.

```
🪶🤙🎭😀🌀📦📦
```
Résultat :

`😀🌀`

Le premier 📦 termine le texte et appartient à 🎭 ; le second ferme
l'appel à 🪶, comme d'habitude. Le texte est une chaîne normale : elle
fusionne avec les chaînes voisines et peut être stockée dans une
variable.

```
🪶🤙🎭😀📦🅰️📦
💚🎭🌀📦
🪶🤙💚📦
```
Résultat :

`😀a`

`🌀`

Sans 📦 de fermeture, le texte court jusqu'à la fin de la ligne. Seuls
les emojis peuvent faire partie du texte — tout le reste (lettres,
espaces) est supprimé, comme partout ailleurs dans un fichier. Les
opérateurs et les instructions sont conservés comme texte :

```
🪶🤙🎭➕🤙📦📦
```
Résultat :

`➕🤙`

Pour mettre un 📦 dans le texte, fermez le texte, puis ajoutez `🎭📦📦`,
qui représente un 📦 littéral :

```
🪶🤙🎭😀🌀📦🎭📦📦📦
🪶🤙🎭📦📦📦
```
Résultat :

`😀🌀📦`

`📦`

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

Cette restriction ne s'applique qu'aux fonctions de la table, au début
d'une ligne de premier niveau. Une référence brute est parfaitement
valide — et c'est tout l'intérêt — quand elle est utilisée comme valeur :
passée en argument, affichée au sein d'un appel plus large, ou stockée
dans une variable (voir ci-dessous). Une ligne qui commence par une
*variable* contenant une fonction est différente : voir « Références de
fonction » ci-dessous.

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

Une ligne qui **commence** par une variable contenant une fonction est
une instruction. Si 🤙 suit la variable, la fonction est appelée (son
résultat est jeté, comme pour toute autre instruction) ; sinon la ligne
est une affectation normale et la variable est réassignée :

```
😀🪶
😀🤙Ⓜ️📦
```
Résultat :

`m`

```
😀🪶
😀🔠
🪶🤙😀🤙Ⓜ️📦📦
```
Résultat :

`M`

Ici la deuxième ligne n'a pas de 🤙 : elle réassigne donc 😀 à
`str.upper` ; la troisième ligne l'appelle.

Le résultat de l'appel d'une fonction stockée peut être stocké comme
n'importe quelle autre valeur :

```
😀🔠
💚😀🤙Ⓜ️📦
🪶🤙💚📦
```
Résultat :

`M`

### Paramètres nommés (📛)
Certaines fonctions prennent des paramètres nommés, comme `sep` et `end` de
`print`. Écrivez le nom (c'est du texte, épelé avec les emojis lettres),
puis 📛, puis la valeur, parmi les autres paramètres. Voici
`print("hello world", end=". \n")` :

```
🪶🤙♓🔱🛴🛴🅾️⚰️〰️🅾️®️🛴🆔⛓️‍💥🔱🆖🆔📛⚫️⚰️⤵️📦
🪶🤙Ⓜ️📦
```
Résultat :

`hello world. `

`m`

Ici `end` remplace le saut de ligne habituel de `print` par un point, une
espace et un saut de ligne (`⚫️⚰️⤵️`), donc le second `print` commence sur
une nouvelle ligne.

Un paramètre nommé est un élément de plus dans la liste des paramètres.
Quand deux textes se suivent — le paramètre précédent et le nom, ou une
valeur et le nom suivant — séparez-les avec ⛓️‍💥, sinon ils fusionnent
(voir « Types ») :

```
🪶🤙🅰️⛓️‍💥🅱️⛓️‍💥💲🔱🅿️📛🚥⛓️‍💥🔱🆖🆔📛❗📦
```
Résultat :

`a-b!`

La valeur va jusqu'au prochain ⛓️‍💥 ou 📦 et peut être n'importe quelle
expression : 📛 est appliqué après les opérateurs (et après 🎯), il n'a donc
jamais besoin de groupement.

```
🪶🤙🅰️⛓️‍💥🅱️⛓️‍💥💲🔱🅿️📛🚥➕🚥📦
```
Résultat :

`a--b`

Cela fonctionne avec toute fonction qui accepte le nom, quelle qu'elle
soit : une fonction de la table, une fonction trouvée avec 🔎, ou une
fonction stockée dans une variable (appelée comme instruction quand la
ligne commence par la variable).

```
🪶🤙🗂️🤙🌜1️⃣⛓️‍💥3️⃣⛓️‍💥2️⃣🌛⛓️‍💥®️🔱♈🔱®️💲🔱📛🟢📦📦
🪶🤙🔢🤙🎏🎏⛓️‍💥🅱️🅰️💲🔱📛1️⃣6️⃣📦📦
😀🪶
😀🤙🅰️⛓️‍💥🅱️⛓️‍💥💲🔱🅿️📛🚥📦
```
Résultat :

`[3, 2, 1]`

`255`

`a-b`

Un nom que la fonction ne connaît pas provoque une `TypeError` de Python.
Un 📛 sans nom avant lui, ou sans valeur après lui, arrête le programme
(`error7` / `error8`).

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

#### Ce qui peut être trouvé
La recherche est un simple `getattr` : n'importe quelle fonction native et
n'importe quelle fonction de n'importe quel module importable peut donc
être trouvée, pas seulement celles qui ont leur propre emoji (testé sur
toutes les fonctions natives dont le nom est en minuscules et sur les
fonctions publiques de `math`, `random`, `time`, `json`, `statistics`,
`itertools`, `operator`, `functools`, `os`, `sys`, `re`, `textwrap`,
`datetime` et `calendar`). Une valeur qui n'est pas une fonction (comme
`math.pi`) est renvoyée telle quelle, et un module trouvé ainsi peut être
donné à 🐙 pour atteindre ce qu'il contient.

#### Épeler un nom
Un nom est du texte, construit avec les emojis lettres et 🥿 (`_`). Les
chiffres sont des nombres, pas du texte : un nom qui en contient
s'assemble donc avec ➕ et 🔤 (`str`) ; les majuscules viennent de 🔠 de
la même façon. Par exemple `math.log10` :

```
😀🔎🤙🛴🅾️🐍➕🔤🤙1️⃣0️⃣📦⛓️‍💥Ⓜ️🅰️™️♓📦
🪶🤙😀🤙1️⃣0️⃣0️⃣0️⃣📦📦
```
Résultat :

`3.0`

#### Limites
- **Tout n'a pas un nom à rechercher.** 🙅, 🏁, 👀, 🔎 et 🐙 sont définies
  par l'interpréteur lui-même (`b.py`), et `find` refuse les modules `b`
  et `c` : utilisez leur propre emoji.
- **Une fonction ne peut pas être passée en argument**, pas même comme
  paramètre nommé. Une référence donnée en paramètre arrive à la fonction
  appelée sous forme du texte `<fonction NOM>` (c'est ce qui rend
  l'affichage d'une référence lisible), donc les fonctions qui attendent
  une fonction — `map`, `filter`, `functools.reduce`, un paramètre `key=`,
  ou 🐙 appliqué à une fonction ou une classe — ne sont pas utilisables.

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
| 🎯 | `[ ]` | Élément à un index : `liste 🎯 index` (voir « Récupérer un élément ») |

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
opérations sont évaluées de gauche à droite — sauf 🎯, toujours appliqué
en premier (voir « Récupérer un élément »).

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

UwU Script n'a pas d'affectation `=`. Une ligne qui commence par un emoji
inconnu, ou par une variable existante, l'assigne : tout ce qui suit ce
premier emoji est la valeur.

```
😀5️⃣0️⃣
🪶🤙😀📦

😀1️⃣0️⃣
🪶🤙😀📦
```
Résultat :

`50`

`10`

Une seule variable est assignée par ligne : un second nom sur la ligne
est donc lu comme faisant partie de la valeur (et c'est une erreur s'il
est inconnu). Si la valeur est composée de plusieurs valeurs séparées par
⛓️‍💥, la première est conservée. Une ligne avec un nom et sans valeur arrête
le programme avec `error9`.

```
😀5️⃣⛓️‍💥🅰️
🪶🤙😀📦
```
Résultat :

`5`

Une variable peut contenir n'importe quelle valeur, y compris une
fonction (voir « Références de fonction ») et le résultat d'un appel de
fonction.

### If (condition)
Le mot-clé `if` est 🤔, une valeur booléenne doit le suivre directement.
Le bloc `if` continue jusqu'au prochain 🔚. Tout ce qui se trouve entre
🤔 et 🔚 n'est exécuté que si le booléen vaut `True`.

Une comparaison peut être assignée à une variable comme n'importe quelle
autre valeur. La condition après 🤔 doit être une seule valeur booléenne
— une variable qui en contient une, ou une comparaison groupée avec 🌜🌛
— et une comparaison écrite directement après 🤔 n'est pas supportée,
donc les exemples ci-dessous la stockent d'abord :

```
😀8️⃣💪2️⃣
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
😀8️⃣🤏2️⃣
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
- Création d'objets

Le support des nombres aléatoires, les appels façon objet/attribut, et
un grand nombre de caractères spéciaux figuraient auparavant ici comme
prévus — ils sont maintenant implémentés (🎲/🎰/🎁/⏳, 🐙, et la table de
ponctuation ci-dessus).

Ne comptez pas sur ce qu'il reste ci-dessus : les utiliser aujourd'hui
échouera, car ils ne sont pas encore enregistrés dans la table de
conversion.
