import pandas as pd 
import json


SPREADSHEET_QUERY = "https://docs.google.com/spreadsheets/d/12ieimF4voBMBUZ-7y_KP6BHR_O-87cKeAGA0fiLW4m0/gviz/tq?tq=select%20*"
SPREADSHEET_ID = "12ieimF4voBMBUZ-7y_KP6BHR_O-87cKeAGA0fiLW4m0"


def pull_data(spreadsheet_query):
