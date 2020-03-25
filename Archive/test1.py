from flask import Flask
import webbrowser
import file_open

app = Flask(__name__)

@app.route("/")
def out_page():
    out_data = file_open.finput()
    return out_data

if __name__ == '__main__':
    webbrowser.open('http://127.0.0.1:6000/')
    app.run(port=6000, debug=1)