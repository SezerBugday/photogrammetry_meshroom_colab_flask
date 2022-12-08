from flask import Flask, flash, request, redirect, url_for, render_template
from werkzeug.utils import secure_filename

TEMPLATE = "/content/"

app = Flask(__name__, template_folder=TEMPLATE)

app.config['UPLOAD_FOLDER'] = "/content/input"

ngrok.set_auth_token("2GxLRDzBS0fgWEesR7tac2e9BOs_6vtYMQMcNB3ETtSi2a8q7")
public_url = ngrok.connect(port_no).public_url

print(f"To acces the Gloable link please click {public_url}")


@app.route("/", methods=["GET", "POST"])
def upload_file():
    if request.method == 'POST':
        files = request.files.getlist("image")
        for file in files:
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], file.filename))
            
            
        os.system("rembg p /content/input   /content/input")
        
        return
    
    return render_template("index.html")


@app.route("/denemeeee")
def Ac():
    return render_template("dene.html")


if __name__ == "__main__":
    app.run()
