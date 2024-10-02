def filter_data(data, column, value):
    """ Filter the dataset by a specific column and value """
    filtered_data = data[data[column] == value]
    return filtered_data
