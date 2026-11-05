from locust import HttpUser, task, between

class Prueba(HttpUser):

    @task
    def probar(self):
        self.client.get("/products") #En la interfaz web en el host se pone https://fakestoreapi.com