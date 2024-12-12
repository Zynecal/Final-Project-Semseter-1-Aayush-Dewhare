import requests
from tkinter import *

def newWindow():
    # create root window
    root = Tk()

    # root window title and dimension
    root.title('TaskFlow - Interactive Homework Tracker')

    # set geometry 
    root.geometry('1920x1080')

    # execute tkinter
    root.mainloop()

# establish url and api token
canvas_url = "https://dublinusd.instructure.com/"
api_token = "8844~UZE83EW8BN2W6CQzNKnL2Nw3kFtvPFWMnrDXcLZPNA8hGDTyGmKvc6mwvX9RPXCt"
course_id = "19099"

# create an API endpoint
url  = f'{canvas_url}/api/v1/courses/{course_id}/assignments'

#print(url)

# header with api token for auth
headers = {
    "Authorization": f"Bearer {api_token}"
}

#print(headers)

# get request 
response = requests.get(url, headers=headers)

#print(response)

if response.status_code == 200:
    assignments = response.json()
    print('Assignments:')

    for assignment in assignments:
        print(f'Assignment Name: {assignment['name']}')
        print(f"Due Date: {assignment['due_at']}")

