from flask import Flask, request

app = Flask(__name__)

@app.route('/register', methods=['POST'] )
def register():

    print( request.form.get('name') )
    print( request.form.get('age') )
    
    return 'Successful registration'


if __name__ == '__main__':

    app.run()