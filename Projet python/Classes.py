# Correction de G. Poux-Médard, 2021-2022

# =============== 2.1 : La classe Document ===============
class Document:
    # Initialisation des variables de la classe
    def __init__(self, titre="", auteur="", date="", url="", texte=""):
        self.titre = titre
        self.auteur = auteur
        self.date = date
        self.url = url
        self.texte = texte

# =============== 2.2 : REPRESENTATIONS ===============
    # Fonction qui renvoie le texte à afficher lorsqu'on tape repr(classe)
    def __repr__(self):
        return f"Titre : {self.titre}\tAuteur : {self.auteur}\tDate : {self.date}\tURL : {self.url}\tTexte : {self.texte}\t"

    # Fonction qui renvoie le texte à afficher lorsqu'on tape str(classe)
    def __str__(self):
        return f"{self.titre}, par {self.auteur}"



# =============== 2.4 : La classe Author ===============
class Author:
    def __init__(self, name):
        self.name = name
        self.ndoc = 0
        self.production = []
# =============== 2.5 : ADD ===============
    def add(self, production):
        self.ndoc += 1
        self.production.append(production)
    def __str__(self):
        return f"Auteur : {self.name}\t# productions : {self.ndoc}"
    
class RedditDocument(Document):
    
    def __init__(self,nb_comment="",titre="", auteur="", date="", url="", texte=""):
        super.__init__(titre="", auteur="", date="", url="", texte="")
        self.nb_comment=nb_comment
        
    def get_nb_comment(self):
        return self.nb_comment

    def set_nb_comment(self, nb_comment):
        self.nb_comment = nb_comment 
        
    def __str__(self):
        super.__str__(self)
        
class ArxivDocument(Document):
    def __init__(self,coAuthors,titre="", auteur="", date="", url="", texte=""):
        super.__init__(titre="", auteur="", date="", url="", texte="")
        self.coAuthors=coAuthors
        
        def get_coAthors(self):
            return self.coAuthors

        def set_coAthors(self, nb_comment):
            self.coAuthors = coAuthors 
            
        def __str__(self):
            super.__str__(self)
        