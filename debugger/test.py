import argparse
import kubernetes.client as k8s
from kubernetes.client import rest
import requests
from kubernetes.client.api import CustomObjectsApi

class ApimOperator:
    def __init__(self, url, api_manager_host, api_manager_token):
        self.url = url
        self.api_manager_host = api_manager_host
        self.api_manager_token = api_manager_token

    def publish_to_api_manager(self):
        response = requests.get(self.url)
        if response.status_code != 200:
            raise Exception("Failed to download Swagger file")

        swagger_file = response.text

        configuration = k8s.Configuration()
        configuration.host = self.api_manager_host
        configuration.verify_ssl = False

        api_instance = k8s.ApiClient(configuration)
        custom_objects_api = CustomObjectsApi(api_instance)

        api_instance.set_default_header('Authorization', 'Bearer ' + self.api_manager_token)

        try:
            custom_objects_api.create_namespaced_custom_object(
                group="axp.axonect.com",
                version="v1",
                plural="apiartifacts",
                namespace="default",
                body={
                    "apiDefinition": swagger_file,
                    "apiDefinitionType": "SWAGGER",
                    "gatewayLabels": {
                        "label1": "value1",
                        "label2": "value2"
                    }
                }
            )
            print("Swagger file published to Axonect API Manager")
        except rest.ApiException as e:
            print("Exception when calling Axonect API Manager: %s\n" % e)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="APIM Operator")
    parser.add_argument("--url", help="Swagger file")
    parser.add_argument("--host", help="host")
    parser.add_argument("--token", help="token")

    args = parser.parse_args()

    petstore_operator = ApimOperator(args.url, args.host, args.token)
    petstore_operator.publish_to_api_manager()
