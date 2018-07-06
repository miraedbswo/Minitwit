from main import create_app
import config

app = create_app(config.Config())

app.run()
