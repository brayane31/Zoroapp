from flask import Flask, render_template, request, url_for,redirect
import pymysql

app = Flask(__name__)
conn = pymysql.connect(host='localhost',
                             user='root',
                             password='',
                             database='zorodb')

@app.route('/')
def Connexion():
    return render_template("Connexion.html")



@app.route('/Base')
def Accueil():
    return render_template("./Base.html")




@app.route("/Liste_produit")
def Listproduit():
    cursor = conn.cursor(pymysql.cursors.DictCursor)
    s = "SELECT * FROM produit"
    cursor.execute(s)
    liste = cursor.fetchall()
    return render_template("/produit/Liste_produit.html", liste=liste)



@app.route("/Ajout_produit", methods = ['GET', 'POST'])
def Ajoutproduit():
    conn = pymysql.connect(host='localhost',
                           user='root',
                           password='',
                           database='zorodb')
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

@app.route("/delete_msg/<int:id>",methods=["GET", "POST"])
def delete_msg(id):
    conn = pymysql.connect(host='localhost',
                           user='root',
                           password='',
                           database='zorodb')
    cursor = conn.cursor()
    cursor.execute("select * from produit where IdProduit=%s", (id,))
    id_prod = cursor.fetchone()
    cursor.close()
    return render_template("./produit/Delete_produit.html", id_prod=id_prod)

@app.route("/delete_produit/<int:id>")
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


@app.route("/Comfirmer_produit")
def valproduit():
    cursor = conn.cursor()
    s = "SELECT * FROM Produit"
    cursor.execute(s)
    liste = cursor.fetchall()
    return render_template("/produit/Liste_produit.html", liste=liste)






@app.route("/Valmoproduit")
def Moproduit():
    cursor = conn.cursor(pymysql.cursors.DictCursor)
    s = "SELECT * FROM produit"
    cursor.execute(s)
    liste = cursor.fetchall()
    return render_template("/produit/ModifValproduit.html", liste=liste)

if __name__== '__main__':
    app.run(debug=True)