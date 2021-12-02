from pathlib import Path


class Constants:
  def ROOT_PATH():
    return Path(__file__).parent.parent
  
  def POKE_API_URL():
    return 'https://pokeapi.co/api/v2/pokemon'
