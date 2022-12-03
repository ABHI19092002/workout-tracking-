import requests
import os
from datetime import datetime

GENDER = "male"
WEIGHT_KG = 50
HEIGHT_CM = 172
AGE = 19

api_key = os.environ.get("API_KEY")
api_id = os.environ.get("API_ID")

exercise_text = input("Enter KM you run today: ")

headers = {
    "x-app-id": api_id,
    "x-app-key": api_key
}

api_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"

parameters = {
    "query": exercise_text,
    "gender": GENDER,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT_CM,
    "age": AGE
}

response = requests.post(api_endpoint, json=parameters, headers=headers)
result = response.json()
print(result)

post_endpoint = os.environ.get("SHEET_ENDPOINT")
today_date = datetime.now().strftime("%d/%m/%Y")
now_time = datetime.now().strftime("%X")
secret_token =os.environ.get("SECRET_TOKEN")
secret_header = {
    "Authorization": f"Bearer {secret_token}"
}

#for exercise in result["exercises"]:
#    sheet_inputs = {
#        "workout": {
#            "date": today_date,
#            "time": now_time,
#            "exercise": exercise["name"].title(),
#            "duration": exercise["duration_min"],
#            "calories": exercise["nf_calories"]
#        }
#    }
#
#    sheet_response = requests.post(post_endpoint, json=sheet_inputs, headers=secret_header)
#