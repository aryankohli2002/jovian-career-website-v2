from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, text
import os
result_dict=[]
db_connection_string = os.environ['DB_CONNECTION_STRING']
engine = create_engine(db_connection_string)

def load_jobs_from_db():
  with engine.connect() as conn:
    result = conn.execute(text("select * from jobs"))
    for row in result.all():
      result_dict.append(row._asdict())
      
  return result_dict
  
def load_job_from_db_with_id(id):
  with engine.connect() as conn:
    result = conn.execute(text("select * from jobs where id=:val"), {"val": id})
    row = result.all()
    if len(row) == 0:
      return None
    else:
      return row[0]._asdict()
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

