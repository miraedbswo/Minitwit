def route(app):
    from api import user
    app.register_blueprint(user.api.blueprint)
