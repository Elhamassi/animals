from flask import Flask, render_template, request
from werkzeug.utils import secure_filename
import keras
from keras.preprocessing import image
import numpy as np

from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/')
def indexget():
    return render_template('index.html')


@app.route('/',methods=['GET','POST'])
def upload():

   if request.method == 'POST':
      f = request.files['file']
      f.save("./pic/"+secure_filename(f.filename))
      ## load tensorflow model
      model = keras.models.load_model('./model/model.h5')
      
      img = image.load_img("./pic/"+secure_filename(f.filename), target_size = (64, 64))
      img = image.img_to_array(img)
      img = np.expand_dims(img, axis = 0)

      my_prediction = model.predict(img)
      if my_prediction[0] ==1:
        return render_template('index.html', text="Dog",pic=f.filename)
      return render_template('index.html', text="Cat",pic=f.filename)
    

      

    #md = open('./model/model.h5','rb') 
    #modelprd = pickle.load(md)
	
    #if request.method == 'POST':
        #print(request.form['img'])
        #my_prediction = modelprd.predict(data) 

    #return str(my_prediction[0])
    

#Calling the main function and running the flask app 
if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0")