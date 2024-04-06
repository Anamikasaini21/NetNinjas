# from flask import Flask,render_template

# app = Flask(__name__)

# @app.route("/home")
# @app.route("/")
# def home():   
#     return render_template("index.html")


# @app.route("/upload.html")
# def upload():
#     return render_template("upload.html")

# @app.route("/Tryon2D.html")
# def Tryon2D():
#     return render_template("Tryon2D.html")


# if __name__ == "__main__":
#     app.run(debug=True)

import base64
from PIL import Image
from io import BytesIO
from flask import Flask, render_template, request
import os
import pickle
import numpy as np
from numpy.linalg import norm
import tensorflow
from tensorflow.keras.preprocessing import image
from tensorflow.keras.layers import GlobalMaxPooling2D
from tensorflow.keras.applications.resnet50 import ResNet50, preprocess_input
from sklearn.neighbors import NearestNeighbors

app = Flask(__name__)

# Load pre-trained ResNet50 model
model = ResNet50(weights='imagenet', include_top=False, input_shape=(224, 224, 3))
model.trainable = False
model = tensorflow.keras.Sequential([
    model,
    GlobalMaxPooling2D()
])

# Load pre-computed features and filenames
feature_list = pickle.load(open('embeddings.pkl', 'rb'))
filenames = pickle.load(open('filenames.pkl', 'rb'))


def feature_extraction(img_path, model):
    img = image.load_img(img_path, target_size=(224, 224))
    img_array = image.img_to_array(img)
    expanded_img_array = np.expand_dims(img_array, axis=0)
    result = model.predict(preprocess_input(expanded_img_array)).flatten()
    normalized_result = result / norm(result)
    return normalized_result


def recommend(features, feature_list):
    neighbors = NearestNeighbors(n_neighbors=6, algorithm='brute', metric='euclidean')
    neighbors.fit(feature_list)
    distances, indices = neighbors.kneighbors([features])
    return indices


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/upload.html")
def upload():
    return render_template("upload.html")


@app.route("/Tryon2D.html")
def Tryon2D():
    return render_template("Tryon2D.html")


@app.route("/upload", methods=['POST'])
def upload_file():
    if request.method == 'POST':
        # Get the blob data from the request
        blob_data = request.get_data()

        # Decode the blob data
        decoded_data = base64.b64decode(blob_data)

        # Create a BytesIO object
        image_bytes = BytesIO(decoded_data)

        # Create an Image object
        image = Image.open(image_bytes)

        # Save the image
        file_path = "uploads/images/output.jpg"  # Specify the file path where you want to save the image
        image.save(file_path)

        # You can continue with your feature extraction, recommendation, and rendering logic here

        return "Image uploaded successfully"
    # if request.method == 'POST':
    #     if 'file' not in request.files:
    #         return render_template("upload.html", error="No file part")
    #     file = request.files['file']
    #     if file.filename == '':
    #         return render_template("upload.html", error="No selected file")
    #     if file:
    #         # Save the uploaded file
    #         file_path = os.path.join("uploads/images/", file.filename)
    #         file.save(file_path)
    #         # Feature extraction
    #         features = feature_extraction(file_path, model)
    #         # Recommendation
    #         indices = recommend(features, feature_list)
    #         # Render the result
    #         return render_template("result.html", file_path=file_path, filenames=[filenames[i] for i in indices[0]])
    #     else:
    #         return render_template("upload.html", error="Some error occurred")

       
if __name__ == "__main__":
    app.run(debug=True)





