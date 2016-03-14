#!/usr/bin/python3.5

import configparser

# On lit le fichier de config
fieldConfig = configparser.ConfigParser()
fieldConfig.read('config.ini')

# On va chercher les sections (champs) du fichier de config
sectionList = fieldConfig.sections()

print('Liste totale des champs :', sectionList)

# On vérifie que le champs est à prendre en compte (True - False)
# On construit une liste en conséquence
fieldList = []

for fieldName in sectionList :
	if fieldConfig.getboolean(fieldName,'active') == True:
		fieldList.append(fieldName)
		
print('Liste des champs actifs :',fieldList)

# On souhaite obtenir les descriptions des champs actifs :
for singleField in fieldList:
	print('Description des champs actifs :', fieldConfig.get(singleField, 'description'))