from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/')
def upload_form():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload_file():
    if request.method == 'POST':
        f = request.files['file']
        f.save(f.filename)  # Saves the file in the current directory
        return 'File uploaded successfully!'

if __name__ == '__main__':
    app.run(debug=True)
