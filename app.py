import os
from utils import *
from flask import Flask, request, jsonify
from translate import Translator
from config import *

app = Flask(__name__)
translator = Translator(MODEL_PATH)

app.config["DEBUG"] = True

@app.route('/', methods=["GET"])
def health_check():
    """Confirms service is running"""
    return "Machine translation service is up and running."

@app.route('/lang_routes', methods = ["GET"])
def get_lang_route():
    lang = request.args['lang']
    all_langs = translator.get_supported_langs()
    lang_routes = [l for l in all_langs if l[0] == lang]
    return jsonify({"output":lang_routes})

@app.route('/supported_languages', methods=["GET"])
def get_supported_languages():
    langs = translator.get_supported_langs()
    return jsonify({"output":langs})

@app.route('/translate', methods=["POST"])
def get_prediction():
    source = request.json['source']
    target = request.json['target']
    text = request.json['text']
    translation = translator.translate(source, target, text)
    return jsonify({"output":translation})

@app.route('/translate-json', methods=["POST"])
def get_prediction_for_full_json():
    source = request.args.get('source')
    target = request.args.get('target')

    crawl_request_object(request.json, source, target)

    return jsonify(request.json)



app.run(host="localhost", port="3000")