from sqlalchemy import Column, String, Integer, Float, ForeignKey, Boolean
from saleapps2.saleapp import db, app
from sqlalchemy.orm import relationship


class Category(db.Model):
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(100), nullable=True)
    products = relationship('Product', backref="category", lazy=True)

    def __str__(self):
        return self.name


class Product(db.Model):
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50), unique=True, nullable=False)
    price = Column(Float, default=0)
    image = Column(String(300),
                   default='https://res.cloudinary.com/dy1unykph/image/upload/v1729842193'
                           '/iPhone_15_Pro_Natural_1_ltf9vr.webp')
    active = Column(Boolean, default=True)
    category_id = Column(Integer, ForeignKey(Category.id), nullable=True)

    def __str__(self):
        return self.name


class User(db.Model):
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50))
    username = Column(String(50), unique=True, nullable=False)
    password = Column(String(50), nullable=False)
    active = Column(Boolean, default=True)
    avatar = Column(String(300),
                    default='https://res.cloudinary.com/dy1unykph/image/upload/v1729842193/iPhone_15_Pro_Natural_1_ltf9vr.webp')

    def __str__(self):
        self.name


if __name__ == "__main__":
    with app.app_context():
        # db.create_all()
        # c1 = Category(name="Mobile")
        # c2 = Category(name="Tablet")
        # c3 = Category(name="Laptop")
        # db.session.add_all([c1, c2, c3])
        # import json
        #
        # with open('data/products.json', encoding='utf-8') as f:
        #     products = json.load(f)
        #     for p in products:
        #         prod = Product(**p)
        #         db.session.add(prod)
        #
        import hashlib

        password = str(hashlib.md5("123".encode('utf-8')).hexdigest())

        u = User(name='Nhat', username='user', password=password)
        db.session.add(u)
        db.session.commit()
