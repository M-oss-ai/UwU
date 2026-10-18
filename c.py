import grapheme
import emoji as em
import sys
import os
import inspect
from b import table, MESSAGES, Instructions, Variable, Operation, Parms_Noinatif, function_name, sans_selecteur, TABLE_SANS_SELECTEUR
import types

# un appel de fonction UwU utilise plusieurs appels Python : avec la limite par défaut (1000) la récursion s'arrête vers 150 niveaux
sys.setrecursionlimit(5000)
INSTRUCTION_WANT_END = ["if", "for", "while", "def", "class", "try"]

# break, continue et return remontent comme des exceptions Python mais ne sont pas des erreurs : un except ne doit pas les attraper
class ControleUwU(BaseException):
    pass

class Continuer(ControleUwU):
    pass

class Arreter(ControleUwU):
    pass

class Retour(ControleUwU):
    def __init__(self, valeur):
        self.valeur = valeur

# ce que raise lève quand la valeur n'est pas une exception Python (un texte, un objet...) : un except la compare à cette valeur
class ErreurUwU(Exception):
    def __init__(self, valeur):
        super().__init__(valeur)
        self.valeur = valeur

# un contexte par fonction ou par corps de classe en cours d'exécution : nombre de boucles ouvertes (pour break et continue) et return autorisé
CONTEXTE = [{"boucles": 0, "retour": False}]

# erreurs en cours de traitement par un except : un raise seul relance la dernière
ERREURS = []

# la ligne de a.txt en cours d'exécution : une erreur la donne à la fin de sa ligne d'emojis
POSITION = [0]

# les mots-clés du langage par nom (« end bloc » devient end_bloc) : les messages d'erreur montrent ainsi toujours les bons emojis
SYMBOLES = {valeur.name.replace(" ", "_"): emoji for emoji, valeur in table.items() if type(valeur) == Instructions}
EMOJI_L = next(emoji for emoji, valeur in table.items() if valeur == "l")
CHIFFRES = {str(valeur): emoji for emoji, valeur in table.items() if type(valeur) == int}

def emoji_de(valeur):
    return next((emoji for emoji, autre in table.items() if autre is valeur), "?")

# affiche une erreur du langage (voir MESSAGES dans b.py) puis arrête le programme
def echouer(cle, ligne=None, **infos):
    moquerie, description = MESSAGES[cle]
    if ligne is None:
        ligne = POSITION[0]

    infos = {**SYMBOLES, **infos, "ligne": ligne}
    print(moquerie.format(**infos) + " " + EMOJI_L + "".join(CHIFFRES[chiffre] for chiffre in str(ligne)))
    print(description.format(**infos))
    sys.exit(1)

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
    # forces[i] vaut True quand final_liste[i] a été séparé de l'élément précédent par ⛓️‍💥
    forces = []
    for place in range(len(liste)):
        if place >= skip:
            emoji = liste[place]
            if not emoji in table.keys():
                echouer("emoji_inconnu", emoji=emoji)

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
                    
                    case "nomme":
                        pass

                    case "attribut":
                        do_index(final_liste, forces)
                        if separer or len(final_liste) == 0 or type(final_liste[-1]) in (Operation, Instructions):
                            echouer("attribut_sans_objet")

                        if place + 1 >= len(liste) or type(table.get(liste[place + 1])) in (Operation, Instructions):
                            echouer("attribut_sans_nom")

                        # la valeur de l'attribut prend la place de l'objet : si un ⛓️‍💥 le séparait de ce qui précède, elle en reste séparée
                        separer = forces.pop()
                        value = getattr(final_liste.pop(), liste[place + 1])
                        skip = place + 2
                        if callable(value):
                            resultats = call_function(value, liste[place + 2:], liste[place + 1])
                            value = resultats[0]
                            skip = place + 1 + resultats[1]

                    case _ if value.name in end_wanted:
                        return (do_opperation(final_liste), place + 2)

                    case _:
                        echouer("mot_cle_en_valeur", emoji=emoji)

            else:
                if type(value) == Variable:
                    value = value.value

                if callable(value):
                    resultats = call_function(value, liste[place + 1:], emoji)
                    value = resultats[0]
                    skip = place + resultats[1]

            if len(final_liste) == 0 or separer:
                forces.append(separer)
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
                    forces.append(False)
            else:
                final_liste.append(value)
                forces.append(False)
    return (do_opperation(final_liste), len(liste) + 1)

