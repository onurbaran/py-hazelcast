# py-hazelcast (alpha)

Basic python-hazelcast client over Hazelcast's REST API.
py-hazelcast supports only basic map operations now. Queue support will be developed as soon.

### My Hazelcast & py-hazelcast Use Case : 

data --> (n) app servers (prepare to map/reduce process with Hazelcast) --> Spark (py-spark) --> S3, dashboard and reporting
										  		
I'm using Hazelcast for a real time event processing & streaming project. 
Raw data formattig and first-level basic parsing operations runs on Hazelcast. 
Application runs (n) server with Hazelcast on AWS with ASG. (application scales up/down according to real time data volume or size)

Every instance knows what kind of data is streaming, which key(s) are unformatted etc with py-hazelcast. 

	



