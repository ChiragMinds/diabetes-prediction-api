import pickle
import pandas as pd

# import the ml model
with open('model/model.pkl', 'rb') as f:
    model = pickle.load(f)

#MLFlow
MODEL_VERSION = '1.0.0'

# Get class labels from the model
class_labels = model.classes_.tolist()

def predict_output(user_input: dict):

    df = pd.DataFrame(user_input)

    if hasattr(model, "feature_names_in_"):
        df = df[model.feature_names_in_]

    predicted_class = model.predict(df)[0].item()

    if hasattr(model, "predict_proba"):
        probabilities = model.predict_proba(df)[0]
        confidence = probabilities.max().item()
        class_probs = {
            str(label): prob.item()
            for label, prob in zip(class_labels, map(lambda p:round(p, 2), probabilities))
        }
    else:
        confidence = None
        class_probs = None

    return {
        "predicted_category": predicted_class,
        "confidence": round(confidence, 2) if confidence is not None else None,
        "class_probabilities": class_probs
    }