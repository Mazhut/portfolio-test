from flask import Flask, render_template, url_for, request, redirect
import csv
app = Flask(__name__)


if __name__ == "__main__":
    app.run(port=8000, debug=True)


@app.route('/index.html')
def my_home():
    return render_template('index.html')


# def write_to_file(data):
#     with open('database.txt', mode='a') as database:
#         email = data['email']
#         subject = data['subject']
#         message = data['message']
#         file = database.write(f'\n{email}, {subject}, {message}')


def write_to_csv(data):
    with open('database.csv', mode='a') as database2:
        email = data['email']
        subject = data['subject']
        message = data['message']
        csv_writer = csv.writer(database2, delimiter=',', quotechar='"', quoting=csv.QUOTE_NOTNULL)
        csv_writer.writerow({email, subject, message})


@app.route('/<string:page_name>')
def html_page(page_name):
    return render_template(page_name)


@app.route('/submit_form', methods=['GET', 'POST'])
def submit_form():
    if request.method == 'POST':
        try:
            data = request.form.to_dict()
            write_to_csv(data)
            return redirect('thankyou.html')
        except BaseException:
            return 'Did not save to database'
    else:
        return 'Something went wrong. Try again'
