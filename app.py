import os
from flask import Flask
import os
from flask import Flask, render_template as template, session, url_for, request, redirect
app = Flask(__name__)
app.secret_key = os.urandom(8)
vorur = [
    [0,"Bolur","bolur.png",2000],
    [1,"Skyrta","skyrta.png",4000],
    [2,"Húfa","hufa.png",2300],
    [3,"Vettlingar","vettlingar.png",2500],
    [4,"Buxur","buxur.png",4100]
]
@app.route('/')
def home(): # Importaði render_template sem "template" fyrir þægindi
    karfa = []
    fjoldi = 0
    if "karfa" in session:
        karfa = session["karfa"]
        fjoldi = len(karfa)
    return template("index.html", vorur = vorur, fjoldi = fjoldi)
@app.route("/karfa")
def karfa():
    karfa = []
    summa = 0
    if "karfa" in session:
        karfa = session["karfa"]
        fjoldi = len(karfa) # Fj vara í körfu
        for i in karfa:
            summa += int(i[3])
        print(karfa)    
        return template("karfa.html",karfa = karfa, tom = False, fjoldi=fjoldi, summa = summa)

    else:
        return template("karfa.html", karfa = karfa, tom = True)
@app.route("/add/<int:id>")
def add(id):
    karfa = []
    fjoldi = 0
    if "karfa" in session:
        karfa = session["karfa"]
        karfa.append(vorur[id])
        session["karfa"] = karfa
        fjoldi = len(karfa)
    else:
        karfa.append(vorur[id])
        session["karfa"] = karfa
        fjoldi = len(karfa)
    
    return redirect("/")
    #return template("index.html", vorur = vorur, fjoldi = fjoldi)
@app.route("/eyda/<int:id>")
def eydavoru(id):
    karfa = []
    karfa = session["karfa"]
    index = 0
    for i in range(len(karfa)):
        if karfa[i][0] == id:
            index = i
            break
    karfa.remove(karfa[index])
    session["karfa"] = karfa
    
    return redirect(url_for("index"))
    
@app.route("/logout",methods=["GET","POST"])
def logout():
   session.pop("karfa",None)
   return redirect(url_for("index"))

@app.errorhandler(404)
def pagenotfound(error):
    return template("404.html"), 404

if __name__ == '__main__':
    #app.run()
    app.run(debug=True, use_reloader=True)