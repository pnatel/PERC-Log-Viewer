from flask import Flask, render_template, request
from tty_module import filter_array_IO
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

    data = filter_array_IO (io_file=f, substrList=issue_combined)
    return data


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=1)


