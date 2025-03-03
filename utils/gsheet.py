import logging
import os
import tempfile

import gspread
from dotenv import load_dotenv
from oauth2client.service_account import ServiceAccountCredentials

load_dotenv()

CREDENTIALS_JSON = os.getenv("CREDENTIALS_JSON")


def get_gsheet_client():
    fp = tempfile.NamedTemporaryFile(delete=False)
    fp.write(CREDENTIALS_JSON.encode("utf-8"))
    fp.close()
    scope = [
        "https://spreadsheets.google.com/feeds",
        "https://www.googleapis.com/auth/drive",
    ]
    creds = ServiceAccountCredentials.from_json_keyfile_name(fp.name, scope)
    os.unlink(fp.name)
    return gspread.authorize(creds)


def get_sheet_by_id(sheet_url, sheet_id):
    client = get_gsheet_client()
    worksheets = client.open_by_url(sheet_url).worksheets()
    sheet = next(
        (sheet for sheet in worksheets if str(sheet.id) == str(sheet_id)), None
    )
    return sheet


def read_gsheet(sheet_url, skip_rows=0, sheet_id=None):
    sheet = get_sheet_by_id(sheet_url, sheet_id)
    return sheet.get_all_values()[skip_rows:]


def update_cell(sheet_url, sheet_id, row, col, value):
    sheet = get_sheet_by_id(sheet_url, sheet_id)
    if sheet:
        try:
            sheet.update_cell(row, col, value)
        except Exception as e:
            logging.info("Cell update failed", extra={"error": str(e)})


def append_row(sheet_url, sheet_id, values):
    sheet = get_sheet_by_id(sheet_url, sheet_id)
    if sheet:
        try:
            sheet.append_row(values)
            logging.info(f"APPENDING ROW {values}")
        except Exception as e:
            logging.info("Row append failed", extra={"error": str(e)})