def en_texte(valeur):
    if isinstance(valeur, ClasseUwU):
        return repr(valeur)

    return "<fonction " + function_name(valeur) + ">" if callable(valeur) else valeur

# retourne (valeur, skip, executee) : executee vaut False quand aucun 🤙 ne suit, valeur est alors la fonction brute
def call_function(func, ligne, label):
    if not (ligne and ligne[0] in table.keys() and type(table[ligne[0]]) == Instructions and table[ligne[0]].name == "executer"):
        return (func, 1, False)

    parametres, skip = get_liste(ligne[1:], end_wanted=["end paramettres"])

    try:
        parms_possible = infos(func)
    except:
        parms_possible = (0, float("inf"))

    if type(parametres) != list:
        parametres = [parametres]

    positionnels = []
    nommes = {}
    for parametre in parametres:
        if type(parametre) == Parms_Noinatif:
            nommes.update(parametre.directory)
        else:
            positionnels.append(parametre)

    if len(positionnels) + len(nommes) < parms_possible[0]:
        echouer("trop_peu", nom=label, recus=len(positionnels) + len(nommes), mini=parms_possible[0])

    elif len(positionnels) > parms_possible[1]:
        echouer("trop_de_valeurs", nom=label, recus=len(positionnels), maxi=parms_possible[1])

    positionnels = [en_texte(parametre) for parametre in positionnels]
    nommes = {nom: en_texte(valeur) for nom, valeur in nommes.items()}

    return (func(*positionnels, **nommes), skip + 1, True)

def do_index(liste, forces=None):
    place = 1
    while place < len(liste) - 1:
        if type(liste[place]) == Operation and liste[place].est_index:
            liste[place - 1 : place + 2] = [liste[place].calcule(liste[place - 1], liste[place + 1])]
            if forces is not None:
                del forces[place : place + 2]
        else:
            place += 1

def do_nomme(liste):
    place = 1
    while place < len(liste) - 1:
        if type(liste[place]) == Instructions and liste[place].name == "nomme":
            liste[place - 1 : place + 2] = [Parms_Noinatif({liste[place - 1]: liste[place + 1]})]
        else:
            place += 1

    for place in range(len(liste)):
        if type(liste[place]) == Instructions and liste[place].name == "nomme":
            echouer("nomme_sans_nom" if place == 0 else "nomme_sans_valeur")

def do_opperation(liste):
    do_index(liste)
    
    skip = 0
    hase_do_opreation = False
    for place in range(len(liste)):
        place -= skip

        if place >= len(liste):
            break

        if type(liste[place]) == Operation:
            if place == 0:
                echouer("operateur_sans_gauche", operateur=emoji_de(liste[place]))
            elif place + 1 >= len(liste):
                echouer("operateur_sans_droite", operateur=emoji_de(liste[place]))
            hase_do_opreation = True
            
            value = liste[place].calcule(liste[place - 1], liste[place + 1])
            
            liste[place - 1 : place + 2] = [value]
            skip += 1
    if len(liste) == 1 and hase_do_opreation:
        return liste[0]

    do_nomme(liste)
    
    return liste

def evaluer(ligne):
    resultat = get_liste(ligne)[0]
    if type(resultat) == list:
        if len(resultat) == 0:
            echouer("valeur_manquante")

        resultat = resultat[0]

    return resultat

def creat_variable(ligne):
    table[ligne[0]] = Variable(evaluer(ligne[1:]))

def est_fin(emoji):
    return emoji in table.keys() and type(table[emoji]) == Instructions and table[emoji].name == "end paramettres"

