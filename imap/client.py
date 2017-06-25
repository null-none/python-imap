import imaplib

class ImapClient(object):

    def __init__(self, email, password):
        self.email = email
        self.password = password
        self.mail = imaplib.IMAP4_SSL('imap.mail.ru')

    def unread(self):
        self.mail.login(self.email, self.password)
        self.mail.list()
        self.mail.select("inbox")
        result, data = self.mail.search(None, "(UNSEEN)")
        return data

    def all(self):
        self.mail.login(self.email, self.password)
        self.mail.list()
        self.mail.select("inbox")
        result, data = self.mail.search(None, "ALL")
        return data

    def read(self):
        self.mail.login(self.email, self.password)
        self.mail.list()
        self.mail.select("inbox")
        result, data = self.mail.search(None, "(SEEN)")
        return data

    def message(self, item):
        result, data = self.mail.fetch(item, "(BODY[HEADER.FIELDS (SUBJECT FROM)])")
        return data

    def flag_read(self, item):
        self.mail.store(item, '+FLAGS', '\Seen')
        return True

    def flag_unread(self, item):
        self.mail.store(item, '-FLAGS', '\Seen')
        return True
