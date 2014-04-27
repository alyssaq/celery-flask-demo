# Celery Demo
Mini Flask app using celery.   
Broker tested with ironmq, redis, mongodb.  
Save results with redis, mongodb.  

## Run the celery worker

    $ celery -A tasks worker -E

## Start the Flask app

    $ python app.py

Open your browser at `0.0.0.0:5000`