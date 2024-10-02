print("Code is running")
# import pdb; pdb.set_trace()

from load_file import load_file
from clean_data import clean_data
from plot_functions import plot_bar_chart, plot_line_chart

def main():
    # Step 1: Load the Data
    data = load_file()
    
    # Step 2: Clean the Data
    cleaned_data = clean_data(data)
    
    # Step 3: Plot Visualizations
    plot_bar_chart(cleaned_data, 'Month', 'Year')
    # or
    plot_line_chart(cleaned_data, 'Month', 'Year')

if __name__ == "__main__":
    main()
