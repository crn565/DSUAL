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
    'VH2': ('voltage', 'armonic2'),
    'VH3': ('voltage', 'armonic3'),
    'VH4': ('voltage', 'armonic3 '),
    'VH5': ('voltage', 'armonic5'),
    'VH6': ('voltage', 'armonic6'),
    'VH7': ('voltage', 'armonic7'),
    'VH8': ('voltage', 'armonic8'),
    'VH9': ('voltage', 'armonic9'),
    'VH10': ('voltage', 'armonic10'),
    'VH11': ('voltage', 'armonic11'),
    'VH12': ('voltage', 'armonic12'),
    'VH13': ('voltage', 'armonic13'),
    'VH14': ('voltage', 'armonic14'),
    'VH15': ('voltage', 'armonic15'),
    'VH16': ('voltage', 'armonic16'),
    'VH17': ('voltage', 'armonic17'),
    'VH18': ('voltage', 'armonic18'),
    'VH19': ('voltage', 'armonic19'),
    'VH20': ('voltage', 'armonic20'),
    'VH21': ('voltage', 'armonic21'),
    'VH22': ('voltage', 'armonic22'),
    'VH23': ('voltage', 'armonic23'),
    'VH24': ('voltage', 'armonic24'),
    'VH25': ('voltage', 'armonic25'),
    'VH26': ('voltage', 'armonic26'),
    'VH27': ('voltage', 'armonic27'),
    'VH28': ('voltage', 'armonic28'),
    'VH29': ('voltage', 'armonic29'),
    'VH30': ('voltage', 'armonic30'),
    'VH31': ('voltage', 'armonic31'),
    'VH32': ('voltage', 'armonic32'),
    'VH33': ('voltage', 'armonic33'),
    'VH34': ('voltage', 'armonic34'),
    'VH35': ('voltage', 'armonic35'),
    'VH36': ('voltage', 'armonic36'),
    'VH37': ('voltage', 'armonic37'),
    'VH38': ('voltage', 'armonic38'),
    'VH39': ('voltage', 'armonic39'),
    'VH40': ('voltage', 'armonic40'),
    'VH41': ('voltage', 'armonic41'),
    'VH42': ('voltage', 'armonic42'),
    'VH43': ('voltage', 'armonic43'),
    'VH44': ('voltage', 'armonic44'),
    'VH45': ('voltage', 'armonic45'),
    'VH46': ('voltage', 'armonic46'),
    'VH47': ('voltage', 'armonic47'),
    'VH48': ('voltage', 'armonic48'),
    'VH49': ('voltage', 'armonic49'),
    'VH50': ('voltage', 'armonic50'),
    'IH1': ('current', 'armonic1'),
    'IH2': ('current', 'armonic2'),
    'IH3': ('current', 'armonic3'),
    'IH4': ('current', 'armonic4'),
    'IH5': ('current', 'armonic5'),
    'IH6': ('current', 'armonic6'),
    'IH7': ('current', 'armonic7'),
    'IH8': ('current', 'armonic8'),
    'IH9': ('current', 'armonic9'),
    'IH10': ('current', 'armonic10'),
    'IH11': ('current', 'armonic11'),
    'IH12': ('current', 'armonic12'),
    'IH13': ('current', 'armonic13'),
    'IH14': ('current', 'armonic14'),
    'IH15': ('current', 'armonic15'),
    'IH16': ('current', 'armonic16'),
    'IH17': ('current', 'armonic17'),
    'IH18': ('current', 'armonic18'),
    'IH19': ('current', 'armonic19'),
    'IH20': ('current', 'armonic20'),
    'IH21': ('current', 'armonic21'),
    'IH22': ('current', 'armonic22'),
    'IH23': ('current', 'armonic23'),
    'IH24': ('current', 'armonic24'),
    'IH25': ('current', 'armonic25'),
    'IH26': ('current', 'armonic26'),
    'IH27': ('current', 'armonic27'),
    'IH28': ('current', 'armonic28'),
    'IH29': ('current', 'armonic29'),
    'IH30': ('current', 'armonic30'),
    'IH31': ('current', 'armonic31'),
    'IH32': ('current', 'armonic32'),
    'IH33': ('current', 'armonic33'),
    'IH34': ('current', 'armonic34'),
    'IH35': ('current', 'armonic35'),
    'IH36': ('current', 'armonic36'),
    'IH37': ('current', 'armonic37'),
    'IH38': ('current', 'armonic38'),
    'IH39': ('current', 'armonic39'),
    'IH40': ('current', 'armonic40'),
    'IH41': ('current', 'armonic41'),
    'IH42': ('current', 'armonic42'),
    'IH43': ('current', 'armonic43'),
    'IH44': ('current', 'armonic44'),
    'IH45': ('current', 'armonic45'),
    'IH46': ('current', 'armonic46'),
    'IH47': ('current', 'armonic47'),
    'IH48': ('current', 'armonic48'),
    'IH49': ('current', 'armonic49'),
    'IH50': ('current', 'armonic50'),
    'PH1': ('power', 'armonic1'),
    'PH2': ('power', 'armonic2'),
    'PH3': ('power', 'armonic3'),
    'PH4': ('power', 'armonic4'),
    'PH5': ('power', 'armonic5'),
    'PH6': ('power', 'armonic6'),
    'PH7': ('power', 'armonic7'),
    'PH8': ('power', 'armonic8'),
    'PH9': ('power', 'armonic9'),
    'PH10': ('power', 'armonic10'),
    'PH11': ('power', 'armonic11'),
    'PH12': ('power', 'armonic12'),
    'PH13': ('power', 'armonic13'),
    'PH14': ('power', 'armonic14'),
    'PH15': ('power', 'armonic15'),
    'PH16': ('power', 'armonic16'),
    'PH17': ('power', 'armonic17'),
    'PH18': ('power', 'armonic18'),
    'PH19': ('power', 'armonic19'),
    'PH20': ('power', 'armonic20'),
    'PH21': ('power', 'armonic21'),
    'PH22': ('power', 'armonic22'),
    'PH23': ('power', 'armonic23'),
    'PH24': ('power', 'armonic24'),
    'PH25': ('power', 'armonic25'),
    'PH26': ('power', 'armonic26'),
    'PH27': ('power', 'armonic27'),
    'PH28': ('power', 'armonic28'),
    'PH29': ('power', 'armonic29'),
    'PH30': ('power', 'armonic30'),
    'PH31': ('power', 'armonic31'),
    'PH32': ('power', 'armonic32'),
    'PH33': ('power', 'armonic33'),
    'PH34': ('power', 'armonic34'),
    'PH35': ('power', 'armonic35'),
    'PH36': ('power', 'armonic36'),
    'PH37': ('power', 'armonic37'),
    'PH38': ('power', 'armonic38'),
    'PH39': ('power', 'armonic39'),
    'PH40': ('power', 'armonic40'),
    'PH41': ('power', 'armonic41'),
    'PH42': ('power', 'armonic42'),
    'PH43': ('power', 'armonic43'),
    'PH44': ('power', 'armonic44'),
    'PH45': ('power', 'armonic45'),
    'PH46': ('power', 'armonic46'),
    'PH47': ('power', 'armonic47'),
    'PH48': ('power', 'armonic48'),
    'PH49': ('power', 'armonic49'),
    'PH50': ('power', 'armonic50')
}

TIMESTAMP_COLUMN_NAME = "timestamp"
TIMEZONE = "Europe/Berlin" 
START_DATETIME, END_DATETIME = '2022-02-02', '2022-02-02'

FREQ = "1T"
#old= 1T  nueva 1S

def convert_ualmt(ualmt_path, output_filename, format="HDF"):
    """
    Parameters
    ----------
    ualmt_path : str
        The root path of the ualmt dataset.
    output_filename : str
        The destination filename (including path and suffix).
    """

    check_directory_exists(ualmt_path)
    idx = pd.date_range(start=START_DATETIME, end=END_DATETIME, freq=FREQ)
    idx = idx.tz_localize('GMT').tz_convert(TIMEZONE)

    # Open data store
    store = get_datastore(output_filename, format, mode='w')
    print ('output_filename',output_filename,'format',format,)
    electricity_path = join(ualmt_path, "electricity")

    print("Path ualmt:",electricity_path) 
    # Mains data
   
    # Vamos a tener 6 appliances
    
    for chan in range(1, 7):
        key = Key(building=1, meter=chan)
        filename = join(electricity_path, "%d.csv" % chan)
        print('')
        print('***********************************************************************************************')
        print('..Loading file   ', chan,'.csv')
        print('Filename ',filename)
        df = pd.read_csv(filename, dtype=np.float64, na_values='\\N')
        print('..Reading file csv')
        print(df)
        
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
        
        #df = reindex_fill_na(df, idx)
        print ('...........Reindexing file')
        print (df)
        
        assert df.isnull().sum().sum() == 0
        store.put(str(key), df)
        print ('File ',chan,' loaded ok') 
        print('***********************************************************************************************')
        print('')
    store.close()
    print ('Joining Medadata ')
    metadata_dir = join(get_module_directory(), 'dataset_converters', 'ualmt', 'metadata')
    convert_yaml_to_hdf5(metadata_dir, output_filename)

    print("Successfully performed the conversion of ualmt to HDF5 format! ")

  