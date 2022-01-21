#POO - Programmation Orienté Objet

class Compteur :
    """Cette classe possède un attribut de classe qui s'incréente à chaque ois
    que lon va crer un object Compteur. chacun de ces objets est rajouté à une 
    liste qui peut être ré-installer par une méthode de classe"""
    
    #attribut de clase
    nb_objets_crees = 0
    objets_crees = []
    
    # Méthode de classe
    def init_objets_crees():
        print(len(Compteur.objets_crees), "objets créés.")
        Compteur.objects_crees = []