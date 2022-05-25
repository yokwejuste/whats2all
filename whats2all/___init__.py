from os import abort
import requests
class Whats2All:
    
    def __init__(self,bearer_token,phone_number_id):
        self.bearer_token = bearer_token
        self.phone_number_id = phone_number_id

        self.base_url = 'https://graph.facebook.com/v13.0'+str(phone_number_id)+'message'

        #set the headers
        self.headers = {
            'Authorization': self.bearer_token,
            'Content-Type' : 'application/json'
        }

    #send text message function
    def send_message(self,phone_number,body,preview_url=False):
        if not phone_number:
            raise Exception('phone number to send message to must be provided')
        if not body:
            raise Exception('message body must be provided')

        data = {
            'messaging_product': 'whatsapp',
            'recipient_type': 'individual',
            'to': str(phone_number),
            'type': 'text',
            'text': {
                'preview_url': preview_url,
                'body': body
            }   
        }
        try:
            res = requests.post(self.base_url,data=data,headers=self.headers)
            
            if res.status_code == requests.codes.ok:
                return res.json() 
            else:
                raise Exception(res['message'])

        except Exception as error:
            abort(res['status_code'],res['message'])