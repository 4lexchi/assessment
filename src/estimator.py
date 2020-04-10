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
  if data["periodType"] == "months": # if the duration provided in the data is in months
    duration *= 30

  currentlyInfected = data["reportedCases"] * 10
  severeImpact = data["reportedCases"] * 50
  severeCasesByRequestedtime = 1
  hospitalBedsByRequestedTime = 1
  availableHospitalBeds = (data["totalHospitalBeds"] * 0.35)

  data = {
  "data": data, # the data provided
  "impact": {
    "currentlyInfected": currentlyInfected,
    "infectionsByRequestedTime": currentlyInfected,
    "severeCasesByRequestedtime": severeCasesByRequestedtime,
    "hospitalBedsByRequestedTime": hospitalBedsByRequestedTime
    },

  "severeImpact": {
    "currentlyInfected": severeImpact,
    "infectionsByRequestedTime": severeImpact,
    "severeCasesByRequestedtime": severeCasesByRequestedtime,
    "hospitalBedsByRequestedTime": hospitalBedsByRequestedTime
    }
  }

  x = data["impact"] # creates a dictionary from data
  y = data["severeImpact"] # creates a dictionary from data

  x["infectionsByRequestedTime"] = x["infectionsByRequestedTime"] * (2 ** (duration // 3)) # (calculates the projected number) of infections
  y["infectionsByRequestedTime"] = y["infectionsByRequestedTime"] * (2 ** (duration // 3)) # (calculates the projected number) of severe infections
  x["severeCasesByRequestedtime"] = int(x["infectionsByRequestedTime"] * 0.15) # "" severe cases
  y["severeCasesByRequestedtime"] = int(y["infectionsByRequestedTime"] * 0.15) # "" severe cases
  x["hospitalBedsByRequestedTime"] = int(availableHospitalBeds - x["severeCasesByRequestedtime"]) # "" bed availability
  y["hospitalBedsByRequestedTime"] = int(availableHospitalBeds - y["severeCasesByRequestedtime"]) # "" bed availability

  # print(type(data))
  # print(data)

  return(data) # outputs the worked on data
 

# estimator(data)