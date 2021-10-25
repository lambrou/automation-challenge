import time
from locust import HttpUser, task, between

class BoomtownUser(HttpUser):
	wait_time = between(1, 5)
	search_api = 'https://api.preprod.goboomtown.com/sdk/v1/kb/search'
	search_query = '?query=customer'

	def on_start(self):
		self.client.headers = {
			'Origin': search_api,
			'X-Boomtown-Key': '4dZ8mxjtkdLW3KLZJdaP5uHWtjk4eLrBDnLJB2hA6EUS',
			'X-Boomtown-Integration': 'MF49ER'	
		}
		r = self.client.get(self.search_api)

		print(r.cookies)

	@task
	def search(self):
		with self.client.get(self.search_api + self.search_query, catch_response=True, body={'X-Boomtown-Key': '4dZ8mxjtkdLW3KLZJdaP5uHWtjk4eLrBDnLJB2hA6EUS','X-Boomtown-Integration': 'MF49ER'}) as response:
			print(response.text)