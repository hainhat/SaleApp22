from flask_admin import Admin, BaseView, expose, AdminIndexView
from flask_admin.contrib.sqla import ModelView
from models import Category, Product, UserEnum
from flask_login import current_user, logout_user
from flask import redirect

from saleapps2.saleapp import app, db, dao


class MyModelView(ModelView):
    def is_accessible(self):
        return current_user.is_authenticated and current_user.role == UserEnum.ADMIN


class MyBaseView(BaseView):
    def is_accessible(self):
        return current_user.is_authenticated


class MyCategoryView(MyModelView):
    column_list = ["name", "products"]


class MyProductView(MyModelView):
    column_list = ["name", "category_id", "image"]
    column_searchable_list = ["id", "name"]
    column_filters = ["id", "name"]
    can_export = True


class StatsView(MyBaseView):
    @expose('/')
    def index(self):
        return self.render("admin/stats.html")


class LogoutView(MyBaseView):
    @expose('/')
    def index(self):
        logout_user()
        return redirect('/admin')


class MyAdminIndexView(AdminIndexView):
    @expose('/')
    def index(self):
        stats = dao.count_product_by_cate()
        return self.render('admin/index.html', stats=stats)


admin = Admin(app=app, name="E-Commerce Administrator", template_mode="bootstrap4", index_view=MyAdminIndexView())

admin.add_view(MyCategoryView(Category, db.session))
admin.add_view(MyProductView(Product, db.session))
admin.add_view(StatsView(name="Thống kê"))
admin.add_view(LogoutView(name="Đăng xuất"))
