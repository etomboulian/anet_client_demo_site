import sys; sys.path.append('C:\\dev\\anet_website\\anet_client')
from flask import Flask, render_template
from anet_client import SystemApiClient
from dotenv import load_dotenv
import os

load_dotenv()


app = Flask(__name__)
client = SystemApiClient(
	os.environ.get("ORG_NAME"), 
	os.environ.get("COUNTRY"), 
	os.environ.get("API_KEY"), 
	os.environ.get("API_SECRET")
)


# Home Route
@app.route('/', methods=['GET'])
def home() -> str:
    org_data = client.get_organization().body[0]
    return render_template('index.html', org_data=org_data)

# Activities Route
@app.route('/activities', methods=['GET'])
def activities() -> str:
    activity_data = client.get_activities().body
    return render_template('activities.html', activity_data=activity_data)

# Activity Details Route
@app.route('/activities/<activity_id>', methods=['GET'])
def activity_details(activity_id: int) -> str:
    activity_detail_data = client.get_activity_detail(activity_id=activity_id).body[0]
    return render_template('activity_details.html', data=activity_detail_data)

if __name__ == "__main__":
    app.run(debug=True)
    