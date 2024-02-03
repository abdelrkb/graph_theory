import itertools
#-------------------------------------------------------------#
#1 Mots, langages et automates...
#-------------------------------------------------------------#
# #1.1 Mots

#1.1.1 Fonction prefixe
def pref(u):
    """
    Étant donné un mot u passé en paramètre on renvoie la liste de ses préfixes.
    >>> pref("coucou")
    ['', 'c', 'co', 'cou', 'couc', 'couco', 'coucou']
    """
    prefixes = []
    for i in range(len(u)+1):
        prefixes.append(u[:i])
    return prefixes


#1.1.2 Fonction suffixe
def suf(u):
    """
    Étant donné un mot u passé en paramètre on renvoie la liste de ses suffixes.
    >>> suf("couucou")
    ['coucou', 'oucou', 'ucou', 'cou', 'ou', 'u', '']
    """
    suffixes = []
    for i in range(len(u)+1):
        suffixes.append(u[i:])
    return suffixes


#1.1.3 Fonction facteur
def fact(u):
    """
    Étant donné un mot u passé en paramètre on renvoie la liste de ses facteurs.
    >>> fact("coucou")
    ['', 'c', 'co', 'cou', 'couc', 'couco', 'coucou', 'o', 'ou','ouc', 'ouco', 'oucou', 'u', 'uc', 'uco', 'ucou']   
    """
    factors = set()
    for i in range(len(u)):
        for j in range(i, len(u)):
            factors.add(u[i:j+1])
    return sorted(list(factors))



#1.1.4 Fonction miroir
def miroir(u):
    """
    Étant donné un mot u passé en paramètre on renvoie le miroir du mot u.
    >>> miroir("coucou")
    "uocuoc"
    """
    return u[::-1]




#1.2 Langages
#1.2.1. Fonction concatene
def concatene(L1,L2):
    """
    Etant donnés deux langages L1 et L2 renvoie le
    produit de concaténation (sans doublons) de L1 et L2.
    >>> L1=['aa','ab','ba','bb']
    >>> L2=['a', 'b', '']
    >>> concatene((L1,L2))
    ['aaa', 'aab', 'aa', 'aba', 'abb', 'ab', 'baa', 'bab', 'ba', 'bba', 'bbb', 'bb']
    """
    res = set()
    for mot1 in L1:
        for mot2 in L2:
            res.add(mot1 + mot2)
    return sorted(list(res))

#1.2.2 Fonction puis
def puis(L,n):
    """
    étant donnés un langage L et un entier n renvoie le
    langage L^n (sans doublons).
    >>> puis(['aa','ab','ba','bb'],2)
    ['aaaa', 'aaab', 'aaba', 'aabb', 'abaa', 'abab', 'abba', 'abbb', 'baaa', 'baab',
    'baba', 'babb', 'bbaa', 'bbab', 'bbba', 'bbbb']
    """
    res = L[:]
    for i in range(n-1):
        temp = []
        for mot1 in res:
            for mot2 in L:
                concat = mot1 + mot2
                if concat not in temp:
                    temp.append(concat)
        res = temp[:]
    return res

#1.2.3. Pourquoi ne peut-on pas faire de fonction calculant l’étoile d’un langage ?
"""
On peut en théorie calculer l'étoile d'un langage, qui correspond à l'ensemble de toutes les concaténations possibles des mots du langage, y compris les concaténations 
de zéro ou plusieurs mots. Cependant, le problème est que l'étoile d'un langage peut être infini, même si le langage de départ est fini. Par exemple, 
l'étoile du langage {'a', 'b'} est l'ensemble de toutes les chaînes de caractères composées des lettres 'a' et 'b', ce qui est un ensemble infini.
"""

#A retester sinon écrire [''] + mots
#1.2.4 Fonction tousmots
def tousmots(L,n):
    """
    étant donné un alphabet A passé en paramètre
    renvoie la liste de tous les mots de A* de longueur inférieure à n
    >>> tousmots(['a','b'], 3)
    ['a', 'b', 'aa', 'ab', 'ba', 'bb', 'aaa', 'aab',
    'aba', 'abb', 'baa', 'bab', 'bba', 'bbb', '']

    """
    if n == 0:
        return ['']
    else:
        mots = [mot + c for c in L for mot in tousmots(L, n-1)]
        return mots

