import requests

# Étape 1 : Paramètres de l'API
API_KEY = "5e7d51348b43d9c60f6640b1b0594997"
BASE_URL = "http://api.openweathermap.org/data/2.5/weather"
VILLE = "Dakar"

# Étape 2 : Construction de la requête
params = {
    "q": VILLE,
    "appid": API_KEY,
    "units": "metric",       # Température en °C
    "lang": "fr"             # Description en français
}

# Étape 3 : Requête GET
response = requests.get(BASE_URL, params=params)

# Étape 4 : Traitement de la réponse
if response.status_code == 200:
    data = response.json()
    temperature = data["main"]["temp"]
    description = data["weather"][0]["description"]
    humidite = data["main"]["humidity"]

    print(f"Météo à {VILLE}:")
    print(f"-- Température : {temperature}°C")
    print(f"-- Description : {description}")
    print(f"-- Humidité : {humidite}%")
else:
    print(f"Erreur lors de la requête : {response.status_code}")
    print(response.text)