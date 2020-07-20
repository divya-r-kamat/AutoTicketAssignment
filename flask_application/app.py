from flask import Flask,render_template,request
from sklearn.externals import joblib
import helper

# load model
model = joblib.load(open('l1_l2_classification.pkl','rb'))
model_l1_l2 = joblib.load(open('model_l1_l2.pkl','rb'))
model_l3 = joblib.load(open('model_l3.pkl','rb'))

enc = {
       'L1/L2' : 0,
       'L3' : 1 
       }

# list out keys and values separately 
key = list(enc.keys()) 
val = list(enc.values()) 

encoding_l3 = {
        'GRP_10': 0,
        'GRP_12': 1,
        'GRP_13': 2,
        'GRP_14': 3,
        'GRP_16': 4,
        'GRP_17': 5,
        'GRP_18': 6,
        'GRP_19': 7,
        'GRP_2':  8,
        'GRP_24': 9,
        'GRP_25': 10,
        'GRP_26': 11,
        'GRP_29': 12,
        'GRP_3' : 13,
        'GRP_31': 14,
        'GRP_33': 15,
        'GRP_34': 16,
        'GRP_4':  17,
        'GRP_5':  18,
        'GRP_6':  19,
        'GRP_7':  20,
        'GRP_9':  21
        }

# list out keys and values separately 
key_list = list(encoding_l3.keys()) 
val_list = list(encoding_l3.values()) 

encoding_l2 =  {'GRP_0': 0, 'GRP_8': 1}
key_list2 = list(encoding_l2.keys()) 
val_list2 = list(encoding_l2.values()) 

# app
app = Flask(__name__)
@app.route('/')
def home():
	return render_template('home.html')

# routes
@app.route('/predict', methods=['POST'])

def predict():
    # get data

    if request.method == 'POST':	
        message = request.form['message']
        

        ## Clean and preprocess
        message = helper.fn_translate(message)
        message = helper.clean_text(message)
        message = helper.pre_process(message)
        
        data = [message]
        
        
        # predictions
        result = model.predict(data)
        
        # send back to browser
        output = key[val.index(result)]
        
        if output == 'L1/L2':
            group = model_l1_l2.predict(data)

        # send back to browser
            output_final = key_list2[val_list2.index(group)]
        else :
            group = model_l3.predict(data)

        # send back to browser
            output_final = key_list[val_list.index(group)]

    # return data
    return render_template('result.html',prediction = output_final, team= output)

if __name__ == '__main__':
    app.run(port = 5000, debug=True)