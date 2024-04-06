from flask import Flask,render_template

app = Flask(__name__)

@app.route("/home")
@app.route("/")
def home():   
    return render_template("index.html")

# @app.route("/upload", methods=['GET'])
# def recommend(request):
#     print("febj")
#     if request.method == 'GET':
#        return render_template("upload.html")

@app.route("/upload.html")
def upload():
    return render_template("upload.html")

@app.route("/Tryon2D.html")
def Tryon2D():
    return render_template("Tryon2D.html")


if __name__ == "__main__":
    app.run(debug=True)