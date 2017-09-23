from flask import Flask

my_app = Flask(__name__)

def makeHuge(text):
    return '<span style="font-size:78px;">'+text+'</span>'
def makeLink(text, active):
    if active == True:
        return '<a href="'+text+'">'+text+'</a>' + ('&nbsp;'*10)
    return '<u>'+text+'</u>' + ('&nbsp;' * 10)

@my_app.route('/') #127.0.0.1:5000
def home():
    return "Go to: " + makeLink("/", False) + makeLink("cool", True) + makeLink("funny", True) + "<br>" + makeHuge(":-)")

@my_app.route('/cool')
def cool():
    return "Go to: " + makeLink('/', True) + makeLink('cool', False) + makeLink('funny', True) + "<br>" + makeHuge("B-)")

@my_app.route('/funny')
def funny():
    return "Go to: " + makeLink('/', True) + makeLink('cool', True) + makeLink('funny', False) + "<br>" + makeHuge("xD")


if __name__ == '__main__':
    my_app.debug = True #auto-reload when changed
    my_app.run() #run the web app
