import requests
import tkinter as tk

# establish url and api token
canvas_url = "https://dublinusd.instructure.com/"
api_token = "8844~UZE83EW8BN2W6CQzNKnL2Nw3kFtvPFWMnrDXcLZPNA8hGDTyGmKvc6mwvX9RPXCt"
course_id = "19099"
assignment_names = []

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

def newWindow():
    # create window
    window = tk.Tk()

    # window title and dimension
    window.title('TaskFlow - Interactive Homework Tracker')

    # set geometry 
    window.geometry('900x750')
    
    for assignment in assignments:
        print(f"Assignment Name: {assignment['name']}")
        print(f"Due Date: {assignment['due_at']}")

        assignmentName = (f"Assignment Name: {assignment['name']}")
        assignmentDueDate = (f"Due Date: {assignment['due_at']}")
        assignment_names.append(assignmentName)

        #tk.Label(window, text=(assignmentName), font=("Arial", 16)).pack()

    # execute tkinter
    window.mainloop()

newWindow()

