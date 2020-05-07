from flask import Flask
from flask import render_template
import requests

from request_content import get_content

app = Flask(__name__)



@app.route('/')
def main():
    data = get_content() #main functino 
    return render_template('article.html', data=data)

if __name__=="__main__":
    app.run(debug=True)