import sys
import os

# Add the project root to the Python path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from src.data.collectors import LocationCollector, WeatherCollector
from src.data.dataStorage import getWeatherFeatures
from src.models.Baseline import BaselineRuleModel
from src.models.RandomTree import RandomTreeModel

class TestRandomTreeModel:
    def __init__(self, location_name="provo"):
        self.location_name = location_name
        self.instances = []
        self.random_tree_model = RandomTreeModel(self.location_name)


    def test_generate_historical_labels(self):
        print("Testing RandomTreeModel.generate_historical_labels...")
        self.instances = self.random_tree_model.generate_historical_labels(num_samples=5)
        print("✅ generate_historical_labels executed successfully.", len(self.instances), "instances generated.")

    def test_score_historical_data(self):
        print("Testing RandomTreeModel.score_historical_data...")
        # each instance is a BaselineRuleModel object
        score = self.random_tree_model.score_historical_data(self.instances[0])
        print("✅ score_historical_data executed successfully.", "score: ", score)


    def test_predict(self):
        print("Testing RandomTreeModel.predict...")
        self.random_tree_model.generate_historical_labels(num_samples=100)
        self.random_tree_model.prepare_training_data()
        self.random_tree_model.save_training_data()
        self.random_tree_model.train_model()

        prediction = self.random_tree_model.predict()
        print("✅ predict executed successfully.", "prediction: ", prediction)



if __name__ == "__main__":
    print("Running tests for RandomTreeModel...")
    test = TestRandomTreeModel()
    # test.test_generate_historical_labels()
    # test.test_score_historical_data()
    test.test_predict()