# Plant Classification API with Flask

This repository contains the code and documentation for a Flask-based API that performs plant species classification. The API uses a pretrained model to predict the species of a plant from an uploaded image and provides a confidence score for the prediction.

## Table of Contents

- [Overview](#overview)
- [API Endpoint](#api-endpoint)
- [Request and Response Format](#request-and-response-format)
- [Installation](#installation)
- [Running the Application](#running-the-application)
- [Example Usage](#example-usage)

## Overview

The Flask API is designed to classify plant species based on an uploaded image. It utilizes a pretrained classification model and returns a JSON response containing the predicted species and the confidence score.

## API Endpoint

### `/predict`

- **Method**: `POST`
- **Description**: Predicts the species of the plant in the uploaded image.

## Request and Response Format

### Request

- **Content-Type**: `multipart/form-data`
- **Key**: `file`
- **Value**: Image file to be classified

Example cURL request:

```bash
curl -X POST http://127.0.0.1:5000/predict \
  -F file=@path_to_your_image.jpg
```

### Response

The API returns a JSON object with the following structure:

```json
{
    "confidence": 0.9997437596321106,
    "predicted_species": "Singkong"
}
```

- **`confidence`**: The model's confidence score for the prediction.
- **`predicted_species`**: The name of the predicted plant species.

## Installation

1. Clone the repository:

```bash
git clone https://github.com/your-username/plant-classification-api.git
cd plant-classification-api
```

2. Install the required libraries:

```bash
pip install -r requirements.txt
```

## Running the Application

1. Start the Flask application:

```bash
python app.py
```

2. The API will be available at `http://127.0.0.1:5000`.

## Example Usage

You can test the API using tools like `curl`, Postman, or any HTTP client. For example, using Python:

```python
import requests

url = "http://127.0.0.1:5000/predict"
image_path = "path_to_your_image.jpg"

with open(image_path, "rb") as image_file:
    response = requests.post(url, files={"file": image_file})

print(response.json())
```

### Sample Response

```json
{
    "confidence": 0.9997437596321106,
    "predicted_species": "Singkong"
}
```
