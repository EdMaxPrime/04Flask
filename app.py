from flask import Flask

my_app = Flask(__name__)

def makeHuge(text):
    return '<span style="font-size:78px;">'+text+'</span>'
def makeLink(text):
    return '<a href="'+text+'">'+text+'</a>' + ('&nbsp;'*10)
header = "Go to: " + ('&nbsp;'*10) + makeLink('/') + makeLink('/cool') + makeLink('/funny') + '<br>'

@my_app.route('/') #127.0.0.1:5000
def home():
    return header + makeHuge(":-)")

@my_app.route('/cool')
def cool():
    return header + makeHuge("B-)")

@my_app.route('/funny')
def funny():
    return header + makeHuge("xD")


if __name__ == '__main__':
    my_app.debug = True #auto-reload when changed
    my_app.run() #run the web app
