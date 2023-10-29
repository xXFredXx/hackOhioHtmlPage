Mock Data: https://docs.google.com/spreadsheets/d/1awYH2gfv3J0TQvzi3jE7TmuNQ5gnq4AROAk_5bfAntE/edit#gid=0

Server: server3.py
Data Science Script: Data.ipynd
React App: my-app

How to Run: Go to Veeva directory and run "python server3.py", then go to my-app directory and run "npm start".

The google sheet is a placeholder for what would ideally be a GCP/AWS bucket or database. The server stays connected to the webpage and checks for file modifications. If file modifications are found it will wend them to the react page.