#1.3 Automates
#1.3.1 Fonction defauto
def defauto():
    """
    permet de faire la saisie d’un automate (sans doublon).
    """
    auto = {}
    auto["alphabet"] = list(input("Alphabet (séparé par des virgules): ").split(","))
    auto["etats"] = list(input("Ensemble des états (séparé par des virgules): ").split(","))
    auto["transitions"] = []
    auto["I"] = list(input("Ensemble des états initiaux (séparé par des virgules): ").split(","))
    auto["F"] = list(input("Ensemble des états finaux (séparé par des virgules): ").split(","))
    
    transitions = []
    print("Entrez 'stop' quand vous avez finis d'entrez vos transitions")
    while True:
        transition = input("Transition (format: etat,lettre,etat): ")
        if transition == "stop":
            break
        transitions.append(list(transition.split(",")))
    
    auto["transitions"] = transitions
    return auto


#A revoir
#1.3.2 Fonction lirelettre
def lirelettre(T,E,a):
    """
    étant donnés en paramètres une liste de transi- tions T, une liste d’états E et une lettre a, 
    renvoie la liste des états dans lesquels on peut arriver en partant d’un état de E et en lisant la lettre a.
    >>> lirelettre(auto["transitions"],auto["etats"],'a')
    [2,4]
    """
    res = []
    for transition in T:
        if transition[1] == a:
            if transition[0] in E and transition[2] not in res:
                res.append(transition[2])
    return res


#1.3.3 Fonction liremot
def liremot(T,E,m):
    """
    étant donnés en paramètres une liste de transitions T, une liste d’états E et un mot m, 
    renvoie la liste des états dans lesquels on peut arriver en partant d’un état de E et en lisant le mot m.
    """
    liste_mot = []
    for lettre in m:
        liste_mot.append(lettre)
    while (len(liste_mot)>0):
        if lirelettre(T, E, liste_mot[0]):
            chemin = lirelettre(T, E, liste_mot[0])
            E = chemin
            del(liste_mot[0])
        else:
            return None
    return E
            




#1.3.4 fonction accepte
def accepte(auto, m):
    """
    Définir une fonction accepte qui prend en paramètres un automate et un mot m et
    renvoie True si le mot m est accepté par l’automate.
    """
    etats_courants = auto["I"]  # on initialise les états courants avec l'état initial
    for lettre in m:
        etats_suivants = lirelettre(auto["transitions"], etats_courants, lettre)
        etats_courants = etats_suivants
    return bool(set(etats_courants) & set(auto["F"]))

#A refaire pas reussi
#1.3.5 fonction langage_accept

def continuer(etat, chemin, n, results):
    if len(chemin) >= n:
        return []  # le mot est trop long, on s'arrête
    if etat in auto["F"]:     # l'état actuel est un état final, on ajoute le mot à la liste des résultats
        results.append(chemin)
    for transition in auto["transitions"]:
        if transition[0] == etat:    # la transition commence à l'état actuel, on explore la suite du mot
            continuer(transition[2], chemin + transition[1], n, results)

def langage_accept(auto, n):
    """
    Prend en paramètres un automate et un entier n et renvoie la liste des mots de longueur inférieure à n acceptés par l’automate.
    """
    results = []
    for i in auto["I"]:    # pour chaque état initial, on explore toutes les transitions possibles
        continuer(i, "", n, results)
    return results

#-------------------------------------------------------------#
#2 Déterminisation
#-------------------------------------------------------------#

#2.1 fonction deterministe

def deterministe(auto):
    """
    étant donné un automate passé en paramètre renvoie True s’il est déterministe et False sinon.
    """ 
    for i in range(len(auto["transitions"])-1):
        for j in range(i+1, len(auto["transitions"])):
            if (auto["transitions"][i][0] == auto["transitions"][j][0]) and (auto["transitions"][i][1] == auto["transitions"][j][1]):
                return False
    return True

