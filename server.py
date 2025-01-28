from flask import Flask, render_template, request
from DBMS.tablelist import *
 
app = Flask(__name__)

G_user_id = ""
G_data=[]
G_fbdata=[]

@app.route('/')
def index():
    return render_template('login.html')

@app.route('/register', methods=['GET','POST'])
def register():
    if request.method == 'POST':
        
            userid = request.form['userid']
            username = request.form['username']
            password = request.form['password']
            age = request.form['age']
            email = request.form['email']

            usr_aval = user_checker(userid)

            if usr_aval == 0:
                try:
                    # Attempt to insert user data into the database
                    userInsert(user_id=userid, pass_wrd=password, usr_name=username, age=age, mail=email)
                    # If insertion is successful, print a confirmation message
                    print(f"New registration:\nUser ID: {userid}\nUsername: {username}\nPassword: {password}\nAge: {age}\nEmail: {email}")
                    # Render the login page with a success response
                    return render_template('login.html')
                except:
                    # If insertion fails, print a message and render the registration page again
                    print("Insertion failed")
                    return render_template('register.html')
            else:
                # If the user already exists, print a message and render the registration page again
                print("UserId Already exist")
                return render_template('register.html')
        
           
    else:
        return render_template('register.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template('login.html')
    else:
        userid = request.form["userid"]
        user_pass = request.form["password"]

        usr_aval = user_checker(userid)
        if usr_aval != 0:
            res = user_login(user_id=userid, password=user_pass)
            if res == 'True':
                global G_user_id
                G_user_id = userid
                print("Logged in User ID:", G_user_id)
                return render_template("home.html", user_id=G_user_id)
            else:
                return render_template("login.html")
        else:
            print("Invalid UserId")
            return render_template("login.html")

@app.route('/home', methods=['GET','POST'])
def home():
    if request.method == "GET":
        return render_template("home.html", user_id=G_user_id)
    else:
        print("Logged in User ID:", G_user_id)
      # Assuming you have a function to get the user ID
        return render_template("home.html", user_id=G_user_id)



@app.route('/indexpack.html', methods=['GET', 'POST'])
def indexpack():
    if request.method == 'GET':
        return render_template("indexpack.html",user_id=G_user_id)
    else:
        package_name = request.form['package_name']
        company_email = request.form['company_email']
        package_provider = request.form['package_provider']
        package_details = request.form['package_details']
        print(package_name,company_email,package_provider,package_details,G_user_id)
        result= packInsert(package_name = package_name, UserId = G_user_id, package_details=package_details, company_name=package_provider, company_email=company_email)
        if result==True:
            return render_template("home.html",user_id=G_user_id)
        else:
            return render_template("indexpack.html",user_id=G_user_id)

    

@app.route('/tours.html', methods=['GET', 'POST'])
def tours():
    global G_data
    res = getpack()
    print(res)
    if res != False:
        G_data=res
        if request.method == 'GET':
            print(1)
            return render_template("tours.html",data=G_data)
            
        else:
            print(2)
            return render_template("tours.html",data=G_data)
    else:
        print(3)
        return render_template("home.html",user_id=G_user_id)

@app.route('/feedback', methods=['GET'])
def feedback_form():
    global G_fbdata
    res = getfeed()
    if res != False:
        G_fbdata=res
    else:
        G_fbdata=["not available"]
    print(G_fbdata)
    return render_template('feedback.html', Fdata = G_fbdata)

# Route to handle form submission
@app.route('/submit-feedback', methods=['POST'])
def submit_feedback():
    fdbk = request.form['feedback']
    print(fdbk)
    global G_fbdata
    res = getfeed()
    if res != False:
        G_fbdata=res
    else:
        G_fbdata=["not available"]
    print(G_fbdata)
    if fdbk!='':
        res = FbInsert(fdbk)
        if res == True:
            print(1)
            fdbk=''
            return render_template('feedback.html', Fdata = G_fbdata)
        else:
            return render_template('feedback.html', Fdata = G_fbdata)
    else:
        return render_template('feedback.html', Fdata = G_fbdata)
if __name__ == '__main__':
    app.run(debug=True)
