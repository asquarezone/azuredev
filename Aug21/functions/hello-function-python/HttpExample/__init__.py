import logging

import azure.functions as func
import random


def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    
    length = req.params.get('length')
    if 'length' in req.params:
        length = int(req.params.get('length'))

    
    if not length:
        try:
            req_body = req.get_json()
        except ValueError:
            pass
        else:
            length = req_body.get('length')
    if not length:
        length = '12'

    length = int(length)
    password = ''
    characters = list('abcdefghijklmnopqrstuvwxyz')
    characters.extend(list('0123456789'))
    characters.extend(list('$#@!*&'))
    characters.extend(list('ABCDEFGHIJKLMNOPQRSTUVWXYZ'))
    for index in range(length):
        password += random.choice(characters)

    
    return func.HttpResponse(f"The genererate password is  {password} ")
    
