from flask import Flask, render_template, request
import requests

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html',id_list=[5, 12, 40, 65, 100, 30, 78, 88, 35])
#
@app.route('/recommendations', methods=['POST'])
def get_recommendations():
    user_id = request.form['userId']
    print(user_id)
    response = requests.get(f'http://localhost:7071/api/WebAppHttpTrigger?userId={user_id}')
    recommendations = response.json()
    return render_template('results.html', user_id=user_id, recommendations=recommendations)

if __name__ == '__main__':
    app.run()
