import requests



APP_ID = "69c39d92"
API_KEY = "66968c3cb9aeae08cf7c53b916403730	"
USER = "tulan"
user_query = input("Tell me which exercises you did: ")
headers = {
    "x-app-id" : APP_ID,
    "x-app-key" : API_KEY,
}

nutritionix_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"

update_data = {

    "query" : user_query,
    "gender" : "male",
    "weight_kg" : "77",
    "height_cm" : "185",
    "age" : "27",
}


response = requests.post(url=nutritionix_endpoint, json=update_data, headers=headers)
print(response.json())