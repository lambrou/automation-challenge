import time
from locust import HttpUser, task, between

class BoomtownUser(HttpUser):
	wait_time = between(1, 5)
	search_api = 'https://api.preprod.goboomtown.com/sdk/v1/kb/search'
	search_query = '?query=customer'

	def on_start(self):
		self.client.headers = {
			'X-Boomtown-Key': 'f7LrK5AfEfVyX8vmClqtrtYGCzrcUBk8CYVU2PMzfNm5',
			'X-Boomtown-Integration': 'TBYS9Q'	
		}
		
		r = self.client.get(self.search_api)

	@task
	def search(self):
		with self.client.get(self.search_api + self.search_query, catch_response=True) as response:
			rJson = response.json()
			print(rJson)
			assert rJson['success'] is True
			