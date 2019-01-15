import gspread
from oauth2client.service_account import ServiceAccountCredentials

# use creds to create a client to interact with the Google Drive API
scope = ['https://spreadsheets.google.com/feeds','https://www.googleapis.com/auth/drive']
creds = ServiceAccountCredentials.from_json_keyfile_name('client_secret.json', scope)
client = gspread.authorize(creds)

# Find a workbook by name and open the first sheet
worksheet = client.open("VEEP 2017-2018 Application (Responses)").sheet1

# Extract all of the values
Name = worksheet.col_values(2)
Email = worksheet.col_values(5)
Discipline = worksheet.col_values(3)
Year = worksheet.col_values(4)
Phone = worksheet.col_values(6)
Projects = worksheet.col_values(9)
Interview_Offer = worksheet.col_values(18)
