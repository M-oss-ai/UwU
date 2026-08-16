import sys
import builtins
from importlib import import_module

NOM_FICHIER_PY = ["b", "c"]

def find(*arry):
    if len(arry) == 1:
        return getattr(builtins, arry[0])
    
    elif len(arry) == 2 and type(arry[1]) == str and arry[1] not in NOM_FICHIER_PY:
        return getattr(import_module(arry[1]), arry[0])()
    
    elif len(arry) == 2 and type(arry[1]) == list:
        return getattr(builtins, arry[0])(*arry[1])
    
    elif len(arry) >= 3 and arry[1] not in NOM_FICHIER_PY:
        if type(arry[2]) != list:
            return getattr(import_module(arry[1]), arry[0])(arry[2])
        return getattr(import_module(arry[1]), arry[0])(*arry[2])
    
    raise Exception("error8")

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
            case "in":
                def calcule(beafor, after):
                    return beafor in after 
            case "not in":
                def calcule(beafor, after):
                    return beafor not in after
            case ".":
                calcule = ""
                
        self.calcule = calcule
        
    
table = {
    "🅰️" : "a",
    "🅱️" : "b",
    "©️" : "c",
    "🆔" : "d",
    "🔱" : "e",
    "🎏" : "f",
    "🐍" : "g",
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
    "™️" : "t",
    "⛎" : "u",
    "♈" : "v",
    "〰️" : "w",
    "❌" : "x",
    "🩺" : "y",
    "💤" : "z",
    "⚰️" : " ",
    "❗" : "!",
    "❓" : "!",
    "⤵️" : "\n",
    "🗨️" : "",
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
    "🔠" : str.upper,
    "🏷️" : type,
    "🔢" : int,
    "🔤" : str,
    "⚖️" : bool,
    "📋" : list,
    "🧮" : len,
    "📏" : range,
    "🔽" : min,
    "🔼" : max,
    "🗃️" : sum,
    "🗂️" : sorted,
    "🙅" : function_not,
    "🏁" : fin,
    "🔣" : chr,
    "🔎" : find,
    "🪞" : list.copy,
    "📨" : list.append,
    "🎞️" : list.extend,
    "🗑️" : list.remove,
    "🍿" : list.pop,
    "⁉️" : input,
    "😶" : Instructions("chut"),
    "📦" : Instructions("end paramettres"),
    "⛓️‍💥" : Instructions("deconnecter"),
    "🌜" : Instructions("start liste"),
    "🌛" : Instructions("end liste"),
    "🎭" : Instructions("naturalise"),
    "🤔" : Instructions("if"),
    "😏" : Instructions("elif"),
    "😌" : Instructions("else"),
    "🔚" : Instructions("end"),
    "➕" : Operation("plus"),
    "➖" : Operation("moin"),
    "➗" : Operation("divisé"),
    "🟰" : Operation("egale"),
    "🪵" : Operation("division entière"),
    "🪙" : Operation("modulo"),
    "✳️" : Operation("fois"),
    "⚡️" : Operation("puissance"),
    "🟥" : Operation("racine"),
    "🚫" : Operation("pas egale"),
    "💪" : Operation("plus grand"),
    "🤏" : Operation("plus petit"),
    "🤝" : Operation("and"),
    "🔀" : Operation("or") ,
    "📥" : Operation("in"),
    "📤" : Operation("not in"),
    "⚪️" : Operation(".")
}

# random

# fonction d'objet

# caracteres spesiaux

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
