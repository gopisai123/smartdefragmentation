# # src_/predictor.py

# def predict_allocation(allocation_history):
#     # A simple predictor (e.g., predicting the next allocation size based on historical data)
#     if not allocation_history:
#         return 1  # Default prediction if no history

#     avg_size = sum(allocation_history) // len(allocation_history)
#     return avg_size  # Predict average allocation size as a simple approach


# src_/predictor.py (Advanced)
import numpy as np
from sklearn.linear_model import LinearRegression
from collections import deque

class AIPredictor:
    def __init__(self, memory_size=20):
        self.history = []
        self.memory_size = memory_size
        self.X = deque(maxlen=100)  # Features window
        self.y = deque(maxlen=100)  # Labels window
        self.model = LinearRegression()
        
    def add_allocation(self, size, position, fragmentation):
        """Record allocation with contextual features"""
        features = [
            size,
            position/self.memory_size,
            fragmentation,
            len(self.X) % 24  # Simulate time-of-day pattern
        ]
        self.X.append(features)
        self.y.append(size)
        
        if len(self.X) > 10:  # Minimum samples to train
            self.model.fit(np.array(self.X), np.array(self.y))
    
    def predict_next(self):
        """Predict with contextual awareness"""
        if len(self.X) < 5:
            return 1  # Default prediction
            
        # Create prediction features
        last = self.X[-1]
        next_features = [
            last[0],  # Last size
            (last[1] + 0.1) % 1.0,  # Position trend
            last[2] * 0.9,  # Expected fragmentation
            (len(self.X) + 1) % 24  # Next time slot
        ]
        
        prediction = self.model.predict([next_features])[0]
        return np.clip(round(prediction), 1, 4)