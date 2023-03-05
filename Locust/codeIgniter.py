from locust import task, FastHttpUser,TaskSet
from locust.user import wait_time


class websiteUser(FastHttpUser):

   
    host = 'https://codeigniter.herebussiness.com/'

    @task
    def ExcerciseCategories(self):

        response = self.client.get("login")
        self.client.cookiejar.clear()

