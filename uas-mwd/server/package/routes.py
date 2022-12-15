import os
from package import app, db
from flask import render_template, redirect, request, url_for, session, jsonify, send_from_directory
from package.models import User, Product

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
            'img_filepath': all_pakaian[i].img_filepath,
        })
    return jsonify(pakaian_list)
    
@app.route('/makanan', methods=['GET'])
def makanan():
    all_makanan = Product.query.filter_by(category_id=2).all()
    makanan_list = []

    for i in range(len(all_makanan)):
        makanan_list.append({
            'product_id': all_makanan[i].product_id,
            'category_id': all_makanan[i].category_id,
            'product_name': all_makanan[i].product_name,
            'product_price': all_makanan[i].product_price,
            'img_filepath': all_makanan[i].img_filepath,
        })
    return jsonify(makanan_list)
    
@app.route('/alat_tulis', methods=['GET'])
def alat_tulis():
    all_alat_tulis = Product.query.filter_by(category_id=3).all()
    alat_tulis_list = []

    for i in range(len(all_alat_tulis)):
        alat_tulis_list.append({
            'product_id': all_alat_tulis[i].product_id,
            'category_id': all_alat_tulis[i].category_id,
            'product_name': all_alat_tulis[i].product_name,
            'product_price': all_alat_tulis[i].product_price,
            'img_filepath': all_alat_tulis[i].img_filepath,
        })
    return jsonify(alat_tulis_list)

APP_ROOT = os.path.dirname(os.path.abspath(__file__))
app.config['UPLOADED_PHOTOS_DEST'] = os.path.join(APP_ROOT, 'images')

@app.route('/static/<filename>')
def get_file(filename):
    return send_from_directory(app.config['UPLOADED_PHOTOS_DEST'],filename)