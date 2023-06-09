# GptTextRpg
An experiment with to create a structured text-based RPG with dynamic elements provided by a local GPT.

## Running
To Run the program, you can do this one of two ways.

### Local Bare Metal
1. Ensure you have the following dependencies
    * Python 3.10 or above
    * A given LLM model
2. Download and place an LLM bin file in the model folder
3. Create a virtual environment
    * python -m venv <name_of_virtual_environment>
4. Enter virtual environment
    * (On Linux/MacOS) source <name_of_virtual_environment>/bin/activate
3. Install the python dependencies from the requirements.txt file
    * pip install -r requirements.txt
4. Run the the python program
    * python3 main.py
### Docker
1. Ensure you have the following dependencies
    * Docker 20.10 or above
2. Change the Docker daemon settings to have higher memory limit (8 GB should be sufficient)
3. Build the image
    * docker image build -t gpttextrpg .
4. Run the built container
    * docker container run --memory=14g gpttextrpg 

