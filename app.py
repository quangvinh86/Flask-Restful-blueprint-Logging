from flask import Flask
from api.HelloWorld import api_v1_bp
from api.PlaylistAPI import bp_playlist
from Logger import logger, LogLevel, TraceException
from flask_sqlalchemy import SQLAlchemy
from Database import db
import os

app = Flask(__name__)
path_file = os.path.abspath(os.path.dirname(__file__)) + "/chinook.db"
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////' + path_file
db.init_app(app)
app.register_blueprint(api_v1_bp, url_prefix='/api')
app.register_blueprint(bp_playlist, url_prefix='/api')

@app.route('/')
def hello():
    logger.log(LogLevel.INFO, 'xin chao, toi la python')
    try:
        name = 10/3
    except Exception as ex:
        trace = TraceException(ex.__str__())
        logger.log(LogLevel.ERROR, trace.message)

    # app.logger.info('hello world')
    return "hello world"


if __name__ == '__main__':
    # handler = TimedRotatingFileHandler('app.log', interval=1)
    # handler.setLevel(logging.DEBUG)
    # fileFormatter = logging.Formatter('%(asctime)s %(levelname)-8s %(message)s')
    # handler.setFormatter(fileFormatter)
    # app.logger.addHandler(handler)
    # logger = logging.getLogger(__name__)
    app.run(debug=True, port=5002)
