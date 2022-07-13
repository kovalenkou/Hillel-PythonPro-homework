import random
from datetime import datetime
from flask import Flask, request, render_template


app = Flask(__name__)
app.debug = True


@app.route("/")
def index():
    return render_template('index.html')


@app.route("/whoami")
def whoami():
    # browser
    browser = request.headers.get('User-Agent')
    # ip
    ip_address = request.remote_addr
    # Current time on server
    current = datetime.now().strftime("%d/%m/%Y, %H:%M:%S")
    return render_template('whoami.html', browser=browser, ip_address=ip_address, current=current)


@app.route("/source_code")
def source_code():
    with open('app.py') as app_file:
        source_code_text = app_file.read()
    return render_template('source_code.html', source_code_text=source_code_text)


@app.route("/randoms", methods=['GET'])
def randoms_get():
    return render_template('randoms.html')


# 127.0.0.1:5000/randoms?length=42&specials=1&digits=0
@app.route("/randoms", methods=['POST'])
def randoms():
    length = int(request.form.get('length'))
    specials = 1 if request.form.get('specials') == 'on' else 0
    digits = 1 if request.form.get('digits') == 'on' else 0
    res_string = ''
    if (length < 0 or length > 100) or specials not in (0, 1) or digits not in (0, 1):
        if length < 0 or length > 100:
            res_string += f"<p>Input {length} is not correct. Choose integer more than 0 and less then 100!</p>"
        if specials not in (0, 1):
            res_string += f'<p>Input specials: "{specials}" is not correct. Choose 0 or 1!</p>'
        if digits not in (0, 1):
            res_string += f'<p>Input digits: "{digits}" is not correct. Choose 0 or 1!</p>'
    else:
        chars_list = [chr(_) for _ in range(ord('A'), ord('Z')+1)]
        chars_list.extend([chr(_) for _ in range(ord('a'), ord('z') + 1)])
        if specials:
            chars_list.extend([chr(_) for _ in range(ord(' '), ord('/') + 1)])
        if digits:
            chars_list.extend([chr(_) for _ in range(ord('0'), ord('9') + 1)])
        res_string = ''.join(random.choices(chars_list, k=length))
    return render_template('randoms.html', res_string=res_string)


if __name__ == '__main__':
    app.run(use_reloader=True)
