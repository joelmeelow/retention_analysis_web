
from flask import Flask, request, jsonify, render_template, url_for
import os










PEOPLE_FOLDER = os.path.join('static', 'imgs')
# Create flask app
app = Flask(__name__, static_folder='static')
app.config['UPLOAD_FOLDER'] = PEOPLE_FOLDER






@app.route('/')
def show_index():
    full_filename = os.path.join(app.config['UPLOAD_FOLDER'], 'Dashboard 2 sq.png')
    full_filename2 = os.path.join(app.config['UPLOAD_FOLDER'], 'Dashboard 3.png')
   


   
    
    return render_template("index.html", user_image2 = full_filename, user_image3 = full_filename2)






if __name__ == "__main__":
    

    app.run(debug=True)    