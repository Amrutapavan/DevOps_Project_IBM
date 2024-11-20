class Account:
    def __init__(self, id, name, email, address="", phone_number=""):
        self.id = id
        self.name = name
        self.email = email
        self.address = address
        self.phone_number = phone_number

    def serialize(self):
        return {
            'id': self.id,
            'name': self.name,
            'email': self.email,
            'address': self.address,
            'phone_number': self.phone_number
        }