import logging
import uuid

import azure.functions as func


def main(req: func.HttpRequest, queueEmployee: func.Out[str]) -> func.HttpResponse:
    """
    This method will collect the employee information from the http request
    structure
    {
        'name': '<name>',
        'address': '<address>',
        'personal_email': '<email>',
        'reporting_to': '<manager>' 
    }
    """
    logging.info('Python HTTP trigger function processed a request.')

    req_body = req.get_json()
    name = req_body.get('name')
    address = req_body.get('address')
    personal_email = req_body.get('personal_email')
    reporting_to = req_body.get('reporting_to')
    queueEmployee.set(req_body)

    #name = req.params.get('name')
    #if not name:
    #    try:
    #        req_body = req.get_json()
    #    except ValueError:
    #        pass
    #    else:
    #        name = req_body.get('name')

    if name:
        return func.HttpResponse('Processed succesfully')
    else:
        return func.HttpResponse(
             "This HTTP triggered function executed successfully. Pass a name in the query string or in the request body for a personalized response.",
             status_code=200
        )
