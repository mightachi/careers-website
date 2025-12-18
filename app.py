from flask import Flask, render_template

app = Flask(__name__)

JOBS = [
    {
        'id': 1,
        'title': 'Software Engineer',
        'location': 'San Francisco, CA',
        'salary': '$120,000 - $180,000'
    },
    {
        'id': 2,
        'title': 'Product Manager',
        'location': 'New York, NY',
        'salary': '$100,000 - $150,000'
    },
    {
        'id': 3,
        'title': 'Data Analyst',
        'location': 'Remote',
        'salary': '$80,000 - $120,000'
    },
    {
        'id': 4,
        'title': 'UX Designer',
        'location': 'Austin, TX',
        'salary': '$90,000 - $130,000'
    }
]

@app.route('/')
def home():
    return render_template('home.html', jobs=JOBS, company_name='Acme Corp')

@app.route('/job/<int:job_id>')
def job_detail(job_id):
    job = next((j for j in JOBS if j['id'] == job_id), None)
    return render_template('job.html', job=job, company_name='Acme Corp')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