# 🎭📦📦 donne un 📦 littéral ; sinon le premier 📦 ferme le texte
def naturalise(ligne):
    if len(ligne) >= 2 and est_fin(ligne[0]) and est_fin(ligne[1]):
        return (ligne[0], 3)

    value = ""
    for place in range(len(ligne)):
        if est_fin(ligne[place]):
            return (value, place + 2)

        value += ligne[place]

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
        if emoji not in table.keys():
            normalise = sans_selecteur(emoji)
            if normalise in TABLE_SANS_SELECTEUR:
                emoji = TABLE_SANS_SELECTEUR[normalise]

        if look_at_chut and emoji in table.keys() and type(table[emoji]) == Instructions and table[emoji].name == "chut":
            break

        if em.is_emoji(emoji) or emoji in table.keys():

            value.append(emoji)

    return value

def est_instruction(emoji, nom):
    valeur = table.get(emoji)
    return type(valeur) == Instructions and valeur.name == nom

def fin_bloc(fichier):
    pile = []
    for ligne in range(len(fichier)):
        premier = fichier[ligne][0]
        if premier not in table.keys() or type(table[premier]) != Instructions:
            continue

        nom = table[premier].name
        if nom in ("for", "while", "def", "class"):
            pile.append(nom)

        elif nom == "end bloc":
            pile.pop()
            if len(pile) == 0:
                return ligne

    echouer("bloc_jamais_ferme", ligne=fichier[0].numero, ouvert=fichier[0][0])

# numero : la ligne du bloc if, pour les erreurs
def get_end(fichier, numero):
    liste_of_instruction = []
    for ligne in range(len(fichier)):
        if fichier[ligne][0] in table.keys() and type(table[fichier[ligne][0]]) == Instructions:
            value = table[fichier[ligne][0]].name

            if value in INSTRUCTION_WANT_END:
                liste_of_instruction.append(value)

            elif value in ("else", "elif"):
                if liste_of_instruction == []:
                    liste_of_instruction.append(value)

                elif liste_of_instruction[len(liste_of_instruction) - 1] == "try":
                    pass

                elif liste_of_instruction in (["if"], ["elif"]):
                    return (ligne + 1, value)

                elif liste_of_instruction[len(liste_of_instruction) - 1] in ("if", "elif"):
                    liste_of_instruction[len(liste_of_instruction) - 1] = value

                else:
                    echouer("si_mal_forme", ligne=fichier[ligne].numero)

            elif value == "end":
                del liste_of_instruction[len(liste_of_instruction) - 1]
                if len(liste_of_instruction) == 0:
                    return (ligne + 1, "end")

            elif value == "end bloc":
                if liste_of_instruction == [] or liste_of_instruction[len(liste_of_instruction) - 1] not in ("for", "while", "def", "class"):
                    echouer("fermeture_de_travers", ligne=fichier[ligne].numero)

                del liste_of_instruction[len(liste_of_instruction) - 1]

    echouer("si_jamais_ferme", ligne=numero)

# évalue ce qui suit le mot-clé d'une ligne d'en-tête (if, while, for...) : une erreur est alors celle de cette ligne
def evaluer_entete(entete, debut):
    POSITION[0] = entete.numero
    return evaluer(entete[debut:])

def instruction_if(fichier):
    numero = fichier[0].numero

    if evaluer_entete(fichier[0], 1):
        resultat = read_lines(fichier[1:], end_wanted=["end", "else", "elif"], corps=True)
        if resultat[1] is None:
            echouer("si_jamais_ferme", ligne=numero)

        nombre = resultat[0]

        while resultat[1] != "end":
            resultat = get_end(fichier[nombre + 1:], numero)
            nombre += resultat[0] - 1

        return nombre + 2

    else:
        resultat = get_end(fichier, numero)
        if resultat[1] == "end":
            return resultat[0]
        elif resultat[1] == "else":
            corps = read_lines(fichier[resultat[0]:], end_wanted=["end"], corps=True)
            if corps[1] is None:
                echouer("si_jamais_ferme", ligne=numero)

            return resultat[0] + corps[0] + 1
        else:
            return resultat[0] + instruction_if(fichier[resultat[0] - 1:]) - 1


