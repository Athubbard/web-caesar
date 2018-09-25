from flask import Flask, request
from caesar import rotate_string

app = Flask(__name__)
app.config['DEBUG'] = True

form= """
<!DOCTYPE html>

<html>
    <head>
        <style>
            form {{
                background-color: #eee;
                padding: 20px;
                margin: 0 auto;
                width: 540px;
                font: 16px sans-serif;
                border-radius: 10px;
            }}
            textarea {{
                margin: 10px 0;
                width: 540px;
                height: 120px;
            }}
        </style>
    </head>
    <body>
rotate_form 
    <form method= "post">
        <label for= "rotated_character">
            Rotate by:
            <br>
            <input type="text" id="rotated_character" value='0' name="rot"/>
            <br>
            <textarea name="text">{0}</textarea>
        </label>
            <input type="submit" value="submit query"/>
    </form>
    </body>
</html>
"""



@app.route("/")
def index():
    return form.format("")
@app.route("/" , methods=['POST'])
def encrypt():
    rotate = int(request.form['rot'])
    text= str(request.form['text'])
    encrypt= rotate_string(text,rotate)

    return form.format(encrypt)



app.run()    
