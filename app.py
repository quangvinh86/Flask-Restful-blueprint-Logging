from flask import Flask
from api.HelloWorld import api_v1_bp
from Logger import logger, LogLevel, TraceException


app = Flask(__name__)
app.register_blueprint(api_v1_bp, url_prefix='/api')

# logger = None


@app.route('/')
def hello():
    logger.log(LogLevel.INFO, 'xin chao, toi la python')
    try:
        a = 1/0
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
