from pydantic import BaseModel, Field
from typing import Dict

class PredictionResponse(BaseModel):
    predicted_category: int = Field(
        ...,
        description = "The predicted diabetes category label",
        example = "1"
    )

    cofidence: float = Field(
        ...,
        description = "The confidence score of the prediction",
        example = "0.75"
    )

    class_probabilites: Dict[str, float] = Field(
        ...,
        description = "The probabilities for each class label",
        example = {"0": 0.25, "1": 0.75}
    )
