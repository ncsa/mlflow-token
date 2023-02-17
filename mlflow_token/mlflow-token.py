import sys
import time
import os
import urllib

import requests


def get_keycloak_realm_and_client(mlflow_url: str):
    """
    NCSA Deployments of MLFlow are protected by the OAuth2-proxy sidecar. The OAuth2
    start endpoint redirects to our keycloak instance. Find this redirect and morph the
    redirect URL into a device flow start URL.
    :param mlflow_url:
    :return: A tuple with the device flow url and the mlflow instance's client_id
    """
    keycloak_query = requests.get(f"{mlflow_url}/oauth2/start", allow_redirects=False)
    keycloak_url = urllib.parse.urlparse(keycloak_query.next.url)
    client_id = urllib.parse.parse_qs(keycloak_url.query)['client_id'][0]

    # Blank out the query args
    parts = list(keycloak_url[0:6])
    parts[4] = ''
    device_flow_start_url = urllib.parse.urlunparse(parts)
    return device_flow_start_url, client_id


def run():
    realm_url, client_id = get_keycloak_realm_and_client(os.environ['MLFLOW_TRACKING_URI'])

    r = requests.post(realm_url+"/device", data=[("client_id", client_id)])
    device_code = r.json()['device_code']
    print(f"Visit this link to authorize access to MLFlow instance {client_id}")
    print(r.json()['verification_uri_complete'])

    token_query_url = realm_url.replace("protocol/openid-connect/auth",
                                        "protocol/openid-connect/token")

    token = None
    while not token:
        time.sleep(5)
        r2 = requests.post(
            token_query_url,
            data=[
                ("client_id", client_id),
                ("grant_type", "urn:ietf:params:oauth:grant-type:device_code"),
                ("device_code", device_code)
            ])
        if r2.status_code==200:
            token = r2.json()['access_token']

    os.environ["MLFLOW_TRACKING_TOKEN"] = token

    if "--echo" in sys.argv:
        print(f"export MLFLOW_TRACKING_TOKEN={token}")
