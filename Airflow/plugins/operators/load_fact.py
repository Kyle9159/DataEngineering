from airflow.hooks.postgres_hook import PostgresHook
from airflow.models import BaseOperator
from airflow.utils.decorators import apply_defaults

class LoadFactOperator(BaseOperator):
    
    """Airflow operator for loading data into the fact table.
    
    Params:
        conn_id (str): The Redshift Airflow Conn Id.
        sql (str): SQL code to execute. 
    """

    ui_color = '#F98866'

    @apply_defaults
    def __init__(self,
                 conn_id = "",
                 sql = "",
                 *args, **kwargs):

        super(LoadFactOperator, self).__init__(*args, **kwargs)
        self.conn_id = conn_id
        self.sql = sql

    def execute(self, context):
        self.log.info('Insert data into fact table: playsongs')
        redshift = PostgresHook(self.conn_id)        
        redshift.run(self.sql)
