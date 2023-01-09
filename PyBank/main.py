# Dependencies
import os
import csv

# Path to collect data from the Resources folder
budget_csv = os.path.join('Resources', 'budget_data.csv')

# Read in the CSV file
with open(budget_csv, 'r') as csvfile:

    # Split the data on commas
    csvreader = csv.reader(csvfile, delimiter=',')

    # capture the header and move to the next row
    header = next(csvreader) 
    """
    Header: 'Date', 'Profit/Losses'
    format: 'Jan-10', '1088983'
    """
    
    # setting up initial values of variables for calculations
    months = []
    total_pro_los = 0
    former_value = 0
    change = 0
    sum_change_values = 0
    num_values = 0
    max_increase = 0
    date_max_increase = ''
    max_decrease = 0
    date_max_decrease = ''

    # Loop through the rows
    for i, row in enumerate(csvreader):

        # Calculate The total number of months included in the dataset
        """iterating through the data and creating a list with all the months. After the loop is done, employ the set method and len method
        to find the number of non repeating months"""
        months.append(row[0])

        # Calculate the net total amount of "Profit/Losses" over the entire period
        """add current value to total_pro_los"""
        total_pro_los = total_pro_los + int(row[1])

        # calculate the changes in "Profit/Losses" over the entire period, and then the average of those changes
        """calculate the difference between current value and former value, changing the former value after the calculation to
        capture the current one for the next iteration. Start first iteration with former value = current value. 
        Also add the values to a sum and count the number of iterations so average can be calculated following the loop"""
        current_value = int(row[1])
        if i == 0:
            former_value = current_value
        change = current_value - former_value
        sum_change_values = sum_change_values + change
        
        
              
        # find the greatest increase in profits (date and amount) over the entire period
        """if the current value is more than 0 and greater than the former value 
        then update the greatest increase var and the associated date"""
        if change > max_increase:
            max_increase = change
            date_max_increase = row[0]

        # find the greatest decrease in profits (date and amount) over the entire period
        """if the current value is less than 0 and less than the former value 
        then update the greatest decrease var and the associated date"""
        if change < max_decrease:
            max_decrease = change
            date_max_decrease = row[0]

        # updating former value and iteration counter for the next iteration
        former_value = current_value
        num_values += 1

# calculations following loop
total_num_months = len(set(months))
avg_change = round(sum_change_values / (num_values - 1), 2)

# print to terminal and export results to text file 
"""creating a function that does both the printing and the export """
def out(message):
    print(message)
    with open('analysis\pybank_output.txt', 'a') as output:
        print(message, file=output)
        
"""using the function to print and export all the required info"""
out('Financial Analysis')
out('-' *30)
out(f'Total Months: {total_num_months}')
out(f'Total: ${total_pro_los:,}')
out(f'Average Change: ${avg_change}')
out(f'Greatest Increase in Profits: {date_max_increase} (${max_increase:,})')
out(f'Greatest Decrease in Profits: {date_max_decrease} (${max_decrease:,})')
