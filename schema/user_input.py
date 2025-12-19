from pydantic import BaseModel, Field
from typing import Literal, Annotated

# pydantic model to validate incoming data
class UserInput(BaseModel):

    weight: Annotated[float, Field(gt=0, description="Weight in kilograms")]
    height: Annotated[float, Field(gt=0, description="Height in Meters")]
    pregnancies: Annotated[int, Field(ge=0, description="Number of times pregnant")]
    glucose: Annotated[int, Field(ge=0, description="Glucose Level")]
    blood_pressure: Annotated[int, Field(gt=0, description="Blood Pressure value")]
    skin_thickness: Annotated[int, Field(ge=0, description="Skin Thickness")]
    insulin: Annotated[int, Field(ge=0, description="Insulin level")]
    diabetes_pedigree_function: Annotated[float, Field(gt=0, description="Diabetes Pedigree Function value")]
    age: Annotated[int, Field(gt=0, description="Age of the person")]

    # @computed_field
    # @property
    # def bmi(self) -> float:
    #     return self.weight / (self.height ** 2)
    