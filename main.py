from source import load_data 
from source import explore


data = load_data()

print(data.size)

explore.data_shape(data)
explore.data_info(data)
explore.data_missing_values(data)
explore.display_first_5_rows(data)
explore.data_categorical_attributes(data)
explore.display_stats_of_categorical_data(data)
explore.display_stats_of_numerical_data(data)