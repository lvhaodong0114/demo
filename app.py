from flask import Flask
from flask import escape,url_for,render_template,request,redirect,flash
app=Flask(__name__)
app.secret_key = 'dev'
# 运行前输入 $env:FLASK_ENV = "development" 设置为调试模式
# flask run 运行
@app.route('/home')
def hello():
    return '<h1>Hello Totoro!</h1><img src="http://helloflask.com/totoro.gif">'

@app.route('/user/<name>')
def user_page(name):
        return 'User %s' % escape(name)

@app.route('/test')
def test_url_for():
    print(url_for('hello'))
    print(url_for('user_page',name='greyli'))
    print(url_for('user_page',name='peter'))
    print(url_for('test_url_for'))
    print(url_for('test_url_for',num=2))
    return 'test page'

@app.route('/')
def index():
    return render_template('index.html',name=name,movies=movies)

@app.route('/predict',methods=['GET','POST'])
def pre():
    if request.method =='POST':
        hero1=request.form.get('hero1')
        hero2=request.form.get('hero2')
        print(hero1)
        print(hero2)
        flash('Invalid input.')
        return redirect(url_for('index'))
    return render_template('predict.html')

name = 'Grey Li'
movies = [
    {'title': 'My Neighbor Totoro', 'year': '1988'},
    {'title': 'Dead Poets Society', 'year': '1989'},
    {'title': 'A Perfect World', 'year': '1993'},
    {'title': 'Leon', 'year': '1994'},
    {'title': 'Mahjong', 'year': '1996'},
    {'title': 'Swallowtail Butterfly', 'year': '1996'},
    {'title': 'King of Comedy', 'year': '1999'},
    {'title': 'Devils on the Doorstep', 'year': '1999'},
    {'title': 'WALL-E', 'year': '2008'},
    {'title': 'The Pork of Music', 'year': '2012'},
]