import requests
from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse
from gspread_func import *
from dateutil.parser import parse
# from scheduler_func import *



app = Flask(__name__)
count=0

@app.route('/bot',methods=['POST'])
def reply():
    # print("hello")
    # incoming_msg= request.values.get('Body','').strip()
    # print(incoming_msg)
    # resp=MessagingResponse()
    # msg=resp.message()
    # msg.body('HELLO')
    # return str(resp)
    # return "hello world"
    incoming_msg = request.form.get('Body','').lower()
    response = MessagingResponse()
    message=response.message()
    responded = False
   
    words = incoming_msg.split('@')
    if "hello" in incoming_msg:
        reply = "Hello! \nDo you want to set a reminder?"
        message.body(reply)
        responded = True
    
    if len(words) == 1 and "yes" in incoming_msg:
        reminder_string = "Please provide date in the following format only.\n\n"\
        "*Date @* _reminder_To_be_Set"
        message.body(reminder_string)
        responded = True
    if len(words) == 1 and "no" in incoming_msg:
        reply="Ok. Have a nice day!"
        message.body(reply)
        responded = True
    elif len(words)!=1:
        input_type = words[0].strip()
        input_string = words[1].strip()
        reply="your reminder is being saved"
        set_reminder_date(input_type)
        set_reminder_body(input_string)
        message.body(reply)
        responded = True
        


    # elif len(words) != 1:
    #     input_type = words[0].strip().lower()
    #     input_string = words[1].strip()
    #     if input_type == "date":
    #         reply="Please enter the reminder message in the following format only.\n\n"\
    #         "*Reminder @* _type the message_"
    #         set_reminder_date(input_string)
    #         message.body(reply)
    #         responded = True
    #     if input_type == "reminder":
    #         # print("yuhu")
    #         reply="Your reminder is set!"
    #         set_reminder_body(input_string)
    #         message.body(reply)
    #         responded = True
        
    if not responded:
        
        message.body('Incorrect request format. Please enter in the correct format')
    
    return str(response)
    

def set_reminder_date(msg):
        p= parse(msg)
        date=p.strftime('%d/%m/%Y')
        save_reminder_date(date)
        return 0


    
def set_reminder_body(msg):
        save_reminder_body(msg)
        
        return 0

        

        
    
if __name__ == "__main__":
    app.run(debug=True)
    
