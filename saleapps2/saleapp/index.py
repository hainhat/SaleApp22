from flask import render_template, request, redirect
import dao
from saleapp import app


@app.route("/")
def index():
    q = request.args.get("q")
    cate_id = request.args.get("category_id")
    products = dao.load_products(q, cate_id)
    return render_template("index.html", products=products)


@app.route("/products/<int:id>")
def product_details(id):
    product = dao.load_product_by_id(id);
    return render_template("product_details.html", product=product)


@app.context_processor
def common_attribute():
    return {
        "categories": dao.load_categories()
    }


@app.route("/login", methods=['get', 'post'])
def login():
    if request.method.__eq__('POST'):
        print(request.form)
        username=request.form.get('username')
        password=request.form.get('password')
        if username.__eq__('admin') and password.__eq__('123'):
            return redirect("/")

    return render_template("login.html")


if __name__ == '__main__':
    with app.app_context():
        app.run(debug=True)
