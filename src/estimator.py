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

def estimator(data):
  days = 0
  currentlyInfected = data["reportedCases"] * 10
  severeImpact = data["reportedCases"] * 50
  data = {
  "data": data,
  "impact": currentlyInfected,
  "severeImpact": severeImpact
  }
  data["impact"] = data["impact"] * (2 ** (days//3))
  data["severeImpact"] = data["severeImpact"] * (2 ** (days//3))
 # print(data)
  return(data)

estimator(data)