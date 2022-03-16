from pokedex import Constants
from pokedex import CsvExport
from pokedex import Database
from pokedex import GetApiContent
from pokedex import GraphicalInterface

if __name__ == "__main__":
    # Instantiate Database class
    database = Database()
    # Create database
    print(database.create())
    # Store pokémon information in the database
    print(database.insert_pokemon())
    # Create CSV from API
    CsvExport.csv_export(
        "poke_data_api.csv", GetApiContent.poke_data_list(Constants.POKE_API_URL)
    )
    # Create CSV from database
    CsvExport.csv_export(
        "poke_data_database.csv", database.content("SELECT * FROM pokedex")
    )
    # Start GUI
    GraphicalInterface().mainloop()