def verifier_nom(emoji):
    if emoji in table.keys() and type(table[emoji]) != Variable:
        echouer("nom_reserve", emoji=emoji)

def executer_corps(corps):
    CONTEXTE[-1]["boucles"] += 1
    try:
        read_lines(corps, corps=True)

    except Continuer:
        pass

    except Arreter:
        return False

    finally:
        CONTEXTE[-1]["boucles"] -= 1

    return True

def executer_boucle(fichier):
    fin = fin_bloc(fichier)
    corps = fichier[1:fin]
    entete = fichier[0]

    if est_instruction(entete[0], "for"):
        if len(entete) < 3:
            echouer("entete_for")

        verifier_nom(entete[1])
        for element in evaluer_entete(entete, 2):
            table[entete[1]] = Variable(element)
            if not executer_corps(corps):
                break

    else:
        if len(entete) < 2:
            echouer("entete_while")

        while evaluer_entete(entete, 1):
            if not executer_corps(corps):
                break

    return fin + 1

# marqueurs du niveau d'un try : (indice, nom) pour chaque except, else et finally, puis le 🔚 qui ferme le bloc
def decouper_try(fichier):
    pile = []
    marqueurs = []
    for ligne in range(len(fichier)):
        premier = fichier[ligne][0]
        if premier not in table.keys() or type(table[premier]) != Instructions:
            continue

        nom = table[premier].name
        if nom in INSTRUCTION_WANT_END:
            pile.append(nom)

        elif nom in ("end", "end bloc"):
            if len(pile) == 0 or (nom == "end") != (pile[-1] in ("if", "try")):
                echouer("try_ferme_de_travers", ligne=fichier[0].numero)

            pile.pop()
            if len(pile) == 0:
                marqueurs.append((ligne, "end"))
                return marqueurs

        elif len(pile) == 1 and nom in ("except", "else", "finally"):
            marqueurs.append((ligne, nom))

    echouer("try_jamais_ferme", ligne=fichier[0].numero)

# l'erreur correspond à une classe si c'est une exception de cette classe, ou si c'est la valeur levée par raise
def correspond(erreur, types):
    if type(types) != list:
        types = [types]

    for cible in types:
        if not isinstance(cible, type):
            raise TypeError("un except attend une classe d'erreur")

        if isinstance(erreur, cible) or (isinstance(erreur, ErreurUwU) and isinstance(erreur.valeur, cible)):
            return True

    return False

def trouver_gestionnaire(erreur, gestionnaires):
    for gestionnaire in gestionnaires:
        entete = gestionnaire[0]
        if len(entete) <= 2 or correspond(erreur, evaluer_entete(entete, 2)):
            return gestionnaire

    return None

def executer_gestionnaire(entete, corps, erreur):
    if len(entete) > 1:
        table[entete[1]] = Variable(erreur.valeur if isinstance(erreur, ErreurUwU) else erreur)

    ERREURS.append(erreur)
    try:
        read_lines(corps, corps=True)

    finally:
        ERREURS.pop()

def lever(valeur):
    if isinstance(valeur, type) and issubclass(valeur, BaseException):
        raise valeur()

    if isinstance(valeur, BaseException):
        raise valeur

    raise ErreurUwU(valeur)

def relancer():
    if len(ERREURS) == 0:
        raise RuntimeError("aucune erreur à relancer")

    raise ERREURS[-1]

