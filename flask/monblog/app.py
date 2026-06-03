#	app.py
import form
import required

from flask import Flask,request

#	1)	Création	de	l'objet	application
app = Flask(__name__)


@app.route("/")
def accueil():
    return "Page	d'accueil"


@app.route("/contact")
def contact():
    return "Page	de	contact"


@app.route("/a-propos")
def a_propos():
    return "A	propos	de	l'application"


@app.route("/utilisateur/<nom>")
def profil(nom):
    return f"Profil	de	{nom}"


@app.route("/fichier/<path:chemin>")
def voir_fichier(chemin):
    return f"Vous	demandez	:	{chemin}"


@app.route("/connexion", methods=["GET", "POST"])
def connexion():
    if request.method == "POST":
        email = request.form.get("email")
        return f"Tentative	de	connexion	pour	{email}"
    return ""
<form method = "post">
    <input name = "email" type = "email" required>
    <input name = "mdp" type = "password" required>
    <button> Se connecter </button>
</form>
#	3)	Lancement	du	serveur	en	mode	debug
if __name__ == "__main__":
    app.run(debug=True)
