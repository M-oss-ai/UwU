# UwU Script

UwU Script is a programming language that uses **only** emojis as syntax.
It is heavily inspired by Python.

> **Note on this document.** This file corrects the original `README.md`
> and is kept in sync with the actual interpreter (`b.py` / `c.py`).
> Every example below was run against the current code, not just
> hand-derived.

## Documentation

### Comments
Any character that is not an emoji is ignored by the interpreter.
Spaces and tabs are not part of the syntax.

If you want to use emoji characters inside a comment without them being
interpreted, start the comment with 😶. Every emoji found after 😶 on that
line is ignored.

#### Example
```
Letters are ignored 😶 ❤️🌷 these emojis are ignored too 🌷❤️
```

### Hello World
The traditional first program is to print "Hello world!" to the console.
The `print` function is 🪶. As explained in "Functions" below, a function
emoji only runs when 🤙 follows it directly.

```
🪶🤙♓🔱🛴🛴🅾️⚰️〰️🅾️®️🛴🆔📦
```
Result:

`hello world`

### Conversion Table

| Emoji | Value |
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

Punctuation and other special characters:

| Emoji | Value | Emoji | Value |
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

Every emoji has a single meaning. 🤜 🤛 and 🫲 are the characters `{`, `}` and
`]`. 👉, 👈 and 🫷 are keywords, not characters: 👉 👈 surround the parameters of
a function or the arguments of a class, and 🫷 closes a loop, a function or a
class (see "Loops", "User functions" and "Classes and objects"). A keyword has
no value, so it cannot be used inside an expression.

### Types
You can get the type of a value with 🏷️.

To convert between types, use:

| Emoji | Type |
|----|-------|
| 🔤 | `str` |
| 🔢 | `int` |
| ⚖️ | `bool` |
| 📋 | `list` |

When two consecutive values do not have the same type, or are `bool`/`None`,
they stay separate and are printed with a single space between them
(Python's `print` default separator):

```
🪶🤙🅰️1️⃣📦
🪶🤙🟢🔴📦
🪶🤙🕳️🕳️📦
```
Result:

`a 1`

`True False`

`None None`

When two consecutive values are both `str` or both `int`, they are merged:

```
🪶🤙🅰️🅱️📦
🪶🤙0️⃣1️⃣0️⃣📦
```
Result:

`ab`

`10`

You can use ⛓️‍💥 to force two values to stay separate (they are still
printed with a single space between them):

```
🪶🤙🅰️⛓️‍💥🅱️📦
🪶🤙0️⃣⛓️‍💥1️⃣0️⃣📦
```
Result:

`a b`

`0 10`

#### List
Use 🌜🌛 to create a list. Lists have a variable size and can contain
other lists. Printing a list uses Python's own representation, so
strings inside it are shown with quotes:

```
🪶🤙🌜🅰️⛓️‍💥🅱️0️⃣⛓️‍💥1️⃣0️⃣🟢🔴🕳️🌜🌛🌛📦
```
Result:

`['a', 'b', 0, 10, True, False, None, []]`

Use 👀 to index or slice a list — one index returns an item, two indices
return a slice:

```
🪶🤙👀🤙🌜🅰️⛓️‍💥🅱️⛓️‍💥©️🌛1️⃣📦📦
```
Result:

`b`

#### Retrieving an element (🎯)
Put 🎯 between a list (or a string) and an index to get that element —
the equivalent of Python's `("a", "b")[1]`. The first element has index
`0`:

```
🪶🤙🌜🅰️⛓️‍💥🅱️🌛🎯1️⃣📦
🪶🤙🅰️🅱️©️🎯1️⃣📦
```
Result:

`b`

`b`

The list can be a variable or the result of a function, the index can be
any value, and 🎯 can be chained to go into nested lists. When the element
is itself a list, it is kept whole:

```
😀🌜🌜1️⃣⛓️‍💥2️⃣🌛⛓️‍💥3️⃣🌛
🪶🤙😀🎯0️⃣📦
🪶🤙😀🎯0️⃣🎯1️⃣📦
```
Result:

`[1, 2]`

`2`

Unlike the other operators (see "Operators" below), 🎯 is always applied
first, so it needs no grouping. An index can be computed with 🌜🌛, which
is also how you write a negative index (there is no minus sign in
numbers):

```
😀🌜5️⃣⛓️‍💥6️⃣🌛
🪶🤙1️⃣0️⃣➕😀🎯1️⃣📦
🪶🤙😀🎯🌜0️⃣➖1️⃣🌛📦
```
Result:

`16`

`6`

An index outside the list stops the program with Python's `IndexError`.
👀 (above) does the same job as a function, and also cuts slices.

### Literal emoji (🎭)
Emoji normally mean something: 🅰️ is the letter `"a"`, ➕ is an operator,
and an emoji the language does not know is an error. 🎭 turns the emoji
that follow into plain text, exactly as typed, up to the next 📦. It is
how you print an emoji or keep one as data.

```
🪶🤙🎭😀🌀📦📦
```
Result:

`😀🌀`

The first 📦 ends the text and belongs to 🎭; the second one closes the
call to 🪶, as usual. The text is a normal string: it merges with
neighbouring strings and can be stored in a variable.

```
🪶🤙🎭😀📦🅰️📦
💚🎭🌀📦
🪶🤙💚📦
```
Result:

`😀a`

`🌀`

Without a closing 📦, the text runs to the end of the line. Only emoji can
be part of the text — anything else (letters, spaces) is dropped, like
everywhere else in a file. Operators and instructions are kept as text:

```
🪶🤙🎭➕🤙📦📦
```
Result:

`➕🤙`

To put a 📦 inside the text, close the text, then add `🎭📦📦`, which
stands for one literal 📦:

```
🪶🤙🎭😀🌀📦🎭📦📦📦
🪶🤙🎭📦📦📦
```
Result:

`😀🌀📦`

`📦`

### Functions

| Emoji | Function | Description |
|----|---------|-----------------|
| 🪶 | `print` | Same as Python |
| 🔠 | `str.upper` | Same as Python |
| 🏷️ | `type` | Same as Python |
| 🔢 | `int` | Same as Python |
| 🔤 | `str` | Same as Python |
| ⚖️ | `bool` | Same as Python |
| 📋 | `list` | Same as Python |
| 🧮 | `len` | Same as Python |
| 📏 | `range` | Same as Python |
| 🔽 | `min` | Same as Python |
| 🔼 | `max` | Same as Python |
| 🗃️ | `sum` | Same as Python |
| 🗂️ | `sorted` | Same as Python |
| 🙅 | `not` | Inverts `True`/`False` |
| 🏁 | `end` | Ends the program |
| 🔣 | `chr` | Same as Python |
| 🔎 | `find` | Dynamically looks up a builtin or module function by name and returns a **reference** to it (does not call it) |
| 🐙 | `find_attribut` | Dynamically looks up an attribute/method by name on a value and returns it — a reference if it's callable, the plain value otherwise (does not call it) |
| 🪞 | `list.copy` | Same as Python |
| 📨 | `list.append` | Same as Python |
| 🎞️ | `list.extend` | Same as Python |
| 🗑️ | `list.remove` | Same as Python |
| 🍿 | `list.pop` | Same as Python |
| 👀 | `select_in_list` | Index (`l[i]`) or slice (`l[i:j]`) a list |
| ⁉️ | `input` | Same as Python |
| 🎲 | `random.randint` | Same as Python |
| 🎰 | `random.random` | Same as Python |
| 🎁 | `random.choice` | Same as Python |
| ⏳ | `time.sleep` | Same as Python |

**A function emoji does not run on its own.** Encountering one produces a
**reference** to that function — see "Function References" below. To
actually call it, place 🤙 directly after its emoji; the function then
runs using whatever follows, up to the next 📦, as its parameters. You
can nest calls by putting 🤙 after each function that should run:

```
🪶🤙🅰️🔠🤙🅱️📦©️📦
```
Result:

`aBc`

**At the top level (a line's first emoji), a function must be called.**
Leaving it as a bare, uncalled reference with nothing consuming it is an
error — the interpreter assumes a statement that does nothing but build
an unused reference is a mistake:

```
🪶🔠📦
```
Result:

`🤦 🫵 🪶 🤙 ❓ 🙈 🤡 🛴1️⃣`

`Ligne 1 : 🪶 est une fonction, et écrire son nom ne l'exécute pas. Pour l'exécuter, écris 🤙 juste après son nom, puis les valeurs, puis 📦.`

This restriction only applies to the functions of the table, at the start
of a top-level line. A bare reference is perfectly fine — and is the
whole point — when it is used as a value: passed as an argument, printed
as part of a larger call, or stored in a variable (see below). A line
that starts with a *variable* holding a function is different: see
"Function References" below.

### Function References
Encountering a function emoji does not call it — it produces a
**reference** to that function, the function itself, not executed. Used
as plain data (e.g. printed on its own), a reference displays as
`<fonction NAME>`:

```
🪶🤙🔠📦
```
Result:

`<fonction str.upper>`

A reference is not the same type as a string, so — like any two
differently-typed values (see "Types" above) — it does not merge with an
adjacent string; it is printed with a space in between instead:

```
🪶🤙🔠Ⓜ️📦
```
Result:

`<fonction str.upper> m`

To actually **call** a function, put 🤙 directly *after* its emoji — the
values that follow (up to 📦) become its parameters:

```
🪶🤙Ⓜ️📦
```
Result:

`m`

A reference can also be stored in a variable and called later — 🤙
placed directly after a variable that holds a reference calls it, using
whatever follows the variable (up to 📦) as parameters:

```
😀🪶
🪶🤙😀📦
```
Result:

`<fonction print>`

Here 😀 stores the reference to `print` (never called on this line), and
the second line prints that reference as plain data.

```
😀🔠
🪶🤙😀🤙Ⓜ️📦
```
Result:

`M`

Here 😀 stores the reference to `str.upper`, and `🤙😀🤙Ⓜ️` calls it with
`"m"` as the argument.

A line that **starts** with a variable holding a function is a statement.
If 🤙 follows the variable, the function is called (its result is thrown
away, like for any other statement); otherwise the line is a normal
assignment and the variable is reassigned:

```
😀🪶
😀🤙Ⓜ️📦
```
Result:

`m`

```
😀🪶
😀🔠
🪶🤙😀🤙Ⓜ️📦📦
```
Result:

`M`

Here the second line has no 🤙, so it reassigns 😀 to `str.upper`; the
third line calls it.

The result of calling a stored function can be stored like any other
value:

```
😀🔠
💚😀🤙Ⓜ️📦
🪶🤙💚📦
```
Result:

`M`

### Named parameters (📛)
Some functions take named parameters, like the `sep` and `end` of `print`.
Write the name (it is text, spelled with the letter emoji), then 📛, then
the value, among the other parameters. This is
`print("hello world", end=". \n")`:

```
🪶🤙♓🔱🛴🛴🅾️⚰️〰️🅾️®️🛴🆔⛓️‍💥🔱🆖🆔📛⚫️⚰️⤵️📦
🪶🤙Ⓜ️📦
```
Result:

`hello world. `

`m`

Here `end` replaces the usual line break of `print` with a dot, a space and
a line break (`⚫️⚰️⤵️`), so the second `print` starts on a new line.

A named parameter is one more item of the parameter list. When two texts
follow each other — the previous parameter and the name, or a value and the
next name — separate them with ⛓️‍💥, otherwise they merge (see "Types"):

```
🪶🤙🅰️⛓️‍💥🅱️⛓️‍💥💲🔱🅿️📛🚥⛓️‍💥🔱🆖🆔📛❗📦
```
Result:

`a-b!`

The value goes up to the next ⛓️‍💥 or 📦 and can be any expression: 📛 is
applied after the operators (and after 🎯), so it never needs grouping.

```
🪶🤙🅰️⛓️‍💥🅱️⛓️‍💥💲🔱🅿️📛🚥➕🚥📦
```
Result:

`a--b`

It works with any function that accepts the name, whatever the function
is: a function of the table, one found with 🔎, or one stored in a variable
(called as a statement when the line starts with the variable).

```
🪶🤙🗂️🤙🌜1️⃣⛓️‍💥3️⃣⛓️‍💥2️⃣🌛⛓️‍💥®️🔱♈🔱®️💲🔱📛🟢📦📦
🪶🤙🔢🤙🎏🎏⛓️‍💥🅱️🅰️💲🔱📛1️⃣6️⃣📦📦
😀🪶
😀🤙🅰️⛓️‍💥🅱️⛓️‍💥💲🔱🅿️📛🚥📦
```
Result:

`[3, 2, 1]`

`255`

`a-b`

A name the function does not know is a Python `TypeError`. A 📛 with no name
before it, or no value after it, stops the program with an error (see "Error
messages").

### Dynamic Lookup (find / find_attribut)
🔎 (`find`) and 🐙 (`find_attribut`) retrieve functions and attributes
that don't have their own emoji, by name. Like every function, they only
ever return a **reference** — they never call what they find. To use the
result, store it in a variable and call the variable with 🤙, exactly as
in "Function References" above.

`find` takes a name (a string) and looks it up first among Python's
builtins:

```
😀🔎🤙🛴🔱🆖📦
🪶🤙😀🤙♓ℹ️📦📦
```
Result:

`2`

Here 😀 stores a reference to the builtin `len` (looked up by the string
`"len"`, spelled out letter by letter), and the second line calls it on
`"hi"`.

Give `find` a second name — a module — to reach a function from any
importable module, not just the built-in table:

```
🥑🔎🤙®️🅰️🆖🆔ℹ️🆖™️⛓️‍💥®️🅰️🆖🆔🅾️Ⓜ️📦
🪶🤙🥑🤙1️⃣⛓️‍💥1️⃣0️⃣📦📦
```
Result: a random integer between `1` and `10` (`random.randint(1, 10)`).

Note the ⛓️‍💥 between the two names: without it, the adjacent strings
`"randint"` and `"random"` would merge into one (see "Types" above).

`find_attribut` takes a value and an attribute name, and returns
whatever `getattr` would — a bound method reference if the attribute is
callable, or the plain value otherwise:

```
💚🐙🤙♓ℹ️⛓️‍💥⛎🅿️🅿️🔱®️📦
🪶🤙💚🤙📦📦
```
Result:

`HI`

Here 💚 stores a reference to `"hi".upper`, and the second line calls it
with no arguments.

```
🥝🐙🤙5️⃣⛓️‍💥®️🔱🅰️🛴📦
🪶🤙🥝📦
```
Result:

`5`

Here `"real"` names a plain (non-callable) attribute of `5`, so 🥝 holds
the value itself, not a reference — printing it needs no 🤙.

#### What can be found
The lookup is a plain `getattr`, so any builtin and any function of any
importable module can be found, not just the ones that have their own
emoji (checked on every builtin with a lowercase name and on the public
functions of `math`, `random`, `time`, `json`, `statistics`, `itertools`,
`operator`, `functools`, `os`, `sys`, `re`, `textwrap`, `datetime` and
`calendar`). A value that is not a function (like `math.pi`) is returned
as is, and a module found this way can be given to 🐙 to reach what is
inside it.

#### Spelling a name
A name is text, built from the letter emoji and 🥿 (`_`). Digits are
numbers, not text, so a name that contains some is assembled with ➕ and
🔤 (`str`); capital letters come from 🔠 the same way. For instance
`math.log10`:

```
😀🔎🤙🛴🅾️🐍➕🔤🤙1️⃣0️⃣📦⛓️‍💥Ⓜ️🅰️™️♓📦
🪶🤙😀🤙1️⃣0️⃣0️⃣0️⃣📦📦
```
Result:

`3.0`

#### Limits
- **Not everything has a name to look up.** 🙅, 🏁, 👀, 🔎 and 🐙 are
  defined by the interpreter itself (`b.py`), and `find` refuses the
  modules `b` and `c`: use their own emoji.
- **A function cannot be passed as an argument**, not even as a named
  parameter. A reference given as a parameter reaches the called function
  as the text `<fonction NAME>` (that is what makes printing a reference
  readable), so functions that expect a function — `map`, `filter`,
  `functools.reduce`, a `key=` parameter, or 🐙 applied to a function or a
  class — cannot be used.

### Operators

| Emoji | Python | Action |
|----|-------|------|
| ➕ | `+` | Addition |
| ➖ | `-` | Subtraction |
| ➗ | `/` | Division |
| 🪵 | `//` | Floor division |
| 🪙 | `%` | Modulo |
| *️⃣ | `*` | Multiplication |
| ⚡️ | `**` | Exponentiation |
| 🟥 | N/A | Root (`before ** (1 / after)`, e.g. `after = 2` gives a square root) |
| 🟰 | `==` | Equality |
| 🚫 | `!=` | Inequality |
| 💪 | `>` | Greater than |
| 🤏 | `<` | Less than |
| 🤝 | `and` | Logical AND |
| 🔀 | `or` | Logical OR |
| 📥 | `in` | Membership test |
| 📤 | `not in` | Negative membership test |
| ⚪️ | N/A | Joins two integers into a decimal number: `float(str(before) + "." + str(after))` |
| 🎯 | `[ ]` | Element at an index: `list 🎯 index` (see "Retrieving an element") |

To use an operator, place it between two values:

```
🪶🤙1️⃣➕2️⃣📦
🪶🤙🔴🤝🟢📦
```
Result:

`3`

`False`

The decimal-join operator:

```
🪶🤙1️⃣⚪️2️⃣📦
```
Result:

`1.2`

There is no operator priority in UwU Script: all operations are evaluated
left to right — except 🎯, which is always applied first (see "Retrieving
an element").

```
🪶🤙1️⃣➕2️⃣*️⃣3️⃣📦
```
Result:

`9`

Inside 🌜🌛, if the content only contains operators and produces a single
value, it is not treated as a list but as that plain value. This lets you
control evaluation order:

```
🪶🤙🌜1️⃣➕🌜2️⃣*️⃣3️⃣🌛🌛📦
🪶🤙🌜🌜1️⃣➕2️⃣🌛🌛📦
🪶🤙🌜1️⃣➕2️⃣🅰️🌛📦
```
Result:

`7`

`[3]`

`[3, 'a']`

### Variables

UwU Script has no `=` assignment. A line that starts with an unknown
emoji, or with an existing variable, assigns it: everything after that
first emoji is the value.

```
😀5️⃣0️⃣
🪶🤙😀📦

😀1️⃣0️⃣
🪶🤙😀📦
```
Result:

`50`

`10`

Only one variable is assigned per line, so a second name on the line is
read as part of the value (and is an error if it is unknown). If the value
is made of several values separated with ⛓️‍💥, the first one is kept. A
line with a name and no value stops the program with an error.

```
😀5️⃣⛓️‍💥🅰️
🪶🤙😀📦
```
Result:

`5`

A variable can hold any value, including a function (see "Function
References") and the result of a function call.

The emoji that belong to the language — letters, digits, functions,
operators and keywords such as 🌀 or 🤔 — cannot be used as variable names.

### If
The `if` keyword is 🤔, followed by a condition: the first value of what
follows is tested. The `if` block continues until the next 🔚. Everything
between 🤔 and 🔚 is only executed if the condition is true. The condition
can be a comparison written right after 🤔:

```
🤔8️⃣💪2️⃣
🪶🤙🔠🤙®️📦ℹ️🐍♓™️📦
🔚
```
Result:

`Right`

It can also be a variable holding a boolean: a comparison can be assigned
to a variable like any other value, and tested later.

```
😀8️⃣💪2️⃣
🪶🤙😀📦

🤔😀
🪶🤙🔠🤙®️📦ℹ️🐍♓™️📦
🔚
```
Result:

`True`

`Right`

To run something when the boolean is `False`, use 😌. Do not put a 🔚
before 😌:

```
😀8️⃣🤏2️⃣
🪶🤙😀📦

🤔😀
🪶🤙🔠🤙®️📦ℹ️🐍♓™️📦

😌
🪶🤙🔠🤙🆖📦🅾️™️⚰️🔠🤙®️📦ℹ️🐍♓™️📦
🔚
```
Result:

`False`

`Not Right`

You can use 😏 to check a second condition when the first one is `False`,
then a third one, and so on:

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
Result:

`3 Right`

You can also use 😏 without a trailing 😌:

```
🤔🔴
🪶🤙1️⃣⛓️‍💥🔠🤙®️📦ℹ️🐍♓™️📦

😏🟢
🪶🤙2️⃣⛓️‍💥🔠🤙®️📦ℹ️🐍♓™️📦
🔚
```
Result:

`2 Right`

### Loops
A `for` loop repeats a block for every item of a range, a list or a string.
Write 🌀, then the variable that receives each item (an unused emoji, or an
existing variable), then the sequence. The block is made of the following
lines and ends with a line containing only 🫷:

```
🌀😀📏🤙3️⃣📦
🪶🤙😀📦
🫷
```
Result:

`0`

`1`

`2`

The sequence is the first value after the variable: here `📏🤙3️⃣📦` is
`range(3)`, but it can also be a list, a string or a variable holding one.
After the loop, the variable keeps its last value.

```
🌀😀🌜🅰️⛓️‍💥🅱️⛓️‍💥©️🌛
🪶🤙😀📦
🫷
```
Result:

`a`

`b`

`c`

A `while` loop uses 🤗 followed by a condition (like 🤔 does). The block is
repeated as long as the condition is true, and the condition is evaluated
again before each pass:

```
😀0️⃣
🤗😀🤏3️⃣
🪶🤙😀📦
😀😀➕1️⃣
🫷
```
Result:

`0`

`1`

`2`

Inside a loop, ⏭️ goes straight to the next pass and 🛑 leaves the loop.
They can be placed anywhere in the block, typically inside an `if`, and
they only act on the innermost loop:

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
Result:

`0`

`1`

`3`

`4`

Loops can contain other loops, `if` blocks and function definitions. ⏭️ or
🛑 outside a loop, a loop that is never closed and a header with nothing to
loop on stop the program with an error.

### User functions
🌏 defines a function. Write 🌏, the name of the function (an unused emoji,
or an existing variable), then 👉, the names of the parameters (unused
emoji, one after the other) and 👈. The body is made of the following lines
and the definition ends with a line containing only 🫷, like a loop. 🙏 returns a value:

```
🌏💚👉🍎🍌👈
🙏🍎➕🍌
🫷
🪶🤙💚🤙1️⃣⛓️‍💥2️⃣📦📦
```
Result:

`3`

A function is called like any other: 🤙 right after its name, then the
parameters up to 📦. Named parameters work too, giving the parameter's
emoji as text with 🎭. A call with the wrong number of parameters gives the
usual errors.

🙏 leaves the function immediately — even from inside a loop or an `if` —
and gives back the first value written after it. Without 🙏, or with 🙏
alone, the function returns `None`:

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
Result:

`6`

A function can call itself:

```
🌏🧱👉📐👈
🤔📐🤏2️⃣
🙏1️⃣
🔚
🙏📐*️⃣🧱🤙📐➖1️⃣📦
🫷
🪶🤙🧱🤙5️⃣📦📦
```
Result:

`120`

The parameters, and every variable assigned in the body, are local: they
disappear when the function returns and never change a variable of the
same name outside. Variables defined outside can be read. (A list given as
a parameter is not copied, so changing it — with 📨 for example — is
visible outside.)

```
🥕5️⃣
🌏🍞👉👈
🥕9️⃣
🙏🥕
🫷
🪶🤙🍞🤙📦⛓️‍💥🥕📦
```
Result:

`9 5`

A function is an ordinary variable, like the ones holding `print` in
"Function References": it can be reassigned, copied into another variable,
defined again, or defined over a variable that held something else.
Printing it gives `<fonction NAME>`:

```
🌏💚👉👈
🙏1️⃣
🫷
🥑💚
💚5️⃣
🪶🤙🥑🤙📦⛓️‍💥💚📦
```
Result:

`1 5`

Here 🥑 received a copy of the function, then 💚 was reassigned to a number.

🙏 outside a function stops the program, and so does a definition whose
first line has no 👉 … 👈. A recursion can go several hundred levels deep.

### Classes and objects
A class is a model that builds objects. 🏛️ defines one: write 🏛️, the name
of the class (an unused emoji, or an existing variable), then, between 👉
and 👈, the arguments of the class. The arguments can be left out together
with 👉 👈. The class is made of the following lines and ends with a line
containing only 🫷.

Calling the class like a function — 🤙 right after its name, then the values
up to 📦 — creates an object. Each value is stored in the object, under the
emoji of the matching argument, and 🔗 reads it: `🐕🔗🦴` is the attribute 🦴
of the object 🐕.

```
🏛️🐶👉🦴🎂👈
🫷
🐕🐶🤙3️⃣⛓️‍💥5️⃣📦
🪶🤙🐕🔗🦴⛓️‍💥🐕🔗🎂📦
```
Result:

`3 5`

The ⛓️‍💥 keeps the two numbers apart (see "Types"). The name written after 🔗
is an emoji taken as it is: it does not have to be a variable. 🔗 is applied
before the operators, like 🎯, and the two chain from left to right. Here
`😀🎯1️⃣🔗🦴` is the attribute 🦴 of the second item of the list 😀, and ➕ then
uses that result:

```
🏛️🐶👉🦴👈
🫷
😀🌜🐶🤙1️⃣📦⛓️‍💥🐶🤙2️⃣📦🌛
🪶🤙😀🎯1️⃣🔗🦴➕1️⃣0️⃣📦
```
Result:

`12`

A line that starts with an object, 🔗, a name and a value gives that value to
the attribute — and creates the attribute when the object did not have it.
As for variables, only the first value is kept. Attributes can be chained to
reach an object kept inside another one: `🐕🔗🐈🔗🦴`.

```
🏛️🐶👉🦴👈
🫷
🐕🐶🤙3️⃣📦
🐕🔗🦴🐕🔗🦴➕1️⃣
🐕🔗🎂9️⃣
🪶🤙🐕🔗🦴⛓️‍💥🐕🔗🎂📦
```
Result:

`4 9`

Reading an attribute that does not exist is Python's `AttributeError`.

#### Functions of a class
A function defined inside a class (🌏 … 🫷, see "User functions") works on
the objects of the class. Its first parameter receives the object (any unused
emoji — here 🙋); the other parameters are the ones written in the call. To
call it, write the object, 🔗, the name of the function, then 🤙 and the
parameters up to 📦:

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
Result:

`5`

The object in front of 🔗 is given automatically, so it is not written
between 🤙 and 📦. As for any function, a call alone on a line —
`🐕🔗🍖🤙3️⃣📦` — runs the function and drops the result, and without 🤙,
`🐕🔗🍖` is a reference to the function, which can be kept in a variable and
called later. A function of a class can call the other ones through its
first parameter, and can call itself.

#### Values of a class
The lines of a class that are not function definitions run once, when the
class is defined, in a space of their own: the variables they assign do not
exist outside the class. They become values of the class, which every object
of the class can read — and the class itself, with 🔗. Giving an object an
attribute with the same name hides the value for this object only.

```
🏛️🐶👉👈
🦴3️⃣
🫷
🐕🐶🤙📦
🐈🐶🤙📦
🐕🔗🦴7️⃣
🪶🤙🐕🔗🦴⛓️‍💥🐈🔗🦴⛓️‍💥🐶🔗🦴📦
```
Result:

`7 3 3`

Any line can be written there (an `if`, a loop, a print...). They all run
once, at the definition, and not for each object:

```
🏛️🐶👉👈
🪶🤙🅾️🆖©️🔱📦
🫷
🐕🐶🤙📦
🐈🐶🤙📦
```
Result:

`once`

#### Preparing an object (🏗️)
A function named 🏗️ inside a class runs each time an object is created, right
after the arguments are stored, with the object as its only parameter. It is
the place to prepare what each object needs for itself:

```
🏛️🐶👉🦴👈
🌏🏗️👉🙋👈
🙋🔗🎂🙋🔗🦴*️⃣2️⃣
🫷
🫷
🐕🐶🤙4️⃣📦
🪶🤙🐕🔗🦴⛓️‍💥🐕🔗🎂📦
```
Result:

`4 8`

A value that must not be shared between the objects — like a list — has to be
created there: written directly in the class (see above), it would be the
same list for every object.

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
Result:

`[1] []`

🏗️ only exists as the name of a function inside a class: anywhere else it is
an error, like any other reserved emoji.

#### Objects are values
An object is a value like the others: it can be kept in a variable or in a
list, given to a function and compared. Printing an object, a class or the
type of an object (🏷️) gives:

```
🏛️🐶👉👈
🫷
🐕🐶🤙📦
🪶🤙🐕📦
🪶🤙🐶📦
🪶🤙🏷️🤙🐕📦📦
```
Result:

`<objet 🐶>`

`<classe 🐶>`

`<classe 🐶>`

Going through a list of objects and calling their functions:

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
Result:

`1`

`2`

Given to a function, an object is not copied: changing its attributes is
visible outside.

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
Result:

`9`

#### Errors and limits
A class that is never closed, and a header without a name or whose 👉 … 👈 is
not closed, stop the program with an error. So do 🏗️ outside a class, 🙏 in the
lines of a class (outside its functions), ⏭️ or 🛑 there outside a loop, a
wrong number of values when creating an object (the usual errors of
functions), 🔗 with nothing before it or no name after it, and a line
`object 🔗 name` with no value.

There is no inheritance. A class, like a function, cannot be given to
another function as a parameter.

### Errors (try / except / finally / raise)
Some operations fail with a Python error: dividing by zero, converting `abc`
into a number, reading an item that does not exist, asking an object for an
attribute it does not have... With nothing to handle it, an error stops the
program and is reported like every other error (see "Error messages"):

```
🪶🤙1️⃣➗0️⃣📦
🪶🤙🅰️🎏™️🔱®️📦
```
Result:

`💥 🫵 🐍 😭 🤡 🤣 🛴1️⃣`

`Ligne 1 : Python a rencontré une erreur que rien n'a rattrapée : ZeroDivisionError : division by zero. Un bloc 🤞 avec un 😱 permet de la rattraper.`

🤞 starts a block that handles errors, and 😱 says what to do when an error
happens in the lines after 🤞. The block ends with 🔚:

```
🤞
🪶🤙1️⃣➗0️⃣📦
😱😵
🪶🤙😵📦
🔚
```
Result:

`division by zero`

When an error happens, the rest of the lines after 🤞 is skipped, the lines
after 😱 run, and the program goes on after 🔚. 😱 is followed by the variable
that receives the error (an unused emoji, or an existing variable): printing
it shows its message, and it keeps the error after the block.

#### Choosing the errors
After the variable, 😱 can name the kind of error it handles:

| Emoji | Python error | Raised by |
|----|-------|------|
| ⚠️ | `Exception` | every error |
| 🙃 | `ValueError` | a wrong value, like `int("abc")` |
| 🧩 | `TypeError` | values that do not go together, like `1 + "a"` |
| ♾️ | `ZeroDivisionError` | a division by zero |
| 📍 | `IndexError` | an index outside the list |
| 🗝️ | `KeyError` | a missing key |
| 🫥 | `AttributeError` | a missing attribute |

Any other error of Python can be found by its name with 🔎, like any other
builtin (see "Dynamic Lookup").

```
🤞
🪶🤙🔢🤙🅰️🅱️©️📦📦
😱😵♾️
🪶🤙💤🔱®️🅾️📦
😱😵🙃
🪶🤙♈🅰️🛴⛎🔱📦
🔚
```
Result:

`value`

An error that no 😱 accepts goes on: it leaves the block, and stops the
program if nothing else handles it. The 😱 are tried in order and only the
first one that fits runs. To accept several kinds of error, give a list:

```
🤞
🪶🤙1️⃣➗0️⃣📦
😱😵🌜🙃⛓️‍💥♾️🌛
🪶🤙🛴ℹ️💲™️🔱🆔📦
🔚
```
Result:

`listed`

A 😱 with no type handles every error, so it must be the last one, and the
variable can be left out too:

```
🤞
🪶🤙1️⃣➗0️⃣📦
😱
🪶🤙©️🅰️⛎🐍♓™️📦
🔚
```
Result:

`caught`

What can be handled are the errors of Python and the values raised with 🚨
(see below). What cannot are the errors of the language itself (an unknown
emoji, a wrong number of parameters, a badly closed block...; see "Error
messages"), and 🏁, which is not an error: it leaves the block, but 🧹 runs
first.

#### Else and finally
Inside a 🤞 block, 😌 starts lines that run only when no error happened, and
🧹 starts lines that run in every case: after a success, after a handled
error, when the error is not handled (just before the program stops), and
when the block is left by 🙏, 🛑 or ⏭️. The parts come in this order: 😱 (as
many as needed), 😌 (once, and only with at least one 😱), then 🧹 (once). A
🤞 block needs at least one 😱 or a 🧹, and a part out of order or in excess
stops the program with an error, like a block that is not closed by 🔚.

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
Result:

`1`

`3`

`4`

With an error in the first part, 😌 is skipped and 🧹 still runs:

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
Result:

`2`

`4`

🧹 also runs when the block is left by 🙏 — the function still gives back its value:

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
Result:

`done`

`1`

And when it is left by 🛑 or ⏭️ inside a loop:

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
Result:

`0`

`f`

`1`

`f`

`f`

#### Raising an error (🚨)
🚨 raises the first value written after it. An error given a message with 🤙
carries that message:

```
🤞
🚨⚠️🤙🅱️🅾️🅾️Ⓜ️📦
😱😵
🪶🤙😵📦
🔚
```
Result:

`boom`

An error class alone raises a new error of that class:

```
🤞
🚨🙃
😱😵🙃
🪶🤙♈🅰️🛴⛎🔱📦
🔚
```
Result:

`value`

Any other value can be raised — a text, an object. A 😱 without a type
receives it as it is, and a 😱 with a type receives it when it is a value of
that type (🔤 for a text), or when the type is ⚠️:

```
🤞
🚨🅾️🅾️🅿️💲
😱😵
🪶🤙😵📦
🔚
```
Result:

`oops`

Raising an object of your own class gives you errors of your own kind:

```
🏛️🧨👉💬👈
🫷
🤞
🚨🧨🤙Ⓜ️ℹ️🆖🔱📦
😱😵🧨
🪶🤙😵🔗💬📦
🔚
```
Result:

`mine`

🚨 alone, inside a 😱, raises the error being handled again, for an outer
🤞 block to handle:

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
Result:

`inner`

`outer`

🚨 alone outside a 😱 is the Python error `RuntimeError`.

### Error messages
A mistake in a program — an unknown emoji, a block that is never closed, a call
with the wrong number of values, a Python error that nothing handles... —
stops it with an error. Every error is shown the same way, in two lines:

1. a line of emojis that makes fun of you, ending with 🛴 and the number of the
   line of `a.txt` where the error is (🛴 is the letter `l`: `🛴8️⃣0️⃣` reads
   "l80", line 80);
2. below it, a detailed description in words, which starts with `Ligne` and the
   same number (the descriptions are written in French, like the rest of the
   interpreter).

Both lines go to the standard output and the program ends with the exit code 1.
To find the line of an error, read the digits after the last 🛴 of the first
line.

```
😶 a comment

🪶🤙🥭📦
```
Result:

`🤡 🫵 🔍 🥭 🧠 🕳️ 🤣 🛴3️⃣`

`Ligne 3 : l'emoji 🥭 est inconnu. Ce n'est ni une valeur, ni une fonction, ni un mot-clé du langage, et aucune variable ne porte ce nom. Une variable se crée en début de ligne, suivie de sa valeur, et il faut la créer avant de s'en servir.`

The line number is the one an editor shows: comments, blank lines and lines
without any emoji count. It is the line where the error happens — inside a
function, the line in the body of the function; for a block that is never
closed, the line that opens the block. Whatever the program printed before the
error stays printed:

```
🪶🤙🅰️📦
🌀😀📏🤙3️⃣📦
🪶🤙😀📦
```
Result:

`a`

`🤡 🫵 🚪 🔓 🫷 ❌ 🐌 🛴2️⃣`

`Ligne 2 : le bloc ouvert ici par 🌀 n'est jamais fermé. Chaque boucle (🌀, 🤗), fonction (🌏) et classe (🏛️) se termine par une ligne contenant uniquement 🫷.`

```
🌏🧱👉👈
🪶🤙🥭📦
🫷
🧱🤙📦
```
Result:

`🤡 🫵 🔍 🥭 🧠 🕳️ 🤣 🛴2️⃣`

`Ligne 2 : l'emoji 🥭 est inconnu. Ce n'est ni une valeur, ni une fonction, ni un mot-clé du langage, et aucune variable ne porte ce nom. Une variable se crée en début de ligne, suivie de sa valeur, et il faut la créer avant de s'en servir.`

An error that comes from Python itself — a division by zero, a wrong
conversion, an index outside a list... — and that no 🤞 block handles is
reported the same way, and its description ends with the name and the message
of the Python error. So is a value raised with 🚨 that nothing handles.
(Setting the environment variable `UWU_DEBUG` to `1` shows Python's own
traceback instead: it helps to look for a bug in the interpreter itself.)

```
🪶🤙1️⃣➗0️⃣📦
🪶🤙🅰️🎏™️🔱®️📦
```
Result:

`💥 🫵 🐍 😭 🤡 🤣 🛴1️⃣`

`Ligne 1 : Python a rencontré une erreur que rien n'a rattrapée : ZeroDivisionError : division by zero. Un bloc 🤞 avec un 😱 permet de la rattraper.`

Here is every message, with its line of emojis (without the final 🛴 and the
number; 🥭 stands for the emoji concerned) and its cause:

| Line of emojis | Cause |
|----|------|
| 🤡 🫵 🔍 🥭 🧠 🕳️ 🤣 | An emoji that is not a variable (already defined), a value, a function or a keyword is used in an expression. |
| 🙄 🫵 🔑 🥭 🚫 🎁 🤦 | A keyword (🤔, 🌀, 🫷...) is used as a value, inside an expression. |
| 🤦 🫵 🔗 👻 ➡️ 🤡 | 🔗 with nothing before it (or only an operator or a separator). |
| 🙄 🫵 🔗 ❓ 🏷️ 🤡 | 🔗 with no attribute name after it. |
| 🤏 🫵 🧱 🍼 📦 🤡 | A function (or a class) is called with fewer values than it needs. |
| 🤯 🫵 🧱 🐘 📦 🤡 | A function (or a class) is called with more values than it accepts. |
| 🙄 🫵 📛 🪪 🕳️ 🤡 | 📛 with no name before it. |
| 🤦 🫵 📛 🎁 🕳️ 🤡 | 📛 with no value after it. |
| 🙄 🫵 ➕ 👻 🤡 🧮 | An operator at the start of an expression or of a line. |
| 🤦 🫵 ➕ 🕳️ 👻 🤡 | An operator at the end of an expression. |
| 🙄 🫵 🕳️ 🪹 💤 🤡 | A name, or 🤔 😏 🤗, with nothing to evaluate after it. |
| 🙄 🫵 🔗 🕳️ 🪹 🤡 | `object 🔗 name` with no value after the name. |
| 🤡 🫵 🚪 🔓 🫷 ❌ 🐌 | A loop, a function or a class that no 🫷 closes (the line is the one that opens it). |
| 🙄 🫵 🫷 🚪 🚫 🤡 | 🫷 when no loop, function or class is open. |
| 🤦 🫵 🥭 🤔 ❓ 🤡 | 😏, 😌 or 🔚 outside a block opened by 🤔 (or by 🤞 for 😌 and 🔚). |
| 🙄 🫵 🥭 🤞 ❓ 🤡 | 😱 or 🧹 outside a block opened by 🤞. |
| 🤯 🫵 😏 😌 🔀 🤡 | 😏 or 😌 in the wrong order in a block opened by 🤔 (two 😌, for instance). |
| 🤡 🫵 🤔 🚪 🔚 ❌ 🐌 | A block opened by 🤔 that no 🔚 closes. |
| 🤦 🫵 🫷 🧩 🚫 🤡 | 🫷 while a block opened by 🤔 is still open inside the block it would close. |
| 🤡 🫵 🥭 🔒 🚫 😂 | An emoji of the language used as the name of a variable, function, parameter, class, loop variable or error. |
| 🙄 🫵 🌀 🔁 ❓ 🤡 | 🌀 with no loop variable or nothing to loop over. |
| 🙄 🫵 🤗 🔁 ❓ 🤡 | 🤗 with no condition. |
| 🙄 🫵 🌏 🌍 ❓ 🤡 | The first line of a function is not 🌏 name 👉 parameters 👈. |
| 🤦 🫵 👯 🌏 🤡 | Two parameters of a function have the same emoji. |
| 🙄 🫵 🏛️ 🧱 ❓ 🤡 | The first line of a class is not 🏛️ name (👉 arguments 👈). |
| 🤦 🫵 👯 🏛️ 🤡 | Two arguments of a class have the same emoji. |
| 🤦 🫵 🤞 🪤 🕳️ 🤡 | A block opened by 🤞 with neither 😱 nor 🧹. |
| 🤯 🫵 🤞 😱 😌 🧹 🔀 🤡 | 😱, 😌, 🧹 in the wrong order, or too many of them, in a block opened by 🤞. |
| 🙄 🫵 😱 🕸️ 🔚 🤡 | 😱 with no type, when it is not the last 😱. |
| 🤡 🫵 🤞 🚪 🔚 ❌ 🐌 | A block opened by 🤞 that no 🔚 closes. |
| 🤦 🫵 🤞 🧩 🚫 🔚 🤡 | A block opened by 🤞 that is closed by 🫷, or with another block still open inside it. |
| 🙄 🫵 🙏 🏃 🚪 ❓ 🤡 | 🙏 outside a function. |
| 🙄 🫵 🛑 🔁 ❓ 🤡 | 🛑 outside a loop. |
| 🙄 🫵 ⏭️ 🔁 ❓ 🤡 | ⏭️ outside a loop. |
| 🤦 🫵 🥭 🤙 ❓ 🙈 🤡 | A line that starts with a function of the language but has no 🤙. |
| 🙄 🫵 🥭 🧱 ❓ 🤡 | A line that starts with a value (a letter, a digit, 🟢...). |
| 🤡 🫵 🥭 🪑 ❓ 😂 | A keyword that cannot start a line (🔗, 🤙, 📦, 🏗️...). |
| 💥 🫵 🐍 😭 🤡 🤣 | A Python error that nothing handles (division by zero, a wrong conversion, an index outside the list, a missing attribute, 🔎 used wrongly...). |
| 💥 🫵 🚨 🗑️ 🤡 🤣 | A value raised with 🚨 that nothing handles. |

### Summary of the keywords

| Emoji | Role |
|----|------|
| 🌀 | `for` loop: `🌀 variable sequence` |
| 🤗 | `while` loop: `🤗 condition` |
| ⏭️ | `continue` |
| 🛑 | `break` |
| 🫷 | end of a loop, a function or a class (alone on its line) |
| 🌏 | function definition: `🌏 name 👉 parameters 👈` |
| 🙏 | `return` |
| 🏛️ | class definition: `🏛️ name 👉 arguments 👈` |
| 🏗️ | name of the function that prepares each new object (inside a class) |
| 🔗 | attribute of an object: `object 🔗 name` |
| 🤔 😏 😌 🔚 | `if`, `elif`, `else`, end of an `if` |
| 🤞 | `try` |
| 😱 | `except`: `😱 variable type` |
| 😌 | `else` of a `try` |
| 🧹 | `finally` |
| 🔚 | end of a `try` |
| 🚨 | `raise` |

### Roadmap (not implemented yet)
The interpreter's source code (`b.py`) no longer lists any planned feature.
Random numbers, object/attribute-style calls, named parameters, `for` and
`while` loops, user-defined functions, creating objects (classes), errors
(`try`, `except`, `finally`, `raise`) and a large set of special characters
were all planned at some point — they are now implemented (see the sections
above).

Still missing compared to Python: inheritance, default values for
parameters, functions given as arguments (so `map`, `filter` or
`sorted(key=...)` cannot receive a function), `lambda`, comprehensions,
generators (`yield`), `with`, `global`, decorators, dictionary, tuple and set
literals, assigning to an item of a list, the comparisons `>=` and `<=`, and
short-circuit `and` / `or` (both sides are always evaluated).
