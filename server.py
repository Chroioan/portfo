# 
# 1) i went to cmd  
# 2) cd C:\Users\user\Documents\"Programing 2022"\Pythons\Udemy_12_3_2023_WebServer\"web server"
# 3) already created a venv (virtual inviroment)
# 4) start virtual inviroment  .\Scripts\activate.bat 
# 5) pip install Flask
# 6) flask --app server run --debug

import csv
from flask import Flask, render_template, request, redirect
app = Flask(__name__)

# firstTest
# @app.route('/')
# def hello_word():
#     return render_template('index1.html')

# # Univers Web
# @app.route('/index.html')
# def my_home():
#     return render_template('index.html')

# @app.route('/works.html')
# def works():
#     return render_template('works.html')

# @app.route('/work.html')
# def work():
#     return render_template('work.html')

# @app.route('/contact.html')
# def contact():
#     return render_template('contact.html')

# @app.route('/about.html')
# def about():
#     return render_template('about.html')

# Univse Web Clever way
@app.route('/<string:page_name>')
def html_page(page_name):
    return render_template(page_name )


#write the data from submit to a file called database.txt
def write_to_file(data):
    with open('database.txt', mode='a', newline='') as database:
        email = data["email"]
        subject = data["subject"]
        message = data["message"]
    
        file = database.write(f'\n{email},{subject},{message}')


#write the data from submit to a file called database2.csv
def write_to_csv(data):
    with open('database.csv', mode='a', newline='') as database2:
        email = data["email"]
        subject = data["subject"]
        message = data["message"]
    
        csv_writer = csv.writer(database2, delimiter=';',
                                 quotechar='|', quoting=csv.QUOTE_MINIMAL)
        
        csv_writer.writerow([email,subject,message])


# Submit Button (in contact.html the "Sent" Button print us the data to the cmd terminal)
@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method == 'POST':
        try:
            data = request.form.to_dict()
            print(data)
            write_to_file(data)
            write_to_csv(data)
            return redirect('/thankyou.html')
        except:
            return 'did not save to database'
    else:
        return 'error'