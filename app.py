from flask import Flask, request, render_template, redirect , url_for , session

app = Flask(__name__)

app.secret_key ="tik-tok"   #session data is encripted so we need to define a key

@app.route("/")  #flask decorator 
def home():
    bmi = session.pop("bmi" , None) #get and clear session
    category = session.pop("category" , None)
    advice = session.pop("advice" ,None)

    return render_template("index.html" , bmi =  bmi , category = category , advice = advice)



def categorize(bmi):   #categorize the BMI and return the value with the associated advice
    if bmi < 18.5:
        category = "Underweight"
        advice = "Focus on nutrient-rich foods and strength training exercises."
    elif bmi < 24.9:
        category ="Normal"
        advice = "Congratulations! You are on the right track."
    elif bmi < 29.9:
        category = "Overweight"
        advice = "Try regular physical activity and a balanced diet."
    else:
        category = "Obese"
        advice = "Consult a healthcare professional and follow a structured plan."
    return category , advice

@app.route("/calculate", methods = ["POST"])  #fetching the data from the user inputs
def calculate():
    weight = float(request.form["weight"])   #form data is sent as a string so we need to convert it no number for calculations
    height = float(request.form["height"])


    #bmi logic
    bmi = round((weight) / ((height /100) ** 2), 2)
    category , advice = categorize(bmi)

    #store result in session
    session["bmi"] = bmi
    session["category"] = category
    session["advice"] = advice
    
    

    return redirect(url_for("home"))  #redirect back to index.html





if __name__ == "__main__":
    app.run()
