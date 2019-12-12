from flask import Flask, render_template, redirect
from forms import addStudentForm, searchStudentForm
from flask_pymongo import PyMongo
from bson.objectid import ObjectId


app = Flask(__name__)
app.secret_key = "secret key"
app.config["MONGO_URI"] = "mongodb://localhost:27017/send-project-data"
mongo = PyMongo(app)

@app.route('/')
def stuDetails():
    stuList = mongo.db.studentList.find()
    #return favMovies
    return render_template('viewStudents.html', stuList=stuList)

@app.route('/addStudent', methods=['GET','POST'])
def addStudent():
    form = addStudentForm()

    if form.validate_on_submit():
        form_data = {'_id': form.stuId.data, 
                    'stuFirstName': form.stuFirstName.data, 
                    'stuLastName': form.stuLastName.data, 
                    'stuGender': form.stuGender.data, 
                    'stuYearGroup': form.stuYearGroup.data,
                    'stuFormClass': form.stuFormClass.data,
                    'stuSenStatus': form.stuSenStatus.data,
                    'stuBarrier': form.stuBarrier.data,
                    'stuReadingAge': form.stuReadingAge.data,
                    'stuFullDescription': form.stuFullDescription.data}
        addToDb = mongo.db.studentList.insert(form_data)
        return redirect('/')
    return render_template('addStudent.html', form=form)
'''
@app.route('/searchMovie', methods=['GET','POST'])
def searchMovie():
    form = searchStudentForm()

    if form.validate_on_submit():
        result = mongo.db.userMovies.find({'title':{'$regex':'^'+form.movieTitle.data}})
        return render_template('userMovies.html', favMovies=result)
    return render_template('searchMovie.html', form=form)
'''  
# Added delete route from movie-api
@app.route('/delete/<id>', methods=['POST'])
def delete_movie(id):
    mongo.db.studentList.delete_one({'_id': id})
    return redirect('/')

@app.route('/info/<id>', methods=['GET','POST'])
def stuMoreInfo(id):
    moreInfo = mongo.db.studentList.find({'_id': id})

    return render_template('stuMoreDetails.html', moreInfo = moreInfo)
'''
@app.route('/watched/<id>', methods=['POST'])
def watched_movie(id):
    mongo.db.userMovies.update({'_id':id},{'$set':{'watched': 'true'}})
    return redirect('/')

@app.route('/unwatch/<id>', methods=['POST'])
def unwatch_movie(id):
    mongo.db.userMovies.update({'_id':id},{'$set':{'watched': 'false'}})
    return redirect('/')
'''

if __name__ == '__main__':
    app.run(debug=True, port=5000, host='127.0.0.1')