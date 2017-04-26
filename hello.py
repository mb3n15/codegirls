from flask import Flask
from flask import render_template
from flask import request
import requests


key="key-aeabb8b669c6aca67316b5015751a998"
sandbox="sandboxd7af4f4947f44cb3b4f7426feb9fb76a.mailgun.org"

app=Flask("HelloApp1")

@app.route("/")
def hello():
#    return "Hello Everyone!"
    return render_template("hello.html")

@app.route("/404")
def error_404():
#    return "Hello Everyone!"
    return "you should not be here"

@app.route("/aboutme")
def aboutme():
#    return "aboutme"
    return render_template("aboutme.html")


@app.route("/<name>")
def hello_name(name):
#    return "Hello {0}!".format(name.title())
    return render_template("HI.html",name=name.title())


@app.route("/contact", methods=['POST'])
def contact():
       form_data= request.form

       #Get form_data
       name=form_data['name']
       message=form_data['message']
       email=form_data['Email']


       print(name, message, email)
       #email message
       subject="Hello from Maria"
       body="I just wrote to say I welcome you!"

       sender='mb3n15@soton.ac.uk'

       #sending message
       request_url='https://api.mailgun.net/v3/{0}/messages'.format(sandbox)

       email_request = requests.post(request_url, auth=('api',key),data={
           'from': sender,
           'to': email,
           'subject': subject,
           'html':'<html><p><a style="color:orange;font-size:40px; background-color:green;" href="/aboutme">About me</a></p></html>'
       })

       #checking email status
       print('Status:{0}'.format(email_request.status_code))

       print('HTML:{0}'.format(email_request.html))

       return("Form works!")

if __name__=="__main__":
    app.run()
