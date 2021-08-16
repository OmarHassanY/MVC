"""
Routes and views for the flask application.
"""

from datetime import datetime
from flask import render_template
from FlaskWebProject import app
import pypyodbc

connection = pypyodbc.connect('Driver={SQL Server};Server=.;Database=Books;uid=sa;pwd=root12')

cursor = connection.cursor()    
cursor.execute("SELECT * FROM [ProCSharp].[Books]")    
s = "<table style='border:1px solid red'>"    
for row in cursor:    
    s = s + "<tr>"    
for x in row:    
    s = s + "<td>" + str(x) + "</td>"    
s = s + "</tr>"    
connection.close()    
   
@app.route('/')    
@app.route('/home')    
def home():    
    
    return "<html><body>" + s + "</body></html>" 

