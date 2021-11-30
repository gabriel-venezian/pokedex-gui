import sqlite3
from pathlib import Path
from GetApiContent import GetApiContent


ROOT_PATH = Path(__file__).parent.parent
POKE_API_URL = 'https://pokeapi.co/api/v2/pokemon'

class Database:
  def __init__(self):
    # Connect to sqlite database
    self.connection = sqlite3.connect(f'{ROOT_PATH}/../pokedex.db')
    # Create the cursor object
    self.cursor = self.connection.cursor()
    
  def create_database(self):
    with self.connection:
      self.cursor.execute('''
        CREATE TABLE IF NOT EXISTS
          pokedex (
            ID INT NOT NULL,
            NAME VARCHAR NOT NULL,
            IMAGE VARCHAR NOT NULL,
            TYPE VARCHAR NOT NULL,
            PRIMARY KEY(ID)
          );
      ''')
    return print('Database created.')
    
  def store_in_database(self):
    pokemon_data_list = GetApiContent.pokemon_data_list(POKE_API_URL)
    for pokemon in pokemon_data_list:
      poke_id = pokemon[0]
      poke_name = pokemon[1]
      poke_image = pokemon[2]
      poke_type = pokemon[3]
      with self.connection:
        self.cursor.execute('''
          INSERT INTO
            pokedex
          VALUES (?, ?, ?, ?)
        ''', (poke_id, poke_name, poke_image, poke_type))
    return print('Pokemon information loaded.')

test = Database()
test.create_database()
test.store_in_database()
  