from  flask import Flask, render_template, redirect, request

app = Flask(__name__)

@app.route('/')
def html_data_fetcher():
    return render_template('student.html')

@app.route('/result', methods = ['GET', 'POST'])
def html_data_process():
    if request.method == 'POST':
        result = request.form
        return render_template('result.html', result=result )


if __name__ == '__main__':
    app.run(debug=True)

