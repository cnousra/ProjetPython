# Correction de G. Poux-Médard, 2021-2022

from Classes import Author
import re
import pandas as pd

# =============== 2.7 : CLASSE CORPUS ===============
class Corpus:
    def __init__(self, nom):
        self.nom = nom
        self.authors = {}
        self.aut2id = {}
        self.id2doc = {}
        self.ndoc = 0
        self.naut = 0
        self.chaine_unique = ""

    def add(self, doc):
        if doc.auteur not in self.aut2id:
            self.naut += 1
            self.authors[self.naut] = Author(doc.auteur)
            self.aut2id[doc.auteur] = self.naut
        self.authors[self.aut2id[doc.auteur]].add(doc.texte)

        self.ndoc += 1
        self.id2doc[self.ndoc] = doc

# =============== 2.8 : REPRESENTATION ===============
    def show(self, n_docs=-1, tri="abc"):
        docs = list(self.id2doc.values())
        if tri == "abc":  # Tri alphabétique
            docs = list(sorted(docs, key=lambda x: x.titre.lower()))[:n_docs]
        elif tri == "123":  # Tri temporel
            docs = list(sorted(docs, key=lambda x: x.date))[:n_docs]

        print("\n".join(list(map(repr, docs))))

    def __repr__(self):
        docs = list(self.id2doc.values())
        docs = list(sorted(docs, key=lambda x: x.titre.lower()))

        return "\n".join(list(map(str, docs)))
    
    def search(self, mot_cle):
        if not self.chaine_unique:
            corpus_mot_cle = []
            for a in self.authors.values():
                for d in a.production:
                    if re.search(mot_cle,d):
                        corpus_mot_cle.append(d)
            self.chaine_unique = " ".join(corpus_mot_cle)
        return self.chaine_unique
    
    def concorde(self, context_len, mot_cle):       
        df=pd.DataFrame()
        for a in self.authors.values():
            for d in a.production:
                match=re.search(mot_cle,d)
                if match:
                    start=match.start()
                    context_gauche=d[start-context_len:start]
                    context_droit=d[start+len(mot_cle):start+context_len]
                    new_row = pd.DataFrame({"contexte_gauche": [context_gauche], "motif_trouve": [mot_cle],"context_droit": [context_droit]})
                    df = df.append(new_row, ignore_index=True)
        return df
    
    def  nettoyer_texte(self,ch):
        ch=ch.lower()
        ch=ch.replace("\n"," ")
        ch=re.sub(r'[^\w\s]', '', ch)
        ch=re.sub(r'[0-9]', '', ch)
        return ch
    
    def stats(self): 
        freq=pd.DataFrame(columns=["mots","term frequency","document frequency"])
        for a in self.authors.values():
            for d in a.production:
                txt_nettoye=self.nettoyer_texte(d)
                word=txt_nettoye.split()
                for w in word:
                    if w!='':
                        if w in list(freq["mots"]):
                            freq.loc[freq.mots==w,"term frequency"] += 1
                        else:
                            freq.loc[len(freq)] = [w, 1, 0]
         
        for w in list(freq["mots"]):
            for a in self.authors.values():
                for d in a.production:
                    if (re.search(" "+w+" ", self.nettoyer_texte(d))):        
                       freq.loc[freq.mots==w,"document frequency"] += 1
        return freq
    
    
        


