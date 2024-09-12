from flask import Flask, render_template, request, url_for,redirect
import pymysql

app = Flask(__name__)
conn = pymysql.connect(host='localhost',
                             user='root',
                             password='',
                             database='zorodb')

#.........................................Route connexion........................................................
@app.route('/')
def Connexion():
    return render_template("Connexion.html")


#.........................................Route Base........................................................

@app.route('/Base')
def Accueil():
    return render_template("./Base.html")



#.........................................Route produit........................................................

@app.route("/Liste_produit")
def Listproduit():
    cursor = conn.cursor(pymysql.cursors.DictCursor)
    s = "SELECT * FROM produit"
    cursor.execute(s)
    liste = cursor.fetchall()
    return render_template("/produit/Liste_produit.html", liste=liste)



@app.route("/Ajout_produit", methods = ['GET', 'POST'])
def Ajoutproduit():
    if request.method=="POST":
        NomProduit = request.form.get('NomProduit')
        CatProduit = request.form.get('CatProduit')
        PrixUnitaire = request.form.get('PrixUnitaire')
        cursor = conn.cursor(pymysql.cursors.DictCursor)
        cursor.execute("insert into produit (NomProduit, CatProduit, PrixUnitaire)  values (%s,%s,%s)", (NomProduit, CatProduit, PrixUnitaire))
        conn.commit()
        cursor.close()
        return redirect(url_for('Listproduit'))
    return render_template("/produit/Ajout_produit.html")

#Route de modifier produit

@app.route("/Modifif_produit/<string:id>",methods=["GET","POST"])
def Modifier(id):
    conn = pymysql.connect(host='localhost',
                           user='root',
                           password='',
                           database='zorodb')
    cursor = conn.cursor()
    cursor.execute("SELECT *FROM produit WHERE IdProduit=%s", (id,))
    Prod=cursor.fetchone()
    cur = conn.cursor()
    cur.execute("SELECT  * FROM produit GROUP BY CatProduit")
    list = cur.fetchall()
    if request.method == 'POST':
        id = request.form['id']
        Nom = request.form['NomProduit']
        Categorie = request.form['CatProduit']
        Prix = request.form['PrixUnitaire']

        cursor = conn.cursor()
        sql = "UPDATE produit SET  NomProduit=%s, CatProduit=%s, PrixUnitaire=%s WHERE IdProduit=%s"
        cursor.execute(sql, (Nom, Categorie, Prix, id))
        conn.commit()
        cursor.close()
        print(id)
        return redirect(url_for('Listproduit'))
    return render_template("./produit/Modifproduit.html", data = Prod, list = list)

#Route supprimer produit

@app.route("/sup_msg/<int:id>",methods=["GET", "POST"])
def delete_msg(id):
    conn = pymysql.connect(host='localhost',
                           user='root',
                           password='',
                           database='zorodb')
    cursor = conn.cursor()
    cursor.execute("select * from produit where IdProduit=%s", (id,))
    id_prod = cursor.fetchone()
    cursor.close()
    return render_template("./produit/Sup_produit.html", id_prod=id_prod)

@app.route("/sup_produit/<int:id>")
def delete_prod(id):
    conn = pymysql.connect(host='localhost',
                           user='root',
                           password='',
                           database='zorodb')
    cursor = conn.cursor()
    cursor.execute("DELETE FROM Produit WHERE IdProduit=%s", (id,))
    conn.commit()
    cursor.close()
    conn.close()
    return redirect('/Liste_produit')




#..........................................Magasin........................................................................

@app.route("/Liste_magasin")
def Listmagasin():
    cursor = conn.cursor(pymysql.cursors.DictCursor)
    cursor.execute("SELECT * FROM magasin")
    listemag = cursor.fetchall()
    return render_template("/magasin/Liste_magasin.html", listemag=listemag)



@app.route("/Ajout_magasin", methods=['POST', 'GET'])
def Ajoutmagasin():
    if request.method=="POST":
        NomMagasin = request.form.get('NomMagasin')
        AdresseMagasin = request.form.get('AdresseMagasin')
        Telephone = request.form.get('Telephone')
        mail = request.form.get('mail')
        cursor = conn.cursor(pymysql.cursors.DictCursor)
        cursor.execute("insert into magasin (NomMagasin, AdresseMagasin, Telephone, mail)  values (%s,%s,%s,%s)", (NomMagasin, AdresseMagasin, Telephone, mail))
        conn.commit()
        cursor.close()
        return redirect(url_for('Listmagasin'))
    return render_template("./magasin/Ajout_magasin.html")



#..........................................Route supprimer magasin...................................

@app.route("/sup_msgmag/<int:id>",methods=["GET", "POST"])
def delete_msgmag(id):
    conn = pymysql.connect(host='localhost',
                           user='root',
                           password='',
                           database='zorodb')
    cursor = conn.cursor()
    cursor.execute("select * from magasin where IdMagasin=%s", (id,))
    id_mag = cursor.fetchone()
    cursor.close()
    return render_template("./magasin/Sup_magasin.html", id_mag=id_mag)

@app.route("/sup_magasin/<int:id>")
def delete_mag(id):
    conn = pymysql.connect(host='localhost',
                           user='root',
                           password='',
                           database='zorodb')
    cursor = conn.cursor()
    cursor.execute("DELETE FROM magasin WHERE IdMagasin=%s", (id,))
    conn.commit()
    cursor.close()
    conn.close()
    return redirect('/Liste_magasin')

#................................................Route modifier magasin..............................................

