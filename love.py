from twilio.rest import Client 
 
account_sid = 'ACf4c71647ed039df4d415a571e0ffada6' 
auth_token = '8957db9abc0eff1ce86440b1c2bcafa7' 
client = Client(account_sid, auth_token) 
def send_love():
    message = client.messages.create( 
                                  from_='whatsapp:+14155238886',  
                                  body='Good morning',      
                                  to='whatsapp:+917604866659' 
                              ) 
 
    print(message.sid)
