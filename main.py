from flask import Flask, render_template, url_for, request, jsonify
from datetime import datetime, timedelta
import time
from random import randint

app = Flask(__name__)

VALUE_PER_SECOND = 4
RAND_MIN = 50
RAND_MAX = 100
START_VALUE_REQUEST = 0

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/ajaxGetDataSample', methods=['GET'])
def ajaxGetDataSample():
	timePrev = request.args.get('currentDate', 0., type=float)
	if int(timePrev) == START_VALUE_REQUEST:
		timePrev = datetime.now().replace(microsecond=0)
	else:
		timePrev = datetime.fromtimestamp(timePrev)
	timeNow = datetime.now().replace(microsecond=0)
	secondsCount = (timeNow - timePrev).seconds
	result = []
	for i in xrange(secondsCount * VALUE_PER_SECOND):
		j = i / VALUE_PER_SECOND
		v = randint(RAND_MIN, RAND_MAX)
		t = timePrev + timedelta(seconds=j)
		t = time.mktime(t.timetuple())
		result.append(dict(time=t, y=v))

	return jsonify(result=result, secondsCount=secondsCount, start=str(timePrev), end=str(timeNow), 
					_pointer=time.mktime(timeNow.timetuple()))

if __name__ == '__main__':
	app.run(debug=True, host='0.0.0.0')