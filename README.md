### Objective

Pokémon Battlefield 

Implement and code a program that receives the names of 2 pokemons and simulates a battle between the two, the winner will be decided by a calculation of the stats.change field.
Besides this, you should show each pokemons ID card by fetching data from the pokeapi.co for the certain given name .
- Expose an API to start a battle 
- Use models for the pokemons
- The program should handle errors.
- The project should include tests and documentation 

PokéAPI (pokeapi.co)

## Prerequisites
- Python 3.7 or above installed on your system

## Installation
1. Clone the repository to your local machine or download and extract the ZIP file.
2. Open a terminal or command prompt and navigate to the project's root directory.

### Virtual Environment (optional)
1. It's recommended to create a virtual environment to keep the project dependencies isolated. Run the following command to create a new virtual environment named "env":
    ```
    python3 -m venv env
    ```

2. Activate the virtual environment:
- For Windows:
  ```
  env\Scripts\activate
  ```
- For macOS/Linux:
  ```
  source env/bin/activate
  ```

### Install Dependencies
1. Install the required dependencies by running the following command:
    ```
    pip install -r requirements.txt
    ```

### Database Setup (optional)
1. Set up your preferred database (e.g., SQLite, MySQL, PostgreSQL). Default is SQLite.
2. Update the `SQLALCHEMY_DATABASE_URI` configuration in the `app.py` file with the appropriate database connection string.

## Running the Application
1. Run the following command to start the application:
    ```
    python run.py
    ```

2. The Flask development server will start running locally on `http://localhost:5000`.

## API Documentation
You may access the API documentation under http://localhost:5000/api/docs/. The documentation provides details about each endpoint, including the supported HTTP methods, input parameters, response formats, and example requests/responses. It also describes the purpose and functionality of each endpoint, allowing you to understand how to interact with the POKEMON API

## API Endpoints
- **GET /pokemon/{name}**: Fetches information about a Pokémon based on its name.
- **POST /pokemon/battle**: Simulates a battle between two Pokémon.


## Running Tests

1. To run the tests, open a terminal or command prompt and navigate to the project's root directory.
2. Run the following command:
    ```
    pytest tests
    ```
    
    The tests will be executed, and the results will be displayed in the terminal.

## Code

The code for the Pokémon Battle program is organized as follows:

- `app.py`: The main application file that runs the Flask server and handles routing.
- `api.py`: Contains the Flask routes and API endpoints for fetching Pokémon information and simulating battles.
- `models.py`: Defines the Pokémon model using SQLAlchemy for database storage.
- `database.py`: Provides functions for interacting with the database, including storing and retrieving Pokémon information.
- `battle_logic.py`: Contains the battle simulation logic and functions for calculating damage and selecting moves.
- `static/openapi.json`: OpenAPI specification file describing the API endpoints.

