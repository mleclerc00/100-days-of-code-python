from requests import get

parameters = {"amount": 10, "type": "boolean"}

# Get the questions from the API
response = get("https://opentdb.com/api.php", params=parameters)
response.raise_for_status()
question_data = response.json()["results"]
