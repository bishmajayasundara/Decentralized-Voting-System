from fastapi import FastAPI, UploadFile, File
from app import utils, model, schemas

app = FastAPI()

@app.get("/predict")
async def test_predict():
    img_path = r"C:\Users\MSI20\Downloads\WIN_20250414_12_28_10_Pro.png" # Replace with your path
    img_array = utils.preprocess_image_from_path(img_path)  # You’ll define this function
    prediction, label = model.predict(img_array)
    return {"prediction": float(prediction), "label": label}
