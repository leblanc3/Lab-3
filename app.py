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
    original = None
    result = None
    if request.method == 'POST':
        text = request.form.get('inputString', '').strip()
        if text:
            result = text.upper()
            original = text
    return render_template('touppercase.html', result=result, original=original)

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
    return render_template('area_circle.html',result=result , radius=radius)


@app.route('/works/triangle', methods=['GET', 'POST'])
def area_triangle():
    base = None
    height = None
    result = None
    if request.method == 'POST':
        raw_base = request.form.get('base', '').strip()
        raw_height = request.form.get('height', '').strip()
        if raw_base and raw_height:
            try:
                b = float(raw_base)
                h = float(raw_height)
                if b >= 0 and h >= 0:
                    a = 0.5 * b * h
                    result = {
                        "base": round(b, 10),
                        "height": round(h, 10),
                        "area": round(a, 10),
                    }
                    base = raw_base
                    height = raw_height
            except ValueError:
                pass
    return render_template('area_triangle.html', result=result, base=base, height=height)

if __name__ == '__main__':
    app.run(debug=True)