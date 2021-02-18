import os
from flask import Flask, request

UPLOAD_FOLDER = 'uploads'

app = Flask(__name__)

# HTTP POST
@app.route('/', methods=['POST'])

def upload_file():

    # get the file uploaded from client
    file = request.files['file']

    if file:
        
        try:
            file.save( os.path.join(UPLOAD_FOLDER, os.path.basename(file.filename) ) )

        except Exception as e:
            print('error')
            print(e)
            
        return 'Upload is successful'


if __name__ == '__main__':

    app.run()