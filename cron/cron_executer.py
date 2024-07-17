from collections import OrderedDict

import os
from automation.array_join import ArrayJoin
from automation.call_api import CallApi
from automation.conditional_break import ConditionalBreak
from automation.eval import Eval
from automation.read_html import ReadHtml
from dotenv import load_dotenv
from utils.gsheet import read_gsheet, update_cell

load_dotenv()

GSHEET_URL = os.getenv("GSHEET_URL")

STEP_CONFIG = {
    "Read HTML": ReadHtml,
    "Call API": CallApi,
    "Array Join": ArrayJoin,
    "Conditional Break": ConditionalBreak,
    "Eval": Eval,
}

def cron_execute(row):
    variable_sheet_gid = row[0]
    sheet_data = read_gsheet(GSHEET_URL, sheet_id=variable_sheet_gid)
    variables = sheet_data[0]
    row_index = len(sheet_data) + 1
    input_variables = {el: "" for el in variables}
    step_config = OrderedDict((row[i], row[i + 1]) for i in range(1, len(row[1:]), 2))
    for step, config in step_config.items():
        step_executor = STEP_CONFIG[step](config, input_variables)
        execution_response = step_executor.exec()
        input_variables = step_executor.input_variables
        if step == "Conditional Break" and execution_response:
            break
    for i, (key, val) in enumerate(input_variables.items()):
        update_cell(GSHEET_URL, variable_sheet_gid, row_index, i+1, val)
    return "success"