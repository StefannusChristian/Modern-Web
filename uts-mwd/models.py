from app import app,db


class Customer(db.Model):
    __tablename__ = 'customer'
    cust_id = db.Column('cust_id',db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    address = db.Column(db.Text)
    phone = db.Column(db.String(100))
    
    invoices = db.relationship('Invoice',backref='invoice')
    
    def __init__ (self,name,address,phone):
        self.name = name
        self.address = address
        self.phone = phone

class Invoice(db.Model):
    __tablename__ = 'invoice'
    inv_id = db.Column('inv_id',db.Integer, primary_key=True)
    cust_id =  db.Column(db.Integer, db.ForeignKey('customer.cust_id'))
    date = db.Column(db.DateTime)
    amount = db.Column(db.Float)
    remark = db.Column(db.Text)
    status = db.Column(db.Boolean)
    
    def __init__ (self,cust_id,date,amount,remark,status):
        self.cust_id = cust_id
        self.date = date
        self.amount = amount 
        self.remark = remark
        self.status = status

class User(db.Model):
    __tablename__ = 'user'
    user_id = db.Column('user_id',db.Integer, primary_key=True)
    username = db.Column(db.String(100))
    password = db.Column(db.Text)
    role = db.Column(db.String(20))
    
    def __init__ (self,username,password,role):
        self.username = username
        self.password = password
        self.role = role
        
