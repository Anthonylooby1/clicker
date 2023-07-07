from flask import Flask, render_template, request, redirect, session

app = Flask(__name__) 
app.secret_key = "plusone"

@app.route('/')
def clicker():
    if "oneup" not in session:
        session['oneup'] = 1
    else:
        session['oneup'] += 1    
    return render_template("index.html")

@app.route('/addcount', methods=['POST'])
def refresh():
    # print(session['oneup'])
    if request.form['addcount']=="plus":
        session['oneup'] += 1
    elif request.form['addcount']=="reset":
        session['oneup'] = 0   
        print(session['oneup'])   
    
    return redirect("/")

@app.route('/destroy_session')
def destroy():
    session.clear()
    return redirect('/')



if __name__=="__main__":    
    app.run(debug=True)   