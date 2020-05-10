from flask import Flask
from flask import jsonify
from flask_cors import CORS

from request_content import get_content

app = Flask(__name__)
CORS(app)

@app.route('/')
def main():
    data = get_content() #main function
    return jsonify(data)


if __name__=="__main__":
    app.run(debug=True)