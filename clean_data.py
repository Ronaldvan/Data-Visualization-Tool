def clean_data(data):
    """ Cleans the dataset by removing duplicates and filling missing values. """
    data_cleaned = data.drop_duplicates()
    data_cleaned = data_cleaned.fillna(method='ffill')  # Forward fill missing values
    return data_cleaned

# Test the cleaning function
if __name__ == "__main__":
    data = load_file()
    cleaned_data = clean_data(data)
    print(cleaned_data.head())
