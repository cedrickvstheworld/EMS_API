from twilio.rest import Client


def send_sms(msg, phone_number):
    account_sid = 'AC550e18247ce51d01024ef9ccebd71499'
    auth_token = '213de26271164d0a228db1825abd8ed1'
    client = Client(account_sid, auth_token)

    try:
        message = client.messages.create(
            body=msg,
            from_='+17347250077',
            to='+63' + phone_number
        )
        return True
    except Exception as ex:
        print(ex)
        return False
