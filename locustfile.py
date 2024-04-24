from locust import task, HttpUser


class MemePerformance(HttpUser):

    meme_ids = set()
    token = None

    def on_start(self):
        response = self.client.post('/authorize', json={"name": "Volha"}).json()
        self.token = response['token']

    @task(8)
    def get_all_memes(self):
        self.client.get('/meme', headers={'Authorization': f'{self.token}'})

    @task(1)
    def create_meme(self):
        post_body = {
            "info": {
                "colors": [
                    "brw",
                    "green",
                    "blue"
                ],
                "objects": [
                    "sand",
                    "sun"
                ]
            },
            "tags": [
                "summer",
                "hot"
            ],
            "text": "sunny day",
            "url": "https://media.example.com/"
        }
        response = self.client.post('/meme',
                                    headers={'Authorization': f'{self.token}'},
                                    json=post_body)
        self.meme_ids.add(response.json()['id'])

    def on_stop(self):
        for meme_id in self.meme_ids:
            self.client.delete(f'meme/{meme_id}',
                               headers={'Authorization': f'{self.token}'})
