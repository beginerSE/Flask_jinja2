from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def test_jinja():
    return render_template('test_jinja2.html', name="taro")
    
#テスト環境起動
app.run(debug=True)
