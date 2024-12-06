from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView
from models import Category, Product

from saleapps2.saleapp import app, db

admin = Admin(app=app, name="E-Commerce Administrator", template_mode="bootstrap4")


class MyCategoryView(ModelView):
    column_list = ["name", "products"]


class MyProductView(ModelView):
    column_list = ["name", "category_id", "image"]
    column_searchable_list = ["id", "name"]
    column_filters = ["id", "name"]
    can_export = True


admin.add_view(MyCategoryView(Category, db.session))
admin.add_view(MyProductView(Product, db.session))
