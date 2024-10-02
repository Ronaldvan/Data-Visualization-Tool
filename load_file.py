import os

os.environ['TK_SILENCE_DEPRECATION'] = '1'

import tkinter as Tk
from tkinter import filedialog
from tkinter import Tk
import pandas as pd

def load_file():
    """ Opens a file dialog for user to select CSV or Excel file. """
    root = Tk()
    root.withdraw()  # Hides the small Tkinter window
    file_path = filedialog.askopenfilename(title="Select File", filetypes=(("CSV Files", "*.csv"), ("Excel Files", "*.xlsx *.xls")))
    if file_path.endswith('.csv'):
        data = pd.read_csv(file_path)
    elif file_path.endswith('.xlsx') or file_path.endswith('.xls'):
        data = pd.read_excel(file_path)
    else:
        raise ValueError("Unsupported file format")
    return data
