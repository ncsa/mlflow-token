# mlflow-token
Obtain an access token for an MLFlow instance deployed behind OAuth2-proxy and
keycloak. 

This script will use your current setting of `MLFLOW_TRACKING_URI` to look for
the keycloak redirect from it's OAuth2-proxy. From there it will start an
OAuth device flow to allow you to obtain a valid access token. This token will
be set in your environment's `MLFLOW_TRACKING_TOKEN` variable for use by the
MLFlow client libraries.

You can also specify the `--echo` command line argument to get the tool to print
a command for assigning the token to the environment variable.
