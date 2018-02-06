from flask import Blueprint
from flask_restful import Resource, Api, abort, reqparse
from Logger import logger, LogLevel, TraceException
from Database.playlists import Playlists
from Database import db
import json

bp_playlist = Blueprint('bp_playlist', __name__)
api_playlist = Api(bp_playlist)


parser = reqparse.RequestParser()
parser.add_argument('content')


class PlaylistsList(Resource):
    def get(self):
        logger.log(LogLevel.DEBUG, 'get all from playlist')
        try:
            my_dict = {}
            session = db.session()
            my_playlist = session.query(Playlists).all()
            for name in my_playlist:
                my_dict[name.PlaylistId] = name.Name
            print("get_all1", my_dict)
            return json.dumps(my_dict)
        except Exception as ex:
            print("get all2: ", ex.__str__())
            logger.log(LogLevel.ERROR, TraceException(ex.__str__()).message)


    def post(self):
        pass


class Playlist(Resource):
    def get(self, PlaylistId):
        session = db.session()
        my_playlist = session.query(Playlists).filter(Playlists.PlaylistId == PlaylistId)
        if my_playlist != None:
            return my_playlist.__str__()
        else:
            "None"

    def delete(self, PlaylistId):
        pass

    def put(self, PlaylistId):
        pass

api_playlist.add_resource(PlaylistsList, '/playlists')
api_playlist.add_resource(Playlist, '/playlist/<PlaylistId>')
