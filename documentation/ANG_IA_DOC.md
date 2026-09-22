# UwU Script

UwU Script is a programming language that uses **only** emojis as syntax.
It is heavily inspired by Python.

> **Note on this document.** This file corrects the original `README.md`:
> it fixes spelling/grammar issues and, more importantly, re-aligns every
> emoji reference with what is actually implemented in `b.py` / `c.py`.
> The original documentation had drifted out of sync with the interpreter
> (e.g. it referenced emojis for `e`, `f`, `g`, `t`, `v`, `x`, `y`, `!`,
> `\n`, `upper` and "end if" that no longer exist in the code).

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
The `print` function is 🪶.

```
🪶♓🔱🛴🛴🅾️⚰️〰️🅾️®️🛴🆔📦
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

There is currently no emoji mapped to `"."` (period) in the interpreter.

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
they stay separate (joined with `", "` when printed together):

```
🪶🅰️1️⃣📦
🪶🟢🔴📦
🪶🕳️🕳️📦
```
Result:

`a 1`

`True False`

`None None`

When two consecutive values are both `str` or both `int`, they are merged:

```
🪶🅰️🅱️📦
🪶0️⃣1️⃣0️⃣📦
```
Result:

`ab`

`10`

You can use ⛓️‍💥 to force two values to stay separate (joined with `", "`):

```
🪶🅰️⛓️‍💥🅱️📦
🪶0️⃣⛓️‍💥1️⃣0️⃣📦
```
Result:

`a b`

`0 10`

#### List
Use 🌜🌛 to create a list. Lists have a variable size and can contain
other lists.

```
🪶🌜🅰️⛓️‍💥🅱️0️⃣⛓️‍💥1️⃣0️⃣🟢🔴🕳️🌜🌛🌛📦
```
Result:

`[a, b, 0, 10, True, False, None, []]`

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
| 🔎 | `find` | Dynamically looks up and calls a builtin or module function by name |
| 🪞 | `list.copy` | Same as Python |
| 📨 | `list.append` | Same as Python |
| 🎞️ | `list.extend` | Same as Python |
| 🗑️ | `list.remove` | Same as Python |
| 🍿 | `list.pop` | Same as Python |
| ⁉️ | `input` | Same as Python |

Use 📦 to mark the end of a function's parameters.
You can nest function calls:

```
🪶🅰️🔠🅱️📦©️📦
```
Result:

`aBc`

### Operators

| Emoji | Python | Action |
|----|-------|------|
| ➕ | `+` | Addition |
| ➖ | `-` | Subtraction |
| ➗ | `/` | Division |
| 🪵 | `//` | Floor division |
| 🪙 | `%` | Modulo |
| ✳️ | `*` | Multiplication |
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
| ⚪️ | N/A | Reserved / not implemented yet (currently a no-op placeholder) |

To use an operator, place it between two values:

```
🪶1️⃣➕2️⃣📦
🪶🔴🤝🟢📦
```
Result:

`3`

`False`

There is no operator priority in UwU Script: all operations are evaluated
left to right.

```
🪶1️⃣➕2️⃣✳️3️⃣📦
```
Result:

`9`

Inside 🌜🌛, if the content only contains operators and produces a single
value, it is not treated as a list but as that plain value. This lets you
control evaluation order:

```
🪶🌜1️⃣➕🌜2️⃣✳️3️⃣🌛🌛📦
🪶🌜🌜1️⃣➕2️⃣🌛🌛📦
🪶🌜1️⃣➕2️⃣🅰️🌛📦
```
Result:

`7`

`[3]`

`[3, a]`

### Variables

UwU Script has no `=` assignment. You simply put an unknown emoji (or an
existing variable) at the start of the line, followed by its new value.

```
😀5️⃣0️⃣
🪶😀📦

😀1️⃣0️⃣
🪶😀📦
```
Result:

`50`

`10`

You can assign several variables on the same line:

```
😀😛5️⃣⛓️‍💥0️⃣
🪶😀😛📦

😀😇8️⃣⛓️‍💥3️⃣
🪶😀😛😇📦
```
Result:

`5 0`

`8 0 3`

### If
The `if` keyword is 🤔, and a boolean value must follow it directly.
The `if` block continues until the next 🔚. Everything between 🤔 and 🔚
is only executed if the boolean is `True`.

```
😀8️⃣💪2️⃣
🪶😀📦

🤔😀
🪶🔠®️📦ℹ️🐍♓™️📦
🔚
```
Result:

`True`

`Right`

To run something when the boolean is `False`, use 😌. Do not put a 🔚
before 😌:

```
😀8️⃣🤏2️⃣
🪶😀📦

🤔😀
🪶🔠®️📦ℹ️🐍♓™️📦

😌
🪶🔠🆖📦🅾️™️⚰️🔠®️📦ℹ️🐍♓™️📦
🔚
```
Result:

`False`

`Not Right`

You can use 😏 to check a second condition when the first one is `False`,
then a third one, and so on:

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
Result:

`3 Right`

You can also use 😏 without a trailing 😌:

```
🤔🔴
🪶1️⃣⛓️‍💥🔠®️📦ℹ️🐍♓™️📦

😏🟢
🪶2️⃣⛓️‍💥🔠®️📦ℹ️🐍♓™️📦
🔚
```
Result:

`2 Right`

### Roadmap (not implemented yet)
The interpreter's source code (`b.py`) contains comments describing
features that are planned but **not yet available** — there is currently
no emoji bound to them in the conversion table:

- `for` loops (planned emoji: 🌀)
- `while` loops (planned emoji: 🤗)
- User-defined functions with parameters and `return` (planned emojis: 🌏, 👉, 👈, 🙏, 🔃)
- Random number support
- Object/method-style function calls
- Additional special characters

Do not rely on these — using their placeholder emojis today will fail,
since they are not registered in the conversion table yet.
