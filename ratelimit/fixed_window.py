import redis
from datetime import timedelta

def is_rate_limited(r, key, limit, period):
	if r.setnx(key, limit):
		r.expire(key, int(period.total_seconds()))
	
	bucket_val = r.get(key)
	if bucket_val and int(bucket_val) > 0:
		r.decrby(key, 1)
		return False
	
	return True

