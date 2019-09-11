import flask
from flask_restplus import Api

from api.endpoints.images import ns as image_ns
from api.endpoints.videos import ns as video_ns


app = flask.Flask(__name__)
api = Api(app)

api.add_namespace(image_ns)
api.add_namespace(video_ns)


if __name__ == '__main__':
    app.run(debug=True)
