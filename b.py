import sys
import builtins
import time
import random
from importlib import import_module

NOM_FICHIER_PY = ["b", "c"]

def is_digit(string):
    try:
        float(string)
        return True
    except ValueError:
        return False

def select_in_list(liste, *arry):
    if len(arry) == 1:
        return liste[arry[0]]
    else:
        return liste[arry[0]:arry[1]]

def find_attribut(obj, atr):
    attribut = getattr(obj, atr, None)
    return attribut

def find(func, *arry):
    if len(arry) == 0 and func in builtins.__dict__:
        return getattr(builtins, func, None)
    
    elif len(arry) == 1 and type(func) == str and type(arry[0]) == str and arry[0] not in NOM_FICHIER_PY:
        return getattr(import_module(arry[0]), func, None)
            
    else:
        raise ValueError("🔎 attend le nom d'une fonction (du texte) ou, pour la fonction d'un module, le nom de la fonction puis celui du module (deux textes, le module ne pouvant pas être b ni c) ; ici aucun builtin Python ne porte ce nom ou les paramètres ne conviennent pas")

def function_not(value):
    return not value

def fin(*arry):
    sys.exit(1)

def function_name(func):
    return getattr(func, "__qualname__", getattr(func, "__name__", str(func)))

def sans_selecteur(emoji):
    return emoji.replace("︎", "").replace("️", "")

class Instructions():
    def __init__(self, name):
        self.name = name

class Variable():
    def __init__(self, value):
        self.value = value

class Parms_Noinatif():
    def __init__(self, directory):
        self.directory = directory

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
                def calcule(beafor, after):
                    return float(str(int(beafor)) + "." + str(int(after)))
                
            case "index":
                def calcule(beafor, after):
                    return beafor[after]

        self.calcule = calcule
        self.est_index = value == "index"
        
    
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
    "📞" : "\\",
    "🚥" : "-",
    "✴️" : "*",
    "🔘" : "•",
    "💵" : "$",
    "💶" : "€",
    "❤️" : "♥",
    "🦯" : "/",
    "💴" : "¥",
    "💷" : "£",
    "🥿" : "_",
    "⚫️" : ".",
    "🚦" : "|",
    "#️⃣" : "#",
    "▶️" : ">",
    "◀️" : "<",
    "🥓" : "=",
    "🌘" : "(",
    "🌒" : ")",
    "🫳" : "~",
    "✨" : "+",
    "🫐" : ":",
    "🏒" : ";",
    "⤴️" : ",",
    "🍺" : "'",
    "🍻" : "\"",
    "📎" : "&",
    "🎓" : "^",
    "🐌" : "@",
    "💯" : "%",
    "🤜" : "{",
    "🤛" : "}",
    "🫸" : "[",
    "🫲" : "]",
    "❗" : "!",
    "❓" : "?",
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
    "🐙" : find_attribut,
    "🪞" : list.copy,
    "📨" : list.append,
    "🎞️" : list.extend,
    "🗑️" : list.remove,
    "🍿" : list.pop,
    "👀" : select_in_list,
    "⁉️" : input,
    "🎲" : random.randint,
    "🎰" : random.random,
    "🎁" : random.choice,
    "⏳" : time.sleep,
    "⚠️" : Exception,
    "🙃" : ValueError,
    "🧩" : TypeError,
    "♾️" : ZeroDivisionError,
    "📍" : IndexError,
    "🗝️" : KeyError,
    "🫥" : AttributeError,
    "😶" : Instructions("chut"),
    "📦" : Instructions("end paramettres"),
    "⛓️‍💥" : Instructions("deconnecter"),
    "🌜" : Instructions("start liste"),
    "🌛" : Instructions("end liste"),
    "🎭" : Instructions("naturalise"),
    "🤙" : Instructions("executer"),
    "🤔" : Instructions("if"),
    "😏" : Instructions("elif"),
    "😌" : Instructions("else"),
    "🔚" : Instructions("end"),
    "🌀" : Instructions("for"),
    "🤗" : Instructions("while"),
    "🌏" : Instructions("def"),
    "👉" : Instructions("start definition"),
    "👈" : Instructions("end definition"),
    "🙏" : Instructions("return"),
    "⏭️" : Instructions("continue"),
    "🛑" : Instructions("break"),
    "🫷" : Instructions("end bloc"),
    "🏛️" : Instructions("class"),
    "🏗️" : Instructions("init"),
    "🔗" : Instructions("attribut"),
    "🤞" : Instructions("try"),
    "😱" : Instructions("except"),
    "🧹" : Instructions("finally"),
    "🚨" : Instructions("raise"),
    "📛" : Instructions("nomme"),
    "➕" : Operation("plus"),
    "➖" : Operation("moin"),
    "➗" : Operation("divisé"),
    "🟰" : Operation("egale"),
    "🪵" : Operation("division entière"),
    "🪙" : Operation("modulo"),
    "*️⃣" : Operation("fois"),
    "⚡️" : Operation("puissance"),
    "🟥" : Operation("racine"),
    "🚫" : Operation("pas egale"),
    "💪" : Operation("plus grand"),
    "🤏" : Operation("plus petit"),
    "🤝" : Operation("and"),
    "🔀" : Operation("or") ,
    "📥" : Operation("in"),
    "📤" : Operation("not in"),
    "⚪️" : Operation("."),
    "🎯" : Operation("index")
}

