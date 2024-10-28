Real-Time Voting System
This project simulates a distributed voting system, where multiple users (from different locations or browsers) interact concurrently with a centralized system. The votes are distributed across different clients but collected and processed centrally, which is a key aspect of distributed systems. This model can be scaled for real-world polling systems, collaborative decision-making platforms, and multiplayer game voting mechanisms.

Introduction
This is a simple real-time voting system built using Flask and ZeroMQ. It allows multiple users to participate in a series of polls and displays the results once all users have submitted their votes. The purpose of this project is to demonstrate how to implement a distributed voting system, where each participant's vote is recorded, and the results are shown only after everyone has voted.

System Requirements
Python 3.6 or higher
Flask (installed via pip install flask)
ZeroMQ (installed via pip install pyzmq)
Any modern web browser (Chrome, Firefox, Edge, etc.)
A stable internet connection (for real-world use)
How It Works
Each user visits the voting page where they are presented with several poll questions.
The system assigns a unique session ID to each user and tracks their progress through the polls.
After answering each poll question, the user submits their vote.
Once all participants have completed the polls, the system calculates the vote counts for each question.
The final results are displayed, showing whether a particular option won or if there was a tie.
ZeroMQ is used to broadcast vote updates in real-time to all connected clients.
Features
Multi-user support: Multiple users can participate in the polls simultaneously.
Real-time vote tracking with ZeroMQ: Each vote is tracked for the current session and broadcast to other users in real time.
Results shown after all users have voted: The results are displayed only when all required players have submitted their votes.
Tie handling: The system detects ties and displays them appropriately.
Session-based voting: Each user's votes are stored in their session, preventing duplicate votes from the same user.
How to Run the Program
Step 1: Clone the Repository
Download or clone the repository to your local machine using Git or the download button.

bash
Copy code
git clone <repository-url>
Step 2: Install the Dependencies
Navigate to the folder where the repository is located and install the necessary Python packages.

bash
Copy code
pip install flask pyzmq
Step 3: Start the ZeroMQ Server
The ZeroMQ server broadcasts real-time updates to clients. In a terminal, run the ZeroMQ server file:

bash
Copy code
python zeromq_server.py
Step 4: Run the Flask Application
In a separate terminal, start the Flask application:

bash
Copy code
python app.py
The app will start, and you can access it at http://127.0.0.1:5000/poll/1 on your local machine.

Accessing the Application on the Local Network
If you want other devices on your local network to access the application, follow these steps:

Find Your Local IP Address: Run ipconfig (Windows) or ifconfig (Mac/Linux) in the terminal and locate your IPv4 address (e.g., 192.168.x.x).
Update the app.run() Code: In app.py, change the app.run() line to allow network access:
python
Copy code
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
Access the App from Other Devices: Open a browser on another device on the same network and go to http://<Your_Local_IP>:5000/poll/1, replacing <Your_Local_IP> with the IP found in Step 1.
Step 5: Open Multiple Browsers or Incognito Windows
To simulate multiple users, open the voting link http://127.0.0.1:5000/poll/1 or the 192.x.x.x link in different browsers or private/incognito windows.

Changing the Number of Players (Default at 10 for testing purposes)
If you need to change the number of players required to complete the voting, follow these steps:

Open the app.py file in any text editor or IDE.
Look for the line that defines the number of required players:
python
Copy code
required_players = 10
Modify this value to the desired number of players. For example, to set it to 6 players, change the line to:
python
Copy code
required_players = 6
Save the file and restart the program:
bash
Copy code
python app.py
The system will now wait for the specified number of players to complete their votes before displaying the results.
Expected Output
The program will display a series of poll questions. After each user submits their votes for all questions, they will be shown a waiting screen until all users have voted. Once the required number of players has finished voting, the final results will display, showing either a winning option or a tie for each poll question.

Example Output:
Poll 1: The winner is 'Peanut Butter and Jelly' with 3 votes.
Poll 2: It's a tie between 'Harry Potter' (3 votes) and 'Darth Vader' (3 votes).
Poll 3: The winner is 'With a snooze button' with 4 votes.
Real-World Problem and Distributed Systems Application
This project simulates a real-world scenario where multiple users are participating in a vote or poll simultaneously. The concept of tracking individual users' votes and displaying results after everyone has voted applies to many real-world systems, such as:

Online elections or surveys.
Real-time feedback systems during meetings or events.
Distributed decision-making in organizations.
In a distributed system, multiple users may be located across different geographical locations, and their votes need to be aggregated in real-time. This project demonstrates how to manage concurrent inputs (votes) in a distributed fashion, ensuring all participants are accounted for before displaying the final results. The system leverages Flask to manage sessions, ensuring that each user's input is tracked individually, while ZeroMQ broadcasts real-time updates to clients, similar to how a distributed system handles tasks across multiple nodes.

Conclusion
This project illustrates a basic real-time voting system with Flask and ZeroMQ, highlighting the importance of session management, user tracking, and vote aggregation in distributed environments. It is a good foundation for understanding distributed system concepts like real-time synchronization and consensus.

