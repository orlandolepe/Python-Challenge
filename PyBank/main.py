import os
import csv

# read file
csvPath = os.path.join("budget_data.csv")
with open(csvPath, 'r', newline='') as csvFile:
    budgetData = csv.reader(csvFile, delimiter=',')

    # store value from first row
    next(budgetData, None)
    firstRow = next(budgetData)
    previousRow = int(firstRow[1])

    # start variable counters for month, net total tracker, greatest increase and greatest decrease
    months = 1
    netTotal = previousRow
    changeTotal = 0
    greatestIncrease = 0
    greatestLoss = 0
    
    # for loop through rows
    for rows in budgetData:
        date = rows[0]
        currentRow = int(rows[1])
        
        # calculate difference between months
        change = currentRow - previousRow
        changeTotal += change

        # set previous row to current for next run
        previousRow = currentRow

        # determine whether the value is a greatest increase, loss, or neither with conditionals
        if change > greatestIncrease:
            greatestIncrease = change
            increaseDate = date

        if change < greatestLoss:
            greatestLoss = change
            lossDate = date
        
        # add profit/loss to net total tracker
        netTotal += currentRow

        # month counter increment
        months += 1
    
    # average change
    avgChange = round((changeTotal / (months - 1)), 2)

    # summary table results storage
    formatted = (f'Financial Analysis\n'
                f'---------------------------\n'
                f'Total Months: {months}\n'
                f'Total: ${netTotal}\n'
                f'Average Change: ${avgChange}\n'
                f'Greatest Increase in Profits: {increaseDate} (${greatestIncrease})\n'
                f'Greatest Decrease in Profits: {lossDate} (${greatestLoss})'
            )
    
    # print summary
    print(formatted)

    # export a text file with results
    outputPath = os.path.join("pybank_results_orlando")
    with open(outputPath, 'w') as outputFile:
        outputFile.write(formatted)

    # close files
        outputFile.close()