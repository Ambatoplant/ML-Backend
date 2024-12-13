from flask import Flask, request, jsonify
import tensorflow as tf
import numpy as np
import os
from werkzeug.utils import secure_filename
from flask_cors import CORS  # Import Flask-CORS


app = Flask(__name__)
CORS(app)
# Load TFLite model
MODEL_PATH = "model_AmbatoPlant_InceptionV3_V3.tflite"  # Update dengan lokasi model Anda
interpreter = tf.lite.Interpreter(model_path=MODEL_PATH)
interpreter.allocate_tensors()

# Load class names
class_names = ['Bunga Matahari',
 'Delima',
 'Gandum',
 'Jagung',
 'Jambu Batu',
 'Kakao',
 'Kamboja',
 'Kelor',
 'Lidah Buaya',
 'Melati',
 'Nanas',
 'Okra',
 'Singkong',
 'Sorgum',
 'Tomat']

# Input and output details
input_details = interpreter.get_input_details()
output_details = interpreter.get_output_details()

def predict_image_tflite(image_path, interpreter, class_names):
    # Load and preprocess the image
    img = tf.keras.preprocessing.image.load_img(
        image_path, target_size=(224, 224)
    )
    img_array = tf.keras.preprocessing.image.img_to_array(img)
    img_array = tf.keras.applications.inception_v3.preprocess_input(img_array)
    img_array = np.expand_dims(img_array, axis=0)

    # Set the input tensor
    interpreter.set_tensor(input_details[0]['index'], img_array)

    # Run the inference
    interpreter.invoke()

    # Get the output tensor
    predictions = interpreter.get_tensor(output_details[0]['index'])[0]
    predicted_class = class_names[np.argmax(predictions)]
    confidence = np.max(predictions)

    return predicted_class, confidence

@app.route('/predict', methods=['POST'])
def predict():
    # Check if the request has a file
    if 'file' not in request.files:
        return jsonify({"error": "No file part"}), 400

    file = request.files['file']
    if file.filename == '':
        return jsonify({"error": "No selected file"}), 400

    # Save the uploaded file temporarily
    filename = secure_filename(file.filename)
    filepath = os.path.join("uploads", filename)
    os.makedirs("uploads", exist_ok=True)
    file.save(filepath)

    # Perform prediction
    predicted_class, confidence = predict_image_tflite(filepath, interpreter, class_names)

    # Clean up the temporary file
    os.remove(filepath)

    # Ensure JSON serializable types
    return jsonify({
        "predicted_species":predicted_class,
        "confidence": float(confidence)  # Convert float32 to Python float
    })
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)