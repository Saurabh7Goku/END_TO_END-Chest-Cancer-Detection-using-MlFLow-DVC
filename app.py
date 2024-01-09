# from flask import Flask, request, jsonify, render_template
# import os
# from flask_cors import CORS, cross_origin
# from src.utils.common import decodeImage
# from src.pipeline.prediction import PredictionPipeline


# os.putenv('LANG', 'en_US.UTF-8')
# os.putenv('LC_ALL', 'en_US.UTF-8')

# app = Flask(__name__)
# CORS(app)


# class ClientApp:
#     def __init__(self):
#         self.filename = "inputImage.jpg"
#         self.classifier = PredictionPipeline(self.filename)


# @app.route("/", methods=['GET'])
# @cross_origin()
# def home():
#     return render_template('index.html')


# @app.route("/train", methods=['GET','POST'])
# @cross_origin()
# def trainRoute():
#     os.system("python main.py")
#     # os.system("dvc repro")
#     return "Training done successfully!"


# @app.route("/predict", methods=['POST'])
# @cross_origin()
# def predictRoute():
#     clApp = ClientApp()
#     image = request.json['image']
#     decodeImage(image, clApp.filename)
#     result = clApp.classifier.predict()
#     return jsonify(result)



# if __name__ == "__main__":
#     clApp = ClientApp()
#     app.run(host='0.0.0.0', port=8080, debug=True) #for AWS



from flask import jsonify
import streamlit as st
from PIL import Image
import base64
from io import BytesIO
from src.utils.common import decodeImage
from src.pipeline.prediction import PredictionPipeline

class ClientApp:
    def __init__(self):
        self.filename = "inputImage.jpg"
        self.classifier = PredictionPipeline(self.filename)

def main():
    st.set_page_config(page_title="Chest Cancer Classification", page_icon="🩺")

    # CSS styles
    st.markdown("""
        <style>
            .streamlit-container {
                background-color: #eff2f9;
            }
            .st-file-uploader {
                color: #1b2d6b;
                font-size: 20px;
                font-weight: bold;
            }
            .btn-primary {
                background-color: #007bff;
                color: #fff;
                border: none;
                border-radius: 0px;
                padding: 10px 20px;
                margin-top: 10px;
                cursor: pointer;
            }
            .prediction-box {
                display: flex;
                align-items: center;
                justify-content: center;
                height: 50px;
                width: 100%;
                margin-top: 10px;
                font-size: 18px;
                font-weight: bold;
            }
            .normal-result {
                background-color: #28a745; /* Green background for Normal */
                color: #fff;
            }
            .adenocarcinoma-result {
                background-color: #dc3545; /* Red background for Adenocarcinoma */
                color: #fff;
            }
            .sample-image-row {
                display: flex;
                flex-direction: column;
                align-items: center;
                margin-top: 20px;
            }
            .sample-image {
                max-width: 100%;
                max-height: 100%;
                margin: 10px;
            }
        </style>
    """, unsafe_allow_html=True)

    st.title("Chest Cancer Classification")

    clApp = ClientApp()

    uploaded_file = st.file_uploader("Upload Image", type=["jpg", "jpeg", "png"], key="upload_image")
    if uploaded_file is not None:
        image = Image.open(uploaded_file)
        st.image(image, caption="Uploaded Image.", width=200)
        image_base64 = image_to_base64(image)
        decodeImage(image_base64, clApp.filename)

        if st.button("Predict", key="predict_button"):
            result = clApp.classifier.predict()
            show_prediction_result(result)

    # Image Sample Section in the Sidebar
    st.sidebar.header(":blue[Sample Images] :sunglasses:", divider=True)

    normal_images = [
        "static/assets/normal_image_1.png",
        "static/assets/normal_image_2.png",
        "static/assets/normal_image_3.png",
        "static/assets/normal_image_4.png",
        "static/assets/normal_image_5.png",
    ]

    adenocarcinoma_images = [
        "static/assets/cancer_image_1.png",
        "static/assets/cancer_image_2.png",
        "static/assets/cancer_image_3.png",
        "static/assets/cancer_image_4.png",
        "static/assets/cancer_image_5.png",
    ]

    # Selectbox for Normal Images
    selected_normal_image = st.sidebar.selectbox("Select Normal Image", normal_images)
    if selected_normal_image:
        st.sidebar.image(Image.open(selected_normal_image), caption="Selected Normal Image", use_column_width=True)

    # Allow the user to run prediction on the selected normal image
    if st.sidebar.button("Predict Normal Image", key="predict_normal_button"):
        decodeImage(image_to_base64(Image.open(selected_normal_image)), clApp.filename)
        result = clApp.classifier.predict()
        show_prediction_result(result)

    st.sidebar.divider()   
    st.divider()
    # Selectbox for Adenocarcinoma Images
    selected_cancer_image = st.sidebar.selectbox("Select Adenocarcinoma Image", adenocarcinoma_images)
    if selected_cancer_image:
        st.sidebar.image(Image.open(selected_cancer_image), caption="Selected Adenocarcinoma Image", use_column_width=True)

    # Allow the user to run prediction on the selected adenocarcinoma image
    if st.sidebar.button("Predict Adenocarcinoma Image", key="predict_cancer_button"):
        decodeImage(image_to_base64(Image.open(selected_cancer_image)), clApp.filename)
        result = clApp.classifier.predict()
        show_prediction_result(result)

def image_to_base64(image):
    buffered = BytesIO()
    image.save(buffered, format="PNG")
    return base64.b64encode(buffered.getvalue()).decode("utf-8")

def display_sample_images(images):
    st.markdown('<div class="sample-image-row">', unsafe_allow_html=True)
    for image_path in images:
        st.image(image_path, caption="Sample Image", width=100, output_format='PNG', clamp=True)
    st.markdown('</div>', unsafe_allow_html=True)

def show_prediction_result(result):
    prediction_box = st.empty()

    if result and isinstance(result, list) and len(result) > 0:
        prediction_text = result[0].get('image', '')
        if prediction_text == 'Normal':
            prediction_box.markdown('<div class="prediction-box normal-result">{}</div>'.format(prediction_text), unsafe_allow_html=True)
        elif prediction_text == 'Adenocarcinoma Cancer':
            prediction_box.markdown('<div class="prediction-box adenocarcinoma-result">{}</div>'.format(prediction_text), unsafe_allow_html=True)
        else:
            prediction_box.empty()  # Clear the prediction box if result is not Normal or Adenocarcinoma
    else:
        prediction_box.empty()  # Clear the prediction box if the result is not in the expected format

if __name__ == "__main__":
    main()
