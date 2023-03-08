from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = 'gold'
import random
import math

def random_gold(num1,num2):
    gold = random.randint(num1,num2)
    return gold

@app.route('/')
def index():
    max_gold = 100
    if 'gold' not in session:
        session['gold'] = 0
    return render_template('index.html', max_gold = max_gold)

@app.route('/process_money', methods=['POST'])
def process():
    if request.form['gold'] == "farm":
        mined_gold = random_gold(10,20)
        session['gold'] += mined_gold
        print(session['gold'])
        session['activity']= "Earned" ,mined_gold, "gold at farm"
    if request.form['gold'] == "cave":
        mined_gold = random_gold(5,10)
        session['gold'] += mined_gold
        print(session['gold'])
        session['activity'] = "Earned", mined_gold, "gold at cave"
    if request.form['gold'] == "house":
        mined_gold = random_gold(2,5)
        session['gold'] += mined_gold
        print(session['gold'])
        session['activity'] = "Earned" ,mined_gold, "gold at house"
    if request.form['gold'] == "casino":
        mined_gold = random_gold(-50,50)
        if mined_gold < 0:
            print("Out of Gold!!")
        session['gold'] += mined_gold
        print(session['gold'])
        session['activity'] = "Earned" ,mined_gold, "gold at casino"
    return redirect('/')
@app.route("/reset")
def reset():
    session.clear()
    return redirect ('/')








if __name__=="__main__":
    app.run(debug=True)