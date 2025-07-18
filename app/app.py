from flask import Flask,render_template,jsonify

app = Flask(__name__)
Typ_jobs=[
    {'id':2,
     'title':'Data Scientist',
    'location':'New York, NY',
    'salary':'$40000'},
    {'id':3,
         'title':'Business Analyst',
        'location':'Bengaluru, India',
        'salary':'$40000'},
    {'id':4,
         'title':'Data Analyst',
        'location':'San Francisco, us',
        'salary':'$46000'},
    {'id':5,
         'title':'Machine Learning Engineer',
        'location':'London, UK',
        'salary':'$50000'},
    {'id':6,
         'title':'Statistician',
        'location':'Manchester'   ,
        'salary':'$44000'},
    ]
@app.route('/')
def home():
    return render_template('home.html',jobs=Typ_jobs)

@app.route('/api/jobs')
def list_jobs():
    return jsonify(Typ_jobs)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000,debug=True)
