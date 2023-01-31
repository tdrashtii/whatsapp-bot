from twilio.rest import Client
 
account_sid = '*******************************'
auth_token = '********************************'
client = Client(account_sid, auth_token)
def send_rem(date,rem):
    print('sending')
    message = client.messages.create(
                                  from_='whatsapp:+14155238886',
                                  body='*REMINDER* '+ date +'\n'+rem,
                                  to='whatsapp:+91********'
                              )
    client.messages
    print('sent')
     
    print(message.sid)

    return str(message)
