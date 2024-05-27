
import pandas as pd
import sqlalchemy # pip install mysqlclient

relevant_columns = ['OBJECTID', 'GEN', 'BEZ', 'EWZ', 'KFL', 'death_rate', 'cases', 'deaths', 'cases_per_100k', 'cases_per_population', 'BL', 'BL_ID', 'county', 'last_update', 'cases7_per_100k']
rki_data = pd.read_csv('RKI_Corona_Landkreise.csv', usecols=relevant_columns)

engine = sqlalchemy.create_engine("mysql+mysqldb://root:maria@localhost/ix")
con = engine.connect()

table_name = 'rki_daten'
rki_data.to_sql(table_name, con, if_exists = 'append', index = False)
