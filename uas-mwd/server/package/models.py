from package import db
from werkzeug.security import generate_password_hash, check_password_hash

class User(db.Model):
    __tablename__ = 'user'
    user_id = db.Column('user_id',db.Integer, primary_key=True)
    user_name = db.Column(db.String(100))
    user_password = db.Column(db.String(128))
    
    def __init__ (self,username,password):
        self.user_name = username
        self.user_password = self.set_password(password)
    
    def __repr__(self): return '<User {}>'.format(self.user_name)

    def set_password(self, password): return generate_password_hash(password)

    def check_password(self, password): return check_password_hash(self.user_password, password)

class Invoice(db.Model):
    __tablename__ = 'invoice'
    invoice_id = db.Column('invoice_id',db.Integer, primary_key=True)
    user_id =  db.Column(db.Integer, db.ForeignKey('user.user_id'))
    total_price = db.Column(db.Float)
    total_discount = db.Column(db.Float)
    invoice_date = db.Column(db.DateTime)

    def __init__ (self, user_id,total_price,total_discount,invoice_date):
        self.user_id = user_id
        self.total_price = total_price
        self.total_discount = total_discount
        self.invoice_date = invoice_date


class InvoiceDetail(db.Model):
    __tablename__ = 'invoice_detail'
    invoice_detail_id = db.Column('invoice_detail_id',db.Integer, primary_key=True)
    invoice_id =  db.Column(db.Integer, db.ForeignKey('invoice.invoice_id'))
    product_id =  db.Column(db.Integer, db.ForeignKey('product.product_id'))
    qty = db.Column(db.Integer)

    def __init__ (self,invoice_id, product_id,qty):
        self.invoice_id = invoice_id
        self.product_id = product_id
        self.qty = qty


class Category(db.Model):
    __tablename__ = 'category'
    category_id = db.Column('category_id',db.Integer, primary_key=True)
    category_name = db.Column(db.String(100))

    def __init__ (self,category_name):
        self.category_name = category_name


class Product(db.Model):
    __tablename__ = 'product'
    product_id = db.Column('product_id',db.Integer, primary_key=True)
    category_id =  db.Column(db.Integer, db.ForeignKey('category.category_id'))
    product_name = db.Column(db.String(100))
    product_price = db.Column(db.Float)
    img_filepath = db.Column(db.String(255))

    def __init__ (self,category_id, product_name, product_price, img_filepath):
        self.category_id = category_id
        self.product_name = product_name
        self.product_price = product_price
        self.img_filepath = img_filepath




    