#2.2 fonction determinise
def determinise(auto):
    """
    déterminise l’automate passé en paramètre.
    """
    if deterministe(auto) == True:
        return auto

    new_auto ={"alphabet":['a','b'],"etats": [auto["I"]], "transitions":[], "I":[auto["I"]],"F":[]}

    for etat in new_auto["etats"]:
        for lettre in new_auto["alphabet"]:
            if lirelettre(auto["transitions"], etat, lettre):
                new_auto["transitions"].append([etat, lettre, lirelettre(auto["transitions"], etat, lettre)])
                if lirelettre(auto["transitions"], etat, lettre) not in new_auto["etats"]:
                    new_auto["etats"].append(lirelettre(auto["transitions"], etat, lettre))
    for etats in new_auto["etats"]:
        for final in auto["F"]:
            if final in etats:
                new_auto["F"].append(etats)
    return new_auto

#2.3
def rennomage(auto):
    """
    Étant donné un automate passé en paramètre renomme ses états avec les premiers entiers.
    """
    for i in range(len(auto["etats"])):
        temp = auto["etats"][i]
        auto["etats"][i] = i
        for j in range(len(auto["transitions"])):
            if auto["transitions"][j][0] == temp:
                auto["transitions"][j][0] = i
            if auto["transitions"][j][2] == temp:
                auto["transitions"][j][2] = i
        for j in range(len(auto["I"])):
            if auto["I"][j] == temp:
                auto["I"][j] = i
        for j in range(len(auto["F"])):
            if auto["F"][j] == temp:
                auto["F"][j] = i
    return auto

#-------------------------------------------------------------#
#3 Complémentation.
#-------------------------------------------------------------#

#3.1 fonciton complet
def complet(auto):
    """
    étant donné un automate passé en paramètre renvoie True s’il est complet et False sinon.
    >>> complet(auto0)
    False 
    >>> complet(auto1)
    True
    """
    etats = auto["etats"]
    alphabet = auto["alphabet"]
    transitions = auto["transitions"]
    
    for etat in etats:
        for lettre in alphabet:
            trouve = False
            for transition in transitions:
                if transition[0] == etat and transition[1] == lettre:
                    trouve = True
                    break
            if not trouve:
                return False
    
    return True

#3.2 fonction complete
def complete(auto):
    """
    Complète l'automate passé en paramètre en ajoutant un état puits
    >>> complete(auto0)
    {'alphabet': ['a', 'b'], 'etats': [0, 1, 2, 3, 4],'transitions': [[0, 'a', 1], [1, 'a', 1], [1, 'b', 2], [2, 'a', 3],[0, 'b', 4], [2, 'b', 4], [3, 'a', 4], [3, 'b', 4], [4, 'a', 4], [4, 'b', 4]],'I': [0], 'F': [3]}
    """
    # Création de l'état puit
    puit = max(auto["etats"]) + 1
    alphabet = auto["alphabet"]
    transitions = auto["transitions"]
    etats = auto["etats"]
    I = auto["I"]
    F = auto["F"]
    
    # Ajout des transitions manquantes vers l'état puit
    for etat in etats:
        for symbole in alphabet:
            if [etat, symbole] not in [[t[0], t[1]] for t in transitions]:
                transitions.append([etat, symbole, puit])
                
    # Ajout des transitions de l'état puit vers lui-même
    for symbole in alphabet:
        transitions.append([puit, symbole, puit])
    
    # Ajout de l'état puit à la liste des états
    etats.append(puit)
    
    automate_complet = {"alphabet": alphabet,
                        "etats": etats,
                        "transitions": transitions,
                        "I": I,
                        "F": F}
    
    return automate_complet

#3.3 fonction complement

