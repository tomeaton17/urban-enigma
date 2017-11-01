# -*- coding: utf-8 -*-
import sys, os
from pprint import pprint


# For now this solution should suffice
# All new modules we create should go here
# as paths

sys.path.append(os.path.join(sys.path[0], 'bot/src'))


# New imports should be done in the following manner
from instabot import InstaBot

from app import app


app = app

if __name__ == '__main__':
    app.run(debug=True)
    

