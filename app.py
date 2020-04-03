from flask import Flask, flash, request, redirect, render_template, url_for
from werkzeug.utils import secure_filename
from tty_module import filter_array, tty2list
import urllib.request
import os

# basedir = os.path.abspath(os.path.dirname(__file__))
# app = Flask(__name__)
# app.config.update(
#     UPLOADED_PATH=os.path.join(basedir, 'uploads')
# )

UPLOAD_FOLDER = './temp'

app = Flask(__name__)
app.secret_key = "secret key"
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
# app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024
# -----------

ALLOWED_EXTENSIONS = set(['txt', 'log', '134283266'])

def allowed_file(filename):
	return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

def search_options():
    issue_list = ["predictive","state change","uncorrectable","badlba",
	            "unexpected sense","absolute","relative","un-associated","phy bad",
				"soh bad","sas addr","puncturing","certified","package",
				"failed","inserted","removed",": ar",": ld",":ar",":ld"]
    issue_checked = []
    for issue in issue_list:
        if request.form.get(issue):
            issue_checked.append(request.form.get(issue))

    issue_extra = request.form.get('extra')

    print (issue_extra, issue_checked)

    if issue_extra and issue_checked:
        issue_combined = issue_checked + issue_extra.split(",")
        print("checked and extra")
    elif issue_checked:
        issue_combined = issue_checked
        print("checked")
    elif request.form.get('extra'):
        issue_combined = issue_extra.split(",")
    else: 
        issue_combined = [""]
        print("Empty options")
    print('issue comb', issue_combined)
    return issue_combined

@app.route('/', methods = ['GET', 'POST'])
def upload():
    
    if request.method == 'POST':
        # check if the post request has the file part
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['file']
        if file.filename == '':
            flash('No file selected for uploading')
            return redirect(request.url)
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            file.save(file_path)
            flash('File successfully uploaded')
            filter_array (tty2list(file_path), search_options())
            # render_template('index.html', results = data) 
            return redirect(url_for('result')) 
        else: 
            flash('Allowed file types are txt, log, 134283266')
            return redirect(request.url)
 
    # return data
    return render_template('index.html')

@app.route('/result')
def result():
   return render_template('result.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=1)


