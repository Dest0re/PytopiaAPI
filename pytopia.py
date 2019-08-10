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

    def setContactNick(self, pk, newNick):
        return self.send_request('setContactNick', {'contactPublicKey': pk, 'newNick': newNick})

    def sendInstantMessage(self, to, text):
        return self.send_request('sendInstantMessage', {'to': to, 'text': text})

    def sendInstantQuote(self, to, text, id_message):
        return self.send_request('sendInstantQuote', {'to': to, 'text': text, 'id_message': id_message})

    def sendInstantSticker(self, to, collection, name):
        return self.send_request('sendInstantSticker', {'to': to, 'collection': collection, 'name': name})

    def getStickerCollections(self):
        return self.send_request('getStickerCollections')

    def getStickerNamesByCollection(self, collection_name):
        return self.send_request('getStickerNamesByCollection', {'collection_name': collection_name})

    def getImageSticker(self, collection_name, sticker_name, coder):
        return self.send_request('getImageSticker', {'collection_name': collection_name, 'sticker_name': sticker_name,
                                                     'coder': coder})

    def sendInstantBuzz(self, to, comments):
        return self.send_request('sendInstantBuzz', {'to': to, 'comments': comments})

    def sendInstantInvitation(self, to, channelid, description, comments):
        self.send_request('sendInstantInvitation', {'to': to, 'channelid': channelid, 'description': description,
                                                    'comments': comments})

    def removeInstantMessages(self, hex_contact_public_key):
        return self.send_request('removeInstantMessages', {'hex_contact_public_key': hex_contact_public_key})

    def getContactMessages(self, pk):
        return self.send_request('getContactMessages', {'pk': pk})

    def sendEmailMessage(self, *to, subject, body):
        return self.send_request('sendEmailMessage', {'to': to, 'subject': subject, 'body': body})

    def sendPayment(self, cardid, to, amount, comment, fromCard=''):
        return self.send_request('sendPayment', {'cardid': cardid, 'to': to, 'amount': amount, 'comment': comment,
                                                 'fromCard': fromCard})

    def getEmailFolder(self, folderType, filter=''):
        return self.send_request('getEmailFolder', {'folderType': folderType, 'filter': filter})

    def getEmails(self, folderType, filter=''):
        return self.send_request('getEmails', {'folderType': folderType, 'filter': filter})

    def getEmailById(self, id):
        return self.send_request('getEmailById', {'id': id})

    def deleteEmail(self, id):
        return self.send_request('deleteEmail', {'id': id})

    def sendReplyEmailMessage(self, id, body):
        return self.send_request('sendReplyEmailMessage', {'id': id, 'body': body})

    def sendForwardEmailMessage(self, id, to, body):
        return self.send_request('sendForwardEmailMessage', {'id': id, 'to': to, 'body': body})

    def getFinanceSystemInformation(self):
        return self.send_request('getFinanceSystemInformation')

    def getBalance(self):
        return self.send_request('getBalance')

    def getFinanceHistory(self, filters='', referenceNumber='', toDate='', fromDate='', batchId='', fromAmount='',
                          toAmount=''):
        return self.send_request('getFinanceHistory', {'filters': filters, 'referenceNumber': referenceNumber,
                                                       'toDate': toDate, 'fromDate': fromDate, 'batchId': batchId,
                                                       'fromAmount': fromAmount, 'toAmount': toAmount})

    def getCards(self):
        return self.send_request('getCards')

    def addCard(self, name, color, numbers):
        return self.send_request('addCard', {'name': name, 'color': color, 'preorderNumberInCard': numbers})

    def deleteCard(self, cardid):
        return self.send_request('deleteCard', {'cardid': cardid})

    def enableMining(self, enabled):
        return self.send_request('enableMining', {'enable': enabled})

    def enableInterest(self, enabled):
        return self.send_request('enableInterest', {'enable': enabled})

    def enableHistoryMining(self, enabled):
        return self.send_request('enableHistoryMining', {'enable': enabled})

    def statusHistoryMining(self):
        return self.send_request('statusHistoryMining')

    def getMiningBlocks(self):
        return self.send_request('getMiningBlocks')

    def getMiningInfo(self):
        return self.send_request('getMiningInfo')

    def getVouchers(self):
        return self.send_request('getVouchers')

    def createVoucher(self, amount):
        return self.send_request('createVoucher', {'amount': amount})

    def useVoucher(self, voucherid):
        return self.send_request('useVoucher', {'voucherid': voucherid})

    def deleteVoucher(self, voucherid):
        return self.send_request('deleteVoucher', {'voucherid': voucherid})

    def getInvoices(self, cardId='', invoiceId='', pk='', transactionId='', status='', startDateTime='', endDateTime='',
                    referenceNumber=''):
        return self.send_request('getInvoices', {'cardId': cardId, 'invoiceId': invoiceId, 'pk': pk,
                                                 'transactionId': transactionId, 'status': status,
                                                 'startDateTime': startDateTime, 'endDateTime': endDateTime,
                                                 'referenceNumber': referenceNumber})

    def getInvoiceByReferenceNumber(self, referenceNumber):
        return self.send_request('getInvoiceByReferenceNumber', {'referenceNumber': referenceNumber})

    def getTransactionIdByReferenceNumber(self, referenceNumber):
        return self.send_request('getTransactionIdByReferenceNumber', {'referenceNumber': referenceNumber})

    def sendInvoice(self, cardid, amount, comment):
        return self.send_request('sendInvoice', {'cardid': cardid, 'amount': amount, 'comment': comment})

    def acceptInvoice(self, invoiceid):
        return self.send_request('acceptInvoice', {'invoiceid': invoiceid})

    def declineInvoice(self, invoiceid):
        return self.send_request('declineInvoice', {'invoiceid': invoiceid})

    def cancelInvoice(self, invoiceid):
        return self.send_request('cancelInvoice', {'invoiceid': invoiceid})

    def requestUnsTransfer(self, name, hexNewOwnerPk):
        return self.send_request('requestUnsTransfer', {'name': name, 'hexNewOwnerPk': hexNewOwnerPk})

    def acceptUnsTransfer(self, requestid):
        return self.send_request('acceptUnsTransfer', {'requestid': requestid})

    def declineUnsTransfer(self, requestid):
        return self.send_request('declineUnsTransfer', {'requestid': requestid})

    def incomingUnsTransfer(self):
        return self.send_request('incomingUnsTransfer')

    def outgoingUnsTransfer(self):
        return self.send_request('outgoingUnsTransfer')

    def storageWipe(self):
        return self.send_request('storageWipe')

    def sendAuthorizationRequest(self, pk, message):
        return self.send_request('sendAuthorizationRequest', {'pk': pk, 'message': message})

    def acceptAuthorizationRequest(self, pk, message=''):
        return self.send_request('acceptAuthorizationRequest', {'pk': pk, 'message': message})

    def rejectAuthorizationRequest(self, pk, message):
        return self.send_request('rejectAuthorizationRequest', {'pk': pk, 'message': message})

    def deleteContact(self, pk):
        return self.send_request('deleteContact', {'pk': pk})

    def getChannels(self, filter='', channel_type=''):
        return self.send_request('getChannels', {'filter': filter, 'channel_type': channel_type})

    def sendChannelMessage(self, channelid, message):
        return self.send_request('sendChannelMessage', {'channelid': channelid, 'message': message})

    def sendChannelPicture(self, channelid, base64_image, filename_image):
        return self.send_request('sendChannelPicture', {'channelid': channelid, 'base64_image': base64_image,
                                                        'filename_image': filename_image})

    def joinChannel(self, ChannelId, password=''):
        return self.send_request('joinChannel', {'ident': ChannelId, 'password': password})

    def leaveChannel(self, channelid):
        return self.send_request('leaveChannel', {'channelid': channelid})

    def getChannelMessages(self, channelid):
        return self.send_request('getChannelMessages', {'channelid': channelid})

    def getChannelInfo(self, channelid):
        return self.send_request('getChannelInfo', {'channelid': channelid})

    def getChannelModerators(self, channelid):
        return self.send_request('getChannelModerators', {'channelid': channelid})

    def getChannelContacts(self, channelid):
        return self.send_request('getChannelContacts', {'channelid': channelid})

    def getChannelModeratorRight(self, channelid, moderator):
        return self.send_request('getChannelModeratorRight', {'channelid': channelid, 'moderator': moderator})

    def createChannel(self, channel_name, description, read_only, password, language, hashtags, geoTag,
                      base64_avatar_image, hide_in_UI):
        return self.send_request('createChannel', {'channel_name': channel_name, 'description': description,
                                                   'read_only': read_only, 'password': password,
                                                   'language': language, 'hashtags': hashtags, 'geoTag': geoTag,
                                                   'base64_avatar_image': base64_avatar_image,
                                                   'hide_in_UI': hide_in_UI})

    def modifyChannel(self, channelid, description, read_only, language, hashtags, geoTag,
                      base64_avatar_image, hide_in_UI):
        return self.send_request('createChannel', {'channelid': channelid, 'description': description,
                                                   'read_only': read_only,'language': language, 'hashtags': hashtags,
                                                   'geoTag': geoTag, 'base64_avatar_image': base64_avatar_image,
                                                   'hide_in_UI': hide_in_UI})

    def deleteChannel(self, channelid):
        return self.send_request('deleteChannel', {'channelid': channelid})

    def getChannelSystemInfo(self):
        return self.send_request('getChannelSystemInfo')

    def unsCreateRecordRequest(self, nick, valid, isPrimary, ChannelId):
        return self.send_request('unsCreateRecordRequest', {'nick': nick, 'valid': valid, 'isPrimary': isPrimary,
                                                            'channelId': ChannelId})

    def unsModifyRecordRequest(self, nick, valid, isPrimary, ChannelId):
        return self.send_request('unsCreateRecordRequest', {'nick': nick, 'valid': valid, 'isPrimary': isPrimary,
                                                            'channelId': ChannelId})

    def unsDeleteRecordRequest(self, nick):
        return self.send_request('unsDeleteRecordRequest', {'nick': nick})

    def unsSearchByPk(self, filter):
        return self.send_request('unsSearchByPk', {'filter': filter})

    def unsSearchByNick(self, filter):
        return self.send_request('unsSearchByPk', {'filter': filter})

    def getUnsSyncInfo(self):
        return self.send_request('getUnsSyncInfo')

    def unsRegisteredNames(self):
        return self.send_request('unsRegisteredNames')

    def summaryUnsRegisteredNames(self, date_from, date_to):
        return self.send_request('summaryUnsRegisteredNames', {'from_date': date_from, 'to_date': date_to})

    def clearTrayNotifications(self):
        return self.send_request('clearTrayNotifications')

    def getNetworkConnections(self):
        return self.send_request('getNetworkConnections')

    def getProxyMappings(self):
        return self.send_request('getProxyMappings')

    def createProxyMapping(self, srcHost, srcPort, dstHost, dstPort, enabled):
        return self.send_request('createProxyMapping', {'srcHost': srcHost, 'srcPort': srcPort, 'dstHost': dstHost,
                                                        'dstPort': dstPort, 'enabled': enabled})

    def enableProxyMapping(self, mappingId):
        return self.send_request('enableProxyMapping', {'mappingId': mappingId})

    def disableProxyMapping(self, mappingId):
        return self.send_request('disableProxyMapping', {'mappingid': mappingId})

    def removeProxyMapping(self, mappingId):
        return self.send_request('removeProxyMapping', {'mappingId': mappingId})

    def lowTrafficMode(self):
        return self.send_request('lowTrafficMode')

    def setLowTrafficMode(self, enabled):
        return self.send_request('setLowTrafficMode', {'enavled': enabled})

    def getWhoIsInfo(self, name_or_pk):
        return self.send_request('getWhoIsInfo', {'owner': name_or_pk})

    def requestTreasuryInterestRates(self):
        return self.send_request('requestTreasuryInterestRates')

    def getTreasuryInterestRates(self):
        return self.send_request('getTreasuryInterestRates')

    def requestTreasuryTransactionVolumes(self):
        return self.send_request('requestTreasuryTransactionVolumes')

    def getTreasuryTransactionVolumes(self):
        return self.send_request('getTreasuryTransactionVolumes')

    def ucodeEncode(self, hex_code, size_image, coder, format):
        return self.send_request('ucodeEncode', {'hex_code': hex_code, 'size_image': size_image, 'coder': coder,
                                                 'format': format})

    def ucodeDecode(self, base64_image):
        return self.send_request('ucodeDecode', {'base64_image': base64_image})

    def getWebSocketState(self):
        return self.send_request('getWebSocketState')

    def setWebSocketState(self, enabled, port):
        return self.send_request('setWebSocketState', {'enabled': enabled, 'port': port})
