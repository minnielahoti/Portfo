from flask import Flask, render_template, request,redirect
import csv
from datetime import datetime
app = Flask(__name__) #The Flask class is being used to instantiate app
print(__name__)


@app.route('/')
def my_home():
  return render_template('index.html')#this function looks for the file index in a folder labeled Template. That's just how it works

@app.route('/<string:page_name>')
def html_page(page_name):
  return render_template(page_name)
#Instead of using the following code, we want to make it dynamic
'''
@app.route('/index.html')
def my_home():
	return render_template('index.html')#this function looks for the file index in a folder labeled Template. That's just how it works

@app.route('/works.html')
def my_works():
	return render_template('works.html')#this function looks for the file index in a folder labeled Template. That's just how it works

@app.route('/work.html')
def my_work():
	return render_template('work.html')#this function looks for the file index in a folder labeled Template. That's just how it works


@app.route('/about.html')
def my_aboutme():
	return render_template('about.html')#this function looks for the file index in a folder labeled Template. That's just how it works

@app.route('/contact.html')
def contact():
	return render_template('contact.html')#this function looks for the file index in a folder labeled Template. That's just how it works

@app.route('/components.html')
def components():
	return render_template('components.html')#this function looks for the file index in a folder labeled Template. That's just how it works
'''

@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
  if request.method == 'POST':
    data = request.form.to_dict()
    data['date'] = datetime.now().date()
    data['time'] = datetime.now().time()
    print(data)
    
    with open('database.csv','a',newline = '') as csvfile:
      fieldnames = ['email','subject','message','date','time']
      writer = csv.DictWriter(csvfile,fieldnames)
      writer.writeheader()
      writer.writerow(data)
    
  
    return redirect('/thankyou.html')
  else:
    return 'something went wrong'
