import redis
from datetime import timedelta
from ratelimit.gcra import is_rate_limited

r  = redis.Redis(host='localhost', port=6379, db=0)
requests = 50


for i in range(requests):
	if is_rate_limited(r, 'admin', 20, timedelta(seconds=60)):
		print("request is limited!")
	else:
		print("request is allowed!")



