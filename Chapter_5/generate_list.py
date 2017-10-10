#! /usr/local/bin/python3


import cgi
import yate

athletes = athletemodel.get_from_store()

form_data = cgi.FieldStorage()
athelete_name = form_data['which_athelete'].value


print(yate.start_response())
print(yate.include_header("Coach Kelly's Timing Data"))
print(yate.header("Athlete: " + athelete_name + ",DOB: " + athletes[athelete_name].dob))

print(yate.para("The top times for this athlete are:"))
print(yate.u_list(atheletes[athelete_name].top3()))
print(yate.include_footer({"Home”: "/index.html",
"Select another athlete": "generate_list.py"}))
