##
The flask backend  application  is a Movie Review system. 
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
PUT '/movies/<int:movie_id>' : update_movie
_first  we retrieve the movie ID from the URL parameter. After that we get the JSON data from the request body, which contains the updated movie information such as title, release date, genre, director, and description.
_ lastly we use  queries the database to find the movie with the particular ID. If the movie exists, it updates its attributes with the new values from the JSON data. Finally, changes are committed  to the database and returns a JSON response indicating the success of the update operation.
 DELETE `/movies/<movie_id  
 _It retrieves the movie ID from the URL parameter and queries the database to find the movie. If the movie exists, it deletes it from the database and commits the changes. This  function will later returns a JSON response indicating the success of the delete operation.

## The relationships between the models are as follows:
- Each User can have multiple Reviews (one-to-many relationship).
- Each Review belongs to a User and a Movie (many-to-one relationship).
- Each Movie can have multiple Reviews (one-to-many relationship).



##





