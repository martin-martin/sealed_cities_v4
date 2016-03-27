import json

dataset =   [
  {
    "country":"Cyprus",
    "cat_below_25_percent":0,
    "cat_25_to_49_percent":0,
    "cat_50_to_74_percent":2,
    "cat_75_and_above_percent":0,
    "sum_of_cities":2,
    "percentage_cities_50_and_above_percent":100
  },
  {
    "country":"Estonia",
    "cat_below_25_percent":0,
    "cat_25_to_49_percent":0,
    "cat_50_to_74_percent":2,
    "cat_75_and_above_percent":0,
    "sum_of_cities":2,
    "percentage_cities_50_and_above_percent":100
  },
  {
    "country":"Luxembourg",
    "cat_below_25_percent":0,
    "cat_25_to_49_percent":0,
    "cat_50_to_74_percent":1,
    "cat_75_and_above_percent":0,
    "sum_of_cities":1,
    "percentage_cities_50_and_above_percent":100
  },
  {
    "country":"Greece",
    "cat_below_25_percent":0,
    "cat_25_to_49_percent":1,
    "cat_50_to_74_percent":7,
    "cat_75_and_above_percent":2,
    "sum_of_cities":10,
    "percentage_cities_50_and_above_percent":90
  },
  {
    "country":"Hungary",
    "cat_below_25_percent":0,
    "cat_25_to_49_percent":1,
    "cat_50_to_74_percent":8,
    "cat_75_and_above_percent":0,
    "sum_of_cities":9,
    "percentage_cities_50_and_above_percent":89
  },
  {
    "country":"Romania",
    "cat_below_25_percent":0,
    "cat_25_to_49_percent":3,
    "cat_50_to_74_percent":22,
    "cat_75_and_above_percent":2,
    "sum_of_cities":27,
    "percentage_cities_50_and_above_percent":89
  },
  {
    "country":"Slovakia",
    "cat_below_25_percent":0,
    "cat_25_to_49_percent":1,
    "cat_50_to_74_percent":7,
    "cat_75_and_above_percent":0,
    "sum_of_cities":8,
    "percentage_cities_50_and_above_percent":88
  },
  {
    "country":"Croatia",
    "cat_below_25_percent":0,
    "cat_25_to_49_percent":1,
    "cat_50_to_74_percent":4,
    "cat_75_and_above_percent":0,
    "sum_of_cities":5,
    "percentage_cities_50_and_above_percent":80
  },
  {
    "country":"Poland",
    "cat_below_25_percent":0,
    "cat_25_to_49_percent":10,
    "cat_50_to_74_percent":35,
    "cat_75_and_above_percent":0,
    "sum_of_cities":45,
    "percentage_cities_50_and_above_percent":78
  },
  {
    "country":"Spain",
    "cat_below_25_percent":1,
    "cat_25_to_49_percent":13,
    "cat_50_to_74_percent":41,
    "cat_75_and_above_percent":5,
    "sum_of_cities":60,
    "percentage_cities_50_and_above_percent":77
  },
  {
    "country":"Bulgaria",
    "cat_below_25_percent":0,
    "cat_25_to_49_percent":2,
    "cat_50_to_74_percent":6,
    "cat_75_and_above_percent":0,
    "sum_of_cities":8,
    "percentage_cities_50_and_above_percent":75
  },
  {
    "country":"Czech Republic",
    "cat_below_25_percent":0,
    "cat_25_to_49_percent":4,
    "cat_50_to_74_percent":10,
    "cat_75_and_above_percent":0,
    "sum_of_cities":14,
    "percentage_cities_50_and_above_percent":71
  },
  {
    "country":"Germany",
    "cat_below_25_percent":0,
    "cat_25_to_49_percent":25,
    "cat_50_to_74_percent":60,
    "cat_75_and_above_percent":0,
    "sum_of_cities":85,
    "percentage_cities_50_and_above_percent":71
  },
  {
    "country":"Latvia",
    "cat_below_25_percent":0,
    "cat_25_to_49_percent":1,
    "cat_50_to_74_percent":2,
    "cat_75_and_above_percent":0,
    "sum_of_cities":3,
    "percentage_cities_50_and_above_percent":67
  },
  {
    "country":"Ireland",
    "cat_below_25_percent":0,
    "cat_25_to_49_percent":2,
    "cat_50_to_74_percent":3,
    "cat_75_and_above_percent":0,
    "sum_of_cities":5,
    "percentage_cities_50_and_above_percent":60
  },
  {
    "country":"Lithuania",
    "cat_below_25_percent":0,
    "cat_25_to_49_percent":2,
    "cat_50_to_74_percent":3,
    "cat_75_and_above_percent":0,
    "sum_of_cities":5,
    "percentage_cities_50_and_above_percent":60
  },
  {
    "country":"Italy",
    "cat_below_25_percent":0,
    "cat_25_to_49_percent":20,
    "cat_50_to_74_percent":29,
    "cat_75_and_above_percent":0,
    "sum_of_cities":49,
    "percentage_cities_50_and_above_percent":59
  },
  {
    "country":"The Netherlands",
    "cat_below_25_percent":0,
    "cat_25_to_49_percent":15,
    "cat_50_to_74_percent":20,
    "cat_75_and_above_percent":0,
    "sum_of_cities":35,
    "percentage_cities_50_and_above_percent":57
  },
  {
    "country":"France",
    "cat_below_25_percent":0,
    "cat_25_to_49_percent":14,
    "cat_50_to_74_percent":17,
    "cat_75_and_above_percent":0,
    "sum_of_cities":31,
    "percentage_cities_50_and_above_percent":55
  },
  {
    "country":"Portugal",
    "cat_below_25_percent":0,
    "cat_25_to_49_percent":10,
    "cat_50_to_74_percent":9,
    "cat_75_and_above_percent":0,
    "sum_of_cities":19,
    "percentage_cities_50_and_above_percent":47
  },
  {
    "country":"Austria",
    "cat_below_25_percent":0,
    "cat_25_to_49_percent":3,
    "cat_50_to_74_percent":2,
    "cat_75_and_above_percent":0,
    "sum_of_cities":5,
    "percentage_cities_50_and_above_percent":40
  },
  {
    "country":"Belgium",
    "cat_below_25_percent":1,
    "cat_25_to_49_percent":4,
    "cat_50_to_74_percent":2,
    "cat_75_and_above_percent":0,
    "sum_of_cities":7,
    "percentage_cities_50_and_above_percent":29
  },
  {
    "country":"Switzerland",
    "cat_below_25_percent":0,
    "cat_25_to_49_percent":3,
    "cat_50_to_74_percent":1,
    "cat_75_and_above_percent":0,
    "sum_of_cities":4,
    "percentage_cities_50_and_above_percent":25
  },
  {
    "country":"Denmark",
    "cat_below_25_percent":0,
    "cat_25_to_49_percent":3,
    "cat_50_to_74_percent":1,
    "cat_75_and_above_percent":0,
    "sum_of_cities":4,
    "percentage_cities_50_and_above_percent":25
  },
  {
    "country":"United Kingdom",
    "cat_below_25_percent":1,
    "cat_25_to_49_percent":94,
    "cat_50_to_74_percent":11,
    "cat_75_and_above_percent":0,
    "sum_of_cities":106,
    "percentage_cities_50_and_above_percent":10
  },
  {
    "country":"Finland",
    "cat_below_25_percent":0,
    "cat_25_to_49_percent":4,
    "cat_50_to_74_percent":0,
    "cat_75_and_above_percent":0,
    "sum_of_cities":4,
    "percentage_cities_50_and_above_percent":0
  },
  {
    "country":"Malta",
    "cat_below_25_percent":1,
    "cat_25_to_49_percent":1,
    "cat_50_to_74_percent":0,
    "cat_75_and_above_percent":0,
    "sum_of_cities":2,
    "percentage_cities_50_and_above_percent":0
  },
  {
    "country":"Norway",
    "cat_below_25_percent":0,
    "cat_25_to_49_percent":6,
    "cat_50_to_74_percent":0,
    "cat_75_and_above_percent":0,
    "sum_of_cities":6,
    "percentage_cities_50_and_above_percent":0
  },
  {
    "country":"Sweden",
    "cat_below_25_percent":2,
    "cat_25_to_49_percent":10,
    "cat_50_to_74_percent":0,
    "cat_75_and_above_percent":0,
    "sum_of_cities":12,
    "percentage_cities_50_and_above_percent":0
  },
  {
    "country":"Slovenia",
    "cat_below_25_percent":0,
    "cat_25_to_49_percent":2,
    "cat_50_to_74_percent":0,
    "cat_75_and_above_percent":0,
    "sum_of_cities":2,
    "percentage_cities_50_and_above_percent":0
  }
]

