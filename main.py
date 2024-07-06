# main.py

import os
import argparse

def lister_fichiers(repertoire):
    files = os.listdir(repertoire)
    for file in files:
        print(file)

def creer_repertoire(nom):
    os.makedirs(nom)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Gestionnaire de fichiers simple")
    parser.add_argument("--repertoire", default=".", help="Répertoire à lister")
    parser.add_argument("--creer", help="Créer un répertoire")
    args = parser.parse_args()
    
    if args.creer:
        creer_repertoire(args.creer)
    else:
        lister_fichiers(args.repertoire)
