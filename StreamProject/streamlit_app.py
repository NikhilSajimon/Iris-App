import streamlit as st
import pickle

model = pickle.load(open('model/model_rf.pkl', 'rb'))
species_mapping = {
    0: "Setosa",
    1: "Versicolor",
    2: "Virginica"
}

species_images = {
    "Setosa": "images/setosa.jpg",
    "Versicolor": "images/versicolor.jpg",
    "Virginica": "images/virginica.jpg"
}


st.title('Iris Flower Species Prediction')

st.badge('Enter Data', color='green')

with st.form('iris_app_form'):
    pl = st.number_input('Enter petal length')
    pw = st.number_input('Enter petal width')
    sl = st.number_input('Enter sepal length')
    sw = st.number_input('Enter sepal width')
    submitted = st.form_submit_button('Predict Species')

if submitted:
    prediction = model.predict([[pl,pw,sl,sw]])
    predicted_species = species_mapping.get(prediction[0], "Unknown")
    st.success('Predicted Species: {}'.format(predicted_species))

    image_path = species_images.get(predicted_species)
    if image_path:
        st.image(image_path, caption=predicted_species, use_container_width=True)
    else:
        st.warning("No image available for this species.")


