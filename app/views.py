"""
Flask Documentation:     http://flask.pocoo.org/docs/
Jinja2 Documentation:    http://jinja.pocoo.org/2/documentation/
Werkzeug Documentation:  http://werkzeug.pocoo.org/documentation/
This file creates your application.
"""

import os, time
import psycopg2
from app import app, db
from flask import render_template, request, redirect, url_for, flash,json, jsonify,g,session
from forms import LoginForm
from models import UserProfile
from datetime import datetime
from random import getrandbits 
from app.models import UserProfile
from app.forms import LoginForm
from werkzeug.utils import secure_filename



###
# Routing for your application.
###

@app.route('/', methods=["GET", "POST"])
def home():
    
    """Render website's home page."""
    return render_template('home.html')
    
@app.route('/profile/', methods=['POST','GET'])
def add_profile():
    form = LoginForm(request.form)
    if request.method == "POST":
        file = request.files['image']  
        image = secure_filename(file.filename)
        file.save(os.path.join("app/static/uploads", image))
        new_user = UserProfile(form.firstname.data, form.lastname.data,form.username.data, form.age.data, form.gender.data, form.bio.data, image, datetime.now())
        db.session.add(new_user)
        db.session.commit()
        flash('New User Profile created')
        return redirect('/profile/'+str(UserProfile.query.filter_by(username=new_user.username).first().id))
        #return redirect(url_for('list_user_profiles' , id=new_user.id))
    else:
        """Render website's home page."""
        return render_template('add_profile.html', form=form)

      

@app.route('/profiles/',methods=["POST","GET"])
def list_user_profiles():
    users = db.session.query(UserProfile).all()
    list_of_profiles=[]
    for user in users:
        list_of_profiles.append({'username':user.username,'id':user.id})
        if request.method == 'POST' and request.headers['Content-Type']== 'application/json':
            return jsonify(users=userlist)
        return render_template('list_user_profiles.html', users=users)


def timeinfo(entry):
    day = time.strftime("%a")
    date = time.strftime("%d")
    if (date <10):
        date = date.lstrip('0')
    month = time.strftime("%b")
    year = time.strftime("%Y")
    return day + ", " + date + " " + month + " " + year
    
@app.route('/profile/<int:id>', methods=['POST', 'GET'])
def view_individual_profile(id):
    user = UserProfile.query.filter_by(id=id).first()
    if not user:
      flash("No such user")
    else:
      image = '/static/uploads/' + user.image
      if request.method == 'POST' or ('Content-Type' in request.headers and request.headers['Content-Type'] == 'application/json'):
          return jsonify(id=user.id, image=image,firstname=user.firstname, lastname=user.lastname,
          username=user.username,age=user.age,created_on=user.created_on)
      else:
            user = {'id':user.id,'image':image,'firstname':user.firstname, 'lastname':user.lastname,'username':user.username,'age':user.age, 
            'gender':user.gender,'bio':user.bio, 'created_on':timeinfo(user.created_on)}
            return render_template('view_individual_profile.html', user=user)
    return redirect(url_for("profiles"))



@app.route('/about/')
def about():
    """Render the website's about page."""
    return render_template('about.html')



###
# The functions below should be applicable to all Flask apps.
###

@app.route('/<file_name>.txt')
def send_text_file(file_name):
    """Send your static text file."""
    file_dot_text = file_name + '.txt'
    return app.send_static_file(file_dot_text)


@app.after_request
def add_header(response):
    """
    Add headers to both force latest IE rendering engine or Chrome Frame,
    and also to cache the rendered page for 10 minutes.
    """
    response.headers['X-UA-Compatible'] = 'IE=Edge,chrome=1'
    response.headers['Cache-Control'] = 'public, max-age=0'
    return response


@app.errorhandler(404)
def page_not_found(error):
    """Custom 404 page."""
    return render_template('404.html'), 404


if __name__ == '__main__':
    app.run(debug=True,host="0.0.0.0",port="8080")
