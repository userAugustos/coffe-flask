# Coffee-flask

Coffee-flask is an API project designed to connect individuals with the nearest and most highly-rated coffee shops. The project utilizes a database with two main tables: users and locations. Its primary goal is to link users to the most convenient and highly-rated coffee shops based on a sophisticated graph-based search algorithm.

## Features

- **User Management:** Maintain a database of users with relevant information.
- **Location Tracking:** Keep track of coffee shop locations in the database.
- **Graph-Based Searching:** Utilize an efficient graph-based algorithm for effective user-to-coffee shop linkage.
- **Python, Flask, Flask-RESTful, and Pandas:** The project is developed using Python, Flask, Flask-RESTful, and Pandas libraries.

## Installation

1. **Clone the Repository:**
   ```bash
   git clone https://github.com/your-username/Coffee-flask.git
   cd Coffee-flask
  ```

2. **Create a Virtual Environment:**

  ```bash
  python -m venv venv
  ```
3. **Activate the Virtual Environment:**
  - On Windows:
    ```bash
    .\venv\Scripts\activate
    ```
  - On Unix or MacOS::
    ```bash
    source venv/bin/activate
    ```
4. **Install Dependencies:**

  ```bash
  pip install -r requirements.txt
  ```

## Usage

1. **Run the Application:**
  ```bash
  python app.py
  ```