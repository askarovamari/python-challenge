# Import module os and Module for reading csv

import os
import csv

# Set up the path for the CSV file

csvpath = os.path.join("Resources","budget_data.csv")

# Creating lists to store data

months = []
pls = []
monthly_pl_changes = []

# Creating starting variables
 
month_count = 0
total_pl = 0
total_pl_change = 0
starting_profit = 1088983
final_pl = 0

# Improved reading using CSV module

with open(csvpath, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csvreader)

    for rows in csvreader:    

      # Add data from columns into lists to store
      months.append(rows[0])
      pls.append(rows[1])

      # Count total number of months
      month_count = month_count + 1 

      # Calculate total net P/L
      total_pl = total_pl + int(rows[1])

      # Calculate the average change in P/L from month to month
 
      final_pl = int(rows[1])
      monthly_pl_change = final_pl - starting_profit

      # Continue loop/scanning through pl changes with the latest value (e.g Feb/Mar -> Mar/Apr)
      starting_profit = final_pl

      # Add monthly changes into a list to store
      monthly_pl_changes.append(monthly_pl_change)

      total_pl_change = total_pl_change + monthly_pl_change

      #Calculate the average change in profits
      avrg_pl_change = (total_pl_change/month_count)
      
      #Find the max and min change in profits and the corresponding dates these changes were obeserved
      greatest_increase_pl = max(monthly_pl_changes)
      greatest_decrease_pl = min(monthly_pl_changes)

      increase_date = months[monthly_pl_changes.index(greatest_increase_pl)]
      decrease_date = months[monthly_pl_changes.index(greatest_decrease_pl)]
      
    print("----------------------------------------------------------")
    print("Financial Analysis")
    print("----------------------------------------------------------")
    print("Total Months: " + str(month_count))
    print("Total Profits: " + "$" + str(total_pl))
    print("Average Change: " + "$" + str(int(avrg_pl_change)))
    print("Greatest Increase in Profits: " + str(increase_date) + " ($" + str(greatest_increase_pl) + ")")
    print("Greatest Decrease in Profits: " + str(decrease_date) + " ($" + str(greatest_decrease_pl)+ ")")
    print("----------------------------------------------------------")

output_path = os.path.join("Analysis", "analysis.txt")
with open(output_path, 'w') as text:
    text.write("----------------------------------------------------------\n")
    text.write("  Financial Analysis"+ "\n")
    text.write("----------------------------------------------------------\n\n")
    text.write("    Total Months: " + str(month_count) + "\n")
    text.write("    Total: " + "$" + str(total_pl) +"\n")
    text.write("    Average Change: " + '$' + str(int(avrg_pl_change)) + "\n")
    text.write("    Greatest Increase in Profits: " + str(increase_date) + " ($" + str(greatest_increase_pl) + ")\n")
    text.write("    Greatest Decrease in Profits: " + str(decrease_date) + " ($" + str(greatest_decrease_pl) + ")\n")
    text.write("----------------------------------------------------------\n")
