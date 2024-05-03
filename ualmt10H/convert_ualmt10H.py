import pandas as pd
import numpy as np
from os.path import join
from nilmtk.datastore import Key
from nilmtk.measurement import LEVEL_NAMES
from nilmtk.utils import check_directory_exists, get_datastore, get_module_directory
from nilm_metadata import convert_yaml_to_hdf5
from copy import deepcopy

def reindex_fill_na(df, idx):
    df_copy = deepcopy(df)
    df_copy = df_copy.reindex(idx)

    power_columns = [
        x for x in df.columns if x[0] in ['power']]
    non_power_columns = [x for x in df.columns if x not in power_columns]

    for power in power_columns:
        df_copy[power].fillna(0, inplace=True)
    for measurement in non_power_columns:
        df_copy[measurement].fillna(df[measurement].median(), inplace=True)

    return df_copy


column_mapping = {
    'W': ('power', 'active'),
    'A': ('current', ''),
    'PF': ('pf', ''),
    'VA': ('power', 'apparent'),
    'VAR': ('power', 'reactive'),
    'VLN': ('voltage', ''),
    'f': ('frequency', ''),
    'VH1': ('voltage', 'armonic1'),
    'VH3': ('voltage', 'armonic3'),
    'VH5': ('voltage', 'armonic5'),
    'VH7': ('voltage', 'armonic7'),
    'VH9': ('voltage', 'armonic9'),
    'VH11': ('voltage', 'armonic11'),
    'VH13': ('voltage', 'armonic13'),
    'VH15': ('voltage', 'armonic15'),
    'VH17': ('voltage', 'armonic17'),
    'VH19': ('voltage', 'armonic19'),
    'VH21': ('voltage', 'armonic21'),
    'VH23': ('voltage', 'armonic23'),
    'VH25': ('voltage', 'armonic25'),
    'VH27': ('voltage', 'armonic27'),
    'VH29': ('voltage', 'armonic29'),
    'VH31': ('voltage', 'armonic31'),
    'VH33': ('voltage', 'armonic33'),
    'VH35': ('voltage', 'armonic35'),
    'VH37': ('voltage', 'armonic37'),
    'VH39': ('voltage', 'armonic39'),
    'VH41': ('voltage', 'armonic41'),
    'VH43': ('voltage', 'armonic43'),
    'VH45': ('voltage', 'armonic45'),
    'VH47': ('voltage', 'armonic47'),
    'VH49': ('voltage', 'armonic49'),
    'IH1': ('current', 'armonic1'),
    'IH3': ('current', 'armonic3'),
    'IH5': ('current', 'armonic5'),
    'IH7': ('current', 'armonic7'),
    'IH9': ('current', 'armonic9'),
    'IH11': ('current', 'armonic11'),
    'IH13': ('current', 'armonic13'),
    'IH15': ('current', 'armonic15'),
    'IH17': ('current', 'armonic17'),
    'IH19': ('current', 'armonic19'),
    'IH21': ('current', 'armonic21'),
    'IH23': ('current', 'armonic23'),
    'IH25': ('current', 'armonic25'),
    'IH27': ('current', 'armonic27'),
    'IH29': ('current', 'armonic29'),
    'IH31': ('current', 'armonic31'),
    'IH33': ('current', 'armonic33'),
    'IH35': ('current', 'armonic35'),
    'IH37': ('current', 'armonic37'),
    'IH39': ('current', 'armonic39'),
    'IH41': ('current', 'armonic41'),
    'IH43': ('current', 'armonic43'),
    'IH45': ('current', 'armonic45'),
    'IH47': ('current', 'armonic47'),
    'IH49': ('current', 'armonic49'),
    'PH1': ('power', 'armonic1'),
    'PH3': ('power', 'armonic3'),
    'PH5': ('power', 'armonic5'),
    'PH7': ('power', 'armonic7'),
    'PH9': ('power', 'armonic9'),
    'PH11': ('power', 'armonic11'),
    'PH13': ('power', 'armonic13'),
    'PH15': ('power', 'armonic15'),
    'PH17': ('power', 'armonic17'),
    'PH19': ('power', 'armonic19'),
    'PH21': ('power', 'armonic21'),
    'PH23': ('power', 'armonic23'),
    'PH25': ('power', 'armonic25'),
    'PH27': ('power', 'armonic27'),
    'PH29': ('power', 'armonic29'),
    'PH31': ('power', 'armonic31'),
    'PH33': ('power', 'armonic33'),
    'PH35': ('power', 'armonic35'),
    'PH37': ('power', 'armonic37'),
    'PH39': ('power', 'armonic39'),
    'PH41': ('power', 'armonic41'),
    'PH43': ('power', 'armonic43'),
    'PH45': ('power', 'armonic45'),
    'PH47': ('power', 'armonic47'),
    'PH49': ('power', 'armonic49'),
}




