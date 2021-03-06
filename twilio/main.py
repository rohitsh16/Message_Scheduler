
# Download the helper library from https://www.twilio.com/docs/python/install
from twilio.rest import Client     # it helps to contact with server
import sys 
# sys module is a set of functions which provide crucial information about
# how your Python script is interacting with the host system.
account_sid = 'SID goes here'              # Twilio account SID
auth_token = 'auth token goes here'        # Twilio account auth token
client = Client(account_sid, auth_token)   # we are passing the authentication to the Client class of twilio.rest

message = sys.argv[1]              # taking first argument as message from the terminal
try:
     message_create = client.messages.create(
                body=message,       # your message variable content goes here
                from_='XXXXXXXXXX', # Your Twilio Phone Number
                to='+91XXXXXXXXX'   # Phone Number on which you want to send message
          )

     print(message_create.sid)     # to print message id in the terminal
except:
     print("Invalid Number")       # any sort of error in sending the message will lead to this exception block