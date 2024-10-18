# Program #3: US_Population
def main():
    # Have the user input (using a loop) various information that contains three pieces of data: 
    # year, name of state, and population.
    yr_st_pop = []
    while True:
        year = input("Enter the year (or 'done' to finish): ")
        if year.lower() == 'done':
            break
        state = input("Enter the name of the state: ")
        population = input("Enter the population: ")

        # append the data as a list to all_entered_values
        yr_st_pop.append([int(year), state, int(population)])

    year_to_sum = int(input("Enter a year to sum the populations: "))
    # Now have the user enter a year. 
    sum_population_for_year(yr_st_pop, year_to_sum)

    # The program will add the populations from all states in the list of list for that year only.
    # Pass the list and year to the sum_population_for_year

def sum_population_for_year(all_entered_values, year_to_sum):
    sum_population = 0
    for values in all_entered_values:
        year, state, population = values
        if year == year_to_sum:
            sum_population += population

    # print the totalled population
    print(f'Total population for the year {year_to_sum}: {sum_population}')




# Call the main function.
if __name__ == '__main__':
    main()