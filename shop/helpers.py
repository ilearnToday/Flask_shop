import random
from shop import db
from shop.models import Menu, Computers


class Computer:
    computers = 1

    def __init__(self):
        self.name = "Model: MacBook {}".format(self.computers)
        self.price = random.randint(20000, 30000)
        self.currency = '₽'
        self.disk_size = "Disk size:{} Gb".format(random.randint(128, 512))
        self.weight = "Weight: {}".format(random.randrange(1, 3))
        self.memory_size = "RAM memory size: {}".format(4, 32)
        self.display_size = "Display size: {}".format(random.randint(10, 20))
        self.img_link = 'img/{}.jpeg'.format(self.computers)
        self.page_link = '/product/{}'.format(self.computers)
        Computer.computers += 1

    @classmethod
    def generate_n_computers(cls, number_of_computers):
        computers = []
        for i in range(number_of_computers):
            computers.append(cls())
        return computers


def create_db():
    db.drop_all()
    db.create_all()


def fill_db():
    for item in {"description", "stats", "modifications", "prices", "reviews", "discussions"}:
        menu_item = Menu(name=item)
        db.session.add(menu_item)

    computers = Computer.generate_n_computers(5)
    for cmp in computers:
        computer = Computers(name=cmp.name,
                             price=cmp.price,
                             currency=cmp.currency,
                             page_link=cmp.page_link,
                             img_file=cmp.img_link
                             )
        db.session.add(computer)
    db.session.commit()