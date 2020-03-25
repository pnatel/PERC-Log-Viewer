from flask import Flask, render_template, request
from file_open import filter_array, finput
import os

basedir = os.path.abspath(os.path.dirname(__file__))
app = Flask(__name__)
app.config.update(
    UPLOADED_PATH=os.path.join(basedir, 'uploads')
)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/upload', methods=['POST'])
def upload():
    f = request.files['file[0]']
    issue_type = request.form.get('issue')
    data = filter_array (io_file=f, substrList=issue_type.split(","))
    # data = finput(f)
    return data


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=1)


