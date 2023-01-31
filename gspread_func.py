# from oauth2client.service_account import ServiceAccountCredentialspip3 install --upgrade oauth2client 
from oauth2client.service_account import ServiceAccountCredentials
import gspread
import time

scope =['https://www.googleapis.com/auth/spreadsheets',
'https://www.googleapis.com/auth/drive','https://www.googleapis.com/auth/drive.file' ]


c= ServiceAccountCredentials.from_json_keyfile_name("crede.json",scope)
client=gspread.authorize(c)

sheet = client.open("python reminder").sheet1
row_values=sheet.row_values(1)
col_values=sheet.col_values(1)
row_filled=len(col_values)
col_filled=len(row_values)

    
def save_reminder_date(date):

    sheet.update_cell(row_filled+1, 1, date)
    print("saved date!")
    return 0
    
def save_reminder_body(msg):

    sheet.update_cell(row_filled+1, 2, msg)
    print("saved reminder message!")
    return 0

# reminder= client.open("python reminder").sheet1

# reminder.update_cell(1,1,"no hello world") #input value in gsheet
# # i=2
# # print(reminder.cell(i,1).value)
# i=1
# while reminder.cell(i,1).value !=None:
#     i=i+1
#     time.sleep(1)
# reminder.update_cell(i,1,"heyy")    #how to fill data in next cell




