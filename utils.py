from translate import Translator
from config import *

translator = Translator(MODEL_PATH)

def crawl_request_object(dictionary, source, target):
    for key in dictionary:
        value = dictionary[key]
        
        if isinstance(value, dict):
            crawl_request_object(value, source, target)
        else:
            dictionary[key] = translator.translate(source, target, value)[0]