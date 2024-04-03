#code working successfully
'''
Installations required -
pip install cloud-sql-python-connector["pymysql"] SQLAlchemy
pip install google-cloud-secret-manager
pip install sqlalchemy
pip install pymysql
'''
#Import required dependencies
from google.cloud.sql.connector import Connector
import sqlalchemy
from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, text
# Function to get CloudSQL instance password from Secret Manager

def access_secret_version(project_id, secret_id, version_id):
    """
    Access the payload for the given secret version if one exists. The version
    can be a version number as a string (e.g. "5") or an alias (e.g. "latest").
    """

    # Import the Secret Manager client library.
    from google.cloud import secretmanager

    # Create the Secret Manager client.
    client = secretmanager.SecretManagerServiceClient()

    # Build the resource name of the secret version.
    name = f"projects/{project_id}/secrets/{secret_id}/versions/{version_id}"

    # Access the secret version.
    response = client.access_secret_version(request={"name": name})
    # Print the secret payload.
    # snippet is showing how to access the secret material.
    payload = response.payload.data.decode("UTF-8")
    return payload

# Function call to get DB password ino a local varaiable  
db_password = access_secret_version('trim-silicon-419117', 'google_cloud_mysql_password','1')

# initialize Connector object
connector = Connector()

# function to return the database connection
def getconn():
    conn= connector.connect(
        "trim-silicon-419117:us-west1:demo-sql", #cloud sql instance details
        "pymysql",
        user="aryan",
        password=db_password,
        db="jovian"
    )
    return conn
# create connection pool
pool = sqlalchemy.create_engine(
    "mysql+pymysql://",
    creator=getconn,
)

# interact with Cloud SQL database using connection pool
with pool.connect() as conn:
  result = conn.execute(text("select * from jobs"))
  print(result.all())