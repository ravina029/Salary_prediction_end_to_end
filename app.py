import numpy as np 
from flask import Flask, request, jsonify, render_template
#from sklearn.preprocessing import LabelEncoder
import pickle 


app=Flask(__name__)
model=pickle.load(open("model.pkl","rb"))
#label_encoder = pickle.load(open('label_encoder.pkl', 'rb'))

@app.route("/")
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    if request.method == 'POST':
        age = float(request.form['Age'])
        gender = float(request.form['Gender'])
        education_level = float(request.form['Education_Level'])
        job_title = float(request.form['Job_Title'])
        experience = float(request.form['Years_of_Experience'])

        print(request.form['Age'])
        print(request.form['Gender'])
        print(request.form['Education_Level'])
        print(request.form['Job_Title'])
        print(request.form['Years_of_Experience'])

        #Encode categorical features using label encoding
        #gender_encoded = label_encoder.transform([gender])
        #education_level_encoded = label_encoder.transform([education_level])
        #job_title_encoded = label_encoder.transform([job_title])
        # Create a feature vector for prediction
       # features = [age, gender_encoded[0], education_level_encoded[0], job_title_encoded[0], experience]
        features = [age, gender, education_level, job_title, experience]

        #int_features=[int(x) for x in request.form.values()]
        final_features=[np.array(features)]

        # Make predictions with your model
        try:
            prediction = model.predict(final_features)
            output=round(prediction[0],2)
        except Exception as e:
            print(f"Error: {str(e)}")
    
        


        # Display the predicted salary on the result page
        return render_template('predict.html', prediction_text="Employee salary should be $ {:.2f}".format(output))

if __name__ == '__main__':
    app.run(debug=True)
