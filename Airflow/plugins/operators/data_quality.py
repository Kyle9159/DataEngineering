from airflow.hooks.postgres_hook import PostgresHook
from airflow.models import BaseOperator
from airflow.utils.decorators import apply_defaults

class DataQualityOperator(BaseOperator):

    """Operator class for data quality validation.
    
    Params:
        conn_id (str): The Redshift Airflow Conn Id.
        tables (list): The list of tables to be checked.          
    """
    
    ui_color = '#89DA59'

    @apply_defaults
    def __init__(self,
                 conn_id = "",
                 tables = [],
                 *args, **kwargs):

        super(DataQualityOperator, self).__init__(*args, **kwargs)
        self.conn_id = conn_id
        self.tables = tables

    def execute(self, context):
        self.log.info('Data quality validation started...') 
        redshift = PostgresHook(self.redshift_conn_id)    
        for table in self.tables:
            records = redshift.get_records(f'SELECT COUNT(*) FROM {table}')    
            if len(records) < 1 or len(records[0]) < 1 or records[0][0] == 0:
                message = f'Data quality validation failure: table "{table}" is empty'
                self.log.error(message)
                raise ValueError(message)
            self.log.info(f'Data quality validation on table "{table}" passed with {records[0][0]} records') 