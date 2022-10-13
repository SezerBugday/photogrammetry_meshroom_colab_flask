@app.route("/test", methods=['POST','GET'])
def test_page():
  if request.method == "POST":
    image = request.files.get('img', '')
    image = request.form["img"]

    print("img ",image)
    return "<h1> yo! </h1>"
  else:
    return render_template('index.html') 
