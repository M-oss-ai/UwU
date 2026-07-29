# import regex
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
    final_liste = []
    skip = 0
    separer = False
    for place in range(len(liste)):
        if place >= skip:
            emoji = liste[place]
            if not emoji in table.keys():
                print(" 🚫 ❌ "+ emoji +" 🫵 🖕 ")
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
                    
                    case _ if value.name in end_wanted:
                        return (do_opperation(final_liste), place + 2)

                    case _:
                        print(" 🚫 ❓ " + emoji + " 👇 🫵 🖕 ")
                        sys.exit(1)


            elif type(value) == Variable:
                value = value.value
            
            elif type(value) in (types.FunctionType,  types.BuiltinFunctionType):
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
    if len(liste) <= 1:
        return liste
    
    skip = 0
    for place in range(len(liste)):
        place -= skip

        if place >= len(liste):
            break

        if type(liste[place]) == Operation:
            value = liste[place].calcule(liste[place - 1], liste[place + 1])
            liste[place - 1 : place + 2] = [value]
            skip += 1
    
    if len(liste) == 1:
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
    if len(ligne) < 1:
        print("error4")
        sys.exit(1)
        
    for emoji in ligne:
        table[emoji] = emoji

def remplace(ligne):
    if len(ligne) < 2:
        print("error3")
        sys.exit(1)

    match ligne[0] in table.keys(), ligne[1] in table.keys():
        case False, False:
            print("error2")
        case True, False:
            table[ligne[1]] = table[ligne[0]]
            del table[ligne[0]]
        case False, True:
            table[ligne[0]] = table[ligne[1]]
            del table[ligne[1]]
        case True, True:
            table[ligne[0]], table[ligne[1]] = table[ligne[1]], table[ligne[0]]

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

    #for emoji in regex.findall(r"\X", line):
        if emoji in table.keys() and type(table[emoji]) == Instructions and table[emoji].name == "chut" and look_at_chut:
            break

        if em.is_emoji(emoji):
            value.append(emoji)

    return value

def get_end(fichier):
    # print("\n", fichier, "\n")
    liste_of_instruction = []
    # pour toutes les lignes
    for ligne in range(len(fichier)):
        # si c'est une instruction
        if fichier[ligne][0] in table.keys() and type(table[fichier[ligne][0]]) == Instructions:
            value = table[fichier[ligne][0]].name
            # print(liste_of_instruction, value)


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
    if get_liste(fichier[0][1:])[0]:
        resultat = read_lines(fichier[1:], end_wanted=["end", "else", "elif"])
        nombre = resultat[0]

        while resultat[1] != "end":
            resultat = get_end(fichier[nombre + 1:])
            nombre += resultat[0] - 1
            # print(nombre)

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
            match value:
                case types.BuiltinFunctionType() | types.FunctionType():
                    do_function(fichier[ligne][0], fichier[ligne][1:])
                
                case Instructions():
                    match value.name:
                        case "remplace":
                            remplace(fichier[ligne][1:])
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

                case _:
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

translation = reading_code()
read_lines(translation)