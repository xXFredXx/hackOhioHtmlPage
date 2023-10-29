#%%
import requests
import pandas as pd
#%%
url = "https://docs.google.com/spreadsheets/d/1awYH2gfv3J0TQvzi3jE7TmuNQ5gnq4AROAk_5bfAntE/edit#gid=0"

response = requests.get(url)
response.raise_for_status()  # This will raise an exception if there's an error

with open("output.csv", "wb") as file:
    file.write(response.content)
#%%
x = pd.read_csv('output.csv')
x.head(1)
