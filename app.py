from datetime import datetime
from flask import Flask, render_template, request, redirect, url_for
app = Flask(__name__)


@app.route('/')
def index():
   print('Request for index page received')
   return render_template('index.html')


@app.route('/coming_soon', methods=['POST'])
def coming_soon():
       return render_template('coming_soon.html', )



if __name__ == '__main__':
   app.run()