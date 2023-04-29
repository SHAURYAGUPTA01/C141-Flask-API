from flask import jsonify,request,Flask
import csv

all_movies = []
with open("movies.csv" , encoding = "utf-8") as f:
    r  = csv.reader(f)
    data = list(r)
    all_movies = data[1:]
    
like = []
dislike = []
not_watched = []

app = Flask(__name__)


@app.route('/')
def welcome():
    return 'welcome to home page'

@app.route('/get-movie')
def get_movie():
    return jsonify({
        "data" : all_movies[0],
        "status" : "success"
    })

@app.route('/like-movie' ,methods = ["POST"] )
def like_movie():
    global all_movies
    m = all_movies[0]
    all_movies = all_movies[1:]
    like.append(m)
    return jsonify({"status" : "success"}),200

@app.route('/dislike-movies', methods = ["POST"])
def dislike_movies():
    global all_movies
    m = all_movies[0]
    all_movies = all_movies[1:]
    dislike.append(m)
    return jsonify({"status" : "success"}),200

@app.route('/not-watch-movies', methods = ["POST"])
def not_watch_movies():
    global all_movies
    m = all_movies[0]
    all_movies = all_movies[1:]
    not_watched.append(m)
    return jsonify({"status" : "success"}),200

if __name__ == "__main__":
    app.run(debug = True)