from flask import Flask, render_template, request
from Database import DataBase
import Api

site= Flask(__name__)
data=DataBase()

@site.route('/')
def Login():
    return render_template("Login.html")

@site.route('/register')
def Register():
    return render_template("Register.html")

@site.route("/user-register", methods=["post"])
def User_Register():
    Name=request.form.get("Name")
    Email=request.form.get("Email")
    Pass=request.form.get("pass")
    response=data.File_Register(Name, Email, Pass)
    if response:
        return render_template("Login.html", msg="Successfully Registered!!")
    else:
        return render_template("Login.html")

@site.route("/User_Login", methods=["post"])
def User_Login():
    Email = request.form.get("Email")
    Pass = request.form.get("pass")
    response = data.Check_Credentials(Email, Pass)
    
    if response:
        return render_template("Home.html", username=response["name"], email=response["email"])
    else:
        return render_template("Login.html", msg="Invalid Credentials!!")
    
@site.route("/ner")
def NER():
    return render_template("NER.html")

@site.route("/perform-ner", methods=["post"])
def PerformNer():
    entity= request.form.get("entity")
    prompt= request.form.get("prompt")
    response= Api.NER(prompt, entity)
    return render_template("NER.html", msg= response)

@site.route("/sentiment")
def Sentiment():
    return render_template("Sentiment.html")

@site.route("/perform-sentiment-analysis", methods=["post"])
def PerformSentiment():
    prompt= request.form.get("prompt")
    response= Api.Sentiment(prompt)
    return render_template("Sentiment.html" , msg=response)

@site.route("/grammar")
def Language():
    return render_template("Grammar.html")

@site.route("/perform-grammar-check", methods=["post"])
def PerformGrammarCheck():
    prompt= request.form.get("prompt")
    response= Api.Grammar(prompt)
    return render_template("Grammar.html", msg=response)

@site.route("/codegen")
def CodeGen():
    return render_template("CodeGene.html")

@site.route("/perform-code-generation", methods=["post"])
def PerformCodeGen():
    prompt= request.form.get("prompt")
    response= Api.Code(prompt)
    return render_template("CodeGene.html", msg=response)

site.run(debug=True)