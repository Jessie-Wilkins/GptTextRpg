from GptTextRpg.GameWorld.game_map import Room
from langchain import PromptTemplate, LLMChain
from langchain.llms import LlamaCpp
from langchain.callbacks.streaming_stdout import StreamingStdOutCallbackHandler
from tqdm import tqdm
import sys
import os
import requests

class GameNarrator:
    def __init__(self):

        template = """You will get the name of a room, a list of items, and a list of entities; 
        using these values, name and describe the room for me in a few sentences that has those items and entities: 

        For example, if you have a sword and a shield as items, a cyclops as an entity, and an armory as a room, you might describe a room like this: 
        
        In the darkly lit armory, you see a rusty sword hanging on the wall. 
        On the ground, you see a small golden shield that reflects what little light is in the room.
        An angry cyclops stands in the corner eyeing you with hate in its eyes.

        Room Name: 
        {room_name}

        List of items: 
        {list_of_items}

        List of entities:
        {list_of_entities}

        Description: 
        """

        prompt = PromptTemplate(template=template, input_variables=["list_of_items", "room_name", "list_of_entities"])

        url = "https://huggingface.co/TheBloke/orca_mini_3B-GGML/resolve/main/orca-mini-3b.ggmlv3.q4_1.bin"

        local_path = 'model/orca-mini-3b.ggmlv3.q4_1.bin'  # replace with your desired local file path

        if not os.path.exists(local_path):
            response = requests.get(url, stream=True)
            total_size = int(response.headers.get('content-length', 0))
            block_size = 1024
            if response.status_code == 200:
                with open(local_path, 'wb') as file, tqdm(
                total=total_size, unit='B', unit_scale=True, unit_divisor=1024
            ) as progress_bar:
                    for data in response.iter_content(block_size):
                        file.write(data)
                        progress_bar.update(len(data))
                print("Saved model to {}".format(local_path))
            else:
                print("Error downloading model")
                sys.exit(1)

        # Callbacks support token-wise streaming
        callbacks = [StreamingStdOutCallbackHandler()]
        # If you want to use a custom model add the backend parameter
        # Check https://docs.gpt4all.io/gpt4all_python.html for supported backends
        llm = LlamaCpp(max_tokens=1024, n_ctx=2048, model_path=local_path, callbacks=callbacks, verbose=True)

        self.llm_chain = LLMChain(prompt=prompt, llm=llm)

    def describe_room(self, room: Room):
        return self.llm_chain.run(room_name=room.getName(), list_of_items=room.getItems(), list_of_entities=room.getEntityStrings())