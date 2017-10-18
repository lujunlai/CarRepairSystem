from flask import Flask, render_template, send_from_directory

app = Flask(__name__, static_url_path='', static_folder='')


@app.route('/js/<path:path>')
def send_js(path):
    return send_from_directory('templates/js', path)


@app.route('/pic/<path:path>')
def send_pic(path):
    return send_from_directory('templates/pic', path)


@app.route('/css/<path:path>')
def send_css(path):
    return send_from_directory('templates/css', path)


@app.route('/favicon.ico')
def send_favicon():
    return send_from_directory('templates', 'favicon.ico')


@app.route('/')
def index():
    return render_template('index.html')


if __name__ == '__main__':
    app.run()
