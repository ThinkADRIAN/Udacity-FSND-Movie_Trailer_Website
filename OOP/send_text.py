# from twilio.rest import TwilioRestClient
from twilio import rest

account_sid = "AC1b53472a0c214b11d430b38f9e1e38ea" # Your Account SID from www.twilio.com/console
auth_token  = "1b0883bd6daed8df4beea83eede601ee"  # Your Auth Token from www.twilio.com/console

# client = TwilioRestClient(account_sid, auth_token)
client = rest.TwilioRestClient(account_sid, auth_token)

message = client.messages.create(body="Mr. Telephone Man... There's something wrong with my line...",
    to="+14157103111",    # Replace with your phone number
    from_="+19292732831") # Replace with your Twilio number

print(message.sid)
