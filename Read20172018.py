import gspread
import re
from oauth2client.service_account import ServiceAccountCredentials

# use creds to create a client to interact with the Google Drive API
scope = ['https://spreadsheets.google.com/feeds','https://www.googleapis.com/auth/drive']
creds = ServiceAccountCredentials.from_json_keyfile_name('credentials.json', scope)
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

#Hashing email and phone number
hashed_phone = []
hashed_email = []

#Creating a databse for the data
import sqlite3
conn = sqlite3.connect('VEEP_Database.sqlite')
cursor = conn.cursor()
print("Opened database successfully")

cursor.execute('''CREATE TABLE STUDENTS
         (STUDENT_ID INT PRIMARY KEY     NOT NULL,
         NAME           TEXT    NOT NULL,
         EMAIL          TEXT     NOT NULL,
         DISCIPLINE     TEXT   NOT NULL,
         YEAR           TEXT   NOT NULL,
         PHONE          TEXT    NOT NULL,
         INTERVIEW_OFFER TEXT);''')

def enter_into_student_table(student_id, name, email, discipline, year, phone,
    interview_offer):
    cursor.execute("INSERT INTO STUDENTS (STUDENT_ID,NAME,EMAIL,DISCIPLINE,YEAR,PHONE,INTERVIEW_OFFER) \
      VALUES (?, ?, ?, ?, ?, ?, ?)", (student_id, name, email, discipline, year, phone, interview_offer));


for i in range(0, len(Name)):
    #hashed_phone.append(hash(Phone[i]))
    #hashed_email.append(hash(Email[i]))

    if i > 11:
        x = 11
    else:
        x = i

    match = re.search(r"^\D?(\d{3})\D?\D?(\d{3})\D?(\d{4})$", Phone[i])
    #match = re.search(r"(\d{3}[-\.\s]??\d{3}[-\.\s]??\d{4}|\(\d{3}\)\s*\d{3}[-\.\s]??\d{4}|\d{3}[-\.\s]??\d{4})", Phone[i])
    if match:
        phone = match.groups()[0] + match.groups()[1] + match.groups()[2]
    else:
        phone = Phone[i]

    enter_into_student_table(i, Name[i], Email[i], Discipline[i], Year[i],
        phone, Interview_Offer[x])


conn.commit()
conn.close()
print("Committed and closed database successfully")
