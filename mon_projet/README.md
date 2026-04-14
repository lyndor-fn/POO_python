## Objectifs
A. Créer des modules et les organiser.
B. Les importer et s’en servir dans le code.
C. Utilisation des imports relatifs et les packages.
D. Contrôler ce qui est exporté avec __all__.
E. Installer des modules externes et les utiliser.

## Structure du projet
mon_projet/
├── __init__.py
├── main.py
├── main2.py
├── main3.py
├── meteo_main.py
├── maths/
│   ├── __init__.py
│   ├── operations.py
│   └── statistiques.py
├── utils/
│   ├── __init__.py
│   └── string_utils.py
└── requirements.txt

## Étapes d'installation
création d’un environnement (optionnel):
on a créer un environnement virtuel avant d’installer les dépendances avec:
python -m venv env
env\Scripts\activate

Installer les dépendances :
pip install -r requirements.txt

## Commandes d'exécution
-python mon_projet/main.py
-python -m mon_projet.main2
-python mon_projet/main3.py
-python mon_projet/meteo_main.py
