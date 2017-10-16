from flask import Flask, render_template
import views.instagram as my_g
import os
app = Flask(__name__, template_folder='../templates')


@app.route('/')
def index():
    user_name = os.environ['USER_NAME']
    bryoh = my_g.Profile(user_name)

    return render_template('index.html',
                          div=bryoh)


if(__name__ == '__main__'):
    app.run(debug=True)
