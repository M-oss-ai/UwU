import grapheme
import emoji as em
import sys
import inspect
from b import table, Instructions, Variable, Operation
import types
INSTRUCTION_WANT_END = ["if", "for", "while"]

def infos(func):
    sig = inspect.signature(func)
    mini = 0
    maxi = 0

    for p in sig.parameters.values():
        if p.kind in (p.POSITIONAL_ONLY, p.POSITIONAL_OR_KEYWORD):
            maxi += 1
            if p.default is inspect.Parameter.empty:
                mini += 1

        elif p.kind == p.VAR_POSITIONAL:
            maxi = float("inf")

    return mini, maxi

def get_liste(liste, end_wanted=[]):
    Exception("error")
    final_liste = []
    skip = 0
    separer = False
    for place in range(len(liste)):
        if place >= skip:
            emoji = liste[place]
            if not emoji in table.keys():
                print(" 🚫 ❌ " + emoji + " 🫵 🖕 ")
                sys.exit(1)

            value = table[emoji]
            
            if type(value) == Instructions:
                match value.name:
                    case "deconnecter":      
                        separer = True
                        continue
                    
                    case "start liste":
                        resultats = get_liste(liste[place + 1:], end_wanted=["end liste"])
                        value = resultats[0]
                        skip = place + resultats[1]
                    
                    case "input":
                        resultats = get_input(liste[place + 1:])
                        value = resultats[0]
                        skip = place + resultats[1]
                    case "naturalise":
                        resultats = naturalise(liste[place + 1:])
                        value = resultats[0]
                        skip = place + resultats[1]
                    
                    case _ if value.name in end_wanted:
                        return (do_opperation(final_liste), place + 2)

                    case _:
                        print(" 🚫 ❓ " + emoji + " 👇 🫵 🖕 ")
                        sys.exit(1)


            elif type(value) == Variable:
                value = value.value
            
            elif callable(value):
                resultats = do_function(emoji, liste[place + 1:])
                value = resultats[0]
                skip = place + resultats[1]

            if len(final_liste) == 0 or separer:
                separer = False
                final_liste.append(value)
                continue

            if type(value) == type(final_liste[len(final_liste) - 1]):

                if type(value) == int:
                    final_liste[len(final_liste) - 1] = int(str(final_liste[len(final_liste) - 1]) + str(value))

                elif type(value) == str:
                    final_liste[len(final_liste) - 1] += value

                else:
                    final_liste.append(value)
            else:
                final_liste.append(value)
    return (do_opperation(final_liste), len(liste) + 1)

def do_function(emoji, ligne):
    
    func = table[emoji]
    parametres, skip = get_liste(ligne, end_wanted=["end paramettres"])
    
    try:
        parms_possible = infos(func)
    except:
        parms_possible = (0, float("inf"))
    
    if type(parametres) != list:
        parametres = [parametres]

    if len(parametres) < parms_possible[0]:
        print(" 🚫 🤷 " + emoji + " 🤷 📦 🫵 🖕 ")
        sys.exit(1)
    
    elif len(parametres) > parms_possible[1]:
        print(" 🚫 🤯 " + emoji + " 🤯 🫵 🖕 ")
        sys.exit(1)

    return (func(*parametres), skip)

def do_opperation(liste):
    
    
    skip = 0
    for place in range(len(liste)):
        hase_do_opreation = False
        place -= skip

        if place >= len(liste):
            break

        if type(liste[place]) == Operation:
            if place == 0:
                print("error7")
                sys.exit(1)
            elif place + 1 >= len(liste):
                print("error8")
                sys.exit(1)
            hase_do_opreation = True
            value = liste[place].calcule(liste[place - 1], liste[place + 1])
            liste[place - 1 : place + 2] = [value]
            skip += 1
    
    if len(liste) == 1 and hase_do_opreation:
        return liste[0]
    
    return liste

def creat_variable(ligne):
    nombre = 0
    while len(ligne) > nombre and (ligne[nombre] not in table.keys() or type(table[ligne[nombre]]) == Variable):
        nombre += 1
    
    resultat = get_liste(ligne[nombre:])[0]
    nombre = min(len(resultat), nombre)

    for position in range(nombre):
        value = resultat[position]
        table[ligne[position]] = Variable(value)

