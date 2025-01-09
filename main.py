import json
def load_data(file_path):
    with open(file_path, 'r') as file:
        return json.load(file)

def get_popularity(file_path):
    data = load_data(file_path)
    score = 0
    entries = 0
    for stock, sentiment in data.items():

        posi_count = sentiment['positive']
        neg_count = sentiment['negative']
        neu_count = sentiment['neutral']

        entries += posi_count + neg_count + neu_count
        score += (posi_count - neg_count) 

        
    score = score / entries
    return entries, score

paths = ['crypto', 'stocks', 'etf']
for path in paths:
    entries, score = get_popularity(f'{path}_sentiment.json')
    print(f'popularity of {path} is {score} with total messages of {entries}')
