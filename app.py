import os
from celery.result import BaseAsyncResult
from flask import Flask, redirect, request, session, render_template
import tasks

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/queue', methods=['POST'])
def queue():
    res = tasks.add.delay(int(request.form.get('num1', 0)), 
      int(request.form.get('num2', 0)))
    print(res.id)

    return redirect('/result/' + res.id)

@app.route('/result/<key>')
def result(key):
    print(key)
    result = BaseAsyncResult(key, app=tasks.celery)

    if result.ready():
        print(result.get())
        return render_template('result.html', result=result.get())
    elif result.failed():
        return result.traceback
    else:
        return render_template('processing.html')

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=True)
