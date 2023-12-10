import pandas as pd
import numpy as np

def generate_car_matrix(df):
    matrix = df.pivot(index='id_1', columns='id_2', values='car')
    return matrix

def get_type_count(df):
    car_counts = df['car'].value_counts().to_dict()
    return car_counts

def get_bus_indexes(df):
    mean_bus = df['bus'].mean()
    bus_indexes = df[df['bus'] > 2 * mean_bus].index.tolist()
    return bus_indexes

def filter_routes(df):
    mean_truck = df.groupby('route')['truck'].mean()
    filtered_routes = mean_truck[mean_truck > 7].index.tolist()
    return filtered_routes

def multiply_matrix(matrix):
    conditions = [
        (matrix <= 10),
        (matrix > 10) & (matrix <= 50),
        (matrix > 50)
    ]
    values = [matrix, matrix * 2, matrix * 3]
    matrix = np.select(conditions, values, matrix)
    return pd.DataFrame(matrix)

def time_check(df):
    df['timestamp'] = pd.to_datetime(df['timestamp'])
    df['hour'] = df['timestamp'].dt.hour
    df['day'] = df['timestamp'].dt.dayofweek
    completeness_check = df.groupby(['id', 'id_2']).apply(lambda x: x['hour'].nunique() == 24 and x['day'].nunique() == 7)
    return completeness_check
