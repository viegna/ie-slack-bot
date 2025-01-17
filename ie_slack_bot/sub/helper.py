import requests
from requests.auth import HTTPBasicAuth
import os, dotenv
dotenv.load_dotenv()

def post_jira_issue(issue_title, issue_description, project_key, issue_type_id):
    url = os.getenv("JIRA_URL")
    auth = HTTPBasicAuth(os.getenv("JIRA_EMAIL"), os.getenv("JIRA_TOKEN"))

    headers = {
        "Accept": "application/json",
        "Content-Type": "application/json"
    }
    payload = {
        "fields": {
            "project": {
                "key": project_key
            },
            "summary": issue_title,
            "description": issue_description,
            "issuetype": {
                "id": issue_type_id
            }
        }
    }
    response = requests.post(url, json=payload, headers=headers,auth=auth)
    """response = requests.request("POST",url,data=payload,headers=headers,auth=auth)"""
    if response.status_code == 201:
        print("Issue created successfully!")
    else:
        print("Failed to create issue. Error:", response.text)

# Example usage
issue_title = "Sample Issue"
issue_description = "This is a sample issue created using variables."
project_key = "KAN"
issue_type_id = "10001"

post_jira_issue(issue_title, issue_description, project_key, issue_type_id)