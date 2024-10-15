
# Real-Time Voting System
This project simulates a distributed voting system, where multiple 
users (from different locations or browsers) interact concurrently 
with a centralized system. The votes are distributed across different 
clients but collected and processed centrally, which is a key aspect 
of distributed systems. This model can be scaled for real-world polling 
systems, collaborative decision-making platforms, and multiplayer game 
voting mechanisms.

## Introduction

This is a simple real-time voting system built using Flask. 
It allows multiple users to participate in a series of polls 
and displays the results once all users have submitted their votes. 
The purpose of this project is to demonstrate how to implement a 
distributed voting system, where each participant's vote is recorded, 
and the results are shown only after everyone has voted.

## System Requirements

- Python 3.6 or higher
- Flask (installed via `pip install flask`)
- Any modern web browser (Chrome, Firefox, Edge, etc.)
- A stable internet connection (for real-world use)
- Users must be on the same network in order to participate

## How It Works

1. Each user visits the voting page where they are presented with several poll questions.
2. The system assigns a unique session ID to each user and tracks their progress through the polls.
3. After answering each poll question, the user submits their vote.
4. Once all participants have completed the polls, the system calculates the vote counts for each question.
5. The final results are displayed, showing whether a particular option won or if there was a tie.

## Features

- **Multi-user support:** Multiple users can participate in the polls simultaneously.
- **Real-time vote tracking:** Each vote is tracked for the current session and stored in the server.
- **Results shown after all users have voted:** The results are displayed only when all required players have submitted their votes.
- **Tie handling:** The system detects ties and displays them appropriately.
- **Session-based voting:** Each user's votes are stored in their session, preventing duplicate votes from the same user.

## How to Run the Program

1. **Clone the repository:**
   Download or clone the repository to your local machine using Git or the download button.
   ```
   git clone <repository-url>
   ```

2. **Install the dependencies:**
   Navigate to the folder where the repository is located and install the necessary Python packages.
   ```
   pip install flask
   ```

3. **Run the application:**
   Run the Flask application using Python:
   ```
   python app.py
   ```
   The app will start and be accessible at `http://<Your_Local_IP_address/poll/1`.

4. **Open multiple browsers or incognito windows:**
   To simulate multiple users, open the voting link `http://<Your_Local_HTTP_FOR_Players_IP_Address>/poll/1` in different browsers or private/incognito windows.

## Changing the Number of Players (Default at 1 for testing purposes)

If you need to change the number of players required to complete the voting, follow these steps:

1. Open the `app.py` file in any text editor or IDE.
2. Look for the line that defines the number of required players:
   ```python
   required_players = 6
   ```
3. Modify this value to the desired number of players. For example, to set it to 10 players, change the line to:
   ```python
   required_players = 10
   ```
4. Save the file and restart the program:
   ```
   python app.py
   ```
5. The system will now wait for the specified number of players to complete their votes before displaying the results.

## Expected Output

The program will display a series of poll questions. After each user submits their votes for all questions, they will be shown a waiting screen until all users have voted. Once the required number of players has finished voting, the final results will display, showing either a winning option or a tie for each poll question.

### Example Output:
- Poll 1: The winner is 'Peanut Butter and Jelly' with 3 votes.
- Poll 2: It's a tie between 'Harry Potter' (3 votes) and 'Darth Vader' (3 votes).
- Poll 3: The winner is 'With a snooze button' with 4 votes.

## Real-World Problem and Distributed Systems Application

This project simulates a real-world scenario where multiple users are participating in a vote or poll simultaneously. The concept of tracking individual users' votes and displaying results after everyone has voted applies to many real-world systems, such as:
- Online elections or surveys.
- Real-time feedback systems during meetings or events.
- Distributed decision-making in organizations.

In a distributed system, multiple users may be located across different geographical locations, 
and their votes need to be aggregated in real time. This project demonstrates how to manage 
concurrent inputs (votes) in a distributed fashion, ensuring all participants are accounted for 
before displaying the final results. The system leverages Flask to manage sessions, ensuring that 
each user's input is tracked individually, much like a distributed system handles tasks across 
multiple nodes. By extending this project, you could integrate it with a database or cloud-based b
ackend to store results, making it suitable for a larger, real-world distributed system.

## Conclusion

This project illustrates a basic real-time voting system with Flask, highlighting the importance 
of session management, user tracking, and vote aggregation in distributed environments. It is a 
good foundation for understanding distributed system concepts like real-time synchronization and 
consensus.
