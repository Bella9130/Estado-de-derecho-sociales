import os
import openai
from dotenv import load_dotenv
from flask import Flask, render_template, request
import json


#Cargar llaves del archivo .env
load_dotenv()
openai.api_key = os.getenv('bfde36be003d4e95503911c4823c30ae')
elevenlabs_key = os.getenv('bfde36be003d4e95503911c4823c30ae')

app = Flask(__name__)