def register_blueprints(app):

    # config test app blueprint remove it
    from core.example.resources import example
    app.register_blueprint(example, url_prefix="/example")

    return app
