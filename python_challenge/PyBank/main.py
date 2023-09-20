#python program to analyze the finanicial records
import csv

profit_loss_data = []
months = []
changes = []
output = [] #alist to store output data

#define a function to copy data to a text file
def copy_results_tofile(file_path,values):
    with open(file_path, 'w') as file:
        file.write(f"Financial Analysis\n\n")
        file.write("-----------------------------\n\n")   
        file.write(f"Total Months: {values[0]}\n\n")
        file.write(f"Total : {values[1]}\n\n")
        file.write(f"Average Change: {values[2]}\n\n")
        file.write(f"Greatest Increase in Profits: {values[4]} ({values[3]})\n\n")
        file.write(f"Greatest Increase in Profits: {values[6]} ({values[5]})\n\n")

#opening csv file to read and analyze data
with open("Resources/budget_data.csv", encoding="utf-8") as csvfile:
    csvreader = csv.reader(csvfile)
    header = next(csvreader, None) #skip header row

# Loop through each row in the CSV and store date and profit/loss data in a list   
    for bank_data in csvreader:
        months.append(bank_data[0])
        profit_loss_data.append(int(bank_data[1]))

# calculate total months and total amount of profit/loss
total_months =  len(months) 
output.append(total_months)  
total_profit_orloss = sum(profit_loss_data)
output.append(total_profit_orloss) 

#calculate total changes in profit/loss and store the data in a List
for i in range(total_months-1):
    amount_change = int(profit_loss_data[i+1]) - int(profit_loss_data[i])
    changes.append(amount_change)

#calculate total change in profit/loss and avg of the change
total_changes = sum(changes)
avg_profit_loss = round(sum(changes)/len(changes),2)
output.append(avg_profit_loss) #adding output value to output[]

#find greatest increase in profit(date and time)
increase_amount = max(changes)
output.append(increase_amount) 
index1 = changes.index(increase_amount)
inc_profit_date = months[index1+1]
output.append(inc_profit_date) #adding output value to output[]

#find greatest decrease in profit(date and time)
decrease_amount = min(changes)
output.append(decrease_amount) 
index2 = changes.index(decrease_amount)
dec_profit_date = months[index2+1]
output.append(dec_profit_date) #adding output value to output[]

#print the analysis to the terminal  
print("Financial Analysis")
print("-----------------------------\n")   
print(f"Total Months: {total_months}\n")
print(f"Total : {total_profit_orloss}\n")
print(f"Average Change: {avg_profit_loss}\n")
print(f"Greatest Increase in Profits: {inc_profit_date} ({increase_amount})\n")
print(f"Greatest Increase in Profits: {dec_profit_date} ({decrease_amount})\n")

#call function to copy output data to a text file
path_toFile = "analysis/result.txt"
copy_results_tofile(path_toFile,output)





