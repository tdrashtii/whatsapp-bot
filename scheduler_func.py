from twilio_func import *
from datetime import datetime
from datetime import date
from datetime import time
import apscheduler
import pytz
from apscheduler.schedulers.blocking import BlockingScheduler
import gspread
from oauth2client.service_account import ServiceAccountCredentials
from dateutil.parser import parse

s=['https://www.googleapis.com/auth/spreadsheets',
'https://www.googleapis.com/auth/drive']

#p= parse(msg)
dt=date.today().strftime('%d/%m/%Y')
print(dt)
now_date=datetime.strptime(dt,'%d/%m/%Y')
rem_day=now_date.day
rem_month=now_date.month
rem_year=now_date.year
def triggering():
    t=datetime(rem_year,rem_month,rem_day,14,2)
    print("inside triggering")
    local = pytz.timezone("Asia/Kolkata")
    local_dt = local.localize(t, is_dst=None)
    utc_dt = local_dt.astimezone(pytz.utc)


    scheduler = BlockingScheduler()
    creds= ServiceAccountCredentials.from_json_keyfile_name("crede.json",s)
    client=gspread.authorize(creds)

    #sheet = client.open("test")
    worksheet = client.open("python reminder").sheet1
    list_of_lists = worksheet.get_all_values()
    # print(list_of_lists)

    for row in list_of_lists:
        print("inside for loop")

        p= parse(row[0])
        # print(p)
        pp=p.strftime('%d/%m/%Y')
        # print(pp)
        # print(dt)
        # print(row[1])
        # print('Date formats are',pp ,dt)
        if pp == dt:
            print("inside if loop")
            scheduler.add_job(send_rem, 'date', run_date=t, args=[row[0],row[1]])
            print("yoyo")
            
        else:
            pass
       
    scheduler.start()
    # return
triggering()
