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
    'VLN': ('voltage', ""),
    'f': ('frequency', ""),
    'VH1': ('voltage_armonic1', ""),
    'VH2': ('voltage_armonic2', ""),
    'VH3': ('voltage_armonic3', ""),
    'VH4': ('voltage_armonic4', ""),
    'VH5': ('voltage_armonic5', ""),
    'VH6': ('voltage_armonic6', ""),
    'VH7': ('voltage_armonic7', ""),
    'VH8': ('voltage_armonic8', ""),
    'VH9': ('voltage_armonic9', ""),
    'VH10': ('voltage_armonic10', ""),
    'VH11': ('voltage_armonic11', ""),
    'VH12': ('voltage_armonic12', ""),
    'VH13': ('voltage_armonic13', ""),
    'VH14': ('voltage_armonic14', ""),
    'VH15': ('voltage_armonic15', ""),
    'VH16': ('voltage_armonic16', ""),
    'VH17': ('voltage_armonic17', ""),
    'VH18': ('voltage_armonic18', ""),
    'VH19': ('voltage_armonic19', ""),
    'VH20': ('voltage_armonic20', ""),
    'VH21': ('voltage_armonic21', ""),
    'VH22': ('voltage_armonic22', ""),
    'VH23': ('voltage_armonic23', ""),
    'VH24': ('voltage_armonic24', ""),
    'VH25': ('voltage_armonic25', ""),
    'VH26': ('voltage_armonic26', ""),
    'VH27': ('voltage_armonic27', ""),
    'VH28': ('voltage_armonic28', ""),
    'VH29': ('voltage_armonic29', ""),
    'VH30': ('voltage_armonic30', ""),
    'VH31': ('voltage_armonic31', ""),
    'VH32': ('voltage_armonic32', ""),
    'VH33': ('voltage_armonic33', ""),
    'VH34': ('voltage_armonic34', ""),
    'VH35': ('voltage_armonic35', ""),
    'VH36': ('voltage_armonic36', ""),
    'VH37': ('voltage_armonic37', ""),
    'VH38': ('voltage_armonic38', ""),
    'VH39': ('voltage_armonic39', ""),
    'VH40': ('voltage_armonic40', ""),
    'VH41': ('voltage_armonic41', ""),
    'VH42': ('voltage_armonic42', ""),
    'VH43': ('voltage_armonic43', ""),
    'VH44': ('voltage_armonic44', ""),
    'VH45': ('voltage_armonic45', ""),
    'VH46': ('voltage_armonic46', ""),
    'VH47': ('voltage_armonic47', ""),
    'VH48': ('voltage_armonic48', ""),
    'VH49': ('voltage_armonic49', ""),
    'VH50': ('voltage_armonic50', ""),
    'IH1': ('current_armonic1', ""),
    'IH2': ('current_armonic2', ""),
    'IH3': ('current_armonic3', ""),
    'IH4': ('current_armonic4', ""),
    'IH5': ('current_armonic5', ""),
    'IH6': ('current_armonic6', ""),
    'IH7': ('current_armonic7', ""),
    'IH8': ('current_armonic8', ""),
    'IH9': ('current_armonic9', ""),
    'IH10': ('current_armonic10', ""),
    'IH11': ('current_armonic11', ""),
    'IH12': ('current_armonic12', ""),
    'IH13': ('current_armonic13', ""),
    'IH14': ('current_armonic14', ""),
    'IH15': ('current_armonic15', ""),
    'IH16': ('current_armonic16', ""),
    'IH17': ('current_armonic17', ""),
    'IH18': ('current_armonic18', ""),
    'IH19': ('current_armonic19', ""),
    'IH20': ('current_armonic20', ""),
    'IH21': ('current_armonic21', ""),
    'IH22': ('current_armonic22', ""),
    'IH23': ('current_armonic23', ""),
    'IH24': ('current_armonic24', ""),
    'IH25': ('current_armonic25', ""),
    'IH26': ('current_armonic26', ""),
    'IH27': ('current_armonic27', ""),
    'IH28': ('current_armonic28', ""),
    'IH29': ('current_armonic29', ""),
    'IH30': ('current_armonic30', ""),
    'IH31': ('current_armonic31', ""),
    'IH32': ('current_armonic32', ""),
    'IH33': ('current_armonic33', ""),
    'IH34': ('current_armonic34', ""),
    'IH35': ('current_armonic35', ""),
    'IH36': ('current_armonic36', ""),
    'IH37': ('current_armonic37', ""),
    'IH38': ('current_armonic38', ""),
    'IH39': ('current_armonic39', ""),
    'IH40': ('current_armonic40', ""),
    'IH41': ('current_armonic41', ""),
    'IH42': ('current_armonic42', ""),
    'IH43': ('current_armonic43', ""),
    'IH44': ('current_armonic44', ""),
    'IH45': ('current_armonic45', ""),
    'IH46': ('current_armonic46', ""),
    'IH47': ('current_armonic47', ""),
    'IH48': ('current_armonic48', ""),
    'IH49': ('current_armonic49', ""),
    'IH50': ('current_armonic50', ""),
    'PH1': ('power_armonic1', ""),
    'PH2': ('power_armonic2', ""),
    'PH3': ('power_armonic3', ""),
    'PH4': ('power_armonic4', ""),
    'PH5': ('power_armonic5', ""),
    'PH6': ('power_armonic6', ""),
    'PH7': ('power_armonic7', ""),
    'PH8': ('power_armonic8', ""),
    'PH9': ('power_armonic9', ""),
    'PH10': ('power_armonic10', ""),
    'PH11': ('power_armonic11', ""),
    'PH12': ('power_armonic12', ""),
    'PH13': ('power_armonic13', ""),
    'PH14': ('power_armonic14', ""),
    'PH15': ('power_armonic15', ""),
    'PH16': ('power_armonic16', ""),
    'PH17': ('power_armonic17', ""),
    'PH18': ('power_armonic18', ""),
    'PH19': ('power_armonic19', ""),
    'PH20': ('power_armonic20', ""),
    'PH21': ('power_armonic21', ""),
    'PH22': ('power_armonic22', ""),
    'PH23': ('power_armonic23', ""),
    'PH24': ('power_armonic24', ""),
    'PH25': ('power_armonic25', ""),
    'PH26': ('power_armonic26', ""),
    'PH27': ('power_armonic27', ""),
    'PH28': ('power_armonic28', ""),
    'PH29': ('power_armonic29', ""),
    'PH30': ('power_armonic30', ""),
    'PH31': ('power_armonic31', ""),
    'PH32': ('power_armonic32', ""),
    'PH33': ('power_armonic33', ""),
    'PH34': ('power_armonic34', ""),
    'PH35': ('power_armonic35', ""),
    'PH36': ('power_armonic36', ""),
    'PH37': ('power_armonic37', ""),
    'PH38': ('power_armonic38', ""),
    'PH39': ('power_armonic39', ""),
    'PH40': ('power_armonic40', ""),
    'PH41': ('power_armonic41', ""),
    'PH42': ('power_armonic42', ""),
    'PH43': ('power_armonic43', ""),
    'PH44': ('power_armonic44', ""),
    'PH45': ('power_armonic45', ""),
    'PH46': ('power_armonic46', ""),
    'PH47': ('power_armonic47', ""),
    'PH48': ('power_armonic48', ""),
    'PH49': ('power_armonic49', ""),
    'PH50': ('power_armonic50', "")
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
    electricity_path = join(ualmt_path, "electricity")

    print("Path ualmt:",ualmt_path,"/electricity") 
    # Mains data
   
    # Vamos a tener 6 appliances
    
    for chan in range(1, 7):
        key = Key(building=1, meter=chan)
        filename = join(electricity_path, "%d.csv" % chan)
        print('')
        print('***********************************************************************************************')
        print('..Loading file   ', chan,'.csv')
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

  