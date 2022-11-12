import json
import requests
from utils import *
import contextlib
import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))
import time
from tradovate_api import swagger_client
from tradovate_api.swagger_client import configuration
from tradovate_api.swagger_client.rest import ApiException
from pprint import pprint
import broker
from brokers.broker import BrokerSuper
from brokers.broker import BrokerMeta
import datetime
class tradovate_broker(BrokerSuper):
    #def get_position(self):
    #    print("child ib_broker position")
    #    super().get_position()
    def __init__(self):
        # Get a new access taken if we don't have a valid access token
        if ('accessToken' not in os.environ) or ('expirationTime' not in os.environ) or (datetime.datetime.strptime(os.environ['expirationTime'], "%Y-%m-%dT%H:%M:%S.%fZ") <= datetime.datetime.now()):
            
            base_url = 'https://live.tradovateapi.com/v1'

            url = base_url + '/auth/accessTokenRequest'
            data = '''{
            "name": "<account_username>",
            "password": "<account_password>",
            "appId": "<API appId>",
            "appVersion": "0.0.1",
            "deviceId": "<device_id - From API settings screen in your dashboard, click on curl button>",
            "cid": "<API cid>",
            "sec": "<API secret key>"
            }'''

            response = requests.post(url, data=data)

            # For successful API call, response code will be 200 (OK)
            if(response.ok):

                # Loading the response data into a dict variable
                # json.loads takes in only binary or string variables so using content to fetch binary content
                # Loads (Load String) takes a Json file and converts into python data structure (dict or list, depending on JSON)
                jData = json.loads(response.content)

                print("The response contains {0} properties".format(len(jData)))
                print("\n")
                for key in jData:
                    os.environ[key] = str(jData[key])
                    print(key, str(jData[key]))
            else:
            # If response code is not ok (200), print the resulting http error code with description
                response.raise_for_status()

        # create an instance of the API class
        api_instance = swagger_client.AccountingApi(swagger_client.ApiClient())

        try:
            api_response = api_instance.account_list()
            pprint(api_response)
        except ApiException as e:
            print("Exception when calling AccountingApi->account_list: %s\n" % e)


    
    def create_client(self, symbol):
        pass
    
    def place_market_order(self, order_exec_symbol, order_exec_conid, action_side, total_quantity, cont_exchange='GLOBEX', ib_client=None):
        pass
    
    def place_limit_order(self, order_exec_symbol, order_exec_conid, action_side, total_quantity, limit_price, cont_exchange='GLOBEX', ib_client=None):
        pass
    
    def place_stop_order(self, order_exec_symbol, order_exec_conid, action_side, total_quantity, stop_price, cont_exchange='GLOBEX', ib_client=None):
        pass
    
    def get_qualified_contract(self, order_exec_symbol, order_exec_conid, cont_exchange='GLOBEX', ib_client=None):
        pass
    
    def cancel_current_orders(self, order_exec_symbol, ib_client=None):
        pass
    
    def get_position(self, order_exec_symbol, order_exec_conid, cont_exchange='GLOBEX'):
        pass


tvb = tradovate_broker()
