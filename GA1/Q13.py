import os, json, requests
import urllib

def execute(question: str, parameter):
    #return "https://raw.githubusercontent.com/23f2004837/GA1/refs/heads/main/email.json"
           #https://raw.githubusercontent.com/23f2004837/daily-commit/refs/heads/main/23f2004837%40ds.study.iitm.ac.in.json
    email = parameter["email"]
    return run_git_workflow(email)

def run_git_workflow(email):

    # GitHub repository details
    GITHUB_OWNER = "abhisheks407"  # Replace with your GitHub username/org
    GITHUB_REPO = "TDS"   # Replace with your repo name
    WORKFLOW_FILE = "main.yml"  # Name of your workflow file
    BRANCH = ".github/workflows"  # Branch to run the workflow on

    # Personal Access Token (PAT) with `repo` scope
    GITHUB_TOKEN = "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"  # Replace with your actual token

    # GitHub API endpoint
    url = f"https://api.github.com/repos/{GITHUB_OWNER}/{GITHUB_REPO}/actions/workflows/{WORKFLOW_FILE}/dispatches"

    # API request headers
    headers = {
        "Accept": "application/vnd.github+json",
        "Authorization": f"Bearer {GITHUB_TOKEN}",
    }

    # Request body
    # Request body with input parameter
    payload = {
        "ref": BRANCH,  
        "inputs": {
            "email": email
        }
    }
    # Trigger the workflow
    response = requests.post(url, json=payload, headers=headers)

    # Print response status
    if response.status_code == 204:
        print("✅ Workflow triggered successfully!")
    else:
        print(f"❌ Failed to trigger workflow: {response.status_code}")
        print(response.text)
    
    return f"https://raw.githubusercontent.com/abhisheks407/daily-commit/refs/heads/main/{urllib.parse.quote(email)}.json"
