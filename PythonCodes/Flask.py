from flask import Flask, flash, request, redirect, url_for, render_template
from werkzeug.utils import secure_filename

TEMPLATE = "/content/"

app = Flask(__name__, template_folder=TEMPLATE)

app.config['UPLOAD_FOLDER'] = "/content/Uploads"

ngrok.set_auth_token("2DJyoS7QMsne6ZsjPBWlik5uBBv_37hajTNHz6NFWXeczXf7A")
public_url = ngrok.connect(port_no).public_url

print(f"To acces the Gloable link please click {public_url}")


@app.route("/", methods=["GET", "POST"])
def upload_file():
    if request.method == 'POST':
        files = request.files.getlist("image")
        for file in files:
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], file.filename))

        return
    return render_template("index.html")


@app.route("/denemeeee")
def Ac():
    return render_template("dene.html")


if __name__ == "__main__":
    app.run()