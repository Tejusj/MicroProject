import mysql.connector
from mysql.connector import Error
    


    


def userInsert(user_id,pass_wrd,usr_name,age,mail):
    try:
        mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="123456789",
        database="travelapp"
        )
        mycursor = mydb.cursor()
    except Error as e:
        print("Cannot establish connection due to",e)

    insert_query = "INSERT INTO USER (USERID, PASS, NAME, AGE, MAIL) VALUES (%s, %s, %s, %s, %s)"
    user_data = (user_id,pass_wrd,usr_name,age,mail)
    mycursor.execute(insert_query, user_data)
    mydb.commit()
    print("Data inserted successfully.")

    if mydb.is_connected():
        mycursor.close()
        mydb.close()
        print("MySQL connection closed.")

#userInsert(user_id="hari001",pass_wrd="abcd1234",usr_name="haridev",age=30,mail="hari413@gmail.com")

def user_checker(user_id):
    try:
        mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="123456789",
        database="travelapp"
        )
        mycursor = mydb.cursor()
    except Error as e:
        print("Cannot establish connection due to",e)

    qry = "SELECT EXISTS(SELECT * FROM USER WHERE USERID=%s)"
    mycursor.execute(qry, (user_id,))
    result = mycursor.fetchone()[0]
    

    if mydb.is_connected():
        mycursor.close()
        mydb.close()
        print("MySQL connection closed.")
    return result



def user_login(user_id,password):
    try:
        mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="123456789",
        database="travelapp"
        )
        mycursor = mydb.cursor()
        try:   
            qry = "SELECT PASS FROM USER WHERE USERID=%s"
            mycursor.execute(qry, (user_id,))
            DBpass = mycursor.fetchone()[0]
            if DBpass==password:
                return "True"
            else:
                return "False"
        except Error as e:
            print("Cannot execute qry ,",e)
    except Error as e:
        print("Cannot establish connection due to",e)
        return "False"

    if mydb.is_connected():
        mycursor.close()
        mydb.close()
        print("MySQL connection closed.")

def packInsert(package_name, UserId, package_details, company_name, company_email):
    if UserId =="":
        return False
    else:
        try:
            mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            password="123456789",
            database="travelapp"
            )
            mycursor = mydb.cursor()
            qry = "INSERT INTO package (package_name, UserId, package_details, company_name, company_email) VALUES (%s,%s,%s,%s,%s)"
            user_data =(package_name, UserId, package_details, company_name, company_email)
            try:
                mycursor.execute(qry, user_data)
                mydb.commit()
                return True
            except Error as e:
                print("Package Insertion failed")
                return False
    
        except Error as e:
            print("Cannot establish connection due to",e)
            return "False"
        finally:
            if mydb.is_connected():
                mycursor.close()
                mydb.close()
                print("MySQL connection closed.")
    
def getpack():
    try:
        mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            password="123456789",
            database="travelapp"
        )
        mycursor = mydb.cursor()
        try:
            mycursor.execute("SELECT * FROM package ORDER BY package_id DESC")
            data = mycursor.fetchall()
            return data

        except mysql.connector.Error as e:
            print("qry execution not possible ", e)
            return False

    except mysql.connector.Error as e:
        print("Connection not possible ", e)
        return False

    finally:
        if mydb.is_connected():
            mycursor.close()
            mydb.close()
            print("MySQL connection closed.")




def FbInsert(feedback):
    if feedback != '':
        last_feedback = getlastfeed()
        if feedback != last_feedback:
            try:
                mydb = mysql.connector.connect(
                    host="localhost",
                    user="root",
                    password="123456789",
                    database="travelapp"
                )
                mycursor = mydb.cursor()
                qry = "INSERT INTO feedback (Fbtxt) VALUES (%s)"
                mycursor.execute(qry, (feedback,))
                mydb.commit()
                return True
            except mysql.connector.Error as e:
                print("Feedback Insertion failed:", e)
                return False
            finally:
                if mydb.is_connected():
                    mycursor.close()
                    mydb.close()
                    print("MySQL connection closed.")
        else:
            print("Feedback already exists in the database.")
            return False
    else:
        print("Null value feedback.")
        return False
# Test the function

def getfeed():
    try:
        mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            password="123456789",
            database="travelapp"
        )
        mycursor = mydb.cursor()
    
        try:
            mycursor.execute("SELECT Fbtxt FROM feedback ORDER BY Fbid DESC")
            fbdata = mycursor.fetchall()
            return fbdata

        except mysql.connector.Error as e:
            print("qry execution not possible ", e)
            return False

    except mysql.connector.Error as e:
        print("Connection not possible ", e)
        return False

    finally:
        if mydb.is_connected():
            mycursor.close()
            mydb.close()
            print("MySQL connection closed.")



def getlastfeed():
    try:
        mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            password="123456789",
            database="travelapp"
        )
        mycursor = mydb.cursor()
        qry = "SELECT Fbtxt FROM feedback ORDER BY Fbid DESC LIMIT 1;"
        mycursor.execute(qry)
        last_feedback = mycursor.fetchone()
        if last_feedback:
            return last_feedback[0]  # Return the feedback text
        else:
            return None  # No feedback found in the database
    except mysql.connector.Error as e:
        print("Error getting last feedback:", e)
        return None
    finally:
        if mydb.is_connected():
            mycursor.close()
            mydb.close()
            print("MySQL connection closed.")

