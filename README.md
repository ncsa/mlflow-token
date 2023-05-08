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

## Usage In Jupyter Notebook
If you want to authenticate to an MLFlow instance from within a Jupyter notebook
you can add the following lines to a cell:
```python
import mlflow_token
mlflow_token.setup_mlflow_environment("https://mlflow-demo.software-dev.ncsa.illinois.edu/")
```
This will update the notebook's `os.environ` so you can immediately use the 
mlflow SDK. The token will eventually expire, so you may need to occasionally 
re-run the cell.

The cell will print the url for the user to visit and wait for the device
flow to complete.
