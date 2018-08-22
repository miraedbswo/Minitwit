from app import create_app
from config.config import Config

app = create_app(Config)

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True, port=3000)
