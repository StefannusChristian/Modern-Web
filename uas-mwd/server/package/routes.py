from package import app, db
from flask import render_template, redirect, request, url_for, session, jsonify
from package.models import User, Product

@app.route('/', methods=['GET'])
def index():
    all_products = Product.query.all()
    product_list = []

    for i in range(len(all_products)):
        product_list.append({
            'product_id': all_products[i].product_id,
            'category_id': all_products[i].category_id,
            'product_name': all_products[i].product_name,
            'product_price': all_products[i].product_price,
        })
    return jsonify(product_list)

@app.route('/pakaian', methods=['GET'])
def pakaian():
    all_pakaian = Product.query.filter_by(category_id=1).all()
    pakaian_list = []

    for i in range(len(all_pakaian)):
        pakaian_list.append({
            'product_id': all_pakaian[i].product_id,
            'category_id': all_pakaian[i].category_id,
            'product_name': all_pakaian[i].product_name,
            'product_price': all_pakaian[i].product_price,
        })
    return jsonify(pakaian_list)
    
@app.route('/login', methods=['POST', 'GET'])
def login():
    # if session.get("username"):
    #     return redirect(url_for('index'))

    title = 'Login'

    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')

        # If username or password is empty
        if not (username and password):
            return render_template('login.html')
        
        # If username and password is not empty (proceed)
        user_is_found = User.query.filter_by(username=username).first()

        # If user exists in database
        if user_is_found:
            pass_is_valid = user_is_found.check_password(password)

            if pass_is_valid:
                session['username'] = username
                session['role'] = user_is_found.role

                return redirect(url_for(session['role']))

    return render_template('login.html', title=title)

@app.route('/logout')
def logout():
    session["username"] = None
    return redirect(url_for('login'))

