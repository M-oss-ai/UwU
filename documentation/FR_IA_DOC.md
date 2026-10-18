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
| ❓ | `"?"` |
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
| #️⃣ | `"#"` | 🤜 | `"{"` |
| ▶️ | `">"` | 🤛 | `"}"` |
| ◀️ | `"<"` | 🫸 | `"["` |
| 🥓 | `"="` | 🫲 | `"]"` |

Chaque emoji n'a qu'un seul sens. 🤜 🤛 et 🫲 sont les caractères `{`, `}` et
`]`. 👉, 👈 et 🫷 sont des mots-clés, pas des caractères : 👉 👈 entourent les
paramètres d'une fonction ou les arguments d'une classe, et 🫷 ferme une
boucle, une fonction ou une classe (voir « Boucles », « Fonctions définies par
l'utilisateur » et « Classes et objets »). Un mot-clé n'a pas de valeur : on ne
peut pas l'utiliser à l'intérieur d'une expression.

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

`🤦 🫵 🪶 🤙 ❓ 🙈 🤡 🛴1️⃣`

`Ligne 1 : 🪶 est une fonction, et écrire son nom ne l'exécute pas. Pour l'exécuter, écris 🤙 juste après son nom, puis les valeurs, puis 📦.`

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
avec une erreur (voir « Messages d'erreur »).

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
le programme avec une erreur.

```
😀5️⃣⛓️‍💥🅰️
🪶🤙😀📦
```
Résultat :

`5`

Une variable peut contenir n'importe quelle valeur, y compris une
fonction (voir « Références de fonction ») et le résultat d'un appel de
fonction.

Les emojis qui font partie du langage — lettres, chiffres, fonctions,
opérateurs et mots-clés comme 🌀 ou 🤔 — ne peuvent pas servir de noms de
variable.

### If (condition)
Le mot-clé `if` est 🤔, suivi d'une condition : la première valeur de ce
qui suit est testée. Le bloc `if` continue jusqu'au prochain 🔚. Tout ce
qui se trouve entre 🤔 et 🔚 n'est exécuté que si la condition est vraie.
La condition peut être une comparaison écrite juste après 🤔 :

```
🤔8️⃣💪2️⃣
🪶🤙🔠🤙®️📦ℹ️🐍♓™️📦
🔚
```
Résultat :

`Right`

Elle peut aussi être une variable qui contient un booléen : une
comparaison peut être assignée à une variable comme n'importe quelle autre
valeur, puis testée plus tard.

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

### Boucles
Une boucle `for` répète un bloc pour chaque élément d'un range, d'une liste
ou d'une chaîne. Écrivez 🌀, puis la variable qui reçoit chaque élément (un
emoji inutilisé, ou une variable existante), puis la séquence. Le bloc est
formé des lignes suivantes et se termine par une ligne contenant
uniquement 🫷 :

```
🌀😀📏🤙3️⃣📦
🪶🤙😀📦
🫷
```
Résultat :

`0`

`1`

`2`

La séquence est la première valeur après la variable : ici `📏🤙3️⃣📦` est
`range(3)`, mais ce peut aussi être une liste, une chaîne ou une variable
qui en contient une. Après la boucle, la variable garde sa dernière valeur.

```
🌀😀🌜🅰️⛓️‍💥🅱️⛓️‍💥©️🌛
🪶🤙😀📦
🫷
```
Résultat :

`a`

`b`

`c`

Une boucle `while` utilise 🤗 suivi d'une condition (comme 🤔). Le bloc est
répété tant que la condition est vraie, et la condition est évaluée à
nouveau avant chaque passage :

```
😀0️⃣
🤗😀🤏3️⃣
🪶🤙😀📦
😀😀➕1️⃣
🫷
```
Résultat :

`0`

`1`

`2`

Dans une boucle, ⏭️ passe directement au tour suivant et 🛑 quitte la
boucle. On peut les placer n'importe où dans le bloc, typiquement dans un
`if`, et ils n'agissent que sur la boucle la plus intérieure :

```
🌀😀📏🤙1️⃣0️⃣📦
🤔😀🟰2️⃣
⏭️
🔚
🤔😀🟰5️⃣
🛑
🔚
🪶🤙😀📦
🫷
```
Résultat :

`0`

`1`

`3`

`4`

Les boucles peuvent contenir d'autres boucles, des blocs `if` et des
définitions de fonction. ⏭️ ou 🛑 hors d'une boucle, une boucle jamais
fermée et un en-tête sans rien à parcourir arrêtent le programme avec une
erreur.

### Fonctions définies par l'utilisateur
🌏 définit une fonction. Écrivez 🌏, le nom de la fonction (un emoji
inutilisé, ou une variable existante), puis 👉, les noms des paramètres
(des emojis inutilisés, les uns après les autres) et 👈. Le corps est formé
des lignes suivantes et la définition se termine par une ligne contenant
uniquement 🫷, comme une boucle. 🙏 renvoie une valeur :

```
🌏💚👉🍎🍌👈
🙏🍎➕🍌
🫷
🪶🤙💚🤙1️⃣⛓️‍💥2️⃣📦📦
```
Résultat :

`3`

Une fonction s'appelle comme toute autre : 🤙 juste après son nom, puis les
paramètres jusqu'à 📦. Les paramètres nommés fonctionnent aussi, en
donnant l'emoji du paramètre comme texte avec 🎭. Un appel avec un mauvais
nombre de paramètres donne les erreurs habituelles.

🙏 quitte la fonction immédiatement — même depuis une boucle ou un `if` —
et renvoie la première valeur écrite après lui. Sans 🙏, ou avec 🙏 seul,
la fonction renvoie `None` :

```
🌏💚👉🍎👈
🌀😀🍎
🤔😀🪙2️⃣🟰0️⃣
🙏😀
🔚
🫷
🙏🕳️
🫷
🪶🤙💚🤙🌜3️⃣⛓️‍💥5️⃣⛓️‍💥6️⃣⛓️‍💥7️⃣🌛📦📦
```
Résultat :

`6`

Une fonction peut s'appeler elle-même :

```
🌏🧱👉📐👈
🤔📐🤏2️⃣
🙏1️⃣
🔚
🙏📐*️⃣🧱🤙📐➖1️⃣📦
🫷
🪶🤙🧱🤙5️⃣📦📦
```
Résultat :

`120`

Les paramètres, et toute variable assignée dans le corps, sont locaux :
ils disparaissent quand la fonction se termine et ne modifient jamais une
variable de même nom à l'extérieur. Les variables définies à l'extérieur
peuvent être lues. (Une liste donnée en paramètre n'est pas copiée : la
modifier — avec 📨 par exemple — est visible à l'extérieur.)

```
🥕5️⃣
🌏🍞👉👈
🥕9️⃣
🙏🥕
🫷
🪶🤙🍞🤙📦⛓️‍💥🥕📦
```
Résultat :

`9 5`

Une fonction est une variable ordinaire, comme celles qui contiennent
`print` dans « Références de fonction » : on peut la réassigner, la copier
dans une autre variable, la définir à nouveau, ou la définir par-dessus une
variable qui contenait autre chose. L'afficher donne `<fonction NOM>` :

```
🌏💚👉👈
🙏1️⃣
🫷
🥑💚
💚5️⃣
🪶🤙🥑🤙📦⛓️‍💥💚📦
```
Résultat :

`1 5`

Ici 🥑 a reçu une copie de la fonction, puis 💚 a été réassignée à un
nombre.

🙏 hors d'une fonction arrête le programme, tout comme une définition dont
la première ligne n'a pas de 👉 … 👈. Une récursion peut aller à plusieurs
centaines de niveaux.

### Classes et objets
Une classe est un modèle qui construit des objets. 🏛️ en définit une :
écrivez 🏛️, le nom de la classe (un emoji inutilisé, ou une variable
existante), puis, entre 👉 et 👈, les arguments de la classe. On peut omettre
les arguments en même temps que 👉 👈. La classe est formée des lignes
suivantes et se termine par une ligne contenant uniquement 🫷.

Appeler la classe comme une fonction — 🤙 juste après son nom, puis les
valeurs jusqu'à 📦 — crée un objet. Chaque valeur est rangée dans l'objet,
sous l'emoji de l'argument correspondant, et 🔗 la lit : `🐕🔗🦴` est
l'attribut 🦴 de l'objet 🐕.

```
🏛️🐶👉🦴🎂👈
🫷
🐕🐶🤙3️⃣⛓️‍💥5️⃣📦
🪶🤙🐕🔗🦴⛓️‍💥🐕🔗🎂📦
```
Résultat :

`3 5`

Le ⛓️‍💥 garde les deux nombres séparés (voir « Types »). Le nom écrit après 🔗
est un emoji pris tel quel : ce n'est pas forcément une variable. 🔗 est
appliqué avant les opérateurs, comme 🎯, et les deux s'enchaînent de gauche à
droite. Ici `😀🎯1️⃣🔗🦴` est l'attribut 🦴 du deuxième élément de la liste 😀,
et ➕ utilise ensuite ce résultat :

```
🏛️🐶👉🦴👈
🫷
😀🌜🐶🤙1️⃣📦⛓️‍💥🐶🤙2️⃣📦🌛
🪶🤙😀🎯1️⃣🔗🦴➕1️⃣0️⃣📦
```
Résultat :

`12`

Une ligne qui commence par un objet, 🔗, un nom et une valeur donne cette
valeur à l'attribut — et crée l'attribut si l'objet ne l'avait pas. Comme pour
les variables, seule la première valeur est conservée. Les attributs peuvent
s'enchaîner pour atteindre un objet rangé dans un autre : `🐕🔗🐈🔗🦴`.

```
🏛️🐶👉🦴👈
🫷
🐕🐶🤙3️⃣📦
🐕🔗🦴🐕🔗🦴➕1️⃣
🐕🔗🎂9️⃣
🪶🤙🐕🔗🦴⛓️‍💥🐕🔗🎂📦
```
Résultat :

`4 9`

Lire un attribut qui n'existe pas donne l'erreur Python `AttributeError`.

#### Fonctions d'une classe
Une fonction définie dans une classe (🌏 … 🫷, voir « Fonctions définies par
l'utilisateur ») travaille sur les objets de la classe. Son premier paramètre
reçoit l'objet (un emoji inutilisé quelconque — ici 🙋) ; les autres
paramètres sont ceux écrits dans l'appel. Pour l'appeler, écrivez l'objet, 🔗,
le nom de la fonction, puis 🤙 et les paramètres jusqu'à 📦 :

```
🏛️🐶👉🦴👈
🌏🍖👉🙋🍎👈
🙋🔗🦴🙋🔗🦴➕🍎
🫷
🌏🧺👉🙋👈
🙏🙋🔗🦴
🫷
🫷
🐕🐶🤙2️⃣📦
🐕🔗🍖🤙3️⃣📦
🪶🤙🐕🔗🧺🤙📦📦
```
Résultat :

`5`

L'objet placé devant 🔗 est donné automatiquement : il ne s'écrit donc pas
entre 🤙 et 📦. Comme pour toute fonction, un appel seul sur une ligne —
`🐕🔗🍖🤙3️⃣📦` — exécute la fonction et jette le résultat, et sans 🤙,
`🐕🔗🍖` est une référence à la fonction, qu'on peut ranger dans une variable
et appeler plus tard. Une fonction de classe peut appeler les autres par son
premier paramètre, et peut s'appeler elle-même.

#### Valeurs d'une classe
Les lignes d'une classe qui ne sont pas des définitions de fonction
s'exécutent une seule fois, quand la classe est définie, dans un espace à
part : les variables qu'elles assignent n'existent pas en dehors de la
classe. Elles deviennent des valeurs de la classe, que tous les objets de la
classe peuvent lire — ainsi que la classe elle-même, avec 🔗. Donner à un
objet un attribut du même nom masque la valeur pour cet objet seulement.

```
🏛️🐶👉👈
🦴3️⃣
🫷
🐕🐶🤙📦
🐈🐶🤙📦
🐕🔗🦴7️⃣
🪶🤙🐕🔗🦴⛓️‍💥🐈🔗🦴⛓️‍💥🐶🔗🦴📦
```
Résultat :

`7 3 3`

N'importe quelle ligne peut s'y trouver (un `if`, une boucle, un
affichage...). Elles s'exécutent toutes une seule fois, à la définition, et
pas pour chaque objet :

```
🏛️🐶👉👈
🪶🤙🅾️🆖©️🔱📦
🫷
🐕🐶🤙📦
🐈🐶🤙📦
```
Résultat :

`once`

#### Préparer un objet (🏗️)
Une fonction nommée 🏗️ dans une classe s'exécute à chaque création d'objet,
juste après le rangement des arguments, avec l'objet pour seul paramètre.
C'est l'endroit où préparer ce dont chaque objet a besoin pour lui :

```
🏛️🐶👉🦴👈
🌏🏗️👉🙋👈
🙋🔗🎂🙋🔗🦴*️⃣2️⃣
🫷
🫷
🐕🐶🤙4️⃣📦
🪶🤙🐕🔗🦴⛓️‍💥🐕🔗🎂📦
```
Résultat :

`4 8`

Une valeur qui ne doit pas être partagée entre les objets — comme une liste —
doit être créée là : écrite directement dans la classe (voir plus haut), ce
serait la même liste pour tous les objets.

```
🏛️🐶👉👈
🌏🏗️👉🙋👈
🙋🔗🦴🌜🌛
🫷
🫷
🐕🐶🤙📦
🐈🐶🤙📦
📨🤙🐕🔗🦴⛓️‍💥1️⃣📦
🪶🤙🐕🔗🦴⛓️‍💥🐈🔗🦴📦
```
Résultat :

`[1] []`

🏗️ n'existe que comme nom d'une fonction dans une classe : ailleurs, c'est
une erreur, comme pour tout emoji réservé.

#### Les objets sont des valeurs
Un objet est une valeur comme les autres : on peut le ranger dans une
variable ou dans une liste, le donner à une fonction et le comparer. Afficher
un objet, une classe ou le type d'un objet (🏷️) donne :

```
🏛️🐶👉👈
🫷
🐕🐶🤙📦
🪶🤙🐕📦
🪶🤙🐶📦
🪶🤙🏷️🤙🐕📦📦
```
Résultat :

`<objet 🐶>`

`<classe 🐶>`

`<classe 🐶>`

Parcourir une liste d'objets et appeler leurs fonctions :

```
🏛️🐶👉🦴👈
🌏🔊👉🙋👈
🪶🤙🙋🔗🦴📦
🫷
🫷
🌀🐕🌜🐶🤙1️⃣📦⛓️‍💥🐶🤙2️⃣📦🌛
🐕🔗🔊🤙📦
🫷
```
Résultat :

`1`

`2`

Donné à une fonction, un objet n'est pas copié : changer ses attributs se voit
à l'extérieur.

```
🏛️🐶👉🦴👈
🫷
🌏🧱👉🍎👈
🍎🔗🦴9️⃣
🫷
🐕🐶🤙1️⃣📦
🧱🤙🐕📦
🪶🤙🐕🔗🦴📦
```
Résultat :

`9`

#### Erreurs et limites
Une classe jamais fermée, et un en-tête sans nom ou dont le 👉 … 👈 n'est pas
fermé, arrêtent le programme avec une erreur. Il en va de même pour 🏗️ en
dehors d'une classe, pour 🙏 dans les lignes d'une classe (hors de ses
fonctions), pour ⏭️ ou 🛑 y figurant hors d'une boucle, pour un mauvais nombre
de valeurs à la création d'un objet (les erreurs habituelles des fonctions),
pour 🔗 sans rien devant ou sans nom derrière, et pour une ligne `objet 🔗 nom`
sans valeur.

Il n'y a pas d'héritage. Une classe, comme une fonction, ne peut pas être
donnée en paramètre à une autre fonction.

### Erreurs (try / except / finally / raise)
Certaines opérations échouent avec une erreur Python : diviser par zéro,
convertir `abc` en nombre, lire un élément qui n'existe pas, demander à un
objet un attribut qu'il n'a pas... Sans rien pour la traiter, une erreur
arrête le programme et est signalée comme toutes les autres erreurs (voir
« Messages d'erreur ») :

```
🪶🤙1️⃣➗0️⃣📦
🪶🤙🅰️🎏™️🔱®️📦
```
Résultat :

`💥 🫵 🐍 😭 🤡 🤣 🛴1️⃣`

`Ligne 1 : Python a rencontré une erreur que rien n'a rattrapée : ZeroDivisionError : division by zero. Un bloc 🤞 avec un 😱 permet de la rattraper.`

🤞 commence un bloc qui traite les erreurs, et 😱 dit quoi faire quand une
erreur survient dans les lignes après 🤞. Le bloc se termine par 🔚 :

```
🤞
🪶🤙1️⃣➗0️⃣📦
😱😵
🪶🤙😵📦
🔚
```
Résultat :

`division by zero`

Quand une erreur survient, le reste des lignes après 🤞 est ignoré, les lignes
après 😱 s'exécutent, et le programme continue après 🔚. 😱 est suivi de la
variable qui reçoit l'erreur (un emoji inutilisé, ou une variable existante) :
l'afficher montre son message, et elle garde l'erreur après le bloc.

#### Choisir les erreurs
Après la variable, 😱 peut nommer le genre d'erreur qu'il traite :

| Emoji | Erreur Python | Levée par |
|----|-------|------|
| ⚠️ | `Exception` | toutes les erreurs |
| 🙃 | `ValueError` | une mauvaise valeur, comme `int("abc")` |
| 🧩 | `TypeError` | des valeurs qui ne vont pas ensemble, comme `1 + "a"` |
| ♾️ | `ZeroDivisionError` | une division par zéro |
| 📍 | `IndexError` | un indice hors de la liste |
| 🗝️ | `KeyError` | une clé absente |
| 🫥 | `AttributeError` | un attribut absent |

Toute autre erreur de Python peut être trouvée par son nom avec 🔎, comme
n'importe quel builtin (voir « Recherche dynamique »).

```
🤞
🪶🤙🔢🤙🅰️🅱️©️📦📦
😱😵♾️
🪶🤙💤🔱®️🅾️📦
😱😵🙃
🪶🤙♈🅰️🛴⛎🔱📦
🔚
```
Résultat :

`value`

Une erreur qu'aucun 😱 n'accepte continue son chemin : elle quitte le bloc, et
arrête le programme si rien d'autre ne la traite. Les 😱 sont essayés dans
l'ordre et seul le premier qui convient s'exécute. Pour accepter plusieurs
genres d'erreur, donnez une liste :

```
🤞
🪶🤙1️⃣➗0️⃣📦
😱😵🌜🙃⛓️‍💥♾️🌛
🪶🤙🛴ℹ️💲™️🔱🆔📦
🔚
```
Résultat :

`listed`

Un 😱 sans type traite toutes les erreurs : il doit donc être le dernier, et
on peut aussi omettre la variable :

```
🤞
🪶🤙1️⃣➗0️⃣📦
😱
🪶🤙©️🅰️⛎🐍♓™️📦
🔚
```
Résultat :

`caught`

On peut traiter les erreurs de Python et les valeurs levées avec 🚨 (voir
plus bas). On ne peut pas traiter les erreurs du langage lui-même (emoji
inconnu, mauvais nombre de paramètres, bloc mal fermé... ; voir « Messages
d'erreur »), ni 🏁, qui n'est pas une erreur : il quitte le bloc, mais 🧹
s'exécute d'abord.

#### Sinon et finalement
Dans un bloc 🤞, 😌 commence des lignes exécutées seulement si aucune erreur
n'est survenue, et 🧹 des lignes exécutées dans tous les cas : après un
succès, après une erreur traitée, quand l'erreur n'est pas traitée (juste
avant l'arrêt du programme), et quand le bloc est quitté par 🙏, 🛑 ou ⏭️. Les
parties se suivent dans cet ordre : 😱 (autant que nécessaire), 😌 (une fois,
et seulement avec au moins un 😱), puis 🧹 (une fois). Un bloc 🤞 a besoin d'au
moins un 😱 ou d'un 🧹, et une partie dans le désordre ou en trop arrête le
programme avec une erreur, comme un bloc qui n'est pas fermé par 🔚.

```
🤞
🪶🤙1️⃣📦
😱😵
🪶🤙2️⃣📦
😌
🪶🤙3️⃣📦
🧹
🪶🤙4️⃣📦
🔚
```
Résultat :

`1`

`3`

`4`

Avec une erreur dans la première partie, 😌 est ignoré et 🧹 s'exécute quand même :

```
🤞
🪶🤙1️⃣➗0️⃣📦
😱😵
🪶🤙2️⃣📦
😌
🪶🤙3️⃣📦
🧹
🪶🤙4️⃣📦
🔚
```
Résultat :

`2`

`4`

🧹 s'exécute aussi quand le bloc est quitté par 🙏 — la fonction renvoie quand même sa valeur :

```
🌏🧱👉👈
🤞
🙏1️⃣
🧹
🪶🤙🆔🅾️🆖🔱📦
🔚
🫷
🪶🤙🧱🤙📦📦
```
Résultat :

`done`

`1`

Et quand il est quitté par 🛑 ou ⏭️ dans une boucle :

```
🌀😀📏🤙5️⃣📦
🤞
🤔😀🟰2️⃣
🛑
🔚
🪶🤙😀📦
🧹
🪶🤙🎏📦
🔚
🫷
```
Résultat :

`0`

`f`

`1`

`f`

`f`

#### Lever une erreur (🚨)
🚨 lève la première valeur écrite après lui. Une erreur à laquelle on donne un
message avec 🤙 porte ce message :

```
🤞
🚨⚠️🤙🅱️🅾️🅾️Ⓜ️📦
😱😵
🪶🤙😵📦
🔚
```
Résultat :

`boom`

Une classe d'erreur seule lève une nouvelle erreur de cette classe :

```
🤞
🚨🙃
😱😵🙃
🪶🤙♈🅰️🛴⛎🔱📦
🔚
```
Résultat :

`value`

N'importe quelle autre valeur peut être levée — un texte, un objet. Un 😱 sans
type la reçoit telle quelle, et un 😱 avec un type la reçoit si c'est une
valeur de ce type (🔤 pour un texte), ou si le type est ⚠️ :

```
🤞
🚨🅾️🅾️🅿️💲
😱😵
🪶🤙😵📦
🔚
```
Résultat :

`oops`

Lever un objet de votre propre classe donne des erreurs de votre propre
genre :

```
🏛️🧨👉💬👈
🫷
🤞
🚨🧨🤙Ⓜ️ℹ️🆖🔱📦
😱😵🧨
🪶🤙😵🔗💬📦
🔚
```
Résultat :

`mine`

🚨 seul, dans un 😱, lève à nouveau l'erreur en cours de traitement, pour
qu'un bloc 🤞 extérieur la traite :

```
🤞
🤞
🪶🤙1️⃣➗0️⃣📦
😱😵
🪶🤙ℹ️🆖🆖🔱®️📦
🚨
🔚
😱🤕♾️
🪶🤙🅾️⛎™️🔱®️📦
🔚
```
Résultat :

`inner`

`outer`

🚨 seul en dehors d'un 😱 donne l'erreur Python `RuntimeError`.

### Messages d'erreur
Une erreur dans un programme — un emoji inconnu, un bloc jamais fermé, un appel
avec le mauvais nombre de valeurs, une erreur Python que rien ne traite... —
l'arrête avec un message d'erreur. Toutes les erreurs s'affichent de la même
façon, sur deux lignes :

1. une ligne d'emojis qui se moque de vous, finie par 🛴 et le numéro de la
   ligne de `a.txt` où se trouve l'erreur (🛴 est la lettre `l` : `🛴8️⃣0️⃣` se
   lit « l80 », ligne 80) ;
2. en dessous, une description détaillée en toutes lettres, qui commence par
   `Ligne` et le même numéro.

Les deux lignes vont sur la sortie standard et le programme se termine avec le
code de sortie 1. Pour trouver la ligne d'une erreur, lisez les chiffres après le
dernier 🛴 de la première ligne.

```
😶 a comment

🪶🤙🥭📦
```
Résultat :

`🤡 🫵 🔍 🥭 🧠 🕳️ 🤣 🛴3️⃣`

`Ligne 3 : l'emoji 🥭 est inconnu. Ce n'est ni une valeur, ni une fonction, ni un mot-clé du langage, et aucune variable ne porte ce nom. Une variable se crée en début de ligne, suivie de sa valeur, et il faut la créer avant de s'en servir.`

Le numéro de ligne est celui qu'affiche un éditeur : les commentaires, les
lignes vides et les lignes sans aucun emoji comptent. C'est la ligne où
l'erreur se produit — dans une fonction, la ligne dans le corps de la
fonction ; pour un bloc jamais fermé, la ligne qui ouvre le bloc. Ce que le
programme a affiché avant l'erreur reste affiché :

```
🪶🤙🅰️📦
🌀😀📏🤙3️⃣📦
🪶🤙😀📦
```
Résultat :

`a`

`🤡 🫵 🚪 🔓 🫷 ❌ 🐌 🛴2️⃣`

`Ligne 2 : le bloc ouvert ici par 🌀 n'est jamais fermé. Chaque boucle (🌀, 🤗), fonction (🌏) et classe (🏛️) se termine par une ligne contenant uniquement 🫷.`

```
🌏🧱👉👈
🪶🤙🥭📦
🫷
🧱🤙📦
```
Résultat :

`🤡 🫵 🔍 🥭 🧠 🕳️ 🤣 🛴2️⃣`

`Ligne 2 : l'emoji 🥭 est inconnu. Ce n'est ni une valeur, ni une fonction, ni un mot-clé du langage, et aucune variable ne porte ce nom. Une variable se crée en début de ligne, suivie de sa valeur, et il faut la créer avant de s'en servir.`

Une erreur qui vient de Python lui-même — une division par zéro, une mauvaise
conversion, un indice hors d'une liste... — et qu'aucun bloc 🤞 ne traite est
signalée de la même façon, et sa description se termine par le nom et le
message de l'erreur Python. Il en va de même pour une valeur levée avec 🚨 que
rien ne traite. (Mettre la variable d'environnement `UWU_DEBUG` à `1` affiche à
la place l'erreur complète de Python : cela aide à chercher un bug de
l'interpréteur lui-même.)

```
🪶🤙1️⃣➗0️⃣📦
🪶🤙🅰️🎏™️🔱®️📦
```
Résultat :

`💥 🫵 🐍 😭 🤡 🤣 🛴1️⃣`

`Ligne 1 : Python a rencontré une erreur que rien n'a rattrapée : ZeroDivisionError : division by zero. Un bloc 🤞 avec un 😱 permet de la rattraper.`

Voici tous les messages, avec leur ligne d'emojis (sans le 🛴 final ni le
numéro ; 🥭 représente l'emoji concerné) et leur cause :

| Ligne d'emojis | Cause |
|----|------|
| 🤡 🫵 🔍 🥭 🧠 🕳️ 🤣 | Un emoji qui n'est ni une variable (déjà définie), ni une valeur, ni une fonction, ni un mot-clé est utilisé dans une expression. |
| 🙄 🫵 🔑 🥭 🚫 🎁 🤦 | Un mot-clé (🤔, 🌀, 🫷...) est utilisé comme valeur, au milieu d'une expression. |
| 🤦 🫵 🔗 👻 ➡️ 🤡 | 🔗 sans rien devant lui (ou seulement un opérateur ou un séparateur). |
| 🙄 🫵 🔗 ❓ 🏷️ 🤡 | 🔗 sans nom d'attribut après lui. |
| 🤏 🫵 🧱 🍼 📦 🤡 | Une fonction (ou une classe) est appelée avec moins de valeurs qu'il n'en faut. |
| 🤯 🫵 🧱 🐘 📦 🤡 | Une fonction (ou une classe) est appelée avec plus de valeurs qu'elle n'en accepte. |
| 🙄 🫵 📛 🪪 🕳️ 🤡 | 📛 sans nom avant lui. |
| 🤦 🫵 📛 🎁 🕳️ 🤡 | 📛 sans valeur après lui. |
| 🙄 🫵 ➕ 👻 🤡 🧮 | Un opérateur au début d'une expression ou d'une ligne. |
| 🤦 🫵 ➕ 🕳️ 👻 🤡 | Un opérateur à la fin d'une expression. |
| 🙄 🫵 🕳️ 🪹 💤 🤡 | Un nom, ou 🤔 😏 🤗, sans rien à évaluer après lui. |
| 🙄 🫵 🔗 🕳️ 🪹 🤡 | `objet 🔗 nom` sans valeur après le nom. |
| 🤡 🫵 🚪 🔓 🫷 ❌ 🐌 | Une boucle, une fonction ou une classe qu'aucun 🫷 ne ferme (la ligne est celle qui l'ouvre). |
| 🙄 🫵 🫷 🚪 🚫 🤡 | Un 🫷 alors qu'aucune boucle, fonction ou classe n'est ouverte. |
| 🤦 🫵 🥭 🤔 ❓ 🤡 | Un 😏, 😌 ou 🔚 en dehors d'un bloc 🤔 (ou d'un bloc 🤞 pour 😌 et 🔚). |
| 🙄 🫵 🥭 🤞 ❓ 🤡 | Un 😱 ou 🧹 en dehors d'un bloc 🤞. |
| 🤯 🫵 😏 😌 🔀 🤡 | 😏 ou 😌 dans le mauvais ordre dans un bloc 🤔 (deux 😌, par exemple). |
| 🤡 🫵 🤔 🚪 🔚 ❌ 🐌 | Un bloc 🤔 qu'aucun 🔚 ne ferme. |
| 🤦 🫵 🫷 🧩 🚫 🤡 | Un 🫷 alors qu'un bloc 🤔 est encore ouvert à l'intérieur du bloc qu'il fermerait. |
| 🤡 🫵 🥭 🔒 🚫 😂 | Un emoji du langage est utilisé comme nom de variable, de fonction, de paramètre, de classe, de variable de boucle ou d'erreur. |
| 🙄 🫵 🌀 🔁 ❓ 🤡 | Un 🌀 sans variable de boucle ou sans rien à parcourir. |
| 🙄 🫵 🤗 🔁 ❓ 🤡 | Un 🤗 sans condition. |
| 🙄 🫵 🌏 🌍 ❓ 🤡 | La première ligne d'une fonction n'est pas 🌏 nom 👉 paramètres 👈. |
| 🤦 🫵 👯 🌏 🤡 | Deux paramètres d'une fonction ont le même emoji. |
| 🙄 🫵 🏛️ 🧱 ❓ 🤡 | La première ligne d'une classe n'est pas 🏛️ nom (👉 arguments 👈). |
| 🤦 🫵 👯 🏛️ 🤡 | Deux arguments d'une classe ont le même emoji. |
| 🤦 🫵 🤞 🪤 🕳️ 🤡 | Un bloc 🤞 sans 😱 ni 🧹. |
| 🤯 🫵 🤞 😱 😌 🧹 🔀 🤡 | 😱, 😌, 🧹 dans le mauvais ordre, ou en trop, dans un bloc 🤞. |
| 🙄 🫵 😱 🕸️ 🔚 🤡 | Un 😱 sans type qui n'est pas le dernier 😱. |
| 🤡 🫵 🤞 🚪 🔚 ❌ 🐌 | Un bloc 🤞 qu'aucun 🔚 ne ferme. |
| 🤦 🫵 🤞 🧩 🚫 🔚 🤡 | Un bloc 🤞 fermé par 🫷, ou avec un autre bloc encore ouvert à l'intérieur. |
| 🙄 🫵 🙏 🏃 🚪 ❓ 🤡 | 🙏 en dehors d'une fonction. |
| 🙄 🫵 🛑 🔁 ❓ 🤡 | 🛑 en dehors d'une boucle. |
| 🙄 🫵 ⏭️ 🔁 ❓ 🤡 | ⏭️ en dehors d'une boucle. |
| 🤦 🫵 🥭 🤙 ❓ 🙈 🤡 | Une ligne qui commence par une fonction du langage mais sans 🤙. |
| 🙄 🫵 🥭 🧱 ❓ 🤡 | Une ligne qui commence par une valeur (une lettre, un chiffre, 🟢...). |
| 🤡 🫵 🥭 🪑 ❓ 😂 | Un mot-clé qui ne peut pas commencer une ligne (🔗, 🤙, 📦, 🏗️...). |
| 💥 🫵 🐍 😭 🤡 🤣 | Une erreur de Python que rien ne traite (division par zéro, mauvaise conversion, indice hors de la liste, attribut absent, 🔎 mal utilisé...). |
| 💥 🫵 🚨 🗑️ 🤡 🤣 | Une valeur levée avec 🚨 que rien ne traite. |

### Récapitulatif des mots-clés

| Emoji | Rôle |
|----|------|
| 🌀 | boucle `for` : `🌀 variable séquence` |
| 🤗 | boucle `while` : `🤗 condition` |
| ⏭️ | `continue` |
| 🛑 | `break` |
| 🫷 | fin d'une boucle, d'une fonction ou d'une classe (seul sur sa ligne) |
| 🌏 | définition de fonction : `🌏 nom 👉 paramètres 👈` |
| 🙏 | `return` |
| 🏛️ | définition de classe : `🏛️ nom 👉 arguments 👈` |
| 🏗️ | nom de la fonction qui prépare chaque nouvel objet (dans une classe) |
| 🔗 | attribut d'un objet : `objet 🔗 nom` |
| 🤔 😏 😌 🔚 | `if`, `elif`, `else`, fin d'un `if` |
| 🤞 | `try` |
| 😱 | `except` : `😱 variable type` |
| 😌 | `else` d'un `try` |
| 🧹 | `finally` |
| 🔚 | fin d'un `try` |
| 🚨 | `raise` |

### Feuille de route (pas encore implémenté)
Le code source de l'interpréteur (`b.py`) ne liste plus aucune fonctionnalité
prévue. Le support des nombres aléatoires, les appels façon objet/attribut,
les paramètres nommés, les boucles `for` et `while`, les fonctions définies
par l'utilisateur, la création d'objets (classes), les erreurs (`try`,
`except`, `finally`, `raise`) et un grand nombre de caractères spéciaux
figuraient auparavant ici comme prévus — ils sont maintenant implémentés (voir
les sections ci-dessus).

Ce que Python a encore et pas UwU Script : l'héritage, les valeurs par défaut
des paramètres, les fonctions données en argument (donc `map`, `filter` ou
`sorted(key=...)` ne peuvent pas recevoir de fonction), `lambda`, les
compréhensions, les générateurs (`yield`), `with`, `global`, les décorateurs,
les littéraux de dictionnaire, de tuple et d'ensemble, l'affectation à un
élément d'une liste, les comparaisons `>=` et `<=`, et les `and` / `or`
court-circuités (les deux côtés sont toujours évalués).
