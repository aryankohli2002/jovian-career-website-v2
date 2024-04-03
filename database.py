from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, text
import os
result_dict=[]
db_connection_string = os.environ['DB_CONNECTION_STRING']

def load_jobs_from_db():
  engine = create_engine(db_connection_string)
  with engine.connect() as conn:
    result = conn.execute(text("select * from jobs"))
    for row in result.all():
      result_dict.append(row._asdict())
      
  return result_dict
  
  

# # Construct the connection URL
# connection_url = f"mysql+mysqldb://aryan@/jovian?unix_socket=/cloudsql/trim-silicon-419117:demo-sql"

# # Create the SQLAlchemy engine
# engine = create_engine(connection_url)

# # engine = create_engine(
# #     "mysql+mysqld://aryan:1234@34.83.3.64/jovian",
# #     connect_args={
# #         "ssl": {
# #             "ca": "/home/gord/client-ssl/ca.pem",
# #             "cert": "/home/gord/client-ssl/client-cert.pem",
# #             "key": "/home/gord/client-ssl/client-key.pem"
# #         }
# #     }
# # )

