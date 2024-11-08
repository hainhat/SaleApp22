from sqlalchemy import Column, String, Integer
from saleapp import db, app


class Category(db.Model):
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(100), nullable=True)

    def __str__(self):
        return self.name


if __name__ == "__main__":
    with app.app_context():
        # db.create_all()
        c1 = Category(name="Mobile")
        c2 = Category(name="Tablet")
        c3 = Category(name="Laptop")
        db.session.add_all([c1, c2, c3])
        db.session.commit()
