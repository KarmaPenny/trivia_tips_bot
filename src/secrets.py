import boto3
import json
from pydantic import BaseModel, Extra

class Secrets(BaseModel, extra=Extra.allow):
  pass

def load(id: str) -> Secrets:
  session = boto3.session.Session()
  client = session.client(service_name="secretsmanager", region_name=session.region_name)
  secret = client.get_secret_value(SecretId="tomato_jakes_trivia_bot_secrets")
  return Secrets(**json.loads(secret["SecretString"]))
