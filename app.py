from flask import Flask, render_template
import views.instagram as my_g
import os
app = Flask(__name__)


@app.route('/')
def index():
    user_name = os.environ['USER_NAME']
    bryoh = my_g.Profile(user_name)
    return render_template('index.html',
                          user=bryoh.username, followers=bryoh.followers,
                           following=bryoh.follows,
                           pp=bryoh.profile_picture_link, bio=bryoh.bio
                           )


if(__name__ == '__main__'):
    app.run(debug=True)
