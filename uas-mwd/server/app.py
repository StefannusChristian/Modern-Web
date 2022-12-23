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

def reset_tables():
    with app.app_context():
        db.drop_all()
        db.session.commit()
        db.create_all()
        db.session.commit()

def create_tables():
    with app.app_context():
        user1 = User("user1","123")
        user2 = User("user2","123")
        db.session.add(user1)
        db.session.add(user2)

        pakaian = Category("Pakaian")
        makanan = Category("Makanan")
        alat_tulis = Category("Alat Tulis")
        db.session.add(pakaian)
        db.session.add(makanan)
        db.session.add(alat_tulis)

        kaos = Product(1,"kaos",75900,"static/images/pakaian/kaos.jpeg")
        hoodie = Product(1,"hoodie",257999,"static/images/pakaian/hoodie.jpeg")
        sweater = Product(1,"sweater",149999,"static/images/pakaian/sweater.jpeg")
        kaos_kaki = Product(1,"kaos kaki",149999,"static/images/pakaian/kaos_kaki.jpg")
        kemeja = Product(1,"kemeja",149999,"static/images/pakaian/kemeja.jpg")
        jogging_pants = Product(1,"jogging pants",149999,"static/images/pakaian/jogging_pants.jpg")

        db.session.add(kaos)
        db.session.add(hoodie)
        db.session.add(sweater)
        db.session.add(kaos_kaki)
        db.session.add(kemeja)
        db.session.add(jogging_pants)

        kripik_kentang =  Product(2,"kripik_kentang",10000,"static/images/makanan/keripik_kentang.jpeg")
        krupuk_udang = Product(2,"krupuk_udang",9750,"static/images/makanan/kerupuk_udang.jpeg")
        oreo = Product(2,"oreo",8000,"static/images/makanan/oreo.jpeg")
        chitato = Product(2,"chitato",15999,"static/images/makanan/chitato.jpg")
        indomie = Product(2,"indomie",5000,"static/images/makanan/indomie.jpg")
        popcorn = Product(2,"popcorn",15500,"static/images/makanan/popcorn.jpeg")

        db.session.add(kripik_kentang)
        db.session.add(krupuk_udang)
        db.session.add(oreo)
        db.session.add(chitato)
        db.session.add(indomie)
        db.session.add(popcorn)

        pensil = Product(3,"pensil",5000,"static/images/alat_tulis/pencil.jpeg")
        penghapus = Product(3,"penghapus",3000,"static/images/alat_tulis/penghapus.jpeg")
        penggaris = Product(3,"penggaris",10000,"static/images/alat_tulis/penggaris.jpeg")
        gunting = Product(3,"gunting",7500,"static/images/alat_tulis/gunting.jpeg")
        rautan = Product(3,"rautan",6780,"static/images/alat_tulis/rautan.jpeg")
        pena = Product(3,"pena",20000,"static/images/alat_tulis/pena.jpeg")

        db.session.add(pensil)
        db.session.add(penghapus)
        db.session.add(penggaris)
        db.session.add(gunting)
        db.session.add(rautan)
        db.session.add(pena)

        # teknologi = Category("Laptop")
        # db.session.add(teknologi)
        # laptop = Product(4,"laptop",5000000,"")
        # db.session.add(laptop)


        db.session.commit()

if __name__ == '__main__':
    reset_tables()
    create_tables()
    app.run(port=5000, debug=True, threaded=False)