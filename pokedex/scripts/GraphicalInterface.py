from PIL import Image, ImageTk
import tkinter as tk
import urllib3 
from io import BytesIO
import sys
sys.path.insert(0, 'pokedex')
from Database import Database

window = tk.Tk()
window.geometry('950x950')
window.title('Pokédex')

class GraphicalInterface():
  def __init__(self, window):
    self.title_label = tk.Label(window, text="Pokedex", background='yellow')
    self.title_label.config(font=("Merriweather", 32), fg='green')
    self.title_label.pack(padx=10, pady=10)

    self.pokemon_image = tk.Label(window)
    self.pokemon_image.pack(padx=10, pady=10)

    self.pokemon_information = tk.Label(window)
    self.pokemon_information.config(font=("Merriweather", 24))
    self.pokemon_information.pack(padx=10, pady=10)

    self.pokemon_types = tk.Label(window)
    self.pokemon_types.config(font=("Merriweather", 24))
    self.pokemon_types.pack(padx=10, pady=10)

    self.label_id_name = tk.Label(text="Pokemon ID or Name")
    self.label_id_name.config(font=("Merriweather", 24))
    self.label_id_name.pack(padx=10, pady=10)

    self.text_id_name = tk.Text(window, height=1)
    self.text_id_name.config(font=("Merriweather", 24))
    self.text_id_name.pack(padx=10, pady=10)

    self.btn_load = tk.Button(window, text="SCAN", command=self.load_pokemon)
    self.btn_load.config(font=("Merriweather", 24))
    self.btn_load.pack(padx=10, pady=10)     

  # Function to load pokemon
  def load_pokemon(self):
    database = Database()
    # Get the inputed information
    poke_search = self.text_id_name.get(1.0, "end-1c")

    # Return a single tuple from query result set
    with database.connection:
      database.cursor.execute('SELECT * FROM pokedex WHERE id = ? OR name LIKE ?;', (poke_search, f'%{poke_search}%',))
      poke_data = list(database.cursor.fetchone())
      poke_id = poke_data[0]
      poke_name = poke_data[1]
      poke_image = poke_data[2]
      poke_type = poke_data[3]

    # Image
    http = urllib3.PoolManager()
    img = http.request('GET', poke_image)
    image = Image.open(BytesIO(img.data))
    poke_img = ImageTk.PhotoImage(image)
    
    self.pokemon_image.config(image=poke_img)
    self.pokemon_image.image = poke_img

    self.pokemon_information.config(text=f'#{poke_id} {poke_name.capitalize()}')
    self.pokemon_types.config(text=f'{poke_type.capitalize()}')

GraphicalInterface(window)
window.mainloop()   
