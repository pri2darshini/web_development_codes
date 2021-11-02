from flask import Flask,render_template,redirect,url_for
app=Flask(__name__)
##@app.route('/')
##def index():
##   return render_template('index.html')

@app.route('/')
@app.route('/index1')
def index1():
    return render_template('index1.html')

@app.route('/species')
def species():
    return render_template('species.html')

@app.route('/images')
def images():
    return render_template('images.html')

@app.route('/quicklinks')
def quicklinks():
    return render_template('quicklinks.html')

@app.route('/kitchen')
def kitchen():
    return render_template('kitchen.html')

@app.route('/people')
def people():
    return render_template('people.html')

if __name__ == "__main__":
    app.run()
