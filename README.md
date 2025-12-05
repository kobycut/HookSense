#  🎣 HookSense 🎣
Machine Learning focused agent that gathers live forecast, barometric pressure, and moon cycle data to predict how good a day is to go fishing. Provides information of what water depth fish will be at, etc.

## Tech Stack

**Python:** Machine learning and Data Science techniques easily available. Libraries listed below provide value for the prediction model.

**Pandas Library:** Manipulate and handle essential data, dataframe utility.

**Numpy Library:** Numerical operations, math etc.

**Scikit-learn:** Data manipulation and Random Forest Regression model.

### Variables used and API's for each
- **Location** (OpenWeather API)
- **Temperature** (Visual Crossing API)
- **Rainfall/precipitation** (Visual Crossing API)
- **Barometric pressure** (Visual Crossing API)
- **Wind speed** (Visual Crossing API)
- **Cloud cover** (Visual Crossing API)
- **Moon cycle** (Visual Crossing API)
- **Historical data** (Visual Crossing API)

### Machine Learning Techniques
**Prediction Target:** Predict whether a day is good for fishing

**Classification:** Rating score out of 100, 100 being the perfect day for fishing and 0 being the worst

**Model Type:** Rule-Based Heuristic, Random Forest, another model if there's time

### Plan
<img width="600" height="600" alt="image" src="https://github.com/user-attachments/assets/94d848d5-9d78-4b01-a707-01ced788f7e5" />

### Actual Time Taken
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
   - Creates n samples, each sample being a baseline model instance with a random date and location.
2. Prepare training data
   - Takes each sample and extracts each feature value combination and the associated total score. All of these values are appended to a dataframe. This dataframe holds all the prepared historical data.
3. Save training data
   - Saves the prepared training data dataframe to a csv so that it can be used in the future to train the model.
4. Train model
   - Uses RandomForestRegressor model with parameters=(estimators=100, depth=10, random state=42, jobs=1), fits the model with the saved training data and then calculates feature importance.
5. Predict
    - Uses fitted model to predict score for given features of given date and location. Returns a prediction out of 100 of how good a day it is to go fishing.

### What I would do differently if I could start over
If I could start over I would definitely spend more time gathering real fishing data and how it correlates to the given weather conditions. Having better baseline data for what makes a good fishing day would help the model make a better prediction. This data could also be used to train the Random Forest model instead of having to use the baseline model which most likely is resulting in slightly skewed data. If I could start over I would find better initial prediction data.
### Lessons Learned
There are many many various factors that make a prediction model accurate. There is always more that can be done to make it more accurate. These models can get very complicated very quickly due to the amount of conditions and data they require to make a decent prediction. The Random Forest Regressor was simple enough to use once all the data was gathered, cleaned, prepared, and saved. The hard part about this assigment were the data gathering and cleaning. Using the actual model was fairly straight forward and not too difficult. Using Sklearn and Numpy as tools helped with the training and fitting the model. This was an insightful project to work on and it will be interesting to go fishing on the days my model says are the best and see the results first hand :)) 🐟🎣

### Final Results!


