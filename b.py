import sys

def upper(text):
    return text.upper()

def get_type(value):
    if type(value) == Variable:
        return type(value.value)
        
    elif type(value) in (Instructions, Operation):
        print("error7")
        sys.exit(1)
    
    return type(value)

def convert_to_str(value):
    return str(value)

def convert_to_int(value):
    return int(value)

def convert_to_bool(value):
    return bool(value)

def creat_range(*arry): 
    return range(*arry)

def function_not(value):
    return not value

def fin(*arry):
    sys.exit(1)

class Instructions():
    def __init__(self, name):
        self.name = name

class Variable():
    def __init__(self, value):
        self.value = value

class Operation():
    def __init__(self, value):
    
        match value:
            case "plus":
                def calcule(beafor, after):
                    return beafor + after
            case "moin":
                def calcule(beafor, after):
                    return beafor - after
            case "divisé":
                def calcule(beafor, after):
                    return beafor / after
            case "division entière":
                def calcule(beafor, after):
                    return beafor // after
            case "modulo":
                def calcule(beafor, after):
                    return beafor % after
            case "fois":
                def calcule(beafor, after):
                    return beafor * after
            case "puissance":
                def calcule(beafor, after):
                    return beafor ** after
            case "racine":
                def calcule(beafor, after):
                    return beafor ** (1 / after)
            case "egale":
                def calcule(beafor, after):
                    return beafor == after
            case "pas egale":
                def calcule(beafor, after):
                    return beafor != after
            case "plus grand":
                def calcule(beafor, after):
                    return beafor > after
            case "plus petit":
                def calcule(beafor, after):
                    return beafor < after
            case "and":
                def calcule(beafor, after):
                    return beafor and after
            case "or":
                def calcule(beafor, after):
                    return beafor or after
        self.calcule = calcule
    
table = {
    "🅰️" : "a",
    "🅱️" : "b",
    "©️" : "c",
    "🆔" : "d",
    "😦" : "e",
    "🔥" : "f",
    "🦍" : "g",
    "♓" : "h",
    "ℹ️" : "i",
    "🎷" : "j",
    "🔑" : "k",
    "🛴" : "l",
    "Ⓜ️" : "m",
    "🆖" : "n",
    "🅾️" : "o",
    "🅿️" : "p",
    "🔍" : "q",
    "®️" : "r",
    "💲" : "s",
    "👕" : "t",
    "⛎" : "u",
    "🚗" : "v",
    "〰️" : "w",
    "🐦" : "x",
    "🦞" : "y",
    "💤" : "z",
    "⚰" : " ",
    "‼️" : "!",
    "👊" : ".",
    "🗨️" : "",
    "👇" : "\n",
    "0️⃣" : 0,
    "1️⃣" : 1,
    "2️⃣" : 2,
    "3️⃣" : 3,
    "4️⃣" : 4,
    "5️⃣" : 5,
    "6️⃣" : 6,
    "7️⃣" : 7,
    "8️⃣" : 8,
    "9️⃣" : 9,
    "🟢" : True,
    "🔴" : False,
    "🕳️" : None,
    "🪶" : print,
    "🐷" : upper,
    "🏷️" : get_type,
    "🔢" : convert_to_int,
    "🔤" : convert_to_str,
    "🔤" : convert_to_str,
    "⚖️" : convert_to_bool,
    "🧮" : len,
    "📏" : creat_range,
    "🔽" : min,
    "🔼" : max,
    "🗂️" : sorted,
    "🙅" : function_not,
    "🏁" : fin,
    "❓" : Instructions("input"),
    "🤐" : Instructions("chut"),
    "📦" : Instructions("end paramettres"),
    "⛓️‍💥" : Instructions("deconnecter"),
    "🌜" : Instructions("start liste"),
    "🌛" : Instructions("end liste"),
    "🔄" : Instructions("remplace"),
    "🎭" : Instructions("naturalise"),
    "🤔" : Instructions("if"),
    "😌" : Instructions("else"),
    "😏" : Instructions("elif"),
    "🫷" : Instructions("end"),
    "➕" : Operation("plus"),
    "➖" : Operation("moin"),
    "➗" : Operation("divisé"),
    "🪵" : Operation("division entière"),
    "🪙" : Operation("modulo"),
    "✖️" : Operation("fois"),
    "⚡" : Operation("puissance"),
    "🟥" : Operation("racine"),
    "🟰" : Operation("egale"),
    "🚫" : Operation("pas egale"),
    "💪" : Operation("plus grand"),
    "🤏" : Operation("plus petit"),
    "🤝" : Operation("and"),
    "🔀" : Operation("or")
}

# change 🔄 and 🎭

# get text white aski code

# get a function white text

# import a module white text

# integre float

# for 🌀 <new> <range or liste>
# continue 
# break
# end : next 🫷

# while 🤗 <booleant>
# continue 
# break
# end : next 🫷

# créé une fonction 🌏 <new> 👉 <new> <new> <new> 👈
# return 🙏
# end : next 🫷🔃
