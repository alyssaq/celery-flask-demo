# Celery Demo
Mini Flask app using celery.   
Broker tested with ironmq, redis, mongodb.  
Save results with redis, mongodb.  

## Running

To run the demo:

#### 1. Clone the repo

    $ git clone git@github.com:alyssaq/celery-flask-demo.git

#### 2. Run the celery worker

    $ celery -A tasks worker -E

#### 3. Start the Flask app

    $ python app.py

#### 4. Open your browser at `0.0.0.0:5000` and add numbers!
