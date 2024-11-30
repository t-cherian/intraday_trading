#!/usr/bin/env python3
import tkinter as tk
from tkinter import filedialog, messagebox
import pandas as pd
import webbrowser
from pandastable import Table

# Helper functions
def open_url(url):
    webbrowser.open(url)

def process_csv():
    try:
        # Load the first CSV file
        file_path1 = filedialog.askopenfilename(title="Open First CSV File", filetypes=[("CSV Files", "*.csv")])
        if not file_path1:
            return
        df1 = pd.read_csv(file_path1, header=None)  # Load without headers for manipulation

        # Update row 1 values for columns G and H
        if 5 in df1.columns:
            df1.iloc[0, 6] = "Daily"  # Column G
        if 6 in df1.columns:
            df1.iloc[0, 7] = "Yearly"   # Column H

        # Set row 1 as headers
        df1.columns = df1.iloc[0]
        df1 = df1[1:]  # Remove the first row

        # Remove specified columns (only if they exist)
        columns_to_remove = ["Date", "Underlying Previous Day Close Price (B)", "Underlying Log Returns (C) = LN(A/B)", "Previous Day Underlying Volatility (D)"]
        existing_columns_to_remove = [col for col in columns_to_remove if col in df1.columns]
        df1.drop(columns=existing_columns_to_remove, inplace=True)

        # Ensure columns "Daily" and "Yearly" exist before creating percentages
        if "Daily" in df1.columns and "Yearly" in df1.columns:
            df1["Daily"] = pd.to_numeric(df1["Daily"], errors='coerce')  # Convert to numeric
            df1["Yearly"] = pd.to_numeric(df1["Yearly"], errors='coerce')  # Convert to numeric
            df1["Daily %"] = df1["Daily"] * 100
            df1["Yearly %"] = df1["Yearly"] * 100
        else:
            messagebox.showerror("Error", "Columns 'Daily' or 'Yearly' not found in the first CSV.")
            return

        # Load the second CSV file
        file_path2 = filedialog.askopenfilename(title="Open Second CSV File", filetypes=[("CSV Files", "*.csv")])
        if not file_path2:
            return
        df2 = pd.read_csv(file_path2)

        # Check if columns "A" in df1 and "C" in df2 exist before filtering
        if "Symbol" in df1.columns and "Symbol" in df2.columns:
            merged_df = df1[df1["Symbol"].isin(df2["Symbol"])]
        else:
            messagebox.showerror("Error", "Columns 'A' in the first CSV or 'C' in the second CSV are missing.")
            return

        # Display the final table
        display_table(merged_df)
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {e}")

def display_table(dataframe):
    # Create a new window to display the table
    table_window = tk.Toplevel(root)
    table_window.title("Processed Data")

    frame = tk.Frame(table_window)
    frame.pack(fill=tk.BOTH, expand=True)

    # Display the table with sorting capabilities
    pt = Table(frame, dataframe=dataframe, showtoolbar=True, showstatusbar=True)
    pt.show()

# Main GUI
root = tk.Tk()
root.title("CSV File Processor")
root.geometry("400x200")

# Buttons
btn_open_nse_reports = tk.Button(root, text="Open NSE Reports Website", command=lambda: open_url("https://www.nseindia.com/all-reports"))
btn_open_nse_reports.pack(pady=10)

btn_open_nifty_index = tk.Button(root, text="Open Nifty Index Website", command=lambda: open_url("https://www.nseindia.com/products-services/indices-nifty100-index"))
btn_open_nifty_index.pack(pady=10)

btn_process_csv = tk.Button(root, text="Process CSV Files", command=process_csv)
btn_process_csv.pack(pady=10)

root.mainloop()
