import sqlite3
from Constants import Constants
from GetApiContent import GetApiContent


class Database:
  """
  Class responsible for define the database methods.
  """
  def __init__(self):
    """
    Database class constructor.

    Contains the connection and cursor objects from sqlite3.
    """
    # Connect to sqlite database
    self.connection = sqlite3.connect(f'{Constants.ROOT_PATH()}/../pokedex.db')
    # Create the cursor object
    self.cursor = self.connection.cursor()
    
  def create_database(self):
    """
    Method for create the database and also the application main
    table.
    """
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
      
  def database_content(self, query):
    """
    Method for select information from the database.

    Args:
    query (string): expects a query string to be executed.
    """
    database_content = []
    with self.connection:
      db_content = self.cursor.execute(query)
    for row in db_content:
      database_content.append(row)
    return database_content

  def store_in_database(self):
    """
    Method for insert information in the database.

    Verifies if the table is empty before it's insertion.
    """
    if (self.database_content('SELECT * FROM pokedex')) == []:
      poke_data_list = GetApiContent.poke_data_list(Constants.POKE_API_URL())
      for pokemon in poke_data_list:
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
    return print('Pokémon information loaded.')
