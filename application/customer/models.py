from application import db

class Customer(db.Model):
    number = db.Column(db.Integer, primary_key=True)
    date_created = db.Column(db.DateTime, default=db.func.current_timestamp())
    date_modified = db.Column(db.DateTime, default=db.func.current_timestamp(),
    onupdate=db.func.current_timestamp())

    name = db.Column(db.String(144), nullable=False)
    address = db.Column(db.String(255))

    def __init__(self, name, address):
        self.name = name
        self.address = address