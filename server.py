from flask import Flask, render_template, request, redirect
import csv
app = Flask(__name__)

print(__name__)


# @app.route('/<username>/<int:post_id>')
# def hello_world(username, post_id=None):
#     return render_template('index.html', name=username, post_id=post_id)

@app.route('/')
def home():
    return render_template('index.html')


@app.route('/<string:page_name>')
def html_page(page_name):
    return render_template(page_name)


def write_to_file(data):
    with open('database.txt', mode='a') as database:
        email = data["email"]
        subject = data['subject']
        message = data['message']
        file = database.write(f'\n{email},{subject},{message}')


def write_to_csv(data):
    with open('database.csv', newline='', mode='a') as csv_file:
        email = data["email"]
        subject = data['subject']
        message = data['message']
        csv_writer = csv.writer(csv_file, delimiter='|',
                                quotechar='"',  quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow([email, subject, message])


@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method == 'POST':
        try:
            data = request.form.to_dict()
            # print(data)
            write_to_file(data)
            write_to_csv(data)
            return redirect('/thankyou.html')
        except:
            return 'did not save to database'
    else:
        print('Something is wrong')
    return 'form submitted!!!'
