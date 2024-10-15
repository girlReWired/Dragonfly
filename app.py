import os
from flask import Flask, render_template, request, session, redirect, url_for, jsonify

app = Flask(__name__)
app.secret_key = os.urandom(24)  # A random secret key is required for session management

# List of poll questions and options
polls = [
    {
        "question": "If you could only eat one food for the rest of your life, what would it be?",
        "options": ["Ramen", "Mushroom Soup", "Salad", "Peanut Butter and Jelly", "Deli Meat"]
    },
    {
        "question": "If you could be any fictional character for a day, who would you choose?",
        "options": ["Captain Underpants", "Katniss Everdeen", "Indiana Jones", "Harry Potter", "Darth Vader"]
    },
    {
        "question": "What's the best way to start a day?",
        "options": ["With a cup of coffee", "With a nice warm shower", "With a cold beer", "With a snooze button"]
    },
]

# Variables to store votes and user data
votes = [{} for _ in polls]  # A list of dictionaries to store votes for each poll question
user_votes = {}  # A dictionary to track each user's voting progress
required_players = 6  # Number of players required for the poll
finished_players = 0  # Count of players who have finished voting

# Main route for serving poll pages
@app.route('/poll/<int:poll_number>', methods=['GET', 'POST'])
def poll(poll_number):
    global finished_players, required_players

    # Create a session for the user if they don't already have one
    if 'user_id' not in session:
        session['user_id'] = os.urandom(16)  # Assign a unique ID to the user
        user_votes[session['user_id']] = []  # Initialize the user's vote list
        print(f"User {session['user_id']} has started voting.")

    if request.method == 'POST':
        option = request.form.get('option')
        if option:
            # Record the user's vote for the current poll if they haven't already voted
            if len(user_votes[session['user_id']]) < poll_number:
                user_votes[session['user_id']].append(option)
                # Store the vote under the user's session ID
                if poll_number - 1 in votes:
                    votes[poll_number - 1][session['user_id']] = option
                else:
                    votes[poll_number - 1] = {session['user_id']: option}  # Initialize if necessary

        # Redirect to the next poll question or final results
        if poll_number < len(polls):
            return redirect(url_for('poll', poll_number=poll_number + 1))
        else:
            # If the user finishes all polls, increment the finished players count
            if len(user_votes[session['user_id']]) == len(polls):
                finished_players += 1
                print(f"Finished players: {finished_players}/{required_players}")

            # Check if all required players have completed the poll
            if finished_players >= required_players:
                return redirect(url_for('final_results'))
            else:
                return render_template('waiting.html')  # Show waiting screen until all votes are in

    # Render the poll template with the current question and options
    poll_data = polls[poll_number - 1]
    return render_template('poll.html', poll=poll_data, poll_number=poll_number)

# Route for displaying the final results
@app.route('/final_results')
def final_results():
    # Debug: Print votes to the console for tracking
    print("Votes data:", votes)

    # Calculate and display the winners of each poll question
    winners = []
    for poll_index, poll_votes in enumerate(votes):
        vote_count = {}

        # Count the votes for each option
        for vote in poll_votes.values():
            vote_count[vote] = vote_count.get(vote, 0) + 1

        # Debug: Print vote counts for each poll
        print(f"Poll {poll_index + 1} vote counts:", vote_count)

        # Find the highest number of votes any option received
        max_votes = max(vote_count.values())

        # Identify all options with the highest votes (to handle ties)
        winners_for_poll = [option for option, count in vote_count.items() if count == max_votes]

        # Show the vote counts and check for ties
        if len(winners_for_poll) > 1:
            winners.append(f"Poll {poll_index + 1}: It's a tie between: {', '.join([f'{option} ({vote_count[option]} votes)' for option in winners_for_poll])}")
        else:
            winners.append(f"Poll {poll_index + 1}: The winner is: {winners_for_poll[0]} with {vote_count[winners_for_poll[0]]} votes.")

    # Render the final results template with the winner data
    return render_template('final_results.html', winners=winners)

# Route to check if all players have completed their votes
@app.route('/check_votes')
def check_votes():
    global finished_players, required_players
    if finished_players >= required_players:
        return jsonify(all_voted=True)  # Send JSON response to notify the client
    return jsonify(all_voted=False)  # Notify the client that voting is still ongoing


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)  # Run the app on port 5000
