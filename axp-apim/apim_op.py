import logging
from random import random
from venv import logger
import kopf
from kubernetes import client, config
import asyncio

config.load_kube_config()

@kopf.on.create('axp.axonect.com', 'v1', 'apis')
def create_api(body, **kwargs):
    api = client.ApiClient()
    core_v1_api = client.CoreV1Api(api)
    app_v1_api = client.AppsV1Api(api)

    namespace = body['metadata']['namespace']
    name = body['metadata']['name']
    swaggerConfig = body['spec']['swaggerConfigMapName']
    