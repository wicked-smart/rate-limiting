import redis
from datetime import timedelta
from ratelimit.fixed_window import is_rate_limited

r  = redis.Redis(host='localhost', port=6379, db=0)
requests = 25


for i in range(requests):
	if is_rate_limited(r, 'admin', 20, timedelta(seconds=30)):
		print("request is limited!")
	else:
		print("request is allowed!")