def complement(auto):
    """
    étant donné un automate passé en paramètre acceptant un langage L renvoie un automate acceptant le complement de L. 
    N’hésitez pas à utiliser les fonctions précédemment définies.
    """
    auto = determinise(auto)
    auto = rennomage(auto)
    if complet(auto) != True:
        auto = complete(auto)
    auto = rennomage(auto)
    for etat in auto["etats"]:
        if etat in auto["F"]:
            auto["F"].remove(etat)
        else:
            auto["F"].append(etat)

    return auto

#-------------------------------------------------------------#
#4 Automates Produit.
#-------------------------------------------------------------#

def veriflirelettre(T, e, a):
    res = []
    for transition in T:
        if transition[1] == a:
            if transition[0] == e and transition[2] not in res:
                res.append(transition[2])
    return res

#4.1 foncction inter
def inter(auto1, auto2):
    """
    étant donnés deux automates déterministes passés en paramètres acceptant respectivement les langages L1 et L2, 
    renvoie l’automate produit acceptant l’intersection L1 ∩ L2.
    """
    new_auto = dict()

    new_auto["alphabet"] = []
    for lettre in auto1["alphabet"]:
        new_auto["alphabet"].append(lettre)
    for lettre in auto2["alphabet"]:
        if lettre not in new_auto["alphabet"]:
            new_auto["alphabet"].append(lettre)

    new_auto["I"] = []
    for initial1 in auto1["I"]:
        for initial2 in auto2["I"]:
            new_auto["I"].append((initial1, initial2))
        
    new_auto["etats"] = []
    for initial in new_auto["I"]:
        new_auto["etats"].append(initial)

    new_auto["transitions"] = []
    for etat in new_auto["etats"]:
        for lettre in new_auto["alphabet"]:
            for transition1 in auto1["transitions"]:
                for transition2 in auto2["transitions"]:
                    if (transition1[0] == etat[0]) and (transition2[0] == etat[1]) and (transition1[1] == transition2[1]):
                        if [(transition1[0], transition2[0]), transition1[1], (transition1[2], transition2[2])] not in new_auto["transitions"]:
                            new_auto["transitions"].append([(transition1[0], transition2[0]), transition1[1], (transition1[2], transition2[2])])
                        if (transition1[2], transition2[2]) not in new_auto["etats"]:
                            new_auto["etats"].append((transition1[2], transition2[2]))



    new_auto["F"] = []
    for etatfin1 in auto1["F"]:
        for etatfin2 in auto2["F"]:
            new_auto["F"].append((etatfin1, etatfin2))

    return new_auto

#4.2 fonction différence
def difference(auto1, auto2):
    """
    étant donnés deux automates déterministes passés en paramètres acceptant respectivement les langages L1 et L2, 
    renvoie l’automate produit acceptant la difference L1 \ L2. 
    """
    auto1 = determinise(auto1)
    auto1 = rennomage(auto1)
    if complet(auto1) != True:
        auto1 = complete(auto1)
    auto1 = rennomage(auto1)
    auto2 = determinise(auto2)
    auto2 = rennomage(auto2)
    if complet(auto2) != True:
        auto2 = complete(auto2)
    auto2 = rennomage(auto2)
    return inter(auto1, complement(auto2))

#-------------------------------------------------------------#
#5 Propriété de fermeture
#-------------------------------------------------------------#

#5.1 fonction prefixe
def prefixe(auto):
    """
    étant donné un automate émondé acceptant L renvoie
    un automate acceptant l’ensemble des préfixes des mots de L
    """
    auto["F"] = auto["etats"]
    return auto

#5.2 fonction suffixe
def suffixe(auto):
    """
    étant donné un automate émondé acceptant L renvoie
    un automate acceptant l’ensemble des préfixes des mots de L
    """
    auto["I"] = auto["etats"]
    return auto

#5.3 fonction facteur
def facteur(auto):
    """
    étant donné un automate émondé acceptant L renvoie
    un automate acceptant l’ensemble des facteurs des mots de L.
    """
    return suffixe(prefixe(auto))

