#!/usr/bin/env python

import json
import os

from flask import Flask
from flask import send_from_directory
from flask import request
from flask_restful import Api
from flask_restful import reqparse
from flask_restful import Resource
import werkzeug
from werkzeug.utils import secure_filename

app = Flask(__name__)
api = Api(app)
app.config['UPLOAD_FOLDER'] = "./uploads"


class LocalStorage(Resource):

    def get(self, filename=None):
        download_path = os.path.join(app.config['UPLOAD_FOLDER'],
                                     filename)
        if os.path.exists(download_path):
            if request.args.get("meta") == "yes":
                return {"path": filename,
                        "size": os.stat(download_path).st_size}
            else:
                return send_from_directory(
                        directory=app.config['UPLOAD_FOLDER'],
                        filename=filename)
        else:
            return {}

    def post(self, filename=None):
        parser = reqparse.RequestParser()
        parser.add_argument("files", location="files", action="append",
                            type=werkzeug.datastructures.FileStorage)
        args = parser.parse_args()
        uploaded_files = {"uploaded": []}
        for file in args["files"]:
            secured_filename = secure_filename(file.filename)
            upload_path = os.path.join(app.config['UPLOAD_FOLDER'],
                                       secured_filename)
            file.save(upload_path)
            uploaded_files["uploaded"].append({
                "path": secured_filename,
                "size": os.stat(upload_path).st_size})
        
        return uploaded_files


api.add_resource(LocalStorage,
                 "/local",
                 "/local/<string:filename>")

if __name__ == '__main__':
    app.run(debug=True)
