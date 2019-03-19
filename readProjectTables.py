import gspread
import re
from oauth2client.service_account import ServiceAccountCredentials

# use creds to create a client to interact with the Google Drive API
scope = ['https://spreadsheets.google.com/feeds','https://www.googleapis.com/auth/drive']
creds = ServiceAccountCredentials.from_json_keyfile_name('credentials.json', scope)
client = gspread.authorize(creds)

# Read 2018 projects
worksheet = client.open("2018").sheet1

Top_Row = worksheet.row_values(1)
Num_Col = len(Top_Row)
People = []

for i in range(1, Num_Col):
    #starting indexing People at 1, first index
 #is team name, rest are team members
    People.append(worksheet.col_values(i))
    Team = People[i-1][0]
    print(People[i-1])
    print(Team)

#-------------------------------------------------------------------------------
#Read 2017 projects
worksheet2 = client.open("2017").sheet1

team0_2017 = []
teams2017 = []

#The following values are hardcoded due to the unorganized nature of the spreadsheets
for i in range(2, 6):
    team0_2017.append(worksheet2.cell(i, 2).value)

teams2017.append(worksheet2.cell(1,1).value)

team1_2017 = []

for i in range(8, 11):
    team1_2017.append(worksheet2.cell(i, 2).value)

teams2017.append(worksheet2.cell(7,1).value)

team2_2017 = []

for i in range(14, 17):
    team2_2017.append(worksheet2.cell(i, 2).value)

teams2017.append(worksheet2.cell(13,1).value)

team3_2017 = []

for i in range(20, 23):
    team3_2017.append(worksheet2.cell(i, 2).value)

teams2017.append(worksheet2.cell(19,1).value)

team4_2017 = []

for i in range(26, 31):
    team2_2017.append(worksheet2.cell(i, 2).value)

teams2017.append(worksheet2.cell(25,1).value)

team5_2017 = []

for i in range(34, 37):
    team5_2017.append(worksheet2.cell(i, 2).value)

teams2017.append(worksheet2.cell(33,1).value)

team6_2017 = []

for i in range(40, 43):
    team5_2017.append(worksheet2.cell(i, 2).value)

teams2017.append(worksheet2.cell(39,1).value)

team7_2017 = []

for i in range(46, 51):
    team7_2017.append(worksheet2.cell(i, 2).value)

teams2017.append(worksheet2.cell(45,1).value)

team8_2017 = []

for i in range(55, 60):
    team7_2017.append(worksheet2.cell(i, 2).value)

teams2017.append(worksheet2.cell(54,1).value)

team9_2017 = []

for i in range(64, 69):
    team7_2017.append(worksheet2.cell(i, 2).value)

teams2017.append(worksheet2.cell(63,1).value)

team10_2017 = []

for i in range(72, 78):
    team7_2017.append(worksheet2.cell(i, 2).value)

teams2017.append(worksheet2.cell(71,1).value)

print(teams2017)
