import tkinter as tk
import urllib3 
from io import BytesIO
from PIL import Image, ImageTk
from .Database import Database

class GraphicalInterface(tk.Tk):
  """
  Class responsible for the definition of Graphical
  User Interface properties.
  """
  def __init__(self):
    """
    GraphicalInterface class constructor.

    Contains the properties used for generate the graphical
    user interface.
    """
    super().__init__()
    
    # Root Window
    self.title('Pokédex GUI')
    self.geometry(f'{self.winfo_screenwidth() // 2}x{self.winfo_screenheight()}')
        
    # Application title
    self.title = tk.Label(self, text='POKÉDEX')
    self.title.config(font=('Kanit 48 bold'))
    self.title.place(relx=0.5, rely=0.07, anchor='center')

    # Pokémon image
    self.pokemon_image = tk.Label(self)
    self.pokemon_image.place(relx=0.5, rely=0.35, anchor='center')

    # Pokémon name
    self.pokemon_information = tk.Label(self)
    self.pokemon_information.config(font=('Roboto 36 bold'))
    self.pokemon_information.place(relx=0.5, rely=0.62, anchor='center')

    # Pokémon type
    self.pokemon_types = tk.Label(self)
    self.pokemon_types.config(font=('Roboto 36 bold'))
    self.pokemon_types.place(relx=0.5, rely=0.69, anchor='center')

    # Search pokémon bar 
    self.search_pokemon = tk.Text(self, height=1, width=35, bg='#FFFFFF', fg='#111111', padx=10, pady=10)
    self.search_pokemon.config(font=('Roboto" 24'), fg='#111111')
    self.search_pokemon.insert(1.0, 'Pokédex number or pokémon name...')
    self.search_pokemon.place(relx=0.5, rely=0.8, anchor='center')

    # Search information button
    self.search_info = tk.Button(self, text='SEARCH', command=self.load_pokemon)
    self.search_info.config(font=('Kanit 24'), fg='#111111')
    self.search_info.place(relx=0.5, rely=0.9, anchor='center')
  
  # Load pokémon function
  def load_pokemon(self):
    poke_search = self.search_pokemon.get(1.0, 'end-1c')
    poke_data = Database().pokemon_data(poke_search)

    if poke_data: 
      self.render_info(
        poke_id = poke_data[0], 
        poke_name = poke_data[1], 
        poke_image = poke_data[2], 
        poke_type = poke_data[3]
      )
    else:
      self.render_info(
        poke_id = '404',
        poke_name = 'Unown',
        poke_image = 'https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/official-artwork/201.png',
        poke_type = "Not found"
      )
      
  def clear_input(self):
    self.search_pokemon.delete(1.0, 'end')

  def render_info(self, poke_id, poke_name, poke_image, poke_type):
    http = urllib3.PoolManager()
    img = http.request('GET', poke_image)
    image = Image.open(BytesIO(img.data))
    resize_img = image.resize((350, 350))
    poke_img = ImageTk.PhotoImage(resize_img)
      
    self.pokemon_image.config(image=poke_img)
    self.pokemon_image.image = poke_img
    self.pokemon_information.config(text=f'#{poke_id} {poke_name.capitalize()}')
    self.pokemon_types.config(text=f'{poke_type.capitalize()}')    

    self.clear_input()
