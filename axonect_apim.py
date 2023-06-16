import kopf
import logging
from kubernetes import client, config


@kopf.on.create('axp.axonect.com','v1','apims')
def create_apim(body, **kwargs):
    api = client.ApiClient()
    app_api=client.AppsV1Api(api)
    core_api=client.CoreV1Api(api)

    namespace=body['metadata']['namespace']
    name=body['metadata']['name']

@kopf.on.update('axp.axonect.com','v1','apims')
def update_apim(body, **kwargs):
    api = client.ApiClient()
    app_api=client.AppsV1Api(api)
    core_api=client.CoreV1Api(api)

@kopf.on.delete('axp.axonect.com','v1','apims')
def delete_apim(body, **kwargs):
    api = client.ApiClient()
    app_api=client.AppsV1Api(api)
    core_api=client.CoreV1Api(api)

@kopf.on.create('axp.axonect.com', 'v1', 'apis')
def create_api(body, **kwargs):
    api = client.ApiClient()
    app_api=client.AppsV1Api(api)
    core_api=client.CoreV1Api(api)
