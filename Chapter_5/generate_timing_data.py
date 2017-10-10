#! /usr/local/bin/python3

import cgi




form_data = cgi.FieldStorage()

athelete_name = form_data['which_athelete'].value
