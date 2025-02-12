from locust import HttpUser, task


class MyUser(HttpUser):
    def on_start(self):
        response = self.client.post(
            "/accounts/api/v2/jwt/create/",
            data={"email": "erfan6235@gmail.com", "password": "123"},
        ).json()
        self.client.headers = {"Authorization": f"Bearer {response.get('access',None)}"}

    @task
    def post_list(self):
        self.client.get("/blog/api/v1/post/")

    @task
    def post_category(self):
        self.client.get("/blog/api/v1/category/")
