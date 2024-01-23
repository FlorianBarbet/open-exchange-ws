from flask import Flask

from cron import scheduler
from routes import rate_bp

app = Flask(__name__)

app.register_blueprint(rate_bp, url_prefix="/rates")


@app.teardown_appcontext
def stop_scheduler(e):
    print(e)
    if scheduler.running:
        scheduler.shutdown()
    return {'message': "hello world"}


@app.after_request
def add_header(response):
    response.headers.add('Access-Control-Allow-Headers', 'Content-Type')
    response.headers.add('Access-Control-Allow-Methods', 'GET')
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response


if __name__ == '__main__':
    app.run()
