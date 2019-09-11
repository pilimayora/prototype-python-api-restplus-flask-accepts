from flask_restplus import Resource, Namespace, reqparse
from flask_accepts import accepts, responds
from api.models.video import Video
from api.schemas.video_schema import VideoSchema


ns = Namespace('video', description="Operations related to videos")

parser = reqparse.RequestParser()
parser.add_argument('id', type=int, location='path')


@ns.route("/")
class VideoResource(Resource):

    @ns.expect(parser)
    @responds(schema=VideoSchema, api=ns)
    def get(self, **kwargs):
        return Video('test', 1000)

    @accepts(schema=VideoSchema, api=ns)
    @responds(schema=VideoSchema, api=ns)
    def post(self):
        return Video('test', 500)


@ns.route("s/")
class VideoListResource(Resource):

    @responds(schema=VideoSchema(many=True), api=ns)
    def get(self):
        return [Video('test', 1000)]
