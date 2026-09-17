Data Visualization Tool

A Python-based data analysis tool for loading, cleaning, filtering, and visualizing datasets. The project uses a modular structure to separate data loading, cleaning, filtering, visualization, and export functionality.

Tech Stack

* Python
* Pandas — data loading and transformation
* Matplotlib & Seaborn — data visualization
* Tkinter — file selection interface
* FPDF — basic PDF report generation

Features

* Load CSV and Excel datasets through a file-selection dialog.
* Remove duplicate records from datasets.
* Handle missing values using forward filling.
* Filter data by column and value.
* Generate bar charts and line charts.
* Save generated visualizations as PNG files.
* Generate a basic PDF summary of a dataset.

Project Structure

* main.py — coordinates the data loading, cleaning, and visualization workflow.
* load_file.py — loads CSV or Excel files selected by the user.
* clean_data.py — removes duplicates and handles missing values.
* filter_data.py — filters datasets using a specified column and value.
* plot_functions.py — generates bar and line chart visualizations.
* export.py — generates a basic PDF dataset report.
* sales_data.csv — sample dataset.
* bar_chart.png and line_chart.png — example visualization outputs.

How It Works

The application follows a simple data-processing workflow:

Select Dataset
      |
      v
   Load Data
      |
      v
  Clean Data
      |
      v
Filter / Analyze
      |
      v
  Visualize Data
      |
      v
PNG Charts / PDF Report

This modular structure keeps individual responsibilities separated and makes the application easier to extend.

Running the Project

Install the required Python libraries:

pip install pandas matplotlib seaborn openpyxl fpdf

Run the application:

python main.py

Select a CSV or Excel dataset when prompted. The application will load and clean the dataset before generating visualizations.

Example Output

The repository includes examples of the generated visualizations:

* bar_chart.png
* line_chart.png

What I Learned

This project gave me practical experience working with Python for data processing and visualization. I worked with Pandas for dataset manipulation, implemented reusable functions for different stages of the workflow, and used Matplotlib and Seaborn to turn processed data into visual outputs.

It also helped reinforce the value of separating functionality into smaller modules rather than placing the entire data-processing workflow in a single script.
