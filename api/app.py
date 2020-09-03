# -*- coding: utf-8 -*-
import settings
from flask import Flask
from views import router

app = Flask(__name__)
app.register_blueprint(router)

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=settings.API_DEBUG)