def instruction_try(fichier):
    marqueurs = decouper_try(fichier)
    fin = marqueurs[-1][0]
    noms = [nom for indice, nom in marqueurs[:-1]]
    ordre = {"except": 0, "else": 1, "finally": 2}
    if "except" not in noms and "finally" not in noms:
        echouer("try_sans_clause", ligne=fichier[0].numero)

    if noms != sorted(noms, key=ordre.get) or noms.count("else") > 1 or noms.count("finally") > 1 or ("else" in noms and "except" not in noms):
        echouer("try_mauvais_ordre", ligne=fichier[0].numero)

    essai = fichier[1:marqueurs[0][0]]
    gestionnaires = []
    sinon = None
    finalement = None
    for place in range(len(marqueurs) - 1):
        indice, nom = marqueurs[place]
        corps = fichier[indice + 1:marqueurs[place + 1][0]]
        if nom == "except":
            gestionnaires.append((fichier[indice], corps))
        elif nom == "else":
            sinon = corps
        else:
            finalement = corps

    for numero in range(len(gestionnaires)):
        entete = gestionnaires[numero][0]
        if len(entete) > 1:
            POSITION[0] = entete.numero
            verifier_nom(entete[1])

        # un except sans type attrape tout : il doit être le dernier
        if len(entete) <= 2 and numero < len(gestionnaires) - 1:
            echouer("except_sans_type_pas_dernier", ligne=entete.numero)

    try:
        try:
            read_lines(essai, corps=True)

        except Exception as erreur:
            position = POSITION[0]
            gestionnaire = trouver_gestionnaire(erreur, gestionnaires)
            if gestionnaire is None:
                POSITION[0] = position
                raise

            executer_gestionnaire(gestionnaire[0], gestionnaire[1], erreur)

        else:
            if sinon is not None:
                read_lines(sinon, corps=True)

    finally:
        if finalement is not None:
            position = POSITION[0]
            read_lines(finalement, corps=True)
            POSITION[0] = position

    return fin + 1

# associe les valeurs reçues aux noms des paramètres : positionnelles d'abord, puis nommées
def associer_parametres(parametres, args, kwargs):
    if len(args) > len(parametres):
        raise TypeError("trop de paramètres")

    valeurs = dict(zip(parametres, args))
    for nom, valeur in kwargs.items():
        if nom not in parametres or nom in valeurs:
            raise TypeError("paramètre nommé inconnu ou déjà donné : " + nom)

        valeurs[nom] = valeur

    if len(valeurs) != len(parametres):
        raise TypeError("paramètres manquants")

    return valeurs

# une fonction de classe appelée depuis un objet : l'objet est son premier paramètre
class MethodeLiee():
    def __init__(self, fonction, instance):
        self.fonction = fonction
        self.instance = instance
        self.__name__ = fonction.__name__
        self.__qualname__ = fonction.__qualname__
        self.__signature__ = inspect.Signature(list(fonction.__signature__.parameters.values())[1:])

    def __call__(self, *args, **kwargs):
        return self.fonction(self.instance, *args, **kwargs)

    def __repr__(self):
        return "<fonction " + self.__qualname__ + ">"

class FonctionUwU():
    def __init__(self, nom, parametres, corps):
        self.parametres = parametres
        self.corps = corps
        self.__name__ = nom
        self.__qualname__ = nom
        self.__signature__ = inspect.Signature([
            inspect.Parameter("p" + str(place), inspect.Parameter.POSITIONAL_OR_KEYWORD)
            for place in range(len(parametres))
        ])

    def __get__(self, instance, classe=None):
        return self if instance is None else MethodeLiee(self, instance)

    def __repr__(self):
        return "<fonction " + self.__qualname__ + ">"

    def __call__(self, *args, **kwargs):
        valeurs = associer_parametres(self.parametres, args, kwargs)

        sauvegarde = dict(table)
        position = POSITION[0]
        CONTEXTE.append({"boucles": 0, "retour": True})
        try:
            for nom, valeur in valeurs.items():
                table[nom] = Variable(valeur)

            try:
                read_lines(self.corps, corps=True)

            except Retour as retour:
                POSITION[0] = position
                return retour.valeur

            POSITION[0] = position
            return None

        finally:
            CONTEXTE.pop()
            table.clear()
            table.update(sauvegarde)

