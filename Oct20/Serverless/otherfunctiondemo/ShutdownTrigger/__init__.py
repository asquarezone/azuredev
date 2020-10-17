import datetime
import logging
import json

import azure.functions as func
from azure.identity import ClientSecretCredential
from azure.mgmt.compute import ComputeManagementClient


def main(mytimer: func.TimerRequest) -> None:
    utc_timestamp = datetime.datetime.utcnow().replace(
        tzinfo=datetime.timezone.utc).isoformat()
    dict_json = json.loads('credential.json')
    subscription_id = dict_json['subscriptionid']
    credentials = ClientSecretCredential(
        tenant_id = dict_json['tenantid'],
        client_id = dict_json['clientid'],
        client_secret = dict_json['clientsecret']
    )
    compute_client = ComputeManagementClient(subscription_id, credentials)
    all_vms = compute_client.virtual_machines.list_all
    for vm in all_vms:
        # vm.deallocate()
        pass



    if mytimer.past_due:
        logging.info('The timer is past due!')

    logging.info('Python timer trigger function ran at %s', utc_timestamp)
