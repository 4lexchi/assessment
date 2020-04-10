# The data provided

"""data = {
  "region": {
    "name": "Africa",
    "avgAge": 19.7,
    "avgDailyIncomeInUSD": 5,
    "avgDailyIncomePopulation": 0.71
  },
  "periodType": "days",
  "timeToElapse": 58,
  "reportedCases": 674,
  "population": 66622705,
  "totalHospitalBeds": 1380614
}
"""


def estimator(data): # this function outputs a dictionary after working on the data provided
  duration = data["timeToElapse"] # number of days, weeks or months
  income = data["region"]["avgDailyIncomeInUSD"] # daily income
  average = data["region"]["avgDailyIncomePopulation"] # percentage that earns the income above
  currentlyInfected = data["reportedCases"] * 10
  severeImpact = data["reportedCases"] * 50
  availableHospitalBeds = (data["totalHospitalBeds"] * 0.35)
  

  if data["periodType"] == "days": # (if the duration provided in the data is in) days
    duration *= 1
  if data["periodType"] == "weeks": # "" weeks
    duration *= 7
  if data["periodType"] == "months": # "" months
    duration *= 30

  data = {
  "data": data, # the data provided
  "impact": {
    "currentlyInfected": currentlyInfected,
    "infectionsByRequestedTime": currentlyInfected,
    },

  "severeImpact": {
    "currentlyInfected": severeImpact,
    "infectionsByRequestedTime": severeImpact,
   }
  }

  x = data["impact"] # creates a dictionary from data
  y = data["severeImpact"] # creates a dictionary from data

  x["infectionsByRequestedTime"] = x["infectionsByRequestedTime"] * (2 ** (duration // 3)) # (estimates the projected number of) infections
  y["infectionsByRequestedTime"] = y["infectionsByRequestedTime"] * (2 ** (duration // 3)) # (estimates the projected number of) severe infections
  x["severeCasesByRequestedTime"] = int(x["infectionsByRequestedTime"] * 0.15) # "" severe cases
  y["severeCasesByRequestedTime"] = int(y["infectionsByRequestedTime"] * 0.15) # "" 
  x["hospitalBedsByRequestedTime"] = int(availableHospitalBeds - x["severeCasesByRequestedTime"]) # "" bed availability
  y["hospitalBedsByRequestedTime"] = int(availableHospitalBeds - y["severeCasesByRequestedTime"]) # "" 
  x["casesForICUByRequestedTime"] = int(x["infectionsByRequestedTime"] * 0.05) # "" ICU care
  y["casesForICUByRequestedTime"] = int(y["infectionsByRequestedTime"] * 0.05) # ""
  x["casesForVentilatorsByRequestedTime"] = int(x["infectionsByRequestedTime"] * 0.02) # "" cases to require ventilators
  y["casesForVentilatorsByRequestedTime"] = int(y["infectionsByRequestedTime"] * 0.02) # ""
  x["dollarsInFlight"] = int(((x["infectionsByRequestedTime"]) * average * income) / duration) # estimates the amount of money lost within the period 
  y["dollarsInFlight"] = int(((y["infectionsByRequestedTime"]) * average * income) / duration) # ""
  x.update()
  y.update()

  # print(type(data))
  # print(data)

  return(data) # outputs the worked on data
 

# estimator(data)