from flask import Flask, render_template
app = Flask(__name__)


@app.route('/')
def test_jinja2():
    return render_template('test_jinja2.html', name="taro")


# 追加した処理
@app.route('/test_ifa')
def if_testa(name=None):
    name = 'jiro'
    return render_template('test_if.html', name=name)


@app.route('/test_ifb')
def if_testb(name=None):
    name = 'sumijiro'
    return render_template('test_if.html', name=name)


# テスト環境起動
app.run(debug=True)
