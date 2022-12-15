from package import app, db
from package.models import User, Invoice, InvoiceDetail, Category, Product

@app.shell_context_processor
def make_shell_context(): return {
    'db': db, 
    'User': User,
    'Invoice': Invoice,
    'InvoiceDetail': InvoiceDetail,
    'Category': Category,
    'Product': Product
    }
