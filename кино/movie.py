from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

movies = []

@app.route('/')
def index():
    return render_template('index.html', movies=movies)

@app.route('/add', methods=['POST'])
def add_movie():
    title = request.form['title']
    year = request.form['year']
    genre = request.form['genre']
    
    movie = {
        'title': title,
        'year': year,
        'genre': genre
    }
    movies.append(movie)
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
