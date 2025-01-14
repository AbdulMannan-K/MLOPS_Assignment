import pandas as pd
from surprise import Reader, Dataset
from surprise import SVD
import joblib

# Load MovieLens dataset
data = pd.read_csv('path/to/movielens_dataset.csv')

# Define Reader object for Surprise library
reader = Reader(rating_scale=(1, 5))

# Load dataset into Surprise Dataset format
dataset = Dataset.load_from_df(data[['userId', 'movieId', 'rating']], reader)

# Train SVD algorithm
algo = SVD()
trainset = dataset.build_full_trainset()
algo.fit(trainset)

# Serialize and save the trained model to a file
joblib.dump(algo, 'model.pkl')
