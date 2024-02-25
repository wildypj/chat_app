Overview

This project is an Open Chat Web App that allows users to chat in real-time. It is built using Python for the backend, JavaScript, HTML, and CSS for the frontend, and Flask to connect the frontend and backend. The app utilizes Flask-SocketIO for real-time communication between clients and the server.

Files

app.py: This Python script contains the backend logic using Flask and Flask-SocketIO. It handles message sending, user connections, disconnections, and broadcasting messages to all connected clients.
templates folder:
index.html: The main HTML template for the chat interface. It includes input fields for username and messages, a list of connected users, and a container for displaying messages. JavaScript code for client-side interaction is included in this file.
static folder:
styles.css: CSS styles for styling the HTML templates.
Setup Instructions

Install Python if not already installed.
Install Flask and Flask-SocketIO by running:
Copy code
pip install Flask Flask-SocketIO
Run the app.py file using Python:
Copy code
python app.py
Access the application through a web browser at http://localhost:5000.
Usage

Enter a username in the username input field.
Type your message in the message input field.
Press the "Send" button or hit Enter/Return to send the message.
Users can also click on another user's name in the user list to automatically insert their username in the message input field, allowing for easy targeting of messages to specific users.
Messages are displayed in real-time in the message container, and the user list updates dynamically as users join or leave the chat.
JavaScript Code

The JavaScript code for client-side interaction is included in the <script> section of the index.html file. It handles sending messages, displaying messages, and updating the user list in real-time.

Note

Users can send messages to specific users by mentioning their username preceded by "@". For example, "@John Hello!" will send a message "Hello!" to the user named "John".
The app is designed for open communication, so there are no private or direct messaging features.
Credits

Flask: Flask
Flask-SocketIO: Flask-SocketIO
License

This project is licensed under the MIT License.
