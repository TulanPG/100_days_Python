
from twilio.rest import Client
import requests

account_sid = "ACcafd34be34a7545926109200825cf4b0"
auth_token = "d9e6ce53e8520e0c02464d877803e7de"
OWM_Endpoint = "https://api.openweathermap.org/data/2.5/onecall"
api_key = "127dbad9658d998d37d1b90f3be86858"
exclude_id = "current,minutely,daily,alerts"

weather_params = {
    "lat": 54.357041,
    "lon": 18.577538,
    "appid": api_key,
    "exclude": exclude_id
}

response = requests.get(OWM_Endpoint, params=weather_params)
response.raise_for_status()
weather_data = response.json()
weather_slice = weather_data["hourly"][:12]

will_rain = False

for hour_data in weather_slice:
    condition_code = (hour_data["weather"][0]["id"])
    if int(condition_code) < 700:
        will_rain = True

if will_rain:
    client = Client(account_sid, auth_token)

    message = client.messages \
        .create(
        body="Weź parasol, będzie padać!.",
        from_='+18454098841',
        to='+48662577226'
    )

if not will_rain:
    print("Good weather")




