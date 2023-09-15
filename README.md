# Read me 
1- Fawzi

1. `data_shape(df)`:
   - This function prints the shape of the DataFrame, which includes the number of rows and columns.
   - Insight: the data has 1309  rows and  12  columns.

2. `data_info(df)`:
   - This function prints the output of `df.info()`, which includes the data type of each column and the count of non-null values.
   - Insight: we can see that the data has numerical and non-numerical attributes and It has some missing values 

3. `data_missing_values(df)`:
   - This function prints the count of missing values for each column in the DataFrame.
   - Insight: we can see Survived,Age,Cabin,Embarked,Fare attributes have missing values.

4. `display_first_5_rows(df)`:
   - This function displays the first 5 rows of the DataFrame.
   - Insight: It provides a preview of the dataset, showing the initial records.

5. `data_categorical_attributes(df)`:
   - This function identifies and prints the names of columns with object data types (typically categorical columns).
   - Insight: we can see that ['Name', 'Sex', 'Ticket', 'Cabin', 'Embarked'] attributes that have object data.

6. `display_stats_of_numerical_data(df)`:
   - This function prints basic summary statistics for numerical columns (e.g., count, mean, std, min, max, quartiles).
   - Insight: It provides statistical insights into the distribution of numerical data.

7. `display_stats_of_categorical_data(df)`:
   - This function prints basic summary statistics for categorical columns (e.g., count, unique values, top value, frequency of top value).
   - Insight: It provides summary statistics for categorical data, such as the most common categories and their frequencies.


Issue 3: By Sally

Insights on Age_group and Survival rates:

Raw number of Survived among different age groups:
Among the 891 individuals in the dataset, I observed the following number of survivors in each age group:
  * Kids (0-16 years old): 100 individuals
  * Adults (16-55 years old): 574 individuals
  * Elders (55+ years old): 40 individuals

Relation between age groups and survival rates (relative to the entire sample):
When considering the entire sample, I find the following survival rates for each age group:
  * Kids (0-16 years old): 55.00%
  * Adults (16-55 years old): 38.85%
  * Elders (55+ years old): 30.00%

Relation between age groups and survival rates (relative to each age group):
When examining the survival rates within each age group, I find the following insights:
  * Among kids, approximately 11.22% of individuals survived.
  * For adults, a significantly higher proportion, about 64.42%, managed to survive.
  * In contrast, the elder group had a survival rate of approximately 4.49%.

These findings indicate a notable discrepancy in survival rates between age groups. Children and adults had significantly higher chances of surviving compared to elders. This may be attributed to various factors.
