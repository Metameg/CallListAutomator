import gspread
from oauth2client.service_account import ServiceAccountCredentials

def connect_to_sheet():
    # Define the scope
    scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]

    # Add your credentials to the account
    creds = ServiceAccountCredentials.from_json_keyfile_name('./credentials.json', scope)

    # Authorize the clientsheet
    client = gspread.authorize(creds)

    # Get the instance of the Spreadsheet
    sheet = client.open('TDD_CallList')

    # Get the first sheet of the Spreadsheet
    worksheet = sheet.get_worksheet(0)

    return worksheet
    

    # Alternatively, you can update a range of cells
#     data = [
#         ["Name", "Age"],
#         ["Alice", 30],
#         ["Bob", 25]
#     ]
#     worksheet.update('C1:D3', data)

# connect_to_sheet()
