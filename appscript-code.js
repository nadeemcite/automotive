SHEET_URL = ""
VERCEL_LINK = ""

function runScript() {
    const worksheet = SpreadsheetApp
        .openByUrl(SHEET_URL);

    const sheet = worksheet.getSheetByName('MASTER');
    const rows = sheet.getDataRange().getValues();
    for (let i = 1; i < rows.length; i++) {
        const variableSheetId = rows[i][1].toLocaleString('fullwide', { useGrouping: false });
        const reqArray = [variableSheetId, ...rows[i].slice(2)]
        const url = VERCEL_LINK;
        Logger.info(reqArray)
        const options = {
            "method": "post",
            "headers": {
                "Content-Type": "application/x-www-form-urlencoded"
            },
            "payload": {
                "data": JSON.stringify(reqArray)
            },
            'muteHttpExceptions': true
        };
        const response = UrlFetchApp.fetch(url, options);
        Logger.info(response)
    }
}