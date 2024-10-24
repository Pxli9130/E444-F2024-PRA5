# %%
import requests

api_url = 'http://pra53-env.eba-jiexkzpm.us-east-1.elasticbeanstalk.com/predict'

test_cases = [
    {"text": "This is fake news about an event that never happened."},
    {"text": "Another fake news input to test the model."},
    {"text": "Some Liberal MPs issue a deadline to Trudeau: make up your mind to stay or go by Oct. 28"},
    {"text": "Bank of Canada makes a chunkier rate cut, lowering by half point for 1st time since pandemic"}
]

for i, test_case in enumerate(test_cases):
    response = requests.post(api_url, json=test_case)
    print(f"Test Case {i+1} - Status Code: {response.status_code}")
    print(f"Test Case {i+1} - Raw Response: {response.text}")

    try:
        json_response = response.json()
        print(f"Test Case {i+1} - JSON Response: {json_response}")
    except requests.exceptions.JSONDecodeError:
        print(f"Test Case {i+1} - Failed to decode JSON")

# %%
