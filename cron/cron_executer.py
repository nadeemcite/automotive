from collections import OrderedDict

import os
from automation.array_join import ArrayJoin
from automation.call_api import CallApi
from automation.read_html import ReadHtml
import json
from dotenv import load_dotenv
from utils.gsheet import read_gsheet, update_cell

load_dotenv()

GSHEET_URL = os.getenv("GSHEET_URL")

STEP_CONFIG = {
    "Read HTML": ReadHtml,
    "Call API": CallApi,
    "Array Join": ArrayJoin
}

def cron_execute(row):
    variable_sheet_gid = row[0]
    row_index = len(read_gsheet(GSHEET_URL, sheet_id=variable_sheet_gid)) + 1
    input_variables = {el: "" for el in json.loads(row[1])}
    step_config = OrderedDict((row[i], row[i + 1]) for i in range(2, len(row[1:]), 2))
    for step, config in step_config.items():
        step_executor = STEP_CONFIG[step](config, input_variables)
        step_executor.exec()
        input_variables = step_executor.input_variables
    for i, (key, val) in enumerate(input_variables.items()):
        update_cell(GSHEET_URL, variable_sheet_gid, row_index, i+1, val)
    return "success"