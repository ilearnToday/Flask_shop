from shop import db


class Menu(db.Model):
    id = db.Column(db.Integer, primary_key=True, unique=True)
    name = db.Column(db.String(20), nullable=False, unique=True)

    def __repr__(self):
        return f"Menu item:({self.id}, {self.name})"


class Computers(db.Model):
    id = db.Column(db.Integer, primary_key=True, unique=True)
    name = db.Column(db.String(30), nullable=False)
    model = db.Column(db.String(30), nullable=True)
    price = db.Column(db.Float, nullable=False)
    currency = db.Column(db.String(2), nullable=False)
    disk_size = db.Column(db.String(50))
    weight = db.Column(db.Float)
    ram_size = db.Column(db.Integer)
    display_size = db.Column(db.Integer)
    img_file = db.Column(db.String(50), nullable=False, default='default.jpg')
    page_link = db.Column(db.String(50), nullable=False)

    def _repr__(self):
        return f"Computer('{self.id}', '{self.name}')"
