
from sqlalchemy import create_engine
import pandas as pd
# zusätzlich das Modul 'mysqlclient' installieren


# Datenquelle: SQL-Tabelle einlesen
user = 'root'
passwd = 'maria'
host = 'localhost'
db = 'ix'

sqlEngine = create_engine(f'mysql+mysqldb://{user}:{passwd}@{host}/{db}')

with sqlEngine.connect() as dbConnection:
    rki_data = pd.read_sql_table('rki_daten', dbConnection)

# diese Option zeigt alle Spalten an
pd.set_option('display.max_columns', None)
print(rki_data.head())
print(rki_data.info())


# Spalten auswaehlen
relevant_columns = ['OBJECTID', 'GEN', 'BEZ', 'EWZ', 'KFL', 'death_rate', 'cases', 'deaths']

with sqlEngine.connect() as dbConnection:
    rki_data_subset = pd.read_sql_table('rki_daten', dbConnection, columns=relevant_columns)

print(rki_data_subset.info())


# Index setzen
with sqlEngine.connect() as dbConnection:
    rki_data_index = pd.read_sql_table('rki_daten', dbConnection, index_col='OBJECTID')

print(rki_data_index.head())


# Datum parsen
rki_format = '%d.%m.%Y, %H:%M Uhr'

with sqlEngine.connect() as dbConnection:
    rki_data_date = pd.read_sql_table('rki_daten', dbConnection, parse_dates={'last_update': {'format': rki_format}})

print(rki_data_date.head())
print(rki_data_date.info())


# Einschraenkungen / where-Klausel
rki_data_niedersachsen = rki_data[rki_data['BL'] == 'Niedersachsen']
print(rki_data_niedersachsen.head())

laender_filter = rki_data['BL'].isin(['Niedersachsen', 'Hamburg', 'Bremen'])
rki_data_laender = rki_data[laender_filter]
print(rki_data_laender.head(100))


# Daten sortieren
rki_data_laender_sort = rki_data_laender.sort_values(by=['EWZ'], ascending=False, na_position='last')
print(rki_data_laender_sort.head(100))


# Distinct values
rki_data_distinct = rki_data['county'].unique()
print(rki_data_distinct)
distinct_values = rki_data['county'].nunique()
print(distinct_values)


# Spalten umbenennen
rki_data_index.rename(columns = {'GEN': 'Name', 'BEZ': 'Bezeichner', 'EWZ': 'Einwohnerzahl', 'KFL': 'Fläche' }, inplace=True)
print(rki_data_index.head(10))

rki_data_index.index.names = ['Index']
print(rki_data_index.head())


# Ergebnisse speichern
with sqlEngine.connect() as dbConnection:
#   kann nur einmal ausgefüht werden
    rki_data_index.to_sql('rki_results', dbConnection, if_exists='fail')
#   Befehl, um weitere Daten anzuhaengen
#   rki_data_index.to_sql('rki_results', dbConnection, if_exists='append')

rki_excel = 'rki_excel_results.xlsx'
rki_data_index.to_excel(rki_excel)


# Daten gruppieren
rki_data_group_01 = rki_data_index.groupby('BL')
print(rki_data_group_01.head(100))

rki_data_group_02 = rki_data_index.sort_values(['BL', 'Name'], ascending=True).groupby(['BL', 'Name'])
print(rki_data_group_02.head(100))


# mit gruppierten Daten rechnen
rki_data_calc_01 = rki_data_index.groupby('BL')['deaths'].sum()
print(rki_data_calc_01.head(16))

rki_data_calc_02 = rki_data_index.groupby(['BL', 'county'])['deaths'].sum().reset_index().groupby(['BL']).mean()
print(rki_data_calc_02.head(100))


# having
rki_data_having = rki_data_index.groupby('BL')['Einwohnerzahl'].sum() > 5000000
rki_data_having = rki_data_having.loc[rki_data_having.values==True]
print(rki_data_having.head(50))

rki_data_having_02 = rki_data_index.groupby('BL')['deaths'].sum() > 5000
rki_data_having_03 = rki_data_index.loc[rki_data_having.values==True and rki_data_having_02==True]
print(rki_data_having_03.head(50))
