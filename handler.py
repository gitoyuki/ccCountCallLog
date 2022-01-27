import json
from analytics_cc_count import ccCount, toAlpha


def hello(event, context):
    body = {
        "message": "Go Serverless v1.0! Your function executed successfully!",
        "input": event
    }

    ccCount()

    response = {
        "statusCode": 200,
        "body": json.dumps(body)
    }

    return response

    # Use this code if you don't use the http event with the LAMBDA-PROXY
    # integration
    """
    return {
        "message": "Go Serverless v1.0! Your function executed successfully!",
        "event": event
    }
    """

#
# def test():
#     import pandas as pd
#     import numpy as np
#     import gspread as gs
#     from oauth2client.service_account import ServiceAccountCredentials
#     # from gspread_dataframe import get_as_dataframe, set_with_dataframe
#
#     print(pd)
#     print(np)
#     print(gs)
#     print(ServiceAccountCredentials)
#     # print(get_as_dataframe)