# le nom que prend, dans une classe, la fonction qui construit l'objet
CLE_INIT = next(emoji for emoji, valeur in table.items() if type(valeur) == Instructions and valeur.name == "init")

def definir_fonction(fichier):
    fin = fin_bloc(fichier)
    entete = fichier[0]

    if len(entete) < 4 or not est_instruction(entete[2], "start definition") or not est_instruction(entete[-1], "end definition"):
        echouer("entete_def")

    nom = entete[1]
    parametres = entete[3:-1]
    constructeur = CONTEXTE[-1].get("classe", False) and nom == CLE_INIT
    for emoji in ([] if constructeur else [nom]) + parametres:
        verifier_nom(emoji)

    if len(set(parametres)) != len(parametres):
        echouer("parametres_en_double")

    table[nom] = Variable(FonctionUwU(nom, parametres, fichier[1:fin]))
    return fin + 1

class ClasseUwU(type):
    def __repr__(cls):
        return "<classe " + cls.__name__ + ">"

class ObjetUwU(metaclass=ClasseUwU):
    def __repr__(self):
        return "<objet " + type(self).__name__ + ">"

# exécute le corps d'une classe comme un bloc isolé : ce qu'il définit (valeurs et fonctions) devient le contenu de la classe
def executer_classe(corps):
    sauvegarde = dict(table)
    CONTEXTE.append({"boucles": 0, "retour": False, "classe": True})
    try:
        read_lines(corps, corps=True)
        return {nom: variable.value for nom, variable in table.items()
                if type(variable) == Variable and sauvegarde.get(nom) is not variable}

    finally:
        CONTEXTE.pop()
        table.clear()
        table.update(sauvegarde)

def construire_classe(nom, arguments, contenu):
    constructeur = contenu.pop(CLE_INIT, None)

    # les arguments de la classe deviennent des attributs de l'objet, puis la fonction de construction s'exécute
    def initialiser(self, *args, **kwargs):
        for argument, valeur in associer_parametres(arguments, args, kwargs).items():
            setattr(self, argument, valeur)

        if constructeur is not None:
            constructeur(self)

    contenu["__init__"] = initialiser
    contenu["__signature__"] = inspect.Signature([
        inspect.Parameter("p" + str(place), inspect.Parameter.POSITIONAL_OR_KEYWORD)
        for place in range(len(arguments))
    ])
    classe = type(nom, (ObjetUwU,), contenu)
    for cle, valeur in contenu.items():
        if isinstance(valeur, FonctionUwU):
            valeur.__qualname__ = nom + "." + cle

    if constructeur is not None:
        constructeur.__qualname__ = nom + "." + CLE_INIT

    return classe

def definir_classe(fichier):
    fin = fin_bloc(fichier)
    entete = fichier[0]

    if len(entete) < 2:
        echouer("entete_class")

    nom = entete[1]
    if len(entete) == 2:
        arguments = []

    elif len(entete) >= 4 and est_instruction(entete[2], "start definition") and est_instruction(entete[-1], "end definition"):
        arguments = entete[3:-1]

    else:
        echouer("entete_class")

    for emoji in [nom] + arguments:
        verifier_nom(emoji)

    if len(set(arguments)) != len(arguments):
        echouer("arguments_en_double")

    table[nom] = Variable(construire_classe(nom, arguments, executer_classe(fichier[1:fin])))
    return fin + 1

# nombre d'emojis occupés par le début d'une ligne « variable 🔗 nom 🔗 nom … »
def longueur_chemin(ligne):
    fin = 1
    while fin + 1 < len(ligne) and est_instruction(ligne[fin], "attribut"):
        fin += 2

    return fin

# ligne qui commence par un attribut : 🤙 derrière le chemin appelle la fonction, sinon c'est une affectation
def instruction_attribut(ligne, chemin):
    reste = ligne[chemin:]
    if len(reste) == 0:
        echouer("attribut_sans_valeur")

    if est_instruction(reste[0], "executer"):
        get_liste(ligne)
        return

    setattr(evaluer(ligne[:chemin - 2]), ligne[chemin - 1], evaluer(reste))

