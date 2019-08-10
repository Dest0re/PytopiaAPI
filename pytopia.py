import requests
import json


class PytopiaAPI:

    def __init__(self, token, url='http://127.0.0.1:20000/api/1.0'):
        self.token = token
        self.URL = url

    def send_request(self, method, *params):
        if params:
            params = params[0]
        return requests.post(self.URL, data=json.dumps({'method': method,
                                                    'params': params,
                                                 'token': self.token})).json()

    def getSystemInfo(self):
        return self.send_request('getSystemInfo')

    def getProfileStatus(self):
        return self.send_request('getProfileStatus')

    def setProfileStatus(self, status, mood):
        return self.send_request('setProfileStatus', {'status': status, 'mood': mood})

    def getOwnContact(self):
        return self.send_request('getOwnContact')

    def getContacts(self, filter=''):
        return self.send_request('getContacts', {'filter': filter})

    def getContactAvatar(self, pk, coder, format):
        """Method getContactAvatar returns to the Response field the avatar of the selected user in the base64
        or hex format. As a parameter the method uses Public Key of the contact. Format is JPG/PNG"""
        return self.send_request('getContactAvatar', {'pk': pk, 'coder': coder, 'format': format})

    def getChannelAvatar(self, channelid):
        return self.send_request('getChannelAvatar', {'channelid': channelid})

    def setContactGroup(self, pk, groupName):
        return self.send_request('setContactGroup', {'contactPublicKey': pk, 'groupName': groupName})

    def sendChannelMessage(self, channelid, message):
        return self.send_request('sendChannelMessage', {'channelid': channelid, 'message': message})
