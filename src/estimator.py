data = {
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

currentlyInfected = data["reportedCases"] * 10
severeImpact = data["reportedCases"] * 50
output = {
  "data": data,
  "impact": currentlyInfected,
  "severeImpact": severeImpact
}

days = 0

def estimator(days):
  ci = output["impact"] * (2 ** (days//3))
  si = output["severeImpact"] * (2 ** (days//3))
  # print("impact: " + str(ci) + ", severeImpact: " + str(si))
  return ci, si

# estimator(30)