#mMUY IMPORTANTE : DEBEMOS CAMBIAR LA FECHA DE INICIO Y FIN DE LA TOMA DE LAS MUESTRAS 

TIMESTAMP_COLUMN_NAME = "timestamp"
TIMEZONE = "Europe/Berlin" 
#START_DATETIME, END_DATETIME = '2022-11-23', '2022-11-23'



FREQ = "1T"
#old= 1T  nueva 1S

def convert_ualmt2(ualmt_path, output_filename,START_DATETIME, END_DATETIME, format="HDF"):
    """
    Parameters
    ----------
    ualmt_path : str
        The root path of the ualmt dataset.
    output_filename : str
        The destination filename (including path and suffix).
    """

    print ('**********************************************************************')
    print ('**   CARGA DE LOS FICHEROS DE MEDIDAS  OBVIANDO LOS ARMONICOS PARES **')  
    print ('**********************************************************************')
    print()

    check_directory_exists(ualmt_path)
    idx = pd.date_range(start=START_DATETIME, end=END_DATETIME, freq=FREQ)
    idx = idx.tz_localize('GMT').tz_convert(TIMEZONE)

    # Open data store
    store = get_datastore(output_filename, format, mode='w')
    print ('output_filename',output_filename,'format',format,)
    electricity_path = join(ualmt_path, "electricity")

    print("Path ualmt:",electricity_path) 
    # Mains data
   
    # Vamos a tener 11 appliances
    
    for chan in range(1, 12):
        key = Key(building=1, meter=chan)
        filename = join(electricity_path, "%d.csv" % chan)
        print('')
        print('***********************************************************************************************')
        print('..Loading file   ', chan,'.csv')
        print('Filename ',filename)
        df = pd.read_csv(filename, dtype=np.float64, na_values='\\N')
        print('..Reading file csv')
        print(df)
        print ('Eliminando duplicados')
        df.drop_duplicates(subset=["timestamp"], inplace=True)
        df.index = pd.to_datetime(df.timestamp.values, unit='ms', utc=True) #unit='ms'
        df = df.tz_convert(TIMEZONE)
        df = df.drop(TIMESTAMP_COLUMN_NAME, 1)
        print('Conversion of timestamp')
        print (df)
        
        #hasta aqui ok
        df.columns = pd.MultiIndex.from_tuples(
            [column_mapping[x] for x in df.columns],
            names=LEVEL_NAMES
        )
        print('....Loading columns')
        print(df)

        
        
        
        df = df.apply(pd.to_numeric, errors='ignore')
        df = df.dropna()
        df = df.astype(np.float32)
        df = df.sort_index()
        print('.......Sorting index')
        print(df)
        #hasta aqui ok
        
        
        df = df.resample("1S").mean()      #resample("1S")
        print('.........Resampling')
        print(df)
        #aqui falla  con la potencia
        
        #esto estaba comentado
       # df = reindex_fill_na(df, idx)
        print ('...........Reindexing file')
        print (df)
        
        #assert df.isnull().sum().sum() == 0
        store.put(str(key), df)
        print ('File ',chan,' loaded ok') 
        print('***********************************************************************************************')
        print('')
    store.close()
    print ('Joining Medadata ')
    metadata_dir = join(get_module_directory(), 'dataset_converters', 'ualmt2', 'metadata')
    convert_yaml_to_hdf5(metadata_dir, output_filename)

    print("Successfully performed the conversion of ualmt to HDF5 format! ")

  