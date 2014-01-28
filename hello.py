from flask import Flask
from flask import request
    



app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World!'


@app.route('/up', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        file = request.files['file']
        app.logger.debug('file name %s' % file.filename)

    return '''
    <!doctype html>
    <title>Upload new File</title>
    <h1>Upload new File</h1>
    <form action="" method=post enctype=multipart/form-data>
      <p><input type=file name=file>
         <input type=submit value=Upload>
    </form>
    '''

if __name__ == '__main__':
    app.run(debug=True)
