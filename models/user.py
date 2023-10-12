#!/usr/bin/env python3
''' Contains user class '''

from models.base_model import BaseModel

class User(BaseModel):
    ''' A user of hbnb '''

    class_att_dict = {email':str, 'password':str, 'first_name': str, 'last_name': str}

    email = ''
    password = ''
    first_name = ''
    last_name = ''
