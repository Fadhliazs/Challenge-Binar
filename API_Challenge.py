import pandas as pd
import re
from Cleansingan import lowering, textbersih, slangan, bersihan,pisah
data = pd.read_csv("D:\Binar\Data challenge\Data\data.csv", encoding = 'latin-1')
datat = data['Tweet'].tolist
df = lowering(datat)
df_bersih = textbersih(datas)
datas = pisah(df)
df_bersihslang = slangan(df_bersih)
real_df = bersihan(df_bersihslang)

from Flask import Flask, jsonify
app = Flask(__name__)

from flasgger import Swagger, Lazystring, LazyJSONEncoder, swag_from
app.json_encoder = LazyJSONEncoder
swagger_template = dict(
    info = {
        'title': LazyString(lambda: 'API Documentation for Data Processing and Modeling'),
        'version': LazyString(lambda: '1.0.0'),
        'description': LazyString(lambda: 'Dokumentasi API untuk Data Processing dan Modeling')
    },
    host = LazyString(lambda: request.host)
)

swagger_config = {
    "headers": [],
    "specs": [
        {
            "endpoint": 'docs',
            "route": '/docs.json'
        }
    ],
    "static_url_path": "/flasgger_static",
    "swagger_ui": True,
    "specs_route": "/docs/"
}
swagger = Swagger(app, template=swagger_template,config=swagger_config)

@swag_from("docs/text.yml", methods=['GET'])
@app.route('/text', methods=['GET'])
def text():
    json_response = {
        'status_code': 200,
        'description': "tesk bersih nih",
        'data': re.sub('[^a-zA-Z0-9]',' ', text)
    }

    response_data = jsonify(json_response)
    return response_data

@swag_from("docs/text_processing.yml", methods=['POST'])
@app.route('/text-processing', methods=['POST'])
def text():
    json_response = {
        'status_code': 200,
        'description': "tesk bersih nih",
        'data': re.sub('[^a-zA-Z0-9]',' ', text)
    }

    response_data = jsonify(json_response)
    return response_data

if __name__ == '__main__':
    app.run()