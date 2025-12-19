from fastapi import FastAPI
from fastapi.responses import JSONResponse
from schema.user_input import UserInput
from model.predict import predict_output, model, MODEL_VERSION
from schema.prediction_response import PredictionResponse

app = FastAPI()

# Human readable
@app.get('/')
def home():
    return {'message' : 'Diabetes Ptrediction API'}

# machine readable
@app.get('/health')
def health_check():
    return {
        'status': 'OK',
        'version': MODEL_VERSION,
        'model_loaded': model is not None
    }

@app.post('/predict', response_model = PredictionResponse)
def predict_diabetes(input: UserInput):

    bmi = input.weight / (input.height ** 2)

    user_input = ([{

        'Pregnancies': input.pregnancies,
        'Glucose': input.glucose,
        'BloodPressure': input.blood_pressure,
        'SkinThickness': input.skin_thickness,
        'Insulin': input.insulin,
        'BMI': bmi,
        'DiabetesPedigreeFunction': input.diabetes_pedigree_function,
        'Age': input.age
    }])

    try:

        prediction = predict_output(user_input)

        return JSONResponse(
            status_code=200, 
            content={'response': prediction}
        )
    
    except Exception as e:

        return JSONResponse(
            status_code = 500,
            content = str(e)
        )   