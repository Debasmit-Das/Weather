import requests

API_KEY = "4e6f053796c10cd5e008545405cb6b8f"
BASE_URL = "http://api.openweathermap.org/data/2.5/weather"
CITY = input("Enter a city:")
request_url = f"{BASE_URL}?appid={API_KEY}&q={CITY}"
response = requests.get(request_url)
if response.status_code ==200:
    print(response.json()["weather"][0]["description"] )
    print(round(response.json()["main"]["temp"]-273.15))
else:
    print("An error occurred/or te city is not in our databasee")
