import matplotlib.pyplot as plt
import os
import pandas as pd

def caso_who(ruta_archivo_csv: str)-> dict:
    try:    
        path = pd.read_csv(ruta_archivo_csv)
        root_ext = os.path.splitext(path)
        if root_ext[1] == '.csv' :
            df_virus = pd.read_csv(ruta_archivo_csv)
            # df = pd.read_csv('path',index_col='date')
            df_virus['date']=pd.to_datetime(df_virus['date'],infer_datetime_format=True)
            df_virus['cambio']=((df_virus['total_cases_per_million']*df_virus['population'])/1000000) / ((df_virus['hospital_beds_per_thousand']*df_virus['population'])/1000)
            # dataframe nuevo
            df = pd.DataFrame({'date':df_virus['date'],'reason':df_virus['cambio'],'continent':df_virus['continent']})
            df.set_index('date', inplace=True)
            # grouped = df.groupby('continent')
            df_group = df.groupby(['date','continent'])['reason'].mean().reset_index()
            df_respuesta = df_group.pivot(index='date', columns='continent', values='reason')
            df_respuesta
            df_respuesta.plot()  
            return df_respuesta.to_dict()
        else:
            return 'Extensión inválida.'
    except:
        return 'Error al leer el archivo de datos.'



import pandas as pd

def caso_who(ruta_archivo_csv: str)-> dict:
    try:    
        if  ruta_archivo_csv[-4:] == '.csv' :
            df_virus = pd.read_csv(ruta_archivo_csv)
            # df = pd.read_csv('path',index_col='date')
            df_virus['date']=pd.to_datetime(df_virus['date'],infer_datetime_format=True)
            df_virus['cambio']=((df_virus['total_cases_per_million']*df_virus['population'])/1000000) / ((df_virus['hospital_beds_per_thousand']*df_virus['population'])/1000)
            # dataframe nuevo
            df = pd.DataFrame({'date':df_virus['date'],'reason':df_virus['cambio'],'continent':df_virus['continent']})
            df.set_index('date', inplace=True)
            # grouped = df.groupby('continent')
            df_group = df.groupby(['date','continent'])['reason'].mean().reset_index()
            df_respuesta = df_group.pivot(index='date', columns='continent', values='reason')
            df_respuesta
            df_respuesta.plot()  
            return df_respuesta.to_dict()
        else:
            return 'Extensión inválida.'
    except:
        return 'Error al leer el archivo de datos.'




# df['date']=pd.to_datetime(df['date'],infer_datetime_format=True)
# df['reason'] = ((df['total_cases_per_million']/1000000) / (df['hospital_beds_per_thousand']/1000))
# df_resultado = df.groupby(['date','continent']).plot(kind ='bar')
# df_resultado

#

# print(type(df))
# print(df.dtypes)
# print(df.columns)
# print(df.index)
# print(pd.unique(df['location']))
# print(pd.unique(df['continent']))
# head = df.head()
# tail = df.tail()
# sampling = df.sample()
# information = df.info()
# estatistics = df.describe()
# metric_ind = df['country'].std()


# grouped = df.groupby('continent')
# grouped_estx = grouped.describe()
# grouped_metind = grouped.mean()


# serialize_date = df.date
# serialize_country = df.location
# serialize_continent = df.continent

# serialize_country.value_counts().plot(kind ='bar')
# serialize_continent.value_counts().plot(kind ='bar')

# df.value_counts(dropna = False)
# print(information)
