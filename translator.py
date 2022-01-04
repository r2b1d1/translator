from flask import Flask, jsonify
from flask_restful import Resource, Api, reqparse
from translate import Translator
import html


app = Flask(__name__)
api = Api(app)
translator = Translator(to_lang='fr')


class Render(Resource):
    def get(self):
        parser = reqparse.RequestParser()
        parser.add_argument('text', required=True, help='text cannot be empty')
        translation = translator.translate(parser.parse_args()['text'])
        return jsonify({'translation': html.unescape(translation)})


api.add_resource(Render, '/translate')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)
