# Google Sheets Workflow Automation

A Python-based automation tool for reading and processing data from Google Sheets to perform sequential operations in a workflow.

## Overview

This project automates workflow processes by:
- Reading data from Google Sheets
- Processing the data sequentially
- Executing operations based on the workflow defined in the spreadsheet

## Prerequisites

- Python 3.7 or higher
- A Google Cloud Platform account
- Google Sheets API enabled
- Required credentials (service account key)

## Installation

1. **Clone the repository:**

   ```bash
   git clone <repository-url>
   cd <project-directory>
   ```

2. **Install required dependencies:**

   ```bash
   pip install -r requirements.txt
   ```

3. **Set up Google Sheets API:**

   - Go to the [Google Cloud Console](https://console.cloud.google.com/).
   - Create a new project or select an existing one.
   - Enable the Google Sheets API.
   - Create service account credentials.
   - Download the JSON key file.
   - Rename the file to `credentials.json` and place it in the project root.

## Configuration

1. Share your Google Sheet with the service account's email address.
2. Update the `SPREADSHEET_ID` in your configuration. This can be found in the URL of your Google Sheet.

## Usage

Run the main script with the following command:

```bash
python main.py
```