TABLE_SANS_SELECTEUR = {
    sans_selecteur(cle): cle
    for cle in table
}

# Les erreurs du langage. Chaque erreur affiche deux lignes (voir echouer dans c.py) :
#   1. une ligne d'emojis qui se moque de l'utilisateur, finie par 🛴 et le numéro de la ligne de a.txt
#   2. sa description détaillée, en toutes lettres
# {ligne}, {emoji}... sont remplacés au moment de l'erreur ; {if}, {end_bloc}... sont les emojis des mots-clés, pris dans la table
MESSAGES = {
    "emoji_inconnu": (
        "🤡 🫵 🔍 {emoji} 🧠 🕳️ 🤣",
        "Ligne {ligne} : l'emoji {emoji} est inconnu. Ce n'est ni une valeur, ni une fonction, ni un mot-clé du langage, et aucune variable ne porte ce nom. "
        "Une variable se crée en début de ligne, suivie de sa valeur, et il faut la créer avant de s'en servir."),
    "mot_cle_en_valeur": (
        "🙄 🫵 🔑 {emoji} 🚫 🎁 🤦",
        "Ligne {ligne} : {emoji} est un mot-clé du langage. Il structure le programme et n'a pas de valeur, donc il ne peut pas être utilisé au milieu d'une expression "
        "(comme paramètre d'une fonction, ou après le nom d'une variable par exemple)."),
    "attribut_sans_objet": (
        "🤦 🫵 {attribut} 👻 ➡️ 🤡",
        "Ligne {ligne} : le {attribut} sert à lire l'attribut d'un objet, il doit donc être placé juste après cet objet. "
        "Ici il n'y a rien devant lui, ou seulement un opérateur ou un séparateur."),
    "attribut_sans_nom": (
        "🙄 🫵 {attribut} ❓ 🏷️ 🤡",
        "Ligne {ligne} : le {attribut} doit être suivi du nom de l'attribut, c'est-à-dire d'un emoji. "
        "Ici il n'y a rien après lui, ou bien un mot-clé ou un opérateur."),
    "trop_peu": (
        "🤏 🫵 {nom} 🍼 📦 🤡",
        "Ligne {ligne} : {nom} reçoit {recus} valeur(s) alors qu'il en faut au moins {mini}. "
        "Les valeurs d'un appel se séparent avec {deconnecter} quand elles sont du même type, et l'appel se ferme avec {end_paramettres}."),
    "trop_de_valeurs": (
        "🤯 🫵 {nom} 🐘 📦 🤡",
        "Ligne {ligne} : {nom} reçoit {recus} valeur(s) alors qu'il n'en accepte que {maxi}. "
        "Vérifie les {deconnecter} et la fermeture de l'appel avec {end_paramettres}."),
    "nomme_sans_nom": (
        "🙄 🫵 {nomme} 🪪 🕳️ 🤡",
        "Ligne {ligne} : le {nomme} donne un nom à la valeur qui le suit, et ce nom (du texte) doit être écrit juste avant lui. "
        "Ici rien ne le précède."),
    "nomme_sans_valeur": (
        "🤦 🫵 {nomme} 🎁 🕳️ 🤡",
        "Ligne {ligne} : le {nomme} doit être suivi de la valeur du paramètre nommé. Ici il n'y a rien après lui."),
    "operateur_sans_gauche": (
        "🙄 🫵 {operateur} 👻 🤡 🧮",
        "Ligne {ligne} : l'opérateur {operateur} a besoin d'une valeur à sa gauche, mais il est au début. "
        "Un opérateur se place toujours entre deux valeurs."),
    "operateur_sans_droite": (
        "🤦 🫵 {operateur} 🕳️ 👻 🤡",
        "Ligne {ligne} : l'opérateur {operateur} a besoin d'une valeur à sa droite, mais il est à la fin. "
        "Un opérateur se place toujours entre deux valeurs."),
    "valeur_manquante": (
        "🙄 🫵 🕳️ 🪹 💤 🤡",
        "Ligne {ligne} : il manque une valeur. Après le nom d'une variable, ou après {if}, {elif} ou {while}, "
        "la ligne doit contenir de quoi calculer une valeur."),
    "attribut_sans_valeur": (
        "🙄 🫵 {attribut} 🕳️ 🪹 🤡",
        "Ligne {ligne} : il manque la valeur à donner à l'attribut. Une ligne qui commence par un objet, {attribut} et un nom "
        "doit continuer par la valeur de l'attribut (ou par {executer} pour appeler une fonction)."),
    "bloc_jamais_ferme": (
        "🤡 🫵 🚪 🔓 {end_bloc} ❌ 🐌",
        "Ligne {ligne} : le bloc ouvert ici par {ouvert} n'est jamais fermé. "
        "Chaque boucle ({for}, {while}), fonction ({def}) et classe ({class}) se termine par une ligne contenant uniquement {end_bloc}."),
    "fermeture_orpheline": (
        "🙄 🫵 {end_bloc} 🚪 🚫 🤡",
        "Ligne {ligne} : ce {end_bloc} ne ferme rien. Il sert à terminer une boucle ({for}, {while}), une fonction ({def}) ou une classe ({class}), "
        "et aucune n'est ouverte à cet endroit."),
    "si_orphelin": (
        "🤦 🫵 {emoji} 🤔 ❓ 🤡",
        "Ligne {ligne} : {emoji} n'a de sens qu'à l'intérieur d'un bloc ouvert par {if} (ou par {try} pour {else} et {end}), "
        "et aucun n'est ouvert à cet endroit."),
    "clause_orpheline": (
        "🙄 🫵 {emoji} 🤞 ❓ 🤡",
        "Ligne {ligne} : {emoji} n'a de sens qu'à l'intérieur d'un bloc {try}, et aucun n'est ouvert à cet endroit."),
    "si_mal_forme": (
        "🤯 🫵 {elif} {else} 🔀 🤡",
        "Ligne {ligne} : dans un bloc {if}, les parties se suivent dans cet ordre : {elif} autant de fois que nécessaire, "
        "puis {else} une seule fois, à la fin. Ici l'ordre n'est pas respecté."),
    "si_jamais_ferme": (
        "🤡 🫵 {if} 🚪 {end} ❌ 🐌",
        "Ligne {ligne} : le bloc {if} ouvert ici n'est jamais fermé. Il se termine par une ligne contenant uniquement {end}."),
    "fermeture_de_travers": (
        "🤦 🫵 {end_bloc} 🧩 🚫 🤡",
        "Ligne {ligne} : ce {end_bloc} arrive alors qu'un bloc {if} est encore ouvert à l'intérieur. Ferme d'abord ce bloc avec {end}."),
    "nom_reserve": (
        "🤡 🫵 {emoji} 🔒 🚫 😂",
        "Ligne {ligne} : l'emoji {emoji} fait déjà partie du langage (valeur, fonction ou mot-clé). "
        "On ne peut pas l'utiliser comme nom de variable, de fonction, de paramètre, de classe ou d'erreur : choisis un autre emoji."),
    "entete_for": (
        "🙄 🫵 {for} 🔁 ❓ 🤡",
        "Ligne {ligne} : une boucle {for} s'écrit : {for}, le nom de la variable de boucle (un emoji libre), puis ce qu'il faut parcourir "
        "(un range, une liste, un texte...). L'un des deux manque."),
    "entete_while": (
        "🙄 🫵 {while} 🔁 ❓ 🤡",
        "Ligne {ligne} : une boucle {while} s'écrit : {while} suivi d'une condition. La condition manque."),
    "entete_def": (
        "🙄 🫵 {def} 🌍 ❓ 🤡",
        "Ligne {ligne} : une fonction se définit ainsi : {def}, son nom, {start_definition}, ses paramètres (des emojis libres) puis {end_definition}. "
        "La première ligne de cette définition n'a pas cette forme."),
    "parametres_en_double": (
        "🤦 🫵 👯 {def} 🤡",
        "Ligne {ligne} : deux paramètres de la fonction portent le même emoji. Chaque paramètre doit être différent des autres."),
    "entete_class": (
        "🙄 🫵 {class} 🧱 ❓ 🤡",
        "Ligne {ligne} : une classe se définit ainsi : {class}, son nom, puis éventuellement {start_definition}, ses arguments (des emojis libres) et {end_definition}. "
        "La première ligne de cette définition n'a pas cette forme."),
    "arguments_en_double": (
        "🤦 🫵 👯 {class} 🤡",
        "Ligne {ligne} : deux arguments de la classe portent le même emoji. Chaque argument doit être différent des autres."),
    "try_sans_clause": (
        "🤦 🫵 {try} 🪤 🕳️ 🤡",
        "Ligne {ligne} : un bloc {try} a besoin d'au moins un {except} ou un {finally}. Sans eux, il ne sert à rien."),
    "try_mauvais_ordre": (
        "🤯 🫵 {try} {except} {else} {finally} 🔀 🤡",
        "Ligne {ligne} : dans un bloc {try}, les parties se suivent dans cet ordre : {except} (autant que nécessaire), "
        "{else} (une seule fois, et seulement avec au moins un {except}), puis {finally} (une seule fois). Ici l'ordre ou le nombre n'est pas respecté."),
    "except_sans_type_pas_dernier": (
        "🙄 🫵 {except} 🕸️ 🔚 🤡",
        "Ligne {ligne} : un {except} sans type attrape toutes les erreurs. Il doit donc être le dernier, sinon les {except} suivants ne serviraient jamais."),
    "try_jamais_ferme": (
        "🤡 🫵 {try} 🚪 {end} ❌ 🐌",
        "Ligne {ligne} : le bloc {try} ouvert ici n'est jamais fermé. Il se termine par une ligne contenant uniquement {end}."),
    "try_ferme_de_travers": (
        "🤦 🫵 {try} 🧩 🚫 {end} 🤡",
        "Ligne {ligne} : le bloc {try} ouvert ici est fermé de travers : un autre bloc est encore ouvert à l'intérieur, "
        "ou bien il est fermé par {end_bloc} au lieu de {end}."),
    "return_hors_fonction": (
        "🙄 🫵 {return} 🏃 🚪 ❓ 🤡",
        "Ligne {ligne} : {return} ne peut être utilisé qu'à l'intérieur d'une fonction."),
    "break_hors_boucle": (
        "🙄 🫵 {break} 🔁 ❓ 🤡",
        "Ligne {ligne} : {break} ne peut être utilisé qu'à l'intérieur d'une boucle ({for} ou {while})."),
    "continue_hors_boucle": (
        "🙄 🫵 {continue} 🔁 ❓ 🤡",
        "Ligne {ligne} : {continue} ne peut être utilisé qu'à l'intérieur d'une boucle ({for} ou {while})."),
    "fonction_non_appelee": (
        "🤦 🫵 {emoji} {executer} ❓ 🙈 🤡",
        "Ligne {ligne} : {emoji} est une fonction, et écrire son nom ne l'exécute pas. "
        "Pour l'exécuter, écris {executer} juste après son nom, puis les valeurs, puis {end_paramettres}."),
    "valeur_en_debut_de_ligne": (
        "🙄 🫵 {emoji} 🧱 ❓ 🤡",
        "Ligne {ligne} : une ligne ne peut pas commencer par {emoji}, qui est une valeur. "
        "Une ligne commence par le nom d'une variable (suivi de sa valeur), par une fonction (suivie de {executer}) ou par un mot-clé."),
    "instruction_mal_placee": (
        "🤡 🫵 {emoji} 🪑 ❓ 😂",
        "Ligne {ligne} : {emoji} ne peut pas commencer une ligne à cet endroit."),
    "erreur_python": (
        "💥 🫵 🐍 😭 🤡 🤣",
        "Ligne {ligne} : Python a rencontré une erreur que rien n'a rattrapée : {type} : {message}. "
        "Un bloc {try} avec un {except} permet de la rattraper."),
    "valeur_levee": (
        "💥 🫵 {raise} 🗑️ 🤡 🤣",
        "Ligne {ligne} : une valeur a été levée avec {raise} et aucun {except} ne l'a rattrapée : {valeur}."),
}
