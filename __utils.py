import json 



def _translate(key, lang='fr'):
"""
  Fonction pour traduire un mot de reference par rapport 
    à son clé dans le fichier langs.json """
    
  with open('langs.json') as fichier: 
    trans = json.loads(fichier)
  return trans.get(key).get(lang)
  
