from flask import Flask
from flask import request
from flask import render_template
    
from csv_tool import UnicodeReader


app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template('index.html')


@app.route('/up', methods=['GET', 'POST'])
def upload_file():
    data = None
    if request.method == 'POST':
        file = request.files['file']
        app.logger.debug('file name %s' % file.filename)

        ret = []
        rr = UnicodeReader(file,encoding='utf8', delimiter=';', quotechar='"')
        data = []
        for row in rr:
           app.logger.debug(row)
           data.append(row[0])

    return render_template('up.html', data=data)

if __name__ == '__main__':
    app.run(debug=True)
