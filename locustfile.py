from locust import HttpUser, task, between

class Prueba(HttpUser):

    @task
    def probar(self):
        self.client.get("/products")