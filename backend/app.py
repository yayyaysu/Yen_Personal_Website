from flask import Flask, jsonify
from flask_cors import CORS
from api.routes import api
from dotenv import load_dotenv
import os

# 加載環境變數
load_dotenv()

app = Flask(__name__)
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')
CORS(app)

@app.route('/')
def home():
    return jsonify({"message": "Flask is running in Docker!"})

app.register_blueprint(api, url_prefix='/api')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
