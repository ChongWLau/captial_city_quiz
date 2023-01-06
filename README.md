# captial_city_quiz

## Setup

Create and activate virtual environment

```
python3 -m venv venv
source venv/bin/activate
```

Install requirements

```
make install
```

Load the database with countries and their capitals (will also clear any old data beforehand)

```
make load_db
```

Note: for functional reasons, the countries with no capitals will be omitted from this load command.


## Running Locally

Running the service

```
make service
```

Access the quiz by clicking [here](http://127.0.0.1:8000/quiz/) or opening a new browser tab and going to:

```
http://127.0.0.1:8000/quiz/
```


## Testing

To run tests

```
make test
```


## Extra

If you want to clear the database at any point

```
make clear_db
```
