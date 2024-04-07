from flask import Flask, render_template, request
import os
import pickle
import numpy as np
from numpy.linalg import norm
from PIL import Image
from tensorflow.keras.preprocessing import image
from tensorflow.keras.layers import GlobalMaxPooling2D
from tensorflow.keras.applications.resnet50 import ResNet50, preprocess_input
from sklearn.neighbors import NearestNeighbors
import tensorflow  # Add this line to import tensorflow
from flask import jsonify

app = Flask(__name__)

@app.after_request
def after_request(response):
    response.headers.add('Access-Control-Allow-Origin', 'http://localhost:5500')
    response.headers.add('Access-Control-Allow-Headers', 'Content-Type')
    response.headers.add('Access-Control-Allow-Methods', 'POST')
    response.headers.add('Access-Control-Allow-Credentials', 'true')
    return response

# Handle preflight requests
@app.route('/', methods=['OPTIONS'])
def options():
    response = jsonify({'message': 'CORS preflight request successful'})
    response.headers.add('Access-Control-Allow-Headers', 'Content-Type')
    response.headers.add('Access-Control-Allow-Methods', 'POST')
    return response


model = ResNet50(weights='imagenet', include_top=False, input_shape=(224, 224, 3))
model.trainable = False
model = tensorflow.keras.Sequential([
    model,
    GlobalMaxPooling2D()
])

feature_list = pickle.load(open('embeddings.pkl', 'rb'))
filenames = pickle.load(open('filenames.pkl', 'rb'))


def save_uploaded_file(uploaded_file):
    try:
        with open(os.path.join('uploads', uploaded_file.filename), 'wb') as f:
            f.write(uploaded_file.read())
            return uploaded_file.filename
    except:
        return None


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
        uploaded_file = request.files['file']
        if uploaded_file.filename == '':
            return jsonify({"error": "No selected file"})
        if uploaded_file:
            filename = save_uploaded_file(uploaded_file)
            if filename:
                # Feature extraction
                features = feature_extraction(os.path.join("uploads", filename), model)
                # Recommendation
                indices = recommend(features, feature_list)
                # Return the result as a JSON response
                return jsonify({"file_path": filename, "filenames": [filenames[i] for i in indices[0]]})
            else:
                return jsonify({"error": "Failed to save file"})
        else:
            return jsonify({"error": "Some error occurred"})



if __name__ == "__main__":
    app.run(debug=True)
