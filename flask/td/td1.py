from flask import Flask

app = Flask(__name__)

@app.route('/salut/<nom>')
def salut(nom):
    return f"Bonjour {nom}"

@app.route('/carre/<int:n>')
def carre(n):
    return f"Le carré de {n} est {n**2}"

@app.route('/tva/<float:ht>')
def tva(ht):
    ttc = round(ht * 1.18, 2)
    return f"Prix TTC : {ttc}"

if __name__ == "__main__":
    app.run(debug=True)
