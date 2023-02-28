# using flask_restful
import os
from flask import Flask, jsonify, flash, request, redirect, url_for
from flask_restful import Resource, Api
from werkzeug.utils import secure_filename
# creating the flask app
app = Flask(__name__)
# creating an API object
api = Api(app)
UPLOAD_FOLDER = 'E:\gpt3-summarization'
ALLOWED_EXTENSIONS = set(['pdf'])
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
  
# making a class for a particular resource
# the get, post methods correspond to get and post requests
# they are automatically mapped by flask_restful.
# other methods include put, delete, etc.
class Hello(Resource):
  
    # corresponds to the GET request.
    # this function is called whenever there
    # is a GET request for this resource
    def get(self):
  
        return jsonify({'message': 'hello world'})
  
    # Corresponds to POST request
    
    @app.route('/upload', methods=['POST'])
    def upload_file():
        if request.method == 'POST':
            print("helloworld")
            #json_data = request.json
            #print(json_data)
            # check if the post request has the file part
            file = request.files['file']
            # if user does not select file, browser also
            # submit an empty part without filename
            if file.filename == '':
                flash('No selected file')
                return redirect(request.url)
            if file and file.filename != '':
                filename = secure_filename(file.filename)
                file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
                #return redirect(url_for('filename',
                                       # filename=filename))
                return jsonify({'status': '200'})
        return
  
    def allowed_file(filename):
        return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS
    
api.add_resource(Hello, '/');

# driver function
if __name__ == '__main__':
  
    app.run(debug = True)
