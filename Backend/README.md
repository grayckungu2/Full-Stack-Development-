##
The flask backend  application  is a Movie Review system.  It uses SQLAlchemy as an ORM to define and manage the database models.

our application has the following functionalities  

## User Management:
   - GET `/users`: Retrieves a list of all users.
   - POST `/users`: Creates a new user.
   - PUT `/users/<user_id>`: Updates an existing user.
   - DELETE `/users/<user_id>`: Deletes an existing user.

# Review Management:
   - GET `/users/<user_id>/reviews`: Retrieves all reviews for a specific user.
   - POST `/users/<user_id>/reviews`: Creates a new review for a specific user.
   - PUT `/reviews/<review_id>`: Updates an existing review.
   - DELETE `/reviews/<review_id>`: Deletes an existing review.
## Movie management
PUT '/movies/<int:movie_id>' : update_movie`first retrieves the movie ID from the URL parameter. It then gets the JSON data from the request body, which contains the updated movie information such as title, release date, genre, director, and description.
. Next, we use  queries the database to find the movie with the given ID. If the movie exists, it updates its attributes with the new values from the JSON data. Finally, it commits the changes to the database and returns a JSON response indicating the success of the update operation.
 DELETE `/movies/<movie_id  It retrieves the movie ID from the URL parameter and queries the database to find the movie. If the movie exists, it deletes it from the database and commits the changes. The function then returns a JSON response indicating the success of the delete operation.

## The relationships between the models are as follows:
- Each User can have multiple Reviews (one-to-many relationship).
- Each Review belongs to a User and a Movie (many-to-one relationship).
- Each Movie can have multiple Reviews (one-to-many relationship).



##





