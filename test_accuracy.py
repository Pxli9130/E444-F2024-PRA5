# %%
import requests

api_url = 'http://pra53-env.eba-jiexkzpm.us-east-1.elasticbeanstalk.com/predict'

test_cases = {
    'Fake News 1': "fake news 1.",
    'Fake News 2': "fake news 2.",
    'Real News 1': "Some Liberal MPs issue a deadline to Trudeau: make up your mind to stay or go by Oct. 28",
    'Real News 2': "Bank of Canada makes a chunkier rate cut, lowering by half point for 1st time since pandemic."
}

for case_name, text in test_cases.items():
    payload = {'text': text}
    response = requests.post(api_url, json=payload)
    print(f"{case_name} - Status Code: {response.status_code}")
    print(f"Response: {response.json()}")
    print("-" * 50)

# %%
