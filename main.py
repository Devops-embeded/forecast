import requests
import datetime

# Votre clé API Wunderground (remplacez par votre propre clé)
API_KEY = "56cd9f6adae046a58d9f6adae0d6a5d2"
# Coordonnées des lieux
LOCATIONS = {
    "Toulouse": {"lat": 43.6045, "lon": 1.444},
    "Saint-Geours-de-Maremne": {"lat": 43.671, "lon": -1.152},
    "Paris": {"lat": 48.8566, "lon": 2.3522},
}

# URL de l'API Weather Underground
BASE_URL = "https://api.weather.com/v3/wx/forecast/daily/5day"

def fetch_weather_data(api_key, lat, lon):
    """
    Récupère les prévisions météorologiques pour une latitude et une longitude.
    """
    params = {
        "apiKey": api_key,
        "geocode": f"{lat},{lon}",
        "format": "json",
        "units": "m",  # Températures en Celsius
        "language": "fr-FR",  # Langue française
    }
    response = requests.get(BASE_URL, params=params)
    response.raise_for_status()  # Lève une exception si la requête échoue
    return response.json()

def display_forecast(location, data):
    """
    Affiche les prévisions météo pour les lieux données.
    """
    print(f"Prévisions météorologiques pour {location} :")
    for index in range(len(data["temperatureMin"])):
        date = datetime.datetime.strptime(data["validTimeLocal"][index], "%Y-%m-%dT%H:%M:%S%z").date()
        temp_min = data["temperatureMin"][index]
        temp_max = data["temperatureMax"][index]
        print(f"{date}: Min {temp_min}°C, Max {temp_max}°C")
    print()

# Récupération et affichage des données météorologiques pour chaque lieu
try:
    for location, coords in LOCATIONS.items():
        weather_data = fetch_weather_data(API_KEY, coords["lat"], coords["lon"])
        display_forecast(location, weather_data)
except requests.RequestException as e:
    print(f"Erreur lors de la récupération des données : {e}")
except KeyError as e:
    print(f"Clé manquante dans la réponse API : {e}")