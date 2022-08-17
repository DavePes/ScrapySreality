from flask import Flask, render_template
root = 'sreal/html'
app = Flask(__name__, template_folder=root)

port = 8080
@app.route('/')
def home():
   return render_template('index.html')
app.run(host='0.0.0.0',port=port)
