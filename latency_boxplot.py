# %%
import requests
import time
import csv

url = 'http://pra53-env.eba-jiexkzpm.us-east-1.elasticbeanstalk.com/predict'

test_cases = {
    'fake_news_1': "Your fake news article text 1.",
    'fake_news_2': "Your fake news article text 2.",
    'real_news_1': "Your real news article text 1.",
    'real_news_2': "Your real news article text 2."
}

def perform_test(case_name, text):
    latencies = []
    for i in range(100):
        start_time = time.time()
        payload = {'text': text}
        headers = {'Content-Type': 'application/json'}
        try:
            response = requests.post(url, json=payload, headers=headers)
            response.raise_for_status()
        except requests.exceptions.RequestException as e:
            print(f"Request failed: {e}")
            continue
        end_time = time.time()
        latency = (end_time - start_time) * 1000
        latencies.append(latency)
        print(f"{case_name} - Request {i+1}/100 - Latency: {latency:.2f} ms")

    csv_filename = f"results/csv/{case_name}_latency.csv"
    with open(csv_filename, 'w', newline='') as csvfile:
        fieldnames = ['Request Number', 'Latency (ms)']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for idx, latency in enumerate(latencies):
            writer.writerow({'Request Number': idx+1, 'Latency (ms)': latency})
    print(f"Saved latencies to {csv_filename}")
    return latencies

for case_name, text in test_cases.items():
    print(f"Starting performance test for {case_name}")
    perform_test(case_name, text)


# %%

import pandas as pd
import matplotlib.pyplot as plt

all_latencies = {}
test_cases = {
    'fake_news_1': "Your fake news article text 1.",
    'fake_news_2': "Your fake news article text 2.",
    'real_news_1': "Your real news article text 1.",
    'real_news_2': "Your real news article text 2."
}

for case_name in test_cases.keys():
    csv_filename = f"results/csv/{case_name}_latency.csv"
    df = pd.read_csv(csv_filename)
    all_latencies[case_name] = df['Latency (ms)']

df_latencies = pd.DataFrame(all_latencies)

average_latencies = df_latencies.mean()
print("Average Latencies (ms):")
print(average_latencies)

plt.figure(figsize=(10, 6))
df_latencies.boxplot()
plt.title('API Latency Performance')
plt.ylabel('Latency (ms)')
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig('results/boxplot/latency_boxplot.png')
plt.show()

plt.figure(figsize=(10, 6))
df_latencies.boxplot()
plt.title('API Latency Performance')
plt.ylabel('Latency (ms)')
plt.ylim(0, 150)
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig('results/boxplot/latency_boxplot_shrink.png')
plt.show()

# %%