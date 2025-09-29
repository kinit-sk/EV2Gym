# EV2Gym Data Cards

This document provides detailed information about the data files used in the EV2Gym environment. Each data card includes a description of the data, its structure, key statistics, and insights from analysis.

Associated code for data analysis: `notebooks/0.03-pm-ev2gym-eda.ipynb`

## EV Arrival Data

### Distribution of Arrival (Weekday)

Data describes the probability distribution of EV arrivals throughout the day on weekdays for different charging location types.

**Data source:**

- `distribution-of-arrival.csv`

**Columns:**

- `Arrival time`:
  - arrival time
  - data type: string
  - range: 00:00 to 23:45
- `private`:
  - probability of arrival at private charging location
  - data type: float
  - range: 0-100
- `public`:
  - probability of arrival at public charging location
  - data type: float
  - range: 0-100
- `workplace`:
  - probability of arrival at workplace charging location
  - data type: float
  - range: 0-100

**Visualizations:**

- Line plot of arrival probabilities by arrival time in 15 minute intervals

**Insights:**

- For workplace charging location, the probability of arrival is highest in the morning.
- For private charging location, the probability of arrival is highest in the evening hours.
- For public charging location, the probability of arrival follows a duck curve pattern.

**Usage:**

The data are used in the `EV_spawner` function in the `utilities/utils.py` file to determine the probability of arrival on **weekdays** for each charging location type at each arrival time.

### Distribution of Arrival (Weekend)

Data describes the probability distribution of EV arrivals throughout the day on weekends.

**Data source:**

- `distribution-of-arrival-weekend.csv`

**Columns:**

- `Arrival time`:
  - arrival time
  - data type: string
  - range: 00:00 to 23:45
- `private`:
  - probability of arrival at private charging location
  - data type: float
  - range: 0-100
- `public`:
  - probability of arrival at public charging location
  - data type: float
  - range: 0-100

**Visualizations:**

- Line plot of arrival probabilities by arrival time in 15 minute intervals

**Insights:**

- For both the private and public charging locations, the probability of arrival is highest in the evening hours.
- The curve of for the public charging location is a bit shifted to the left compared to the private charging location.

**Usage:**

The data are used in the `EV_spawner` function in the `utilities/utils.py` file to determine the probability of arrival on **weekends** for each charging location type at each arrival time.

## EV Connection Time Data

### Distribution of Connection Time

Data describes how long EVs remain connected to charging stations as a cummulative distribution. Specifically, the cummulative distribution function describes the probability of an EV being connected to the charging station for a certain amount of time t or longer.

**Data source:**

- `distribution-of-connection-time.csv`

**Structure:**

- `Percentage of charging events`:
  - cummulative probability of connection time
  - data type: float
  - range: 0-100
- `private`:
  - time of connection at private charging location in hours
  - data type: float
  - range: 0-72
- `public`:
  - time of connection at public charging location in hours
  - data type: float
  - range: 0-72
- `workplace`:
  - time of connection at workplace charging location in hours
  - data type: float
  - range: 0-72

**Key statistics:**

- Average connection time: ~ 12, 8, 7 hours for private, public, and workplace charging location respectively
- Median connection time: ~ 11, 4, 5 hours for private, public, and workplace charging location respectively
- 75th percentile: ~ 15, 12, 9 hours for private, public, and workplace charging location respectively

**Visualizations:**

- Cumulative distribution function of connection time by location type

**Insights:**

- The connection time is longer for private charging location compared to public and workplace charging location.
- The connection time is longer for public charging location compared to workplace charging location.
- The connection time is no longer than 72 hours for all location types.

**Usage:**

N/A

## EV Energy Demand Data

### Distribution of Energy Demand

Data describes the cummulative distribution of energy demand for EV charging sessions. Specifically, the cummulative distribution function describes the probability of an EV demanding for a certain amount of energy or more in % of battery capacity.

**Data source:**

- `distribution-of-energy-demand.csv`

**Structure:**

- `Percentage of charging events`:
  - cummulative probability of energy demand
  - data type: int
  - range: 0-100
- `private`:
  - energy demand at private charging location in % of battery capacity
  - data type: float
  - range: 0-100
- `public`:
  - energy demand at public charging location in % of battery capacity
  - data type: float
  - range: 0-100
- `workplace`:
  - energy demand at workplace charging location in % of battery capacity
  - data type: float
  - range: 0-100

**Key statistics:**

- Average energy demand: [X kWh]
- Median energy demand: [X kWh]
- 90th percentile: [X kWh]

**Visualizations:**

- Histogram of energy demand values
- Cumulative distribution function

**Insights:**

- [Patterns in energy demand distribution]
- [Implications for grid capacity planning]

**Usage:**

N/A

### Mean Demand per Arrival Time

Data shows how the mean energy demand by arrival time for different location types.

**Data source:**

- `mean-demand-per-arrival.csv`

**Structure:**

- `Arrival Time`:
  - arrival time in 30 minute intervals
  - data type: string
  - range: 00:00 to 23:30
- `home`:
  - mean energy demand at private charging location in kWh
  - data type: float
- `public`:
  - mean energy demand at public charging location in kWh
  - data type: float
- `work`:
  - mean energy demand at workplace charging location in kWh
  - data type: float

**Key statistics:**

