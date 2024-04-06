# from flask import Flask,render_template,request
# from flask_sqlalchemy import SQLAlchemy
# from datetime import datetime

# #request ko bhi import kiya 

# app = Flask(__name__)
# #initialize sqlalchemy
# app.config['SQLALCHEMY_DATABASE_URI']= "sqlite:///todo.db"
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# db = SQLAlchemy(app)


# #seqlalchemy is a orm mapper ye hume python k through database me changes karne ki facility provide karta h 
# #uper humne flask web app/application ko initial kiya

# #class bante hain python me yaha hum class k through bas apna schema define kar rhe hain
# class Todo(db.Model):
#     sno = db.Column(db.Integer,primary_key=True)
#     title = db.Column(db.String(200),nullable=False)
#     desc = db.Column(db.String(500),nullable=False)
#     date_created = db.Column(db.DateTime,default=datetime.utcnow)

#     def __repr__(self) -> str:
#         return f"{self.sno} - {self.title}"
# #HUM YAHA repr method se sno and title dekhna chahte hain    
# #uper nullable false h  matlab matlab title and description false nhi ho sakta


# #home route h     methods ki list pass tabhi ye get post request ko jane ga    def function k name k aage matlab def matlab define
# @app.route('/', methods=['GET','POST'])
# def hello_world():
#     if request.method=='POST': 
#         title=request.form['title']
#         desc=request.form['desc']
#         #agar submit par click to post request then finally terminal me post print
#         # print("post")
#         # print(request.form['title'])
#         #agar hum form ka title lene ki kosis kare to
#     # return 'Hello, World!'
#     #hum chahte hain jase hi koi humare home page pe aaye to hum todo ka instace banaya and usme jo desc and title bo dikhega
#         todo=Todo(title=title,desc=desc)
#         db.session.add(todo)
#         db.session.commit()

#     allTodo = Todo.query.all()
#     return render_template('index.html',allTodo=allTodo)

# #render template return me dene se hum home route par index.html page display/render karva sakte hain browser par

# #product route h 
# # @app.route('/products')
# # def products():
# #     return 'Hello, this is a product page!!!!!'


# @app.route('/show')
# def products():
#     allTodo = Todo.query.all()
#     print(allTodo)
#     return 'this is product page !!!!!'

# #route ki calling yahin se
# if __name__ == "__main__":
#     app.run(debug=True,port=8000)

# #  http://127.0.0.1:8000/products   jo bhi page chaiye uska name / me laga do      

# #hum port khud se bhi  pass kar sakte hain fir ussi port par ye app run mean web app run
# #app chal ja debug mode me taki koi error aaye to  problem vahin dikh jaye
# #uper jo banayi ye humari ek flask app h
 

#  #ye sara documentation of SQlalchemy me padh lo jakar 
#  #jitni bar MYtodo ko ja kar browser par refresh utni bar hi sqliteviewer me table me entity add


from flask import Flask,render_template

app = Flask(__name__)

@app.route("/home")
@app.route("/")
def home():   
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)