def naturalise(ligne):
    value = ""
    for place in range(len(ligne)):
        emoji = ligne[place]
        if emoji in table.keys() and type(table[emoji]) == Instructions and table[emoji].name == "end paramettres":
    
            if len(ligne) > place and ligne[place + 1] in table.keys() and type(table[ligne[place + 1]]) == Instructions and table[ligne[place + 1]].name == "end paramettres":
                value += emoji
                return (value, place + 3)
                
            elif place == 0:
                value += emoji
                
            return (value, place + 2)
            
        value += emoji
    
    return (value, len(ligne) + 1)
    

def get_input(ligne):
    parametres = get_liste(ligne, end_wanted=["end paramettres"])
    value = get_emoji(input(*parametres[0]), look_at_chut=False)
    resultat = ""
    for emoji in value:
        if emoji in table.keys():
            resultat += str(table[emoji])
        else:
            resultat += emoji

    return (resultat, parametres[1])

def get_emoji(line, look_at_chut=True):
    value = []

    for emoji in grapheme.graphemes(line):
        if look_at_chut and emoji in table.keys() and type(table[emoji]) == Instructions and table[emoji].name == "chut":
            break
        
        if em.is_emoji(emoji) or emoji in table.keys():

            value.append(emoji)

    return value

def get_end(fichier):
    liste_of_instruction = []
    for ligne in range(len(fichier)):
        if fichier[ligne][0] in table.keys() and type(table[fichier[ligne][0]]) == Instructions:
            value = table[fichier[ligne][0]].name

            if value in INSTRUCTION_WANT_END:
                liste_of_instruction.append(value)
            
            elif value in ("else", "elif"):
                if liste_of_instruction == []:
                    liste_of_instruction.append(value)

                elif liste_of_instruction in (["if"], ["elif"]):
                    return (ligne + 1, value)
                
                elif liste_of_instruction[len(liste_of_instruction) - 1] in ("if", "elif"):
                    liste_of_instruction[len(liste_of_instruction) - 1] = value

                else:
                    print("error6")
                    sys.exit(1)

            elif value == "end":
                del liste_of_instruction[len(liste_of_instruction) - 1]
                if len(liste_of_instruction) == 0:
                    return (ligne + 1, "end")

    sys.exit(1)

def instruction_if(fichier):
    
    if get_liste(fichier[0][1:])[0][0]:
        resultat = read_lines(fichier[1:], end_wanted=["end", "else", "elif"])
        nombre = resultat[0]

        while resultat[1] != "end":
            resultat = get_end(fichier[nombre + 1:])
            nombre += resultat[0] - 1

        return nombre + 2
    
    else:
        resultat = get_end(fichier)
        if resultat[1] == "end":
            return resultat[0]
        elif resultat[1] == "else":
            return resultat[0] + read_lines(fichier[resultat[0]:], end_wanted=["end"])[0] + 1
        else:
            return resultat[0] + instruction_if(fichier[resultat[0] - 1:]) - 1

    
def read_lines(fichier, end_wanted=[]):
    skip = 0
    for ligne in range(len(fichier)):
        if ligne < skip:
            continue

        if fichier[ligne][0] in table.keys() and type(table[fichier[ligne][0]]) != Variable:
            value = table[fichier[ligne][0]]
            
            if callable(value):
                do_function(fichier[ligne][0], fichier[ligne][1:])
                
            elif type(value) == Instructions:
                match value.name:
                    case "naturalise":
                        naturalise(fichier[ligne][1:])
                    case "input":
                        get_input(fichier[ligne][1:])
                    case "if":
                        skip = ligne + instruction_if(fichier[ligne:])
                    case  x if x in end_wanted:
                        return (ligne, x)
                    case _:
                        print("error5")
                        sys.exit(1)

            else:
                print(" 🚫 " + fichier[ligne][0] + " 🫵 🖕 ")
                sys.exit(1)

        else:
            creat_variable(fichier[ligne])

    sys.exit(1)

def reading_code():
    with open('a.txt', 'r', encoding='utf-8') as fichier:
        translation = []

        for line in fichier:
            value = get_emoji(line)
            if value != []:
                translation.append(value)

    return translation

read_lines(reading_code())