- maximum mean energy demand: ~ 32 kWh
- minimum mean energy demand: ~ 10 kWh

**Visualizations:**

- Line plot of mean energy demand by arrival time

**Insights:**

- the mean energy demand at workplace charging location is overall lower than at home and public charging location.
- for home and public charging location, the mean energy demand is highest in the evening and morning hours.

**Usage:**

The data are used in the `spawn_single_EV` function in the `utilities/utils.py` file to determine the energy required for a spawned EV at a particular arrival time.

## EV Session Length Data

### Mean Session Length per Hour

Data shows how the mean charging session length varies by arrival time for different location types.

**Data source:**

- `mean-session-length-per.csv`

**Structure:**

- `Arrival Time`:
  - arrival time in 30 minute intervals
  - data type: string
  - range: 00:00 to 23:30
- `home`:
  - mean session length at private charging location in hours
  - data type: float
- `public`:
  - mean session length at public charging location in hours
  - data type: float
- `work`:
  - mean session length at workplace charging location in hours
  - data type: float

**Key statistics:**

- maximum mean session length: ~ 15 hours
- minimum mean session length: ~ 2 hour

**Visualizations:**

- Line plot of mean session length by arrival time

**Insights:**

- In evening arrival hours, the mean session length is longer for home and public charging location compared to work charging location.
- Home and public charging locations follow a similar pattern, although shifted.
- The curve for the work location has a declining trend from morning to evening.

**Usage:**

The data are used in the `spawn_single_EV` function in the `utilities/utils.py` file to determine the charging session length for a spawned EV at a particular arrival time.

## Residential Load Data

### Residential Loads

Data describes the inflexible residential electricity load profiles.

**Data source:**

- `residential_loads.csv`

**Structure:**

- The data frame has no header; has 35040 rows and 25 columns.
- The data is in kW.
- The row index is the timestamp in 15 minute intervals for 1 year.
- The columns are the load profiles of different appliances.

**Key statistics:**

- Average daily peak load: ~ 2 kW
- Average daily minimum load: ~ 0.8 kW

**Visualizations:**

- Time series plot of average daily load profile
- Heatmap of average daily load profile by hour for one week
- Time series plot of load profiles for 5 random appliances for one random day
- Time series plot of the sum of 10 random appliances for one random day

**Insights:**

- The average daily load profile is a sawtooth pattern with a peak in the evening and a minimum in the morning.
- The load on weekends is lower than on weekdays.

**Usage:**

The data are used in the `generate_residential_inflexible_loads` function in the `utilities/loaders.py` file to generate the inflexible residential electricity load profiles for each transformer. The generated data is used to create forecast for the inflexible loads.

## PV Generation Data

### PV Generation (Netherlands)

Data describes photovoltaic (PV) electricity generation profiles for one year.

**Data source:**

- `pv_netherlands.csv`

**Structure:**

- **time**:
  - timestamp in 1 hour intervals for 1 year
  - data type: string
  - range: 2019-01-01 00:00:00 to 2020-01-01 00:00:00
- **local_time**:
  - timestamp in 1 hour intervals for 1 year in local time
  - data type: string
  - range: 2019-01-01 01:00:00 to 2020-01-01 01:00:00
- **electricity**:
  - PV electricity generation in kW
  - data type: float
  - range: 0-0.85 kW

**Key statistics:**

- Typical profile of PV generation for a country in central Europe.

**Visualizations:**

- Time series plot of PV generation
- Bar chart of PV generation by hour of day
- Bar chart of PV generation by month

**Insights:**

- N/A

**Usage:**

The data are used in the `generate_pv_generation` function in the `utilities/loaders.py` file to generate the PV generation for each transformer. The generated data is used to create forecast for the PV generation.

## Electricity Price Data

### Day-ahead Prices (Netherlands)

Data describes the day-ahead electricity market prices in the Netherlands from 2015-2024.

**Data source:**

- `Netherlands_day-ahead-2015-2024.csv`

**Structure:**

- **Country**:
  - country
  - data type: string
  - range: Netherlands
- **Datetime (UTC)**:
  - timestamp in 1 hour intervals
  - data type: string
  - range: 2015-01-01 00:00:00 to 2025-01-07 23:00:00
- **Datetime (Local)**:
  - timestamp in 1 hour intervals in local time
  - data type: string
  - range: 2015-01-01 01:00:00 to 2025-01-08 00:00:00
- **Price (EUR/MWhe)**:
  - electricity price in EUR/MWh
  - data type: float
  - range: -500-1000 EUR/MWh

**Key statistics:**

- maximum price: ~ 1000 EUR/MWh
- minimum price: ~ -500 EUR/MWh

**Visualizations:**

- Time series plot of prices from 2015-2024
- Distribution of prices by hour of day

**Insights:**

- The data have mixed formats, some dates are in %Y-%m-%d %H:%M:%S format, some in %d/%m/%Y %H:%M format.
- There are also duplicate datetimes in the data.
- Prices are mostly positive, but there are some negative prices.
- From COVID-19 pandemic and the war in Ukraine, the prices went up significantly in the beginning of 2021.

**Usage:**

The data are used in the `load_electricity_prices` function in the `utilities/loaders.py` file to load the electricity prices. From the electricity prices, the charge and discharge prices are created. It is assumed that the charge and discharge prices are the same, and that the prices are the same for all charging stations.
