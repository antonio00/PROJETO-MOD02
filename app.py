from flask import Flask, render_template, redirect, request
import ctypes

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/home', methods=['GET', 'POST'])
def home():
    if request.form['usuario'] =='admin' and request.form['senha']=='admin':
             
        return render_template('home.html')
    else:
        ctypes.windll.user32.MessageBoxW(0, "Usuário e Senha não conferem"),
        return render_template('index.html')

        
        

if __name__ == '__main__':
    app.run(debug=True)