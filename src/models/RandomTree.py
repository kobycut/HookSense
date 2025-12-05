from src.data.dataStorage import getWeatherFeatures
import random
from datetime import datetime, timedelta
from src.models.Baseline import BaselineRuleModel
import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score


class RandomTreeModel:
    def __init__(self, location_name: str):
        self.getWeatherFeatures = getWeatherFeatures(location_name)
        self.historic_baseline_instances = []
        self.training_data = None  # Will store the formatted training data

    def predict(self):
        """
        Predict fishing quality for the current location using the trained Random Forest model

        Returns:
            float: Predicted fishing quality score
        """
        if not hasattr(self, 'model') or self.model is None:
            raise ValueError("Model not trained. Call train_model() first or use the complete workflow.")

        # Use the current location's weather features (from __init__)
        return self.predict_new_conditions(self.getWeatherFeatures)

    def generate_historical_labels(self, num_samples=10):
        """
        Generate random historical data samples for training
        """
        # Pool of diverse cities worldwide
        city_pool = [
            'New York', 'Miami', 'Seattle', 'Denver', 'Austin',
            'Chicago', 'Los Angeles', 'Portland', 'Boston', 'Phoenix',
            'San Francisco', 'Las Vegas', 'Atlanta', 'Dallas', 'Houston',
            'Minneapolis', 'Detroit', 'Philadelphia', 'San Diego', 'Tampa',
            'London', 'Paris', 'Tokyo', 'Oslo', 'Sydney',
            'Toronto', 'Vancouver', 'Melbourne', 'Berlin', 'Madrid'
        ]

        # Generate random dates between 2015 and 2025
        start_date = datetime(2015, 1, 1)
        end_date = datetime(2025, 12, 4)
        date_range = (end_date - start_date).days

        # Generate random combinations
        samples = []
        for _ in range(num_samples):
            random_city = random.choice(city_pool)
            random_days = random.randint(0, date_range)
            random_date = start_date + timedelta(days=random_days)
            date_str = random_date.strftime('%Y-%m-%d')
            samples.append((random_city, date_str))

        # Create weather feature instances for each sample
        # Store as baseline model instances
        baseline_instance_collection = []
        count = 0
        for city, date in samples:
            count +=1
            try:
                baseline_instance = BaselineRuleModel(city)
                baseline_instance_collection.append(baseline_instance)
                print("Generated sample ", count)
            except Exception as e:
                print(f"Warning: Could not get data for {city} on {date}: {e}")
        self.historic_instances = baseline_instance_collection
        return baseline_instance_collection

    def score_historical_data(self, baseline_instance: BaselineRuleModel):
        return baseline_instance.predict()

    def prepare_training_data(self):
        """
        Convert historical samples into training format (features and labels)

        Returns:
            X: Feature matrix (numpy array or pandas DataFrame)
            y: Labels (numpy array) - fishing quality scores
        """
        if not self.historic_instances:
            print("No historical data. Run generate_historical_labels() first.")
            return None, None

        feature_rows = []
        labels = []

        for baseline_instance in self.historic_instances:
            try:
                # Get weather features from the instance
                weather = baseline_instance.getWeatherFeatures

                # Extract features as a dictionary
                features = {
                    'temperature': weather.get_temperature(),
                    'humidity': weather.get_humidity(),
                    'precipitation': weather.get_precipitation(),
                    'precip_prob': weather.get_precipitation_probability(),
                    'pressure': weather.get_pressure(),
                    'wind_speed': weather.get_wind_speed(),
                    'cloud_cover': weather.get_cloud_cover(),
                    'visibility': weather.get_visibility(),
                    'uv_index': weather.get_uv_index(),
                    'moon_phase': weather.get_moon_phase(),
                }

                # Get label from baseline model prediction
                label = baseline_instance.predict()  # This returns the score

                feature_rows.append(features)
                labels.append(label)

            except Exception as e:
                print(f"Warning: Could not process instance: {e}")
                continue

        # Convert to DataFrame for features and numpy array for labels
        X = pd.DataFrame(feature_rows)
        y = np.array(labels)

        # Store for later use
        self.training_data = {'X': X, 'y': y}

        print(f"✅ Prepared training data: {len(X)} samples, {len(X.columns)} features")
        print(f"   Features: {list(X.columns)}")
        print(f"   Label range: {y.min():.1f} - {y.max():.1f}")

        return X, y

    def save_training_data(self, filepath='data/processed/training_data.csv'):
        """Save the prepared training data to CSV"""
        if self.training_data is None:
            print("No training data to save. Run prepare_training_data() first.")
            return

        # Combine features and labels
        df = self.training_data['X'].copy()
        df['fishing_quality_score'] = self.training_data['y']

        # Save to CSV
        df.to_csv(filepath, index=False)
        print(f"✅ Training data saved to: {filepath}")
        return filepath

    def train_model(self, test_size=0.2, random_state=42):
        """
        Train Random Forest model on the prepared data

        Args:
            test_size: Fraction of data to use for testing (default 0.2 = 20%)
            random_state: Random seed for reproducibility

        Returns:
            dict: Training results including model and metrics
        """
        if self.training_data is None:
            print("No training data available. Run prepare_training_data() first.")
            return None

        X = self.training_data['X']
        y = self.training_data['y']

        # Split into training and testing sets
        X_train, X_test, y_train, y_test = train_test_split(
            X, y, test_size=test_size, random_state=random_state
        )

        print(f"\n Training Random Forest Model...")
        print(f"   Training samples: {len(X_train)}")
        print(f"   Testing samples: {len(X_test)}")

        # Create and train Random Forest model
        self.model = RandomForestRegressor(
            n_estimators=100,      # Number of trees
            max_depth=10,          # Maximum depth of trees
            random_state=random_state,
            n_jobs=-1              # Use all CPU cores
        )

        self.model.fit(X_train, y_train)

        # Make predictions on test set
        y_pred = self.model.predict(X_test)

        # Calculate metrics
        mse = mean_squared_error(y_test, y_pred)
        rmse = np.sqrt(mse)
        r2 = r2_score(y_test, y_pred)

        # Feature importance
        feature_importance = pd.DataFrame({
            'feature': X.columns,
            'importance': self.model.feature_importances_
        }).sort_values('importance', ascending=False)

        print(f"Top Features:")
        for idx, row in feature_importance.head(5).iterrows():
            print(f"   {row['feature']}: {row['importance']:.3f}")

        results = {
            'model': self.model,
            'X_train': X_train,
            'X_test': X_test,
            'y_train': y_train,
            'y_test': y_test,
            'y_pred': y_pred,
            'rmse': rmse,
            'r2': r2,
            'feature_importance': feature_importance
        }

        return results

    def predict_new_conditions(self, weather_features):
        """
        Predict fishing quality for new weather conditions

        Args:
            weather_features: getWeatherFeatures instance or dict with weather data

        Returns:
            float: Predicted fishing quality score
        """
        if not hasattr(self, 'model') or self.model is None:
            print("Model not trained. Run train_model() first.")
            return None

        # Extract features
        if isinstance(weather_features, dict):
            features = weather_features
        else:
            features = {
                'temperature': weather_features.get_temperature(),
                'humidity': weather_features.get_humidity(),
                'precipitation': weather_features.get_precipitation(),
                'precip_prob': weather_features.get_precipitation_probability(),
                'pressure': weather_features.get_pressure(),
                'wind_speed': weather_features.get_wind_speed(),
                'cloud_cover': weather_features.get_cloud_cover(),
                'visibility': weather_features.get_visibility(),
                'uv_index': weather_features.get_uv_index(),
                'moon_phase': weather_features.get_moon_phase(),
            }

        # Convert to DataFrame (same format as training data)
        X_new = pd.DataFrame([features])

        # Make prediction
        prediction = self.model.predict(X_new)[0]

        return prediction