"""
Object Oriented Programming:
"""
# Classes and Objects:
class Contact:
    pass

wmc = Contact()

class Contact:
    # construct
    def __init__(self, cellphone, email):
        self.cellphone = cellphone
        self.email=email

    def getCellphone(self): # self: means the class instance (object)
        print("cellphone: ", self.cellphone)

    def getEmail(self):
        print("email: ", self.email)

    def getContactInformation(self):
        contactInfo = '''
        Contact information:
        - Cellphone: %s
        - Email: %s 
        '''
        print(contactInfo%(self.cellphone, self.email))

contact = Contact("31321513", "wmc@email.domain")
contact.getCellphone()
contact.getEmail()
Contact.getCellphone(contact)
Contact.getEmail(contact)

contact.getContactInformation();

"""
Inheritance:
"""
class TelemarketingContact(Contact):
    def __init__(self, id):
        self.identifier = id

    def getContactInformation(self):
        telemarketingContactInfo = '''
        Contact information:
        - Id: %s
        - Cellphone: %s
        - Email: %s 
        '''
        print(telemarketingContactInfo%(self.identifier, self.cellphone, self.email))

telemarketingContact = TelemarketingContact("1154","5842151","other@emai.domain")
telemarketingContact.getContactInformation()