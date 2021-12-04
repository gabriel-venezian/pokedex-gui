import sys
sys.path.insert(0, 'pokedex')
import tkinter as tk
import urllib3 
from io import BytesIO
from PIL import Image, ImageTk
from Database import Database


window = tk.Tk()
window.geometry('825x1068')
window.title('Pokédex')
window.configure(background = '#f6e652')

class GraphicalInterface():
  """
  Class responsible for the definition of Graphical
  User Interface properties.
  """
  def __init__(self, window):
    """
    GraphicalInterface class constructor.

    Contains the properties used for generate the graphical
    user interface.
    """
    self.title_label = tk.Label(window, text='Pokédex', background='#f6e652')
    self.title_label.config(font=('"Orange Kid" 64 bold'), fg='#41414a')
    self.title_label.pack(padx=10, pady=10)

    self.pokemon_image = tk.Label(window, background='#f6e652')
    self.pokemon_image.pack(padx=10, pady=10)

    self.pokemon_information = tk.Label(window, background='#f6e652')
    self.pokemon_information.config(font=('"Orange Kid" 40 bold'), fg='#41414a')
    self.pokemon_information.pack(padx=10, pady=10)

    self.pokemon_types = tk.Label(window, background='#f6e652')
    self.pokemon_types.config(font=('"Orange Kid" 40 bold'), fg='#41414a')
    self.pokemon_types.pack(padx=10, pady=10)

    self.label_id_name = tk.Label(text='Pokemon ID or Name', background='#f6e652')
    self.label_id_name.config(font=('"Orange Kid" 32 bold'), fg='#41414a')
    self.label_id_name.pack(padx=10, pady=10)

    self.text_id_name = tk.Text(window, height=1)
    self.text_id_name.config(font=('"Orange Kid" 32 bold'), fg='#41414a')
    self.text_id_name.pack(padx=10, pady=10)

    self.btn_load = tk.Button(window, text='SCAN', command=self.load_pokemon)
    self.btn_load.config(font=('"Orange Kid" 32 bold'), fg='#41414a')
    self.btn_load.pack(padx=10, pady=10)     

  # Function to load pokemon
  def load_pokemon(self):
    """
    Method for load the pokémon information in the
    graphical user interface.

    Gets the text inputed from user and executes a query
    in the database, returning a single row of information.
    """
    # Instantiate Database class
    database = Database()

    # Get the inputed information
    poke_search = self.text_id_name.get(1.0, 'end-1c')

    # Return a single tuple from query result set
    try:
      with database.connection:
        database.cursor.execute('SELECT * FROM pokedex WHERE id = ? OR name LIKE ?;', (poke_search, f'%{poke_search}%',))
        poke_data = list(database.cursor.fetchone())
        poke_id = poke_data[0]
        poke_name = poke_data[1]
        poke_image = poke_data[2]
        poke_type = poke_data[3]
      
        # Render image
        http = urllib3.PoolManager()
        img = http.request('GET', poke_image)
        image = Image.open(BytesIO(img.data))
        poke_img = ImageTk.PhotoImage(image)
        
        self.pokemon_image.config(image=poke_img, background='#f6e652')
        self.pokemon_image.image = poke_img

        self.pokemon_information.config(text=f'#{poke_id} {poke_name.capitalize()}')
        self.pokemon_types.config(text=f'{poke_type.capitalize()}')
    except TypeError:
      pass

  def start_gui():
    """
    Method for start the graphical user interface.
    """
    GraphicalInterface(window)
    window.mainloop()  