def get_total_perc(country):
	"""calculates the total percent of soil sealing in a country's cities.

	takes as input a dict representing a country with the following structure:

	{
    "country" : "country_name",
    "cat_below_25_percent" : number of cities fitting this category (int),
    "cat_25_to_49_percent" : number of cities fitting this category (int),
    "cat_50_to_74_percent" : number of cities fitting this category (int),
    "cat_75_and_above_percent" : number of cities fitting this category (int),
    "sum_of_cities" : sum of cities assessed (int),
    "percentage_cities_50_and_above_percent" : percentage value (int)
  	}

	calculates the mean percentage value for each ordinal tier
	(for lack of more precise numbers)
	and from these values the overall percentage of soil sealing over all cites
	of that country.
	returns this rounded percentage value.
	"""
	import numpy as np

	# getting the average percentage values of the ordinal categories
	avg_tier_1 = np.mean([0,24])
	avg_tier_2 = np.mean([25,49])
	avg_tier_3 = np.mean([50,74])
	avg_tier_4 = np.mean([75,100])

	# getting the amount of cities in each tier
	num_cities_tier_1 = country["cat_below_25_percent"]
	num_cities_tier_2 = country["cat_25_to_49_percent"]
	num_cities_tier_3 = country["cat_50_to_74_percent"]
	num_cities_tier_4 = country["cat_75_and_above_percent"]

	# getting the sum and converting it to float for more precise calculation
	sum_of_cities = float(country["sum_of_cities"])

	# calculating the sum of all sealed grounds
	sealed_tier_1 = num_cities_tier_1 * avg_tier_1 / 100
	sealed_tier_2 = num_cities_tier_2 * avg_tier_2 / 100
	sealed_tier_3 = num_cities_tier_3 * avg_tier_3 / 100
	sealed_tier_4 = num_cities_tier_4 * avg_tier_4 / 100
	sum_sealed = sealed_tier_1 + sealed_tier_2 + sealed_tier_3 + sealed_tier_4

	# percentage value compared to amount of cities
	perc_sealed_total = sum_sealed / sum_of_cities * 100

	return round(perc_sealed_total)

def update_countries(dataset):
	"""wrapper function: calculates a percentage value and adds it to dataset.

	calls get_total_perc() for each country in the dataset
	adds a new key to each country's dict storing the new percentage value.
	returns the updated dataset.
	"""
	for country in dataset:
		country["total_sealed_in_percent"] = get_total_perc(country)
	return dataset

# write the output of the wrangling to a .json file
with open('soil_sealing_cities.json', 'w') as f:
  f.write(json.dumps(update_countries(dataset), indent=2))