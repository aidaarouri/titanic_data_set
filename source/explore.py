
def data_shape(df):
    df_shape  = df.shape 
    print('the data has' ,  df_shape[0] ,' rows and ', df_shape[1],' columns')

def data_info(df):
    print("Dataset Info:")
    print(df.info())

def data_missing_values(df):
    print("\nMissing Values:")
    print(df.isnull().sum())

def display_first_5_rows(df):
    print("\nFirst 5 Rows:")
    print(df.head())

def data_categorical_attributes(df):
    categorical_columns = df.select_dtypes(include=['object']).columns.tolist()
    print(categorical_columns)
    print(len(categorical_columns))

def display_stats_of_numerical_data(df):
    print(df.describe())

def display_stats_of_categorical_data(df):
    print(df.describe(include='object'))


