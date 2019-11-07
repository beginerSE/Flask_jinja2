from flask import Flask, render_template
app = Flask(__name__)


@app.route('/')
def test_jinja2():
    return render_template('test_jinja2.html', name="taro")


# if文処理(True)
@app.route('/test_ifa')
def if_testa(name=None):
    name = 'jiro'
    return render_template('test_if.html', name=name)


# if文処理(False)
@app.route('/test_ifb')
def if_testb(name=None):
    name = 'taro'
    return render_template('test_if.html', name=name)


# for文処理
@app.route('/test_for')
def test_for():
    brothers = ["太郎", "次郎", "三郎"]
    return render_template('test_for.html', users=brothers)


# テスト環境起動
app.run(debug=True)
