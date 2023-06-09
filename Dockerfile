FROM python:3.12.0b1-slim-bullseye
COPY . /home/gpttextrpg
WORKDIR /home/gpttextrpg
RUN apt-get update && \
apt-get install python3-dev build-essential libssl-dev libffi-dev virtualenv -y && \
virtualenv gpttextrpg && \
. gpttextrpg/bin/activate && \
pip install --upgrade pip && \
pip install --upgrade setuptools && \
pip install -r requirements.txt

CMD ["/bin/bash", "-c", "source gpttextrpg/bin/activate && python main.py"]
