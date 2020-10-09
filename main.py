from twilio.rest import Client 
 
account_sid = #your account_sid 
auth_token = #your auth_token
client = Client(account_sid, auth_token) 
def send_message():
    message = client.messages.create( 
                              from_=#telio assigned number,  
                              body=#your message,      
                              to=#recepient of the message
                          ) 
 
    print(message.sid)