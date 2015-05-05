from flask import Flask, render_template, url_for, request, jsonify
from datetime import datetime, timedelta
import time
from random import randint

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/ajaxGetDataSample', methods=['GET'])
def ajaxGetDataSample():
	timePrev = request.args.get('currentDate', 0.0, type=float)
	if int(timePrev) == 0:
		timePrev = datetime.now().replace(microsecond=0)
	else:
		timePrev = datetime.fromtimestamp(timePrev)
	timeNow = datetime.now().replace(microsecond=0)
	secondsCount = timeNow - timePrev
	secondsCount = secondsCount.seconds
	result = []
	for i in xrange(secondsCount * 4):
		j = i / 4
		v = randint(50, 100)
		t = timePrev + timedelta(seconds=j)
		t = time.mktime(t.timetuple())
		result.append(dict(time=t, y=v))

	return jsonify(result=result, secondsCount=secondsCount, start=str(timePrev), end=str(timeNow), 
					_pointer=time.mktime(timeNow.timetuple()))

if __name__ == '__main__':
	app.run(debug=True, host='0.0.0.0')