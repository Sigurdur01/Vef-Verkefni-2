from bottle import *

@route("/page1")
def index():
    return template("demo3.tpl")

@route("/page2")
def index():
    return template("demo2.tpl")

@route("/page3")
def index():
    return template("index3.tpl", nafn = "Siggi")

@route("/page4")
def index():
    my_dict={"number":"123","street":"fake str","city":"Fakeville"}
    return template("index4.tpl", my_dict)

@route("/page5")
def index():
    info = {"title":"Beatls",
            "names":["John","Paul","Ringo","George"]}
    return template("index5.tpl",info)

@error(404)
def villa(error):
    return"<h2 style='color:red'>Þessi síða finnst ekki</h2>"
