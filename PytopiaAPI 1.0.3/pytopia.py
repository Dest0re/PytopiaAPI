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
        """Method getSystemInfo returns information about current packaging version of the Utopia application in the
        Response block. The method is called without using any parameters."""
        return self.send_request('getSystemInfo')

    def getProfileStatus(self):
        """Method getProfileStatus returns the profile status."""
        return self.send_request('getProfileStatus')

    def setProfileStatus(self, status, mood):
        """Method setProfileStatus sets the new status, as well as the mood message in the Utopia Ecosystem.
        The method is called by using Status parameter line with possible options: (Available, Away, DoNotDisturb,
        Invisible, Offline) and if desired Mood which contains mood message text (up to 130 symbols). In the Response
        field, the status of completed operation is displayed."""
        return self.send_request('setProfileStatus', {'status': status, 'mood': mood})

    def getOwnContact(self):
        """Method getOwnContact returns information about yourself."""
        return self.send_request('getOwnContact')

    def getContacts(self, filter=''):
        """Method getContacts returns to the Response field the list of contacts, it is possible to search by full or
        partial matching of the Public Key and Nickname. As a parameter it is possible to specify Filter that transfers
        the text line to search for contacts ( has to contain full or partial matching with Public Key or Nickname of
        the searched contact).The Filter "#owner#" will return information about yourself."""
        return self.send_request('getContacts', {'filter': filter})

    def getContactAvatar(self, pk, coder, format):
        """Method getContactAvatar returns to the Response field the avatar of the selected user in the base64
        or hex format. As a parameter the method uses Public Key of the contact. Format is JPG/PNG"""
        return self.send_request('getContactAvatar', {'pk': pk, 'coder': coder, 'format': format})

    def getChannelAvatar(self, channelid, coder, format):
        """Method getChannelAvatar returns to the Response field the avatar of the
        selected channel in the base64 or hex format."""
        return self.send_request('getChannelAvatar', {'channelid': channelid, 'coder': coder, 'format': format})

    def setContactGroup(self, pk, groupName):
        """Method setContactGroup creates group or transfers selected contact into the group in the contact list. The
        method is called by using the Public Key parameters, which pass the Public Key of the contact (Public Key can
        be recognized by using the getContacts method) and Group Name, which passes the group name for creation or
        transfer (up to 32 symbols). In the Response field the status of completion of the operation is displayed."""
        return self.send_request('setContactGroup', {'contactPublicKey': pk, 'groupName': groupName})

    def setContactNick(self, pk, newNick):
        """Method setContactNick sets the selected value for the Nickname field for the selected contact. The method
        is called by using the Public Key parameters, which pass on the Public Key for the contact (Public Key can be
        recognized by using the getContacts method) and New Nick, which passes on the new Nickname (up to 32 symbols).
        Empty value to be set as the Nickname Public Key of the contact. In the Response field the status of completion
        of the operation is displayed."""
        return self.send_request('setContactNick', {'contactPublicKey': pk, 'newNick': newNick})

    def sendInstantMessage(self, to, text):
        """Method sendInstantMessage sends personal message(IM) to the selected contact from the contact list. The
        method is called by using the To parameter, that passes on the Public Key or Nickname to whom the message would
        be sent (Public Key can be recognized by using the getContacts method) and Text, which contains the text of the
        message. In the Response field the status of completion of the operation is displayed."""
        return self.send_request('sendInstantMessage', {'to': to, 'text': text})

    def sendInstantQuote(self, to, text, id_message):
        """Method sendInstantQuote sends quote personal message(IM) to the selected contact
        from the contact list on message by id_message."""
        return self.send_request('sendInstantQuote', {'to': to, 'text': text, 'id_message': id_message})

    def sendInstantSticker(self, to, collection, name):
        """Method sendInstantSticker sends sticker personal message(IM) to the
        selected contact from the contact list a sticker from collection by name."""
        return self.send_request('sendInstantSticker', {'to': to, 'collection': collection, 'name': name})

    def getStickerCollections(self):
        """Method getStickerCollections returns collection names of stickers."""
        return self.send_request('getStickerCollections')

    def getStickerNamesByCollection(self, collection_name):
        """Method getStickerNamesByCollection returns available names from corresponded collection."""
        return self.send_request('getStickerNamesByCollection', {'collection_name': collection_name})

    def getImageSticker(self, collection_name, sticker_name, coder):
        """Method getImageSticker returns image by sticker name from
        corresponded collection in coder that can be equal "BASE64"."""
        return self.send_request('getImageSticker', {'collection_name': collection_name, 'sticker_name': sticker_name,
                                                     'coder': coder})

    def sendInstantBuzz(self, to, comments):
        """Method sendInstantBuzz sends buzz personal message(IM) to the
        selected contact from the contact list with comments."""
        return self.send_request('sendInstantBuzz', {'to': to, 'comments': comments})

    def sendInstantInvitation(self, to, channelid, description, comments):
        """Method sendInstantInvitation sends invitation personal message(IM) to the
        selected contact from the contact list with description and comments on channel_id."""
        return self.send_request('sendInstantInvitation', {'to': to, 'channelid': channelid, 'description': description,
                                                    'comments': comments})

    def removeInstantMessages(self, hex_contact_public_key):
        """Method removeInstantMessages removes all personal message(IM)
        of the selected contact from the contact list."""
        return self.send_request('removeInstantMessages', {'hex_contact_public_key': hex_contact_public_key})

    def getContactMessages(self, pk):
        """Method getContactMessages returns in the Response block the history of communication from personal chat
        with selected contact. The method is called by using the Public Key parameter, that passes on the Public Key of
        the contact (Public Key can be recognized by using the getContacts method)"""
        return self.send_request('getContactMessages', {'pk': pk})

    def sendEmailMessage(self, *to, subject, body):
        """Method sendEmailMessage sends uMail to the selected contact in the Utopia network. The method is called by
        using the To parameter, which passes on the Public Key or Nickname to which the uMail would be sent (Public Key
        can be recognized by using the getContacts method); Subject, that determines the subject of the email; and Body,
        which passes on the text in the body of the uMail. In the Response field the status of
        completion of the operation is displayed."""
        return self.send_request('sendEmailMessage', {'to': to, 'subject': subject, 'body': body})

    def sendPayment(self, cardid, to, amount, comment, fromCard=''):
        """Method sendPayment sends cryptons transfer for the specified amount to the contact or to the card.
        The method is called by using the To parameters (nick, pk, cardid), which pass on the Public Key, Nickname or
        the card number of the user to whom the transfer would be sent (Public Key can be recognized by using the
        getContacts method); Amount, which transfers the amount of transfer (the number needs to be greater than 0 and
        contain no more than 9 character after coma); Comment is optional, which contains the text of the comment
        (up to 148 characters); as well as the optional 'From card' field can be specified, that passes on the card
        number from which the cryptons will be taken from. If the parameter is empty, then cryptons would be deducted
        from the main account. In the Response field the status of completion of the operation is displayed."""
        return self.send_request('sendPayment', {'cardid': cardid, 'to': to, 'amount': amount, 'comment': comment,
                                                 'fromCard': fromCard})

    def getEmailFolder(self, folderType, filter=''):
        """Method getEmailFolder returns to the Response block the list of identifications of uMail emails in the
        selected folder by using specified search filter. The method is called by using the FolderType parameters,
        which pass on the number of the folder from which the list should be taken (numbers of the folders 1-Inbox,
        2-Drafts, 4-Sent, 8-Outbox, 16-Trash) and it is possible to specify the Filter parameter, which passes on the
        text value for the search of emails in uMail (has to contain the full or partial match with the Public Key,
        Nickname or the text of email)."""
        return self.send_request('getEmailFolder', {'folderType': folderType, 'filter': filter})

    def getEmails(self, folderType, filter=''):
        """Method getEmails returns to the Response block the list of detailed of uMail emails in the selected folder
        by using specified search filter. The method is called by using the FolderType parameters, which pass on the
        number of the folder from which the list should be taken (numbers of the folders 1-Inbox, 2-Drafts, 4-Sent,
        8-Outbox, 16-Trash) and it is possible to specify the Filter parameter, which passes on the text value for the
        search of emails in uMail (has to contain the full or partial match with the
        Public Key, Nickname or the text of email)."""
        return self.send_request('getEmails', {'folderType': folderType, 'filter': filter})

    def getEmailById(self, id):
        """Method getEmailById returns the information based on the selected email in uMail. The method is called
        by using the Id parameter, which passes on the id of the email
        (id of the email can be found by using getEmailFolder method)."""
        return self.send_request('getEmailById', {'id': id})

    def deleteEmail(self, id):
        """Method deleteEmail deletes email in uMail. First deletion will move email to the Trash, subsequent
        will remove from the database. The method is called by using the Id parameter which passes on the id of
        the email (id of the email can be found by using getEmailFolder method). In the Response field the
        status of completion of the operation is displayed."""
        return self.send_request('deleteEmail', {'id': id})

    def sendReplyEmailMessage(self, id, body):
        """Method sendReplyEmailMessage creates response email in uMail for the incoming email and sends it to
        the contact with new message. The method is called by using the Id parameters, which pass on the id of
        the email (id of the email can be found by using getEmailFolder method) and Body, which passes on the text of
        the email in uMail. In the Response field the status of completion of the operation is displayed."""
        return self.send_request('sendReplyEmailMessage', {'id': id, 'body': body})

    def sendForwardEmailMessage(self, id, to, body):
        """Method sendForwardEmailMessage creates response email for an incoming email in uMail and sends
        it to the selected contact with the new message. The method is called by using the 'Id' parameter,
        which passes on the id of the email (id of the email can be found by using getEmailFolder method); 'To',
        which passes on the Public Key or Nickname of the user to which the email will be sent; and 'Body', which
        passes on the text in uMail. In the Response field the status of completion of the operation is displayed."""
        return self.send_request('sendForwardEmailMessage', {'id': id, 'to': to, 'body': body})

    def getFinanceSystemInformation(self):
        """Method getFinanceSystemInformation returns in the Response field the information about Utopia
        financial system (information about fees and limits). Method is called without using any parameters."""
        return self.send_request('getFinanceSystemInformation')

    def getBalance(self):
        """Method getBalance returns in the Response field the amount of cryptons on the primary balance,
        without considering the balance on cards. Method is called without using any parameters."""
        return self.send_request('getBalance')

    def getFinanceHistory(self, filters='', referenceNumber='', toDate='', fromDate='', batchId='', fromAmount='',
                          toAmount=''):
        """Method getFinanceHistory allows to receive the history of financial transactions based on the specifications
        in the parameters of the filter. The list of available filters:
        ALL_CARDS
        INCOMING_CARDS
        OUTGOING_CARDS
        CREATED_CARDS
        DELETED_CARDS
        ALL_TRANSFERS
        INCOMING_TRANSFERS
        OUTGOING_TRANSFERS
        ALL_REQUESTS
        AWAITING_REQUESTS
        AUTHORIZED_REQUESTS
        DECLINED_REQUESTS
        CANCELED_REQUESTS
        EXPIRED_REQUESTS
        ALL_APPROVED_REQUESTS
        CREATED_VOUCHERS
        CREATED_VOUCHERS_BATCH
        ACTIVATED_VOUCHERS
        DELETED_VOUCHERS
        ALL_VOUCHERS
        ALL_MINING
        ALL_INTEREST
        ALL_FEE
        ALL_UNS_RECORDS
        UNS_UNS_REGISTRATION
        UNS_UNS_CHANGED
        UNS_UNS_TRANSFERRED
        UNS_UNS_DELETED
        ALL_TRANSACTIONS

        Filters can be combined by using coma : 'ALL_CARDS,ALL_FEE'
        Also the method accepts as the parameter (reference number),
        which passes on the number of the transaction which the
        history should be displayed (empty parameter will start
        returning information starting from the last message)."""
        return self.send_request('getFinanceHistory', {'filters': filters, 'referenceNumber': referenceNumber,
                                                       'toDate': toDate, 'fromDate': fromDate, 'batchId': batchId,
                                                       'fromAmount': fromAmount, 'toAmount': toAmount})

    def getCards(self):
        """Method getCards returns in the Response field the current list of cards and their detailed information
        from uWallet. Method is called without using any parameters."""
        return self.send_request('getCards')

    def addCard(self, name, color, numbers):
        """Method addCard sends the request for creation of new card in uWallet. The method is called by using the
        following parameters: Name, which passes on the name of the new card (can contain between 1 and 32 symbols),
        Color, which passes on the color of the card ( in RGB format, for example '#FFFFFF') and also can specify the
        First 4 numbers of the card for customization ( it is possible to change only 4 first symbols, can contain
        symbols (A-F) and numbers (0-9)). In the Response field the status of
        completion of the operation is displayed."""
        return self.send_request('addCard', {'name': name, 'color': color, 'preorderNumberInCard': numbers})

    def deleteCard(self, cardid):
        """Method deleteCard deletes the existing card from uWallet. The amount from card will be returned
        to the main balance. The following parameter is specified: CardId, which passes on the card number
        ( CardId can be found by using the getCards method). In the Response field the status of
        completion of the operation is displayed."""
        return self.send_request('deleteCard', {'cardid': cardid})

    def enableMining(self, enabled):
        """Method enableMining turns on the mining in the Utopia client (mining is available only for x64 client).
        As a parameter the Status (true/false) is specified, which turns on or off the mining process. In the Response
        field the status of completion of the operation is displayed."""
        return self.send_request('enableMining', {'enable': enabled})

    def enableInterest(self, enabled):
        """Calling the enableInterest method turns on and off the daily interest on the remaining irreducible account
        balance. As a parameter, one of the two statuses, true or false is selected. In the Response field the status
        of completion of turning on or off the operation is displayed."""
        return self.send_request('enableInterest', {'enable': enabled})

    def enableHistoryMining(self, enabled):
        """Calling the enableHistoryMining method changes the option of the automatic reading of the mining history
        from the financial server. As a parameter of the method, the status of true or false is specified. In the
        Response field the status of completion of turning on or off the operation is displayed."""
        return self.send_request('enableHistoryMining', {'enable': enabled})

    def statusHistoryMining(self):
        """Calling the statusHistoryMining method returns in the Response block the status of mining history poll.
        Method is called without using any parameters.
        Meaning of different states:
        0 = STATE_EMPTY
        1 = STATE_IN_PROGRESS
        2 = STATE_RECEIVED_RESPONSE"""
        return self.send_request('statusHistoryMining')

    def getMiningBlocks(self):
        """Method getMiningBlocks returns to the Response field the information about the mining blocks for
        which the reward has been paid. The method is called without using any parameters. """
        return self.send_request('getMiningBlocks')

    def getMiningInfo(self):
        """Method getMiningInfo returns statistics value of mining process."""
        return self.send_request('getMiningInfo')

    def getVouchers(self):
        """Method getVouchers returns to the Response field the information about existing vouchers as a list.
        The method is called without using any parameters. )."""
        return self.send_request('getVouchers')

    def createVoucher(self, amount):
        """Method createVoucher with the mandatory parameter 'amount' creates new voucher for the selected amount in
        the list of own vouchers. The amount for the vouchers is taken from the main account balance. Amount, which
        transfers the amount of transfer (the number needs to be greater than 0 and contain no more than
        9 character after coma); """
        return self.send_request('createVoucher', {'amount': amount})

    def useVoucher(self, voucherid):
        """Method useVoucher allows to use the selected voucher with adding its amount to your main account.
        The method is called with mandatory 'VoucherId' parameter in which the number of the voucher is specified."""
        return self.send_request('useVoucher', {'voucherid': voucherid})

    def deleteVoucher(self, voucherid):
        """Method deleteVoucher allows to remove your own voucher from the existing list with having the amount
        refunded back to your account. The method is called with mandatory 'VoucherId' parameter in which the
        number of the voucher is specified. In the Response field the status of
        completion of the operation is displayed."""
        return self.send_request('deleteVoucher', {'voucherid': voucherid})

    def getInvoices(self, cardId='', invoiceId='', pk='', transactionId='', status='', startDateTime='', endDateTime='',
                    referenceNumber=''):
        """Method getInvoices returns to the Response field the list of active invoiced.
        The method is called with using any optional parameters."""
        return self.send_request('getInvoices', {'cardId': cardId, 'invoiceId': invoiceId, 'pk': pk,
                                                 'transactionId': transactionId, 'status': status,
                                                 'startDateTime': startDateTime, 'endDateTime': endDateTime,
                                                 'referenceNumber': referenceNumber})

    def getInvoiceByReferenceNumber(self, referenceNumber):
        """Method getInvoiceByReferenceNumber allows to receive 'batchid' of the invoice using the ReferenceNumber.
        In the Response field, batchid is returned, which is considered a
        successful status for completion of the operation."""
        return self.send_request('getInvoiceByReferenceNumber', {'referenceNumber': referenceNumber})

    def getTransactionIdByReferenceNumber(self, referenceNumber):
        """Method getTransactionIdByReferenceNumber allows to receive 'batchid' of the transaction by using the
        ReferenceNumber. In the Response field, batchid is returned, which is considered a
        successful status for completion of the operation."""
        return self.send_request('getTransactionIdByReferenceNumber', {'referenceNumber': referenceNumber})

    def sendInvoice(self, cardid, amount, comment):
        """Method sendInvoice sends invoice (Request Cryptons) for deduction of specified amount from specified card.
        In the parameters of the method, the card number of the request recipient is specified (CardId). In the
        second parameter the 'Amount' is specified which transfers the amount of transfer (the number needs to be
        greater than 0 and contain no more than 9 character after coma), and the third parameter is optional, where
        'Comment is optional, which contains the text of the comment (up to 148 characters). """
        return self.send_request('sendInvoice', {'cardid': cardid, 'amount': amount, 'comment': comment})

    def acceptInvoice(self, invoiceid):
        """Method acceptInvoice performs payment of the incoming invoice. The method is called with mandatory
        'InvoiceId' parameter in which the ID of the invoice that needs to be rejected. For receiving ID of the needed
        invoice it is needed to call getInvoices for receiving the list of invoices with their detailed information.
        In response the acceptInvoice method returns in the Response block the results of completing this request. """
        return self.send_request('acceptInvoice', {'invoiceid': invoiceid})

    def declineInvoice(self, invoiceid):
        """Method declineInvoice sends request for declining the payment for the incoming invoice. The method is called
        with mandatory the 'InvoiceId' parameter. Parameter InvoiceId contains the ID value for the invoice that needs
        to be declined. To get the ID of the required invoice it is mandatory to call the getInvoices method for
        receiving the list of invoices with their detailed information. In response the declineInvoice method returns
        in the Response block the results of completing this request. """
        return self.send_request('declineInvoice', {'invoiceid': invoiceid})

    def cancelInvoice(self, invoiceid):
        """Method cancelInvoice allows to cancel the already created invoice. The method is called with mandatory
        'InvoiceId' parameter. Parameter InvoiceId contains the ID value for the invoice that needs to be declined.
        To get the ID of the required invoice it is mandatory to call the getInvoices method for receiving the list of
        invoices with their detailed information. In response the declineInvoice method returns in the Response block
        the results of completing this request. """
        return self.send_request('cancelInvoice', {'invoiceid': invoiceid})

    def requestUnsTransfer(self, name, hexNewOwnerPk):
        """Method requestUnsTransfer allows to transfer the uNS record to contact. The method is called with mandatory
        'Name' and 'Public Key' parameters. Name parameter is the name of the uNS record from the list of own uNS
        records. hexNewOwnerPk represents hash of the public portion of the key (as in some instances, key is now
        known, only hash is), to which the transfer is being made. In the Response field the status of completion
        of the operation is displayed. """
        return self.send_request('requestUnsTransfer', {'name': name, 'hexNewOwnerPk': hexNewOwnerPk})

    def acceptUnsTransfer(self, requestid):
        """Method acceptUnsTransfer allows to accept the incoming record of the uNS transfer. The method is called
        with the mandatory 'RequesId' parameter, which represents the id of the incoming uNS transfer. To receive
        the id of incoming transfers it is necessary to call the incomingUnsTransfer method, which returns the list
        of incoming uNS transfer. In the Response field the status of completion of the acceptUnsTransfer
        operation is displayed. """
        return self.send_request('acceptUnsTransfer', {'requestid': requestid})

    def declineUnsTransfer(self, requestid):
        """Method declineUnsTransfer allows to decline the incoming record of the uNS transfer. The method is called
        with the mandatory 'RequesId' parameter, which represents the id of the incoming uNS transfer. To receive the
        id of incoming transfers it is necessary to call the incomingUnsTransfer method, which returns the list of
        incoming uNS transfer. In the Response field the status of completion of the
        declineUnsTransfer operation is displayed. """
        return self.send_request('declineUnsTransfer', {'requestid': requestid})

    def incomingUnsTransfer(self):
        """Method incomingUnsTransfer returns in the Response field the list of all incoming uNS
        transfer records with their detailed information. The method is called without using any parameters."""
        return self.send_request('incomingUnsTransfer')

    def outgoingUnsTransfer(self):
        """Method outgoingUnsTransfer returns in the Response field the list of all outgoing uNS
        transfer records with their detailed information. The method is called without using any parameters."""
        return self.send_request('outgoingUnsTransfer')

    def storageWipe(self):
        """Attention! The method storageWipe irrevocably removes all databases of the user. The method is called
        without using any parameters. In the Response field the status of completion of the operation is displayed."""
        return self.send_request('storageWipe')

    def sendAuthorizationRequest(self, pk, message):
        """Method sendAuthorizationRequest allows to send the authorization request to add the user to the contact list.
        The method is called with mandatory use of 'Public Key' and 'Message' parameters. The Public Key parameter
        represents the Public Key of the person being added. The message parameter represents itself the text message
        with the request to be authorized. In the Response field the status of completion of
        sending such request is displayed."""
        return self.send_request('sendAuthorizationRequest', {'pk': pk, 'message': message})

    def acceptAuthorizationRequest(self, pk, message=''):
        """Method acceptAuthorizationRequest accepts the incoming authorization request to add user to contacts.
        The method is called with mandatory use of 'Public Key' and 'Message' parameters.
        The Public Key parameter represents the Public Key of the person who send the authorization request.
        The message parameter represents itself the text message.
        In the Response field the status of completion of sending such request is displayed."""
        return self.send_request('acceptAuthorizationRequest', {'pk': pk, 'message': message})

    def rejectAuthorizationRequest(self, pk, message):
        """Method rejectAuthorizationRequest declines the incoming authorization request from user with Public key,
        which is specified as first parameter (Public Key) of the rejectAuthorizationRequest method.
        The second parameter of the method is Message row, that represents itself the response message the user who`s
        authorization is rejected. In the Response field the status of completion of such request is displayed."""
        return self.send_request('rejectAuthorizationRequest', {'pk': pk, 'message': message})

    def deleteContact(self, pk):
        """Method deleteContact allows to perform the operation of removing selected user from the list of contacts.
        The method is called with mandatory use of 'Public Key' parameter that represents Public key of the to be
        removed contact. In the Response field the status of completion of such operation is displayed."""
        return self.send_request('deleteContact', {'pk': pk})

    def getChannels(self, filter='', channel_type=''):
        """Method getChannels returns in the Response field the current list of all channels of Utopia ecosystem,
        it is possible to search by name of the channel (partial or complete matching). As a parameter,
        a Filter can be specified, which can be used for searching of the channel by name
        ( has to contain full or partial matching of the channel name)."""
        return self.send_request('getChannels', {'filter': filter, 'channel_type': channel_type})

    def sendChannelMessage(self, channelid, message):
        """Method sendChannelMessage creates and sends message in the selected channel
        (to send the message the user should have joined this channel and needs to have status 'online').
        To enter the channel, use joinChannel method. As a parameter the method is using the ChannelId,
        which passes on the id of the channel in which the message is being sent
        (finding the id of the channel is possible by using the getChannels method) and Message,
        which contains the text of the message being sent.
        In the Response field the status of completion of the operation is displayed."""
        return self.send_request('sendChannelMessage', {'channelid': channelid, 'message': message})

    def sendChannelPicture(self, channelid, base64_image, filename_image):
        """Method sendChannelPicture creates and sends message with picture in base64 format"""
        return self.send_request('sendChannelPicture', {'channelid': channelid, 'base64_image': base64_image,
                                                        'filename_image': filename_image})

    def joinChannel(self, ChannelId, password=''):
        """Method joinChannel executes an entry into selected channel. The following parameters are specified:
        ChannelId, which passes on the id of the channel in which the message is being sent
        (finding the id of the channel is possible by using the getChannels method);
        when needed the parameter Password is specified, which passes on the password for entry into the channel
        (if left empty, no password is required).
        In the Response field the status of completion of the operation is displayed."""
        return self.send_request('joinChannel', {'ident': ChannelId, 'password': password})

    def leaveChannel(self, channelid):
        """Method leaveChannel executes the exit from the selected channel. As a parameter the method takes the
        ChannelId, which passes on the id of the channel in which the message is being sent
        (finding the id of the channel is possible by using the getChannels method ."""
        return self.send_request('leaveChannel', {'channelid': channelid})

    def getChannelMessages(self, channelid):
        """Method getChannelMessages returns in the Response block the history of communication from selected channel.
        The method is called by using the channelid parameter, that passes on id of channel."""
        return self.send_request('getChannelMessages', {'channelid': channelid})

    def getChannelInfo(self, channelid):
        """Method getChannelInfo returns in the Response field the information about the channel
        ( the response contains following parameters: HideInCommonList, description, geotag, hashtags, languages,
        readonly, title, type, private). As a parameter the method is using the ChannelId for which the user is trying
        to find more information (finding the id of the channel is possible by using the getChannels method)."""
        return self.send_request('getChannelInfo', {'channelid': channelid})

    def getChannelModerators(self, channelid):
        """Method getChannelModerators returns in the Response field the list of Public Keys of moderators.
        As a parameter the ChannelId is used
        (finding the id of the channel is possible by using the getChannels method)."""
        return self.send_request('getChannelModerators', {'channelid': channelid})

    def getChannelContacts(self, channelid):
        """Method getChannelContacts returns in the Response field the list of contacts on channel with details."""
        return self.send_request('getChannelContacts', {'channelid': channelid})

    def getChannelModeratorRight(self, channelid, moderator):
        """Method getChannelModeratorRight returns in the Response field the list of moderator rights in the channel
        ( the response contains parameters as ban, delete, promote).
        As a parameter the method uses: ChannelId from which it is needed to get the list of moderator rights
        (finding the id of the channel is possible by using the getChannels method)
        and Public Key of the channel moderator (finding Public Key(pk) of the channel moderator is possible by using
        the getChannelModerators method). """
        return self.send_request('getChannelModeratorRight', {'channelid': channelid, 'moderator': moderator})

    def createChannel(self, channel_name, description, read_only, password, language, hashtags, geoTag,
                      base64_avatar_image, hide_in_UI):
        """Method createChannel creates uchan record."""
        return self.send_request('createChannel', {'channel_name': channel_name, 'description': description,
                                                   'read_only': read_only, 'password': password,
                                                   'language': language, 'hashtags': hashtags, 'geoTag': geoTag,
                                                   'base64_avatar_image': base64_avatar_image,
                                                   'hide_in_UI': hide_in_UI})

    def modifyChannel(self, channelid, description, read_only, language, hashtags, geoTag,
                      base64_avatar_image, hide_in_UI):
        """Method modifyChannel changes uchan record properties."""
        return self.send_request('createChannel', {'channelid': channelid, 'description': description,
                                                   'read_only': read_only,'language': language, 'hashtags': hashtags,
                                                   'geoTag': geoTag, 'base64_avatar_image': base64_avatar_image,
                                                   'hide_in_UI': hide_in_UI})

    def deleteChannel(self, channelid):
        """Method deleteChannel deletes uchan record."""
        return self.send_request('deleteChannel', {'channelid': channelid})

    def getChannelSystemInfo(self):
        """Method getChannelSystemInfo returns system properties of channels."""
        return self.send_request('getChannelSystemInfo')

    def unsCreateRecordRequest(self, nick, valid, isPrimary, ChannelId):
        """Method unsCreateRecordRequest sends request for uNS name registration in the Utopia ecosystem for the
        selected term. As a parameter the uNS name is used (the name contains symbols (A-Z), numbers (0-9),
        dash symbol (-) and period (.) and can be no greater than 32 symbols in length.) and Valid (yyyy-mm-dd),
        which passes on the final date of the term for this name(uNS) (by default 6 months), isPrimary which specifies
        if the uNS Name is primary, and ChannelId, which passes on the id of the channel in which the message is being
        sent (finding the id of the channel is possible by using the getChannels method). In the Response field the
        status of completion of the operation is displayed."""
        return self.send_request('unsCreateRecordRequest', {'nick': nick, 'valid': valid, 'isPrimary': isPrimary,
                                                            'channelId': ChannelId})

    def unsModifyRecordRequest(self, nick, valid, isPrimary, ChannelId):
        """Method unsModifyRecordRequest sends request for uNS name registration in the Utopia ecosystem for the
        selected term. As a parameter the uNS name is used (the name contains symbols (A-Z), numbers (0-9),
        dash symbol (-) and period (.) and can be no greater than 32 symbols in length.) and Valid (yyyy-mm-dd),
        which passes on the final date of the term for this name(uNS) (by default 6 months). In the Response field the
        status of completion of the operation is displayed."""
        return self.send_request('unsCreateRecordRequest', {'nick': nick, 'valid': valid, 'isPrimary': isPrimary,
                                                            'channelId': ChannelId})

    def unsDeleteRecordRequest(self, nick):
        """Method unsDeleteRecordRequest sends request for deletion of uNS name of the current user. As a parameter
        the uNS name is used ( uNS name can be found by using the unsRegisteredNames method).
        In the Response field the status of completion of the operation is displayed."""
        return self.send_request('unsDeleteRecordRequest', {'nick': nick})

    def unsSearchByPk(self, filter):
        """Method unsSearchByPk returns in the Response field the list of all uNS names with selected 'Filter'
        parameter (contains full or partial matching with the searched uNS name. The name can contain symbols (A-Z),
        numbers (0-9), dash symbol (-) and period (.) and can be no greater than 32 symbols in length.)."""
        return self.send_request('unsSearchByPk', {'filter': filter})

    def unsSearchByNick(self, filter):
        """Method unsSearchByNick returns the list of uNS names by partial or full matching with selected 'Filter'
        parameter (contains full or partial matching with the searched uNS name. The name can contain symbols (A-Z),
        numbers (0-9), dash symbol (-) and period (.) and can be no greater than 32 symbols in length.)."""
        return self.send_request('unsSearchByPk', {'filter': filter})

    def getUnsSyncInfo(self):
        """Method getUnsSyncInfo returns statistics value of sync process."""
        return self.send_request('getUnsSyncInfo')

    def unsRegisteredNames(self):
        """Method unsRegisteredNames returns in the Response field the list of all registered uNS for current user.
        The method is called without using any parameters. """
        return self.send_request('unsRegisteredNames')

    def summaryUnsRegisteredNames(self, date_from, date_to):
        """Method summaryUnsRegisteredNames returns the list count of uNS names by each day"""
        return self.send_request('summaryUnsRegisteredNames', {'from_date': date_from, 'to_date': date_to})

    def clearTrayNotifications(self):
        """Method clearTrayNotifications allows to drop all existing notifications in the tray of the operating system.
        The method is called without using any parameters.
        In the Response field the status of completion of the operation is displayed."""
        return self.send_request('clearTrayNotifications')

    def getNetworkConnections(self):
        """Method getNetworkConnections returns in Response block detailed information about all current network
        connections. The method is called without using any parameters. """
        return self.send_request('getNetworkConnections')

    def getProxyMappings(self):
        """Method getProxyMappings returns in Response block the list of all configured proxy mappings.
        The method is called without using any parameters. """
        return self.send_request('getProxyMappings')

    def createProxyMapping(self, srcHost, srcPort, dstHost, dstPort, enabled):
        """Method createProxyMapping allows to create a 'bridge' type of connections to receive access to the external
        page by the specified ip address and port, when trying to call the inter-network address in the Utopia network
        ( usually used by Idyll browser). The method by using the mandatory parameters SrcHost,SrcPort,DstHost,DstPort,
        Enabled. The SrcHost parameters represents its own uNS name, the request of which would be executed in the
        Idyll browser. The SrcPort parameter represents the port number on which the mapping is planned to be located.
        Parameter DstHost represents itself the ip address of the page on which it will navigate, and parameters
        DstPort is the number of port on which the needed page with specified ip address is located.
        The Enabled parameter represents the activity of such connection as 'true' or 'false'.
        In the Response block the status of completion of the attempt to create a connection
        with specified parameters is displayed."""
        return self.send_request('createProxyMapping', {'srcHost': srcHost, 'srcPort': srcPort, 'dstHost': dstHost,
                                                        'dstPort': dstPort, 'enabled': enabled})

    def enableProxyMapping(self, mappingId):
        """Method enableProxyMapping allows to turn on the ability to use the connection with specified 'MappingId'
        as a parameter when calling this method. To receive the 'MappingId' of the needed connection it is necessary
        to call the getProxyMappings method. In the Response field the status of completion of
        operation of turning on the connection is displayed."""
        return self.send_request('enableProxyMapping', {'mappingId': mappingId})

    def disableProxyMapping(self, mappingId):
        """Method disableProxyMapping allows to turn off the ability to use the connection with specified 'MappingId'
        as a parameter when calling this method. To receive the 'MappingId' of the needed connection it is necessary to
        call the getProxyMappings method. In the Response field the status of completion of operation of
        turning off the connection is displayed."""
        return self.send_request('disableProxyMapping', {'mappingid': mappingId})

    def removeProxyMapping(self, mappingId):
        """Method removeProxyMapping allows to remove the selected configured of proxy mappings.
        The method is called by using the MapingId parameter, which represents the id of the configured proxy
        connection. In the Response field the status of completion of operation of removing the mapping is displayed."""
        return self.send_request('removeProxyMapping', {'mappingId': mappingId})

    def lowTrafficMode(self):
        """Method lowTrafficMode returns in Response block the status of low Traffic mode.
        The method is called without using any parameters. """
        return self.send_request('lowTrafficMode')

    def setLowTrafficMode(self, enabled):
        """Method setLowTrafficMode allows to turn on or off the low Traffic mode.
        The method is called by using the enabled parameter,
        which represents itself a status of true or false that is being set for this particular mode. """
        return self.send_request('setLowTrafficMode', {'enavled': enabled})

    def getWhoIsInfo(self, name_or_pk):
        """Method getWhoIsInfo returns in Response block the detailed information about selected user. As a parameter
        of the method, the Public key of the particular user can be used, or his nickname,
        if such contact was added to the contact list. """
        return self.send_request('getWhoIsInfo', {'owner': name_or_pk})

    def requestTreasuryInterestRates(self):
        """Method requestTreasuryInterestRates makes request to obtain treasury interest rate data"""
        return self.send_request('requestTreasuryInterestRates')

    def getTreasuryInterestRates(self):
        """Method getTreasuryInterestRates returns in Response block the detailed information about
        threasury interest rate"""
        return self.send_request('getTreasuryInterestRates')

    def requestTreasuryTransactionVolumes(self):
        """Method requestTreasuryTransactionVolumes makes request to obtain treasury transaction volume data"""
        return self.send_request('requestTreasuryTransactionVolumes')

    def getTreasuryTransactionVolumes(self):
        """Method getTreasuryTransactionVolumes returns in Response block the detailed
        information about threasury transaction volume"""
        return self.send_request('getTreasuryTransactionVolumes')

    def ucodeEncode(self, hex_code, size_image, coder, format):
        """Method ucodeEncode returns image of ucode in size_image with public key from hex_code"""
        return self.send_request('ucodeEncode', {'hex_code': hex_code, 'size_image': size_image, 'coder': coder,
                                                 'format': format})

    def ucodeDecode(self, base64_image):
        """Method ucodeDecode returns hex public key from image in base64 format."""
        return self.send_request('ucodeDecode', {'base64_image': base64_image})

    def getWebSocketState(self):
        """Method getWebSocketState returns WSS Notifications state, 0 - disabled or active listening port number."""
        return self.send_request('getWebSocketState')

    def setWebSocketState(self, enabled, port):
        """Method setWebSocketState set WSS Notification state."""
        return self.send_request('setWebSocketState', {'enabled': enabled, 'port': port})

    def getLastChannelMessage(self, channelid):
        return self.getChannelMessages(channelid)['result'][0]
