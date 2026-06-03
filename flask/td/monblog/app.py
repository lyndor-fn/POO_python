from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def accueil():
    articles = [
        {"titre": "Découvrir Flask", "auteur": "Aminata", "resume": "Flask est un micro-framework léger et flexible..."},
        {"titre": "Jinja2 en pratique", "auteur": "Mamadou", "resume": "Jinja2 permet de séparer la logique Python du HTML..."},
        {"titre": "Les routes dynamiques", "auteur": "Fatou", "resume": "Avec Flask, on peut définir des routes statiques et dynamiques..."}
    ]
    return render_template("accueil.html", articles=articles)

if __name__ == "__main__":
    app.run(debug=True)
