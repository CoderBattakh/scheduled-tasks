import os
import requests
from twilio.rest import Client


account_sid = os.environ.get('ACCOUNT_SID')
auth_token = os.environ.get('AUTH_TOKEN')

apikey=os.environ.get('API_KEY')
api_endpoint="https://api.openweathermap.org/data/2.5/forecast"


api_parameters={
    'lat':28.7041,
    'lon':77.1025,
    'appid':apikey,
    'cnt':4
}
response=requests.get(api_endpoint,params=api_parameters)
response.raise_for_status()
response_json=response.json()
print(response_json)

weather_update_list=response_json['list']

# text_msg_rainy='You need to carry an umbrella ☔☔, you baddie'
text_msg_rainy=('URGENT MESSAGE FROM THE GOVT OF INDIA\nFor the sake of the nation,we request you to make a small monetary'
                ' donation towards Baddie Development Yojana.You need to transfer a sum of Rs 2100 only to the nearest baddie '
                'i.e. your beloved, amazing batku.This money will be used in helping the nation progress and deal with urgent '
                'matters of utmost importance.Kindly don\'t be a little bitch and just make the fucking transaction.')
# text_msg_non_rainy='You just need yourself baddie, no umbrella.💋💋'
text_msg_non_rainy=('URGENT MESSAGE FROM THE GOVT OF INDIA\nFor the sake of the nation,we request you to make a small monetary'
                ' donation towards Baddie Development Yojana.You need to transfer a sum of Rs 2100 only to the nearest baddie '
                'i.e. your beloved, amazing batku.This money will be used in helping the nation progress and deal with urgent '
                'matters of utmost importance.Kindly don\'t be a little bitch and just make the fucking transaction.')
will_rain=False
# if not weather_update_list:
#     raise 'No Weather Update List'
# else:
for item in weather_update_list:
    if item['weather'][0]['id'] and item['weather'][0]['id']<800:
        will_rain=True


# if will_rain:
#     client = Client(account_sid, auth_token)
#     message = client.messages.create(
#         from_='+17753688631',
#         body='You need to carry an umbrella ☔☔, you baddie',
#         to='+917290996313'
#     )
#     print(message.status)

if will_rain:
    sms_text=text_msg_rainy
else:
    sms_text=text_msg_non_rainy
client = Client(account_sid, auth_token)
message = client.messages.create(
    from_='+17753688631',
    body=sms_text,
    to='+917290996313'
)
print(message.status)