@app.route("/Modif_magasin/<string:id>",methods=["GET","POST"])
def Modifiermag(id):
    conn = pymysql.connect(host='localhost',
                           user='root',
                           password='',
                           database='zorodb')
    cursor = conn.cursor()
    cursor.execute("SELECT *FROM magasin WHERE IdMagasin=%s", (id,))
    Mag=cursor.fetchone()
    if request.method == 'POST':
        IdMagasin = request.form['IdMagasin']
        NomMagasin = request.form['NomMagasin']
        AdresseMagasin = request.form['AdresseMagasin']
        Telephone = request.form['Telephone']
        mail = request.form['mail']

        cursor = conn.cursor()
        sql = "UPDATE magasin SET  NomMagasin=%s, AdresseMagasin=%s, Telephone=%s, mail=%s WHERE IdMagasin=%s"
        cursor.execute(sql, (NomMagasin, AdresseMagasin, Telephone, mail, IdMagasin))
        conn.commit()
        cursor.close()
        print(id)
        return redirect(url_for('Listmagasin'))
    return render_template("./magasin/Modif_magasin.html", data = Mag)


#..........................................Stock........................................................................

@app.route("/Liste_stock")
def Liststock():
    # Exemple de requête SQL pour récupérer un produit spécifique en fonction de l'ID
    cursor = conn.cursor(pymysql.cursors.DictCursor)
    cursor.execute("SELECT Idstock, NomMagasin,NomProduit, Quantitestock FROM stock S JOIN produit P ON S.IdProduit=P.IdProduit JOIN magasin M ON S.IdMagasin=M.IdMagasin")
    stock = cursor.fetchall()
    cursor.close()
    return render_template("./stock/Liste_stock.html", stock=stock)

#............................Ajouter Stock................................................

@app.route("/Ajout_stock", methods=['GET', 'POST'])
def Ajoutstock():
    cursor = conn.cursor(pymysql.cursors.DictCursor)
    # je récupère la liste des produits
    cursor = conn.cursor(pymysql.cursors.DictCursor)
    cursor.execute("SELECT NomProduit, IdProduit FROM produit ")
    listeprode = cursor.fetchall()
    conn.commit()

    # je récupère la liste des magasins
    cursor = conn.cursor(pymysql.cursors.DictCursor)
    cursor.execute("SELECT NomMagasin, IdMagasin FROM magasin ")
    listemage = cursor.fetchall()
    conn.commit()
    if request.method == 'POST':
        #Récupération des données du formulaire si la methode est POST
        IdMagasin = request.form['IdMagasin']
        IdProduit = request.form['IdProduit']
        Quantitestock = request.form['Quantitestock']
        # Traitement des données en creant une liste
        liste = {
            "IdMagasin": IdMagasin,
            "IdProduit": IdProduit,
            "Quantitestock": Quantitestock,
        }
        # Exécution de la requête d'insertion
        cursor = conn.cursor(pymysql.cursors.DictCursor)
        cursor.execute(
            f"INSERT INTO Stock (IdMagasin, IdProduit, Quantitestock) VALUES ('{liste['IdMagasin']}', '{liste['IdProduit']}', '{liste['Quantitestock']}')"
        )
        # Commit des modifications
        cursor.connection.commit()
        cursor = conn.cursor(pymysql.cursors.DictCursor)
        cursor.execute("SELECT Idstock, IdMagasin, IdProduit, Quantitestock FROM Stock ")
        liste = cursor.fetchall()
        # Commit des modifications
        cursor.connection.commit()
        return redirect(url_for('Liststock', liste=liste))
    return render_template("./stock/Ajout_stock.html", listeprode=listeprode, listemage=listemage)

#............................Supprimer Stock................................................

@app.route("/sup_msgstock/<int:id>",methods=["GET", "POST"])
def delete_msgstock(id):
    conn = pymysql.connect(host='localhost',
                           user='root',
                           password='',
                           database='zorodb')
    cursor = conn.cursor()
    cursor.execute("select * from stock where Idstock =%s", (id,))
    id_stock = cursor.fetchone()
    cursor.close()
    return render_template("./stock/Sup_stock.html", id_stock=id_stock)

@app.route("/sup_stock/<int:id>")
def delete_stock(id):
    conn = pymysql.connect(host='localhost',
                           user='root',
                           password='',
                           database='zorodb')
    cursor = conn.cursor()
    cursor.execute("DELETE FROM stock WHERE Idstock=%s", (id,))
    conn.commit()
    cursor.close()
    conn.close()
    return redirect('/Liste_stock')

#............................Modifier Stock................................................

@app.route("/Modif_stock/<string:id>",methods=["GET","POST"])
def Modifierstock(id):
    conn = pymysql.connect(host='localhost',
                           user='root',
                           password='',
                           database='zorodb')
    cursor = conn.cursor()
    cursor.execute("SELECT *FROM stock WHERE Idstock=%s", (id,))
    Stck=cursor.fetchone()
    if request.method == 'POST':
        IdMagasin = request.form['IdMagasin']
        NomMagasin = request.form['NomMagasin']
        AdresseMagasin = request.form['AdresseMagasin']
        Telephone = request.form['Telephone']
        mail = request.form['mail']

        cursor = conn.cursor()
        sql = "UPDATE magasin SET  NomMagasin=%s, AdresseMagasin=%s, Telephone=%s, mail=%s WHERE IdMagasin=%s"
        cursor.execute(sql, (NomMagasin, AdresseMagasin, Telephone, mail, IdMagasin))
        conn.commit()
        cursor.close()
        print(id)
        return redirect(url_for('Liststock'))
    return render_template("./stock/Modif_stock.html", data = Stck)


if __name__== '__main__':
    app.run(debug=True)