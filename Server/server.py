from main import create_app
from config import Config

app = create_app(Config)

app.run(host='127.0.0.1', debug=True, port=80)
