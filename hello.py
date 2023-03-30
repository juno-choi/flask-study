from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return '<h1>hello world</h1>' \
           '<p>이게 뭐냐</p>'

@app.route('/test')
def hello_world2():
    print('test')
    print('test2')
    return 'hello test'

@app.route('/user/<user_name>/<int:user_id>')
def user(user_name, user_id):
    return f'hello , {user_name}({user_id})'

if __name__ == '__main__':
    app.run(debug=True)