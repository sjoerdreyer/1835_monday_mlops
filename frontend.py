import streamlit as st
import requests

st.title('My Iris flower classifier app')
st.write('Select features below:')

sep_len = st.slider('Select a value for Sepal length', min_value=0, max_value=10, value=1, step=1)
sep_wid = st.slider('Select a value for Sepal width', min_value=0, max_value=10, value=1, step=1)
pet_len = st.slider('Select a value for Petal length', min_value=0, max_value=10, value=1, step=1)
pet_wid = st.slider('Select a value for Petal width', min_value=0, max_value=10, value=1, step=1)

url = 'https://api1835monday-1066132381514.europe-west1.run.app/predict'

params = {'sepal_length': sep_len,
          'sepal_width': sep_wid,
          'petal_length': pet_len,
          'petal_width': pet_wid}

response = requests.get(url=url,
                        params=params).json()

def from_num_flower(x):
    if x == 0:
        return 'setosa'
    elif x == 1:
        return 'versicolor'
    else:
        return 'virginica'

prettier_pred = from_num_flower(response['flower'])

st.write('The flower belongs to class', str(prettier_pred))

#note when pushing forntend file:
# 1 cd package_folder
# 2 git init
# 3 gh repo create -> follow instructions
# 4 git add commit and push

# if push not working:
# git remote add origin SSH_url (find it in github)
# check with: git remote -v
