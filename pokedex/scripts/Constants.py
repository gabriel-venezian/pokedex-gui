from pathlib import Path


class Constants:
  """
  Class responsible for definition of 
  constant methods used in the project.
  """
  def ROOT_PATH():
    """
    Method for define project's root path using pathlib.
    """
    return Path(__file__).parent.parent
  
  def POKE_API_URL():
    """
    Method for define Pokémon API URL.
    """
    return 'https://pokeapi.co/api/v2/pokemon'
