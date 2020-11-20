import json 



def translate(key, lang='mg'):
	"""
	  Fonction pour traduire un mot de reference par rapport 
	    à son clé dans le fichier langs.json """
    
	with open('langs.json') as fichier: 
		trans = json.load(fichier)
	mot_cle = trans.get(key)
	if mot_cle:
		return mot_cle.get(lang) \
			if mot_cle.get(lang) else mot_cle
	else:
		return mot_cle  
	return trans.get(key).get(lang)
  
