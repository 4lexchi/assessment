# The data provided

"""data = {
  "region": {
    "name": "Africa",
    "avgAge": 19.7,
    "avgDailyIncomeInUSD": 5,
    "avgDailyIncomePopulation": 0.71
  },
  "periodType": "weeks",
  "timeToElapse": 8,
  "reportedCases": 674,
  "population": 66622705,
  "totalHospitalBeds": 1380614
}
"""


def estimator(data): # this function outputs a dictionary after working on the data provided
  duration = data["timeToElapse"]
  if data["periodType"] == "days": # if the duration provided in the data is in days
    duration *= 1
  if data["periodType"] == "weeks": # if the duration provided in the data is in weeks
    duration *= 7
  if data["periodType"] == "months": # if the duration provided in the data is in weeks
    duration *= 30

  currentlyInfected = data["reportedCases"] * 10
  severeImpact = data["reportedCases"] * 50

  data = {
  "data": data, # the data provided
  "impact": {"currentlyInfected": currentlyInfected, "infectionsByRequestedTime": currentlyInfected},
  "severeImpact": {"currentlyInfected": severeImpact, "infectionsByRequestedTime": severeImpact}
  }

  x = data["impact"] # creates a dictionary from data
  y = data["severeImpact"] # creates a dictionary from data

  x["infectionsByRequestedTime"] = x["infectionsByRequestedTime"] * (2 ** (duration // 3)) # calculates the projected number of infections
  y["infectionsByRequestedTime"] = y["infectionsByRequestedTime"] * (2 ** (duration // 3)) # calculates the projected number of severe infections

# print(type(data))
# print(data)

  return(data) # outputs the worked on data
 

# estimator(data)