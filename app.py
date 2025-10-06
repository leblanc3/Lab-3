from flask import Flask, render_template, redirect, url_for, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/profile')
def profile():
    return render_template('profile.html')

@app.route('/works')
def works():
    return render_template('works.html')

@app.route('/contacts')
def contact():
    return render_template('contacts.html')

@app.route('/works/uppercase', methods=['GET','POST'])
def touppercase():
    result = None
    if request.method == 'POST':
        input_string = request.form.get('inputString', '')
        result = input_string.upper()
    return render_template('touppercase.html', result=result)

@app.route('/works/circle', methods=['GET','POST'])
def area_circle():
    radius = None
    result = None
    if request.method == 'POST':
        raw = request.form.get('radius', '').strip()
        if raw:
            try:
                r = float(raw)
                if r < 0:
                    r = None
                else:
                    import math
                    result = 3.14 * r * r
                    radius = raw
            except ValueError:
                pass
    return render_template('area_circle.html',result=result)


@app.route('/works/triangle', methods=['GET','POST'])
def area_triangle():
    result = None
    if request.method == 'POST':
        try:
            b = float(request.form.get('base', 0))
            h = float(request.form.get('height', 0))
            result = 0.5 * b * h
        except ValueError:
            result = None
    return render_template('triangle_area.html', result=result)

if __name__ == '__main__':
    app.run(debug=True)