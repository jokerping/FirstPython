
'web框架FLask使用'

from flask import Flask,request

app=Flask(__name__)

@app.route('/',methods=['GET','POST'])
def home():
    return '<h1>"张伟大傻逼"<h1>'

@app.route('/signin',methods=['GET'])
def signin_from():
    return '''<from action="/signin" method="post">
              <p><input name="username"></p>
              <p><input name="password" type="password"></p>
              <p><button type="submit">signin</button></p>
              </from>'''
@app.route('/signin',methods=['POST'])
def signin():
    if request.form['username']=='admin' and request.form['password']=='password':
        return '<he>hello admin</h3>'
    return '<h3>Bad username or password.</h3>'


if __name__=='__main__':
    app.run()