import matplotlib.pyplot as plt
import seaborn as sns

def plot_bar_chart(data, x_col, y_col):
    """ Creates a bar chart for the given x and y columns. """
    plt.figure(figsize=(10, 6))
    sns.barplot(x=x_col, y=y_col, data=data)
    plt.title(f'{y_col} vs {x_col}')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig('bar_chart.png')  # Save as PNG file
    plt.show()

def plot_line_chart(data, x_col, y_col):
    """ Creates a line chart for the given x and y columns. """
    plt.figure(figsize=(10, 6))
    plt.plot(data[x_col], data[y_col], marker='o')
    plt.title(f'{y_col} over {x_col}')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig('line_chart.png')  # Save as PNG file
    plt.show()
    