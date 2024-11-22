import math

from flask import render_template, request, redirect
import dao

from saleapps2.saleapp import app


@app.route("/")
def index():
    q = request.args.get("q")
    cate_id = request.args.get("category_id")
    page = request.args.get("page")
    pages = dao.count_product()
    products = dao.load_products(q=q, cate_id=cate_id, page=page)
    return render_template("index.html", products=products, pages=math.ceil(pages / app.config["PAGE_SIZE"]))


@app.route("/products/<int:id>")
def product_details(id):
    product = dao.load_product_by_id(id)
    return render_template("product_details.html", product=product)


@app.context_processor
def common_attribute():
    return {
        "categories": dao.load_categories()
    }


@app.route("/login", methods=['get', 'post'])
def login():
    err_msg = None
    if request.method.__eq__('POST'):
        print(request.form)
        username = request.form.get('username')
        password = request.form.get('password')
        user = dao.auth_user(username=username, password=password)
        if user:
            return redirect("/")
        else:
            err_msg = "Tài khoản hoặc mật khẩu không đúng"

    return render_template("login.html",err_msg=err_msg)


if __name__ == '__main__':
    with app.app_context():
        app.run(debug=True)
