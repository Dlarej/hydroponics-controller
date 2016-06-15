from flask import Flask, request, render_template
from redis import Redis

app = Flask(__name__)
redis = Redis(host='redis', port=6379)

@app.route('/')
def index():
    return "Welcome to Superfood Minifarms!"

@app.route('/monitor', methods=['GET'])
def monitor():
    params = get_monitor_params()
    return render_tamplate("monitor.html", params=params)

@app.route('/controller', methods=['GET','POST'])
def controller():
    if request.method == 'POST':
        redis.set('temp', request.form['temp'])        
        redis.set('light', request.form['light'])        
        redis.set('humid', request.form['humid'])        
        redis.set('fan', request.form['fan'])

    params = get_monitor_params()
    return render_template("controller.html", params=params)

def get_monitor_params():
    params = {}
    params['temp'] = int(redis.get('temp'))
    params['light'] = str(redis.get('light'))
    params['humid'] = str(redis.get('humid'))
    params['fan'] = str(redis.get('fan'))
    return params

if __name__ == "__main__":
    app.run(host="0.0.0.0",debug=True)