#5.4 fonction miroir
def miroir2(auto):
    """
    étant donné un automate émondé acceptant L renvoie
    un automate acceptant l’ensemble des miroirs des mots de L.
    """
    temp = auto["I"][:]
    auto["I"] = auto["F"][:]
    auto["F"] = temp
    return auto

#-------------------------------------------------------------#
#6 Minimisation.
#Partie non réussi du projet nous avons néanmoins laissé des traces de ce que nous avons essayé de faire.
#-------------------------------------------------------------#
def partition_initiale(auto):
    """
    Fonction qui crée la partition initiale en séparant les états finaux des états non-finaux.
    """
    partition = [[etat for etat in auto["etats"] if etat in auto["F"]],
                 [etat for etat in auto["etats"] if etat not in auto["F"]]]
    return partition

def partitionner(partition, auto):
    """
    Fonction qui partitionne les états en fonction des transitions sortantes de chaque état.
    """
    partitions = []
    for groupe in partition:
        nouveaux_groupes = {}
        for etat in groupe:
            transitions = auto["transitions"][etat]
            symboles = auto["alphabet"]
            groupe_suivant = None
            for i in range(len(symboles)):
                symbole = symboles[i]
                etat_suivant = transitions[i]
                for j in range(len(partition)):
                    if etat_suivant in partition[j]:
                        groupe_suivant = j
                        break
                if groupe_suivant in nouveaux_groupes:
                    nouveaux_groupes[groupe_suivant].append((etat, symbole))
                else:
                    nouveaux_groupes[groupe_suivant] = [(etat, symbole)]
        for groupe_suivant in nouveaux_groupes:
            partitions.append([etat for (etat, symbole) in nouveaux_groupes[groupe_suivant]])
    return partitions


def minimise(auto):
    """
    Fonction qui minimise un automate complet et déterministe en utilisant l'algorithme de Moore.
    """
    partition = partition_initiale(auto)
    partitions_courantes = partitionner(partition, auto)
    while len(partitions_courantes) != len(partition):
        partition = partitions_courantes
        partitions_courantes = partitionner(partition, auto)
    return auto


if __name__ == "__main__":
#Automates de test#
#Definition d'automate test
    auto ={"alphabet":['a','b'],"etats": [1,2,3,4],"transitions":[[1,'a',2],[2,'a',2],[2,'b',3],[3,'a',4]],"I":[1],"F":[4]}
    auto0 ={"alphabet":['a','b'],"etats": [0,1,2,3],"transitions":[[0,'a',1],[1,'a',1],[1,'b',2],[2,'a',3]], "I":[0],"F":[3]}
    auto1 ={"alphabet":['a','b'],"etats": [0,1],"transitions":[[0,'a',0],[0,'b',1],[1,'b',1],[1,'a',1]], "I":[0],"F":[1]}
    auto2={"alphabet":['a','b'],"etats": [0,1],"transitions":[[0,'a',0],[0,'a',1],[1,'b',1],[1,'a',1]], "I":[0],"F":[1]}
    auto3 ={"alphabet":['a','b'],"etats": [0,1,2,],"transitions":[[0,'a',1],[0,'a',0],[1,'b',2],[1,'b',1]], "I":[0],"F":[2]}
    auto4 ={"alphabet":['a','b'],"etats": [0,1,2],"transitions":[[0,'a',1],[1,'b',2],[2,'b',2],[2,'a',2]], "I":[0],"F":[2]}
    auto5 ={"alphabet":['a','b'],"etats": [0,1,2],"transitions":[[0,'a',0],[0,'b',1],[1,'a',1],[1,'b',2],[2,'a',2],[2,'b',0]], "I":[0],"F":[0,1]}
    auto6 ={"alphabet":['a','b'],"etats": [0,1,2,3,4,5],
    "transitions":[[0,'a',4],[0,'b',3],[1,'a',5],[1,'b',5],[2,'a',5],[2,'b',2],[3,'a',1],[3,'b',0],[4,'a',1],[4,'b',2],[5,'a',2],[5,'b',5]],"I":[0],"F":[0,1,2,5]}
   
    print(minimise(auto6))
