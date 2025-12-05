# HookSense
Machine Learning focused agent that gathers live forecast, barometric pressure, and moon cycle data to predict how good a day is to go fishing. Provides information of what water depth fish will be at, etc.

## Tech Stack

Python: Easy to use Machine learning and Data Science techniques with. Libraries provide value for the prediction model.
Pandas Library: Manipulate and handling essential data
Numpy Library: Numerical operations
Scikit-learn: Data manipulation

### Variables used and API's for each
- Temperature (OpenWeather API)
- Rainfall/precipitation (Visual Crossing API)
- Barometric pressure (Visual Crossing API)
- Wind speed (OpenWeather API)
- Cloud cover (OpenWeather API)
- Moon cycle (Visual Crossing API)
- Historical data (NOAA CDO API)

### Machine Learning Techniques
Prediction Target: Predict whether a day is good for fishing
Classification: Rating scale of terrible/bad/neutral/good/great/excellent
Model Type: Rule-Based Heuristic, Cecision tree (maybe), Random Forest (if there's time)

### Plan
<img width="600" height="600" alt="image" src="https://github.com/user-attachments/assets/94d848d5-9d78-4b01-a707-01ced788f7e5" />

- [x] Initial Plan (1 hour)
- [x] Tech Stack/Repo Setup (30 minutes)
- [x] Gather Data from API's (2 1/2 hours)
- [x] Store Data (1 hour)
- [x] Data Exploration/Cleaning (3 hours)
- [x] Feature Engineering (1 hour)
- [x] Baseline Model (4 hours)
- [x] Random Forest Model (6 hours)
- [x] Evaluation of Model Prediction (1 hour)
- [ ] Deploy with simple frontend if enough time

### How it works
#### API's
Using the VisualCrossing and OpenWeather API's the feature data is pulled in for a given date and location. Being able to change the date allows it to pull historical weather information that is used to train the Random Forest model. These API's provide the feature data for both models.

#### Baseline Model
The baseline model is a rule model that simply calculates a score based off of fixed values from the feature data. For example, if the moon cycle is close to a full or new moon it returns a moon score of 0.1, otherwise it returns a moon score of 0.6. Each feature has a score calculation such as this. If all feature scores are perfect, when added up they equal a total score of 100, meaning the perfect day for fishing. This baseline model is very simple and is mostly used to evaluate the Random Forest Model and help with training data.

#### Random Forest Model
The Random Forest model has a few key steps.
1. Generate historical data
   - This step 
2. Prepare training data
   - 
3. Save training data
   - 
4. Train model
   - 
5. Predict
    - 

### What I would do differently if I could start over
### Lessons Learned

