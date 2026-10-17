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
| ❓ | `"!"` (currently mapped to `!` as well, not `?` — this looks like a bug in the interpreter, documented here as-is) |
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
| #️⃣ | `"#"` | 👉 | `"{"` |
| ▶️ | `">"` | 👈 | `"}"` |
| ◀️ | `"<"` | 🫸 | `"["` |
| 🥓 | `"="` | 🫷 | `"]"` |

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

`🚫 🤷 🪶 🤷 🤙 🫵 🖕` (error, program stops)

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
before it, or no value after it, stops the program (`error7` / `error8`).

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
line with a name and no value stops the program with `error9`.

```
😀5️⃣⛓️‍💥🅰️
🪶🤙😀📦
```
Result:

`5`

A variable can hold any value, including a function (see "Function
References") and the result of a function call.

### If
The `if` keyword is 🤔, and a boolean value must follow it directly.
The `if` block continues until the next 🔚. Everything between 🤔 and 🔚
is only executed if the boolean is `True`.

A comparison can be assigned to a variable like any other value. The
condition after 🤔 must be a single boolean value — a variable holding
one, or a comparison grouped with 🌜🌛 — and a comparison written
directly after 🤔 is not supported, so the examples below store it first:

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

### Roadmap (not implemented yet)
The interpreter's source code (`b.py`) contains comments describing
features that are still planned but **not yet available**:

- `for` loops (planned emoji: 🌀)
- `while` loops (planned emoji: 🤗)
- User-defined functions with parameters and `return` (planned emojis: 🌏, 🙏, 🔃 — 👉/👈 were originally sketched for this too, but have since been reused for `{`/`}`)
- Creating objects

Random numbers, object/attribute-style calls, and a large set of special
characters were previously listed here as planned — they are now
implemented (🎲/🎰/🎁/⏳, 🐙, and the punctuation table above).

Do not rely on the remaining placeholders — using them today will fail,
since they are not registered in the conversion table yet.