def read_lines(fichier, end_wanted=[], corps=False):
    skip = 0
    for ligne in range(len(fichier)):
        if ligne < skip:
            continue

        POSITION[0] = fichier[ligne].numero

        if fichier[ligne][0] in table.keys():
            value = table[fichier[ligne][0]]

            if type(value) == Variable:
                chemin = longueur_chemin(fichier[ligne])
                if chemin > 1:
                    instruction_attribut(fichier[ligne], chemin)

                elif not (callable(value.value) and call_function(value.value, fichier[ligne][1:], fichier[ligne][0])[2]):
                    creat_variable(fichier[ligne])

            elif callable(value):
                value = call_function(table[fichier[ligne][0]], fichier[ligne][1:], fichier[ligne][0])
                if not value[2]:
                    echouer("fonction_non_appelee", emoji=fichier[ligne][0])

            elif type(value) == Instructions:
                match value.name:
                    case "naturalise":
                        naturalise(fichier[ligne][1:])
                    case "input":
                        get_input(fichier[ligne][1:])
                    case "if":
                        skip = ligne + instruction_if(fichier[ligne:])
                    case "for" | "while":
                        skip = ligne + executer_boucle(fichier[ligne:])
                    case "def":
                        skip = ligne + definir_fonction(fichier[ligne:])
                    case "class":
                        skip = ligne + definir_classe(fichier[ligne:])
                    case "try":
                        skip = ligne + instruction_try(fichier[ligne:])
                    case "raise":
                        if len(fichier[ligne]) > 1:
                            lever(evaluer(fichier[ligne][1:]))

                        relancer()
                    case "return":
                        if not CONTEXTE[-1]["retour"]:
                            echouer("return_hors_fonction")

                        raise Retour(evaluer(fichier[ligne][1:]) if len(fichier[ligne]) > 1 else None)
                    case "continue" | "break":
                        if CONTEXTE[-1]["boucles"] == 0:
                            echouer("continue_hors_boucle" if value.name == "continue" else "break_hors_boucle")

                        raise Continuer() if value.name == "continue" else Arreter()
                    case x if x in end_wanted:
                        return (ligne, x)
                    case "end bloc":
                        echouer("fermeture_orpheline")
                    case "else" | "elif" | "end":
                        echouer("si_mal_forme" if end_wanted else "si_orphelin", emoji=fichier[ligne][0])
                    case "except" | "finally":
                        echouer("clause_orpheline", emoji=fichier[ligne][0])
                    case _:
                        echouer("instruction_mal_placee", emoji=fichier[ligne][0])

            elif type(value) == Operation:
                echouer("operateur_sans_gauche", operateur=fichier[ligne][0])

            else:
                echouer("valeur_en_debut_de_ligne", emoji=fichier[ligne][0])

        else:
            creat_variable(fichier[ligne])

    if corps:
        return (len(fichier), None)

    sys.exit(1)

# une ligne de a.txt : les emojis qu'elle contient et son numéro dans le fichier
class Ligne(list):
    def __init__(self, emojis, numero):
        super().__init__(emojis)
        self.numero = numero

def reading_code():
    with open('a.txt', 'r', encoding='utf-8') as fichier:
        translation = []

        for numero, line in enumerate(fichier, 1):
            value = get_emoji(line)
            if value != []:
                translation.append(Ligne(value, numero))

    return translation

try:
    read_lines(reading_code())

except ErreurUwU as erreur:
    echouer("valeur_levee", valeur=repr(erreur.valeur))

except Exception as erreur:
    # UWU_DEBUG=1 : laisse Python afficher son erreur complète, utile pour chercher un bug de l'interpréteur lui-même
    if os.environ.get("UWU_DEBUG"):
        raise

    echouer("erreur_python", type=type(erreur).__name__, message=str(erreur))
