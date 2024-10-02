                                                                **Data Visualization Tool**


This is a Python-based Data Visualization Tool that allows users to load, clean, filter, and visualize datasets. The tool provides functionality to create bar and line charts, making it ideal for analyzing trends in data.


**Features**
* Data Loading: Load data from various file formats.
* Data Cleaning: Automatically clean the dataset by removing duplicates and filling missing values.
* Data Filtering: Filter the dataset based on specific criteria.
* Data Visualization: Generate bar charts and line charts to visually represent the relationships between different data columns.


**Files Overview**
1. main.py: The main script to run the data visualization process. It loads, cleans, and visualizes the data using bar and line charts.
    * Key Functions:
        * main(): Orchestrates the data analysis workflow by calling functions to load, clean, and visualize the data.
        * Visualization options: Bar charts or line charts based on the Month and Year columns.
2. plot_functions.py: Contains functions for creating visualizations.
    * Key Functions:
        * plot_bar_chart(data, x_col, y_col): Plots a bar chart for the specified columns.
        * plot_line_chart(data, x_col, y_col): Plots a line chart for the specified columns.
3. filter_data.py: Provides a function to filter data based on specific criteria.
    * Key Functions:
        * filter_data(data, column, value): Filters the dataset by a given column and value.
4. clean_data.py: Contains the data cleaning function.
    * Key Functions:
        * clean_data(data): Removes duplicates and fills missing values using forward fill.


**Setup Instructions**

1. Install Required Libraries:
    * Install the necessary Python libraries using pip:bash

      _pip install matplotlib seaborn pandas_

      
2. Run the Tool:
    * Execute the main.py script to load, clean, and visualize your data:bash


      _python main.py_

      
**Usage**
* The tool automatically loads and cleans the dataset. It then generates visualizations based on the Month and Year columns.
* You can choose between bar charts and line charts to analyze the data trends.
* Custom data filtering can be applied by using the filter_data function from filter_data.py.


**Example**
Here’s an example of how the tool works:
1. Load and clean data.
2. Visualize data using bar or line charts.
3. Filter data by specific criteria to focus on particular subsets.


**Output**
The charts will be saved as .png files in the working directory:
* Bar Chart: bar_chart.png
* Line Chart: line_chart.png


**License**
This project is open-source and available under the MIT License.
