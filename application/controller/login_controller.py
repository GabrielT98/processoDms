from flask import render_template, request
from application import app
from application.model.entily.visitante import Visitante

visitante1 = Visitante()
visitante1.setNome("Gabriel")
visitante1.setEmail("selecaoengsoftware@universidadedevassouras.edu.br")
visitante1.setSenha("default123")
@app.route('/')
def index():
    return render_template("login.html")

@app.route("/login")
def login():
    email = request.form.get('email',None)
    senha = request.form.get('senha',None)

    if email == visitante1.getEmail() and senha == visitante1.getSenha():
        return render_template("index.html")
    else:
        return render_template("login.html")
