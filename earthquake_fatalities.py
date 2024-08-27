# Constants
building_stock = 1062040
population = 15927951

# Building damage estimates
collapsed_buildings = 120057
severely_damaged_buildings = 196174
moderately_damaged_buildings = 477777
no_slight_damage_buildings = 249663

# Assumptions for fatality rates
# Minimum Scenario
collapsed_fatality_rate_min = 0.8
severely_damaged_fatality_rate_min = 0.2
moderately_damaged_fatality_rate_min = 0.05
no_slight_damage_fatality_rate_min = 0.005

# Maximum Scenario
collapsed_fatality_rate_max = 0.9
severely_damaged_fatality_rate_max = 0.4
moderately_damaged_fatality_rate_max = 0.1
no_slight_damage_fatality_rate_max = 0.001

# Calculate population per building (assuming even distribution)
population_per_building = population / building_stock

# Minimum Scenario Calculation
min_deaths_collapsed = collapsed_buildings * population_per_building * collapsed_fatality_rate_min
min_deaths_severe = severely_damaged_buildings * population_per_building * severely_damaged_fatality_rate_min
min_deaths_moderate = moderately_damaged_buildings * population_per_building * moderately_damaged_fatality_rate_min
min_deaths_slight = no_slight_damage_buildings * population_per_building * no_slight_damage_fatality_rate_min

min_total_deaths = min_deaths_collapsed + min_deaths_severe + min_deaths_moderate + min_deaths_slight

# Maximum Scenario Calculation
max_deaths_collapsed = collapsed_buildings * population_per_building * collapsed_fatality_rate_max
max_deaths_severe = severely_damaged_buildings * population_per_building * severely_damaged_fatality_rate_max
max_deaths_moderate = moderately_damaged_buildings * population_per_building * moderately_damaged_fatality_rate_max
max_deaths_slight = no_slight_damage_buildings * population_per_building * no_slight_damage_fatality_rate_max

max_total_deaths = max_deaths_collapsed + max_deaths_severe + max_deaths_moderate + max_deaths_slight

# Print the results as integers
print("Minimum Total Deaths:", int(min_total_deaths))
print("Maximum Total Deaths:", int(max_total_deaths))
