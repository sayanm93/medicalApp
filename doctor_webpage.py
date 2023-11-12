from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return "Welcome to the Doctor's Webpage!"

@app.route('/patient_details')
def patient_details():
    # Read patient details from the file or database
    with open("patient_details.txt", "r") as file:
        patient_details = dict(line.strip().split(": ", 1) for line in file)

    return render_template('patient_details.html', patient_details=patient_details)

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
