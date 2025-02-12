# Django Chat Application

This is a real-time chat application built with **Django** and **WebSocket** using **Django Channels**. It allows users to sign up, log in, and chat with other registered users in real-time.

---

## Features
- **User Authentication**: Sign up, log in, and log out functionality.
- **Real-Time Messaging**: Messages are sent and received in real-time using WebSocket.
- **Chat History**: Old messages are retrieved and displayed in the chat interface.
- **User-Friendly Interface**: Clean and intuitive design for a seamless user experience.

---

## Prerequisites
Before running the project, ensure you have the following installed:
- Python 3.8+
- Django 4.0+
- Channels 3.0+

---

## Installation

### 1. Clone the Repository
Clone the repository to your local machine:
```bash
git clone https://github.com/your-username/your-repo-name.git
cd your-repo-name
2. Set Up a Virtual Environment
Create and activate a virtual environment:

bash
Copy
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
3. Install Dependencies
Install the required Python packages:

bash
Copy
pip install -r requirements.txt
4. Set Up the Database
Apply migrations to set up the database:

bash
Copy
python manage.py migrate
5. Create a Superuser
Create a superuser to access the Django admin interface:

bash
Copy
python manage.py createsuperuser
6. Run the Development Server
Start the Django development server:

bash
Copy
python manage.py runserver
7. Access the Application
Open your browser and go to http://127.0.0.1:8000/.

Usage
1. Sign Up
Go to the signup page: http://127.0.0.1:8000/signup/.

Fill out the form to create a new account.

2. Log In
Go to the login page: http://127.0.0.1:8000/accounts/login/.

Enter your credentials to log in.

3. Start Chatting
On the chat home page, select a user from the sidebar to start chatting.

Send and receive messages in real-time.
