# API imports
import requests
import json
# CSV imports
import csv
# Path imports
from pathlib import Path
# SQLite imports
import sqlite3
# Application imports
from PIL import Image, ImageTk
import tkinter as tk
import urllib3 
from io import BytesIO


# Create the colors class
class colors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


# Print console initial message
print(f'''{colors.FAIL}{colors.BOLD}
+------------------------------------------------+
|               _                                |
|   _ __   ___ | | _____ _ __ ___   ___  _ __    |
|  | '_ \ / _ \| |/ / _ \ '_ ` _ \ / _ \| '_ \   |
|  | |_) | (_) |   <  __/ | | | | | (_) | | | |  |
|  | .__/ \___/|_|\_\___|_| |_| |_|\___/|_| |_|  |
|  |_|                                           |
|                                                |
+------------------------------------------------+             
''')

# Get current path
path = Path(__file__).parent.resolve()

# # Create poke_data_list list starting empty
# poke_data_list = []

# # Iterate information about the first generation of pokemon
# for poke_index in range(1, 152):
#   # Connect to the API
#   poke_api = requests.get(f'https://pokeapi.co/api/v2/pokemon/{poke_index}')
#   # Parse API data with JSON
#   poke_information = json.loads(poke_api.text)
#   # Pokemon information
#   poke_id = poke_index
#   poke_name = poke_information['name']
#   poke_image = poke_information['sprites']['front_default']
#   poke_type = poke_information['types'][0]['type']['name']
#   # Create a list of tuples with pokemon information
#   poke_information = (poke_id, poke_name, poke_image, poke_type)
#   poke_data_list.append(poke_information)


# if Path(f'{path}/pokedex.csv').is_file():
#   print('Already exists.')
# else:
#   with open(f'{path}/pokedex.csv', 'w', encoding='UTF-8', newline='') as f:
#     writer = csv.writer(f, delimiter=';')
#     writer.writerow(['ID', 'NAME', 'IMAGE', 'TYPE'])
#     for row in poke_data_list:
#       writer.writerow(row)

# Verify if pokedex database already exists, if doesn't creates it
if Path(f"{path}/pokedex.db").is_file():
  print('Database already exists.')
else:
  f = open(f'{path}/pokedex.db', 'x')

# Connect to sqlite database
con = sqlite3.connect('pokedex.db')

# Create a Cursor object
cur = con.cursor()

# Create the main table
cur.execute('''
  CREATE TABLE IF NOT EXISTS
    pokedex (
      ID INT NOT NULL,
      NAME VARCHAR NOT NULL,
      IMAGE VARCHAR NOT NULL,
      TYPE VARCHAR NOT NULL,
      PRIMARY KEY(ID)
  );
''')

# # Create poke_data_list list starting empty
# poke_data_list = []

# # Iterate information about the first generation of pokemon
# for poke_index in range(1, 152):
#   # Connect to the API
#   poke_api = requests.get(f'https://pokeapi.co/api/v2/pokemon/{poke_index}')
#   # Parse API data with JSON
#   poke_information = json.loads(poke_api.text)
#   # Pokemon information
#   poke_id = poke_information['id']
#   poke_name = poke_information['name']
#   poke_image = poke_information['sprites']['front_default']
#   poke_type = poke_information['types'][0]['type']['name']
#   # Insert pokemon information in the database
#   cur.execute('''
#     INSERT INTO
#       pokedex
#     VALUES (?, ?, ?, ?)
#   ''', (poke_id, poke_name, poke_image, poke_type))
#   # Create a list of tuples with pokemon information
#   poke_information = (poke_id, poke_name, poke_image, poke_type)
#   poke_data_list.append(poke_information)

# # Return a single tuple from query result set
# cur.execute('SELECT * FROM pokedex WHERE id = 2;')
# data = cur.fetchone()
# print(data)

# # Select all information in pokedex table
# db_content = cur.execute('SELECT * FROM pokedex')

# # Export database data into CSV file
# with open(f'{path}/pokedex.csv', 'w', encoding='UTF-8', newline='') as f:
#   writer = csv.writer(f, delimiter=';')
#   writer.writerow(['ID', 'NAME', 'IMAGE', 'TYPE'])
#   for row in db_content:
#     writer.writerow(row)

# Application Configuration
window = tk.Tk()
window.configure(background='black')
window.geometry('600x500')
window.title('Pokedex')
window.config(padx=10, pady=10)

background_image = tk.PhotoImage(file = "./img/bg1.png")
background_label = tk.Label(window, image=background_image)
background_label.place(x=0, y=0, relwidth=1, relheight=1)

title_label = tk.Label(window, text="Pokedex", background='yellow')
title_label.config(font=("Merriweather", 32), fg='green')
title_label.pack(padx=10, pady=10)

pokemon_image = tk.Label(window)
pokemon_image.pack(padx=10, pady=10)

pokemon_information = tk.Label(window)
pokemon_information.config(font=("Merriweather", 16))
pokemon_information.pack(padx=10, pady=10)

pokemon_types = tk.Label(window)
pokemon_types.config(font=("Merriweather", 16))
pokemon_types.pack(padx=10, pady=10)

# Function to load pokemon
def load_pokemon():
  # Get the inputed information
  poke_search = text_id_name.get(1.0, "end-1c")

  # Return a single tuple from query result set
  cur.execute('SELECT * FROM pokedex WHERE id = ? OR name LIKE ?;', (poke_search, f'%{poke_search}%',))
  poke_data = list(cur.fetchone())
  poke_id = poke_data[0]
  poke_name = poke_data[1]
  poke_image = poke_data[2]
  poke_type = poke_data[3]

  print(f'{colors.OKGREEN}{colors.BOLD}Wild {poke_name.upper()} appeared!')

  # Image
  http = urllib3.PoolManager()
  img = http.request('GET', poke_image)
  image = Image.open(BytesIO(img.data))
  poke_img = ImageTk.PhotoImage(image)
  
  pokemon_image.config(image=poke_img)
  pokemon_image.image = poke_img

  pokemon_information.config(text=f'#{poke_id} {poke_name.capitalize()}')
  pokemon_types.config(text=f'{poke_type.capitalize()}')

label_id_name = tk.Label(text="Pokemon ID or Name")
label_id_name.config(font=("Merriweather", 16))
label_id_name.pack(padx=10, pady=10)

text_id_name = tk.Text(window, height=1)
text_id_name.config(font=("Merriweather", 16))
text_id_name.pack(padx=10, pady=10)

btn_load = tk.Button(window, text="SCAN", command=load_pokemon)
btn_load.config(font=("Merriweather", 16))
btn_load.pack(padx=10, pady=10)

window.mainloop()

# Save (commit) the changes
con.commit()

# Close the connection
con.close()
