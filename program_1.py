# Program #1: Rainfall
# Design a program that lets the user enter the total rainfall for each of 12 months into a list.
# The program should calculate and display the total rainfall for the year, 
# the average monthly rainfall, # and the months with the highest and lowest amounts.


# list to store monthly rainfall
rainfall = []

# for loop to get rainfall for every month
for month in range(1, 13):
    while True:
        try:
            # prompt user for rainfall for __ month
            rain = float(input(f"Enter the total rainfall for month {month}: "))
            rainfall.append(rain)
            break
        except ValueError as x:
            print(f"Incorrect input: {x}. Please enter a valid number.")

    # calc total and average rainfall
total_rainfall = sum(rainfall)
average_rainfall = total_rainfall / 12
# find month with the highest and lowest rainfall
highest_rainfall = max(rainfall)
lowest_rainfall = min(rainfall)
# add 1 for month index
highest_month = rainfall.index(highest_rainfall) + 1
lowest_month = rainfall.index(lowest_rainfall) + 1

# display final results
print(f"\nTotal rainfall for the year: {total_rainfall:.2f} inches")
print(f"Average monthly rainfall: {average_rainfall:.2f} inches")
print(f"Month with highest rainfall: Month {highest_month} ({highest_rainfall:.2f} inches)")
print(f"Month with lowest rainfall: Month {lowest_month} ({lowest_rainfall:.2f} inches)")

