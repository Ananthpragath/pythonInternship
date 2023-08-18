from twilio.rest import Client
import re

#your Twilio account SID and auth token
account_sid = 'AC1297df483792926c8e31a2294eb082cf'
auth_token = '653c2d75ac2e4f5a2507b5bd267bc4f2'
twilio_phone_number = '8978792127'  #your twilio phone number

def validate_phone_number(phone_number):
    pattren = r"^d{10}$"
    return re.match(pattren,phone_number)

def send_sms(phone_number,message):
    client = Client(account_sid,auth_token)

    try:

        message = client.messages.create(
            body=message,
            from_=twilio_phone_number,
            to=phone_number
        )
        return message.sid
    except Exception as e:
        return str(e)
    
def main():
    phone_number = input("Enter your phone number:")
    if not validate_phone_number(phone_number):
        print("Invalid phone number formate. please enter a 10-digit number.")
        return
    
    message = input("Enter the message you want to send:")

    response = send_sms(phone_number,message)
    if response.startswith("SM"):
        print("Message sent successfully. Message SID:",response)
    else:
        print("Message sending failed. Error:",response)

if __name__ == "_ _main_ _":
    main()