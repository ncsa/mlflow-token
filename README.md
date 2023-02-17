# mlflow-token
Obtain an access token for an MLFlow instance deployed behind OAuth2-proxy and
keycloak. 

This script will use your current setting of `MLFLOW_TRACKING_URI` to look for
the keycloak redirect from it's OAuth2-proxy. From there it will start an
OAuth device flow to allow you to obtain a valid access token. You can use this
to update your `MLFLOW_TRACKING_TOKEN` by executing the command as
```shell
% export $(mlflow-token)
```
and following the prompt.

