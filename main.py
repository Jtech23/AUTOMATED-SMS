from twilio.rest import Client
import os

account_sid = os.getenv("ACC_SID")
auth_token = os.getenv("AUTH_TOKEN")
client = Client(account_sid, auth_token)

message = client.messages.create(
  body="Hello",
  from_='+17472334694',
  to='+2349063704098'
)
