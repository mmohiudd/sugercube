Sugercube
===

Sugercube is the main ingredient for making socail-able py. 

*In other words*

Sugercube is a python library for social media communication. It provides a basic and simple way of communication for your framework so you can concenrtrate on writing framework logic.


**Flavors:**

Currently it is only offered in `Facebook`. Other types will follow soon.


**Run all tests:**

```
	python -m tests

```


**Run a specific flavor's tests:**

```
	python -m tests.< flavor name >

```

*e.g.*

```
	python -m tests.facebook
	
```


**Sample usage:**

```

	from sugercube.settings import SETTINGS
	from sugercube.facebook import Facebook

	facebook = Facebook(SETTINGS['facebook'])

	# 19292868552 is Facebook developers page
	batch = [
            {  # 0
            	'method': "GET",
                'relative_url': """fql?q=SELECT name, fan_count,website
                FROM page WHERE page_id = 19292868552""",
            },
            {  # 1
                'method': "GET",
                'relative_url': """%s?fields=link""" % (SETTINGS['facebook']['app_id']),
            }
        ]	
    
    # graph call returns result data inside the 'data' variable
    body = json.loads(responses[0]['body'])
        
	# graph call returns result data in the body
    body = json.loads(responses[1]['body'])        
        
```



