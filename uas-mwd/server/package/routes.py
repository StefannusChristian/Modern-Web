import os
from package import app, db
from flask import request, jsonify, send_from_directory
from package.models import User,Product, Invoice, InvoiceDetail, Category
import datetime
from werkzeug.security import check_password_hash
from sqlalchemy import text

@app.route('/login', methods=['POST'])
def login():
    if request.method == 'POST':
        data = request.get_json()
        username = data['username']
        password = data['password']

        if username and password:
            user = User.query.filter_by(user_name=username).first()

            if user:
                if check_password_hash(user.user_password, password):
                    data['message'] = 'login-success'
                    del data['password']
                    return data
                return {'message': 'invalid-credentials'}   
            return {'message': 'invalid-credentials'}
        return {'message': 'invalid-credentials'}
        

@app.route('/latest_invoice_no', methods=['GET'])
def latest_invoice_no():
    get_all_invoices = Invoice.query.all()
    if len(get_all_invoices) == 0:
        latest_invoice_no = 1
    else:
        latest_invoice_no = Invoice.query.all()[-1].invoice_id
    return {'invoice_no': latest_invoice_no}

@app.route('/save_invoice', methods=['POST'])
def save_invoice():
    content_type = request.headers.get('Content-Type')
    if (content_type == 'application/json'):
        product_list = request.json
        print(product_list)
        # POST data to Invoice Table
        user_id = User.query.filter_by(user_name=product_list['user_name']).first().user_id
        price_after_discount = product_list['price_after_diskon']
        the_discount = product_list['diskon']
        inv_date = datetime.date.today()
        new_invoice = Invoice(user_id,price_after_discount,the_discount,inv_date)
        db.session.add(new_invoice)
        db.session.commit()

        # POST data to Invoice Detail Table
        latest_invoice_id = Invoice.query.all()[-1].invoice_id
        for item in product_list['product_list']:
            new_invoice_detail = InvoiceDetail(latest_invoice_id,item['product_id'],item['product_qty'])
            db.session.add(new_invoice_detail)
        db.session.commit()
        return jsonify(product_list)
    else: return 'Content-Type not supported!'

@app.route('/report_sales', methods=['POST'])
def report_sales():
    if request.method == 'POST':
        data = request.get_json()["username"];
        if data:
            user = User.query.filter_by(user_name=data).first()
            user_id = user.user_id

            get_invoices = Invoice.query.filter_by(user_id=user_id).all()
            all_invoices = []
            invoice_details = {}

            for i in range(len(get_invoices)):
                all_invoices.append({
                    'invoice_id': get_invoices[i].invoice_id,
                    'user_id':get_invoices[i].user_id,
                    'total_price':get_invoices[i].total_price,
                    'total_discount':get_invoices[i].total_discount,
                    'invoice_date': str(get_invoices[i].invoice_date.date())[:-1]
                })
                invoice_detail_query = InvoiceDetail.query.filter_by(invoice_id=get_invoices[i].invoice_id).all()
                invoice_details[get_invoices[i].invoice_id] = []
                for j in range(len(invoice_detail_query)):
                    invoice_detail_item = {
                        "invoice_detail_id": invoice_detail_query[j].invoice_detail_id,
                        "invoice_id" : invoice_detail_query[j].invoice_id,
                        "product_name": Product.query.filter_by(product_id=invoice_detail_query[j].product_id).first().product_name,
                        "qty": invoice_detail_query[j].qty
                    }
                    invoice_details[get_invoices[i].invoice_id].append(invoice_detail_item)

            return {'invoices': all_invoices, 'user_id': user_id, 'invoice_details':invoice_details}

@app.route('/categories', methods=['GET'])
def categories():
    get_categories = Category.query.all()
    category_names = []
    for i in range(len(get_categories)):
        category_names.append({"category_id":get_categories[i].category_id,
        "category_name": get_categories[i].category_name
            })
    return jsonify(category_names)


@app.route('/categories/<category_id>', methods=['GET'])
def get_products(category_id):
    all_get_products = Product.query.filter_by(category_id=category_id).all()
    get_products_list = []

    for i in range(len(all_get_products)):
        get_products_list.append({
            'product_id': all_get_products[i].product_id,
            'category_id': all_get_products[i].category_id,
            'product_name': all_get_products[i].product_name,
            'product_price': all_get_products[i].product_price,
            'img_filepath': all_get_products[i].img_filepath,
        })
    return jsonify(get_products_list)

@app.route('/sales_per_category', methods=['POST'])
def sales_per_category():
    if request.method == 'POST':
        data = request.get_json()["username"];
        user = User.query.filter_by(user_name=data).first()
        user_id = user.user_id

        sql = text(f"SELECT *, SUM(invoice_detail.qty) as sum_qty FROM Invoice INNER JOIN Invoice_Detail ON Invoice.invoice_id = Invoice_Detail.invoice_id INNER JOIN Product ON Invoice_Detail.product_id = Product.product_id WHERE Invoice.user_id={user_id} GROUP BY invoice_detail.product_id;")

        result = db.engine.execute(sql)
        collect = []
        for x in result:
            cat_name = Category.query.filter_by(category_id=x[10]).first().category_name
            product_name = Product.query.filter_by(product_id=x[7]).first().product_name
            collect.append({
                "user_id": x[1],
                "product_name": product_name,
                "sum_qty": x[-1],
                "product_price":x[12],
                "category_id":x[10],
                "category_name": cat_name,
                "dis":x[3]
            })
        return jsonify(collect)
    

APP_ROOT = os.path.dirname(os.path.abspath(__file__))
app.config['UPLOADED_PHOTOS_DEST'] = os.path.join(APP_ROOT, 'images')

@app.route('/static/<filename>')
def get_file(filename):
    return send_from_directory(app.config['UPLOADED_PHOTOS_DEST'],filename)