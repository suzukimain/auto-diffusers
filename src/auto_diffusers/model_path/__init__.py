from ..setup.Base_config import Basic_config
from search_hugface import Huggingface
from search_civitai import Civitai
from flax_config import with_Flax
from Perform_path_search import search_path



class Config_Mix(
    Huggingface,
    Civitai,
    with_Flax,
    Basic_config
    ):
    #fix MMO error
    def __init__(self):
        super().__init__()