from flask import Flask

app = Flask(__name__)
print(__name__)
@app.route("/")
def hello():
    return ('<h1 style="text-align:center" >Hello, World!</h1>' 
            '<p> bhanupriya welcome to flask name main function run in pycharm</p>' 
            '<img src="https://www.adorama.com/alc/wp-content/uploads/2021/05/bird-wings-flying.gif" width=200px>')

if __name__ == "__main__":
    app.run(debug=True)