import sys
sys.path.insert(0, 'pokedex/')
from pokedex import Constants
from pokedex import CsvExport
from pokedex import Database
from pokedex import GetApiContent
from pokedex import GraphicalInterface


# # Instantiate Database class
# database = Database()
# # Create database
# database.create_database()
# # Store pokémon information in the database 
# database.store_in_database()

# # Create CSV from API 
# CsvExport.csv_export('poke_data_api.csv', GetApiContent.poke_data_list(Constants.POKE_API_URL()))
# # Create CSV from database
# CsvExport.csv_export('poke_data_database.csv', database.database_content('SELECT * FROM pokedex'))

# Start GUI
if __name__ == "__main__":
  GraphicalInterface().mainloop()
