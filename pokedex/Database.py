import sqlite3

from .Constants import Constants
from .GetApiContent import GetApiContent


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
        self.connection = sqlite3.connect(f"{Constants.ROOT_PATH}/pokedex.db")
        # Create the cursor object
        self.cursor = self.connection.cursor()

    def create(self):
        """
        Method for create the database and also the application main
        table.
        """
        with self.connection:
            self.cursor.execute(
                """
        CREATE TABLE IF NOT EXISTS
          pokedex (
            ID INT NOT NULL,
            NAME VARCHAR NOT NULL,
            IMAGE VARCHAR NOT NULL,
            TYPE VARCHAR NOT NULL,
            PRIMARY KEY(ID)
          );
      """
            )
        return "Database created."

    def content(self, query):
        """
        Method for select content from the database.

        Args:
        query (string): expects a query string to be executed.
        """
        with self.connection:
            db_content = self.cursor.execute(query)
        return list(db_content)

    def insert_pokemon(self):
        """
        Method for insert information in the database.

        Verifies if the table is empty before it's insertion.
        """
        if len(self.content("SELECT * FROM pokedex")) == 0:
            pokemons = GetApiContent.poke_data_list(Constants.POKE_API_URL)
            payload = [
                (pokemon.id, pokemon.name, pokemon.image, pokemon.type)
                for pokemon in pokemons
            ]
            with self.connection:
                self.cursor.executemany(
                    """
          INSERT INTO
            pokedex
          VALUES (?, ?, ?, ?)
        """,
                    payload,
                )
        return "Pokémon information loaded."

    def pokemon_data(self, poke_search):
        self.cursor.execute(
            "SELECT * FROM pokedex WHERE id = ? OR name LIKE ?;",
            (
                poke_search,
                f"%{poke_search}%",
            ),
        )
        return self.cursor.fetchone()
