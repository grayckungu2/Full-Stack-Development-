from flask import Flask, current_app, make_response, request, jsonify, g
from models import db, User, Review, Movie
import os

def create_app():
    app = Flask(__name__)
    app.config.from_object('config.Config')
    db.init_app(app)

    @app.before_request
    def app_path():
        g.path = os.path.abspath(os.getcwd())

    @app.route('/', methods=['GET'])
    def index():
        hoster = request.headers.get('Host')
        appname = current_app.name
        response_body = f'''
            <h1>The host for this page is {hoster}</h1>
            <h2>The name of this application is {appname}</h2>
            <h3>The path of this application on the user's device is {g.path}</h3>
        '''

        status_code = 200
        headers = {}

        return make_response(response_body, status_code, headers)

    @app.route('/users', methods=['GET'])
    def get_users():
        users = User.query.all()
        users_data = [{'id': user.id, 'username': user.username} for user in users]
        return jsonify(users_data)

    @app.route('/users', methods=['POST'])
    def create_user():
        data = request.get_json()
        username = data.get('username')
        new_user = User(username=username)
        db.session.add(new_user)
        db.session.commit()
        return jsonify({'message': 'User created successfully'})

    @app.route('/users/<int:user_id>', methods=['PUT'])
    def update_user(user_id):
        data = request.get_json()
        new_username = data.get('username')

        user = User.query.get(user_id)
        if user:
            user.username = new_username
            db.session.commit()
            return jsonify({'message': 'User updated successfully'})
        else:
            return jsonify({'message': 'User not found'})

    @app.route('/users/<int:user_id>', methods=['DELETE'])
    def delete_user(user_id):
        user = User.query.get(user_id)
        if user:
            db.session.delete(user)
            db.session.commit()
            return jsonify({'message': 'User deleted successfully'})
        else:
            return jsonify({'message': 'User not found'})

    @app.route('/users/<int:user_id>/reviews', methods=['GET'])
    def get_user_reviews(user_id):
        reviews = Review.query.filter_by(user_id=user_id).all()
        reviews_data = [{'id': review.id, 'rating': review.rating, 'comment': review.comment} for review in reviews]
        return jsonify(reviews_data)

    @app.route('/users/<int:user_id>/reviews', methods=['POST'])
    def create_review(user_id):
        data = request.get_json()
        movie_id = data.get('movie_id')
        rating = data.get('rating')
        comment = data.get('comment')
        new_review = Review(user_id=user_id, movie_id=movie_id, rating=rating, comment=comment)
        db.session.add(new_review)
        db.session.commit()
        return jsonify({'message': 'Review created successfully'})

    @app.route('/reviews/<int:review_id>', methods=['PUT'])
    def update_review(review_id):
        data = request.get_json()
        new_rating = data.get('rating')
        new_comment = data.get('comment')

        review = Review.query.get(review_id)
        if review:
            review.rating = new_rating
            review.comment = new_comment
            db.session.commit()
            return jsonify({'message': 'Review updated successfully'})
        else:
            return jsonify({'message': 'Review not found'})

    @app.route('/reviews/<int:review_id>', methods=['DELETE'])
    def delete_review(review_id):
        review = Review.query.get(review_id)
        if review:
            db.session.delete(review)
            db.session.commit()
            return jsonify({'message':'Review not found'})
   
   
    @app.route('/movies/<int:movie_id>', methods=['PUT'])
    def update_movie(movie_id):
    data = request.get_json()
    new_title = data.get('title')
    new_release_date = data.get('release_date')
    new_genre = data.get('genre')
    new_director = data.get('director')
    new_description = data.get('description')

    movie = Movie.query.get(movie_id)
    if movie:
        movie.title = new_title
        movie.release_date = new_release_date
        movie.genre = new_genre
        movie.director = new_director
        movie.description = new_description
        db.session.commit()
        return jsonify({'message': 'Movie updated successfully'})
    else:
        return jsonify({'message': 'Movie not found'})

@app.route('/movies/<int:movie_id>', methods=['DELETE'])
def delete_movie(movie_id):
    movie = Movie.query.get(movie_id)
    if movie:
        db.session.delete(movie)
        db.session.commit()
        return jsonify({'message': 'Movie deleted successfully'})
    else:
        return jsonify({'message': 'Movie not found'}) 
       
    return app
    