from twilio.rest import Client
 
account_sid = 'AC238c00bfad0fdd586e73b8d61ecdb6db'
auth_token = '7ab75aa2615f6c7c3360e985e3922021'
client = Client(account_sid, auth_token)
def send_rem(date,rem):
    print('sending')
    message = client.messages.create(
                                  from_='whatsapp:+14155238886',
                                  body='*REMINDER* '+ date +'\n'+rem,
                                  to='whatsapp:+917718067747'
                              )
    client.messages
    print('sent')
     
    print(message.sid)

    return str(message)