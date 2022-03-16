import requests
from pydantic import BaseModel


class Pokemon(BaseModel):
    id: int
    name: str
    image: str
    type: str


class GetApiContent:
    """
    Class responsible for get pokémon information from PokeAPI.
    """

    def poke_data_list(POKE_API_URL: str):
        """
        Method to get information about the first pokémon generation.

        Args:
          POKE_API_URL (str): API's url.

        Returns:
          List: pokémon data (id, name, image and primitive type).
        """
        # Create poke_data_list starting empty
        poke_data_list = []
        # Iterate information about the first pokémon generation
        for poke_index in range(1, 152):
            # pokémon information
            poke_information = requests.get(f"{POKE_API_URL}/{poke_index}").json()
            id = poke_index
            name = poke_information["name"]
            image = poke_information["sprites"]["other"]["official-artwork"][
                "front_default"
            ]
            type = poke_information["types"][0]["type"]["name"]
            # Create a list of tuples with pokémon information
            poke_information = Pokemon(id=id, name=name, image=image, type=type)
            poke_data_list.append(poke_information)
        return poke_data_list
