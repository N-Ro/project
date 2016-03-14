#!/usr/bin/python3.5

import configparser

# On lit le fichier de config
fieldConfig = configparser.ConfigParser()
fieldConfig.read('config.ini')

# On va chercher les sections du fichier de config
sectionList = fieldConfig.sections()

print(sectionList)