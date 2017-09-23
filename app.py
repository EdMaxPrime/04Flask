from flask import Flask

my_app = Flask(__name__)

@my_app.route('/') #127.0.0.1:5000
def home():
    return "hello"

if __name__ == '__main__':
    my_app.debug = True #auto-reload when changed
    my_app.run() #run the web app
