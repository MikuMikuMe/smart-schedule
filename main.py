Creating a "smart schedule" application involves building a system that can handle various tasks such as managing user data, analyzing preferences, and suggesting optimal meeting times. In the following example, I'll create a simplified version of such an application using Python. This program will assume simplistic data inputs and will focus on demonstrating the basic functionality. In a real-world application, this system would likely be integrated with APIs for schedule management like Google Calendar API.

```python
import datetime
import random

class SmartScheduler:
    def __init__(self):
        # Initialization
        self.users = {}  # Dictionary to store users and their data
        self.meetings = []  # List to store meetings

    def add_user(self, user_id, preferences, availability):
        """Add a user with their preferences and availability."""
        if user_id in self.users:
            print(f"User with ID {user_id} already exists.")
            return

        self.users[user_id] = {
            "preferences": preferences,
            "availability": availability
        }
        print(f"User {user_id} added.")

    def add_meeting(self, meeting_id, participants):
        """Add a meeting with participants."""
        if meeting_id in self.meetings:
            print(f"Meeting {meeting_id} already exists.")
            return

        meeting_data = {
            "meeting_id": meeting_id,
            "participants": participants,
            "scheduled_time": None
        }
        self.meetings.append(meeting_data)
        print(f"Meeting {meeting_id} added.")

    def suggest_meeting_times(self, meeting_id):
        """Suggest best times for a given meeting based on participants' preferences and availability."""
        meeting = next((mtg for mtg in self.meetings if mtg["meeting_id"] == meeting_id), None)
        if not meeting:
            print(f"No meeting found with ID {meeting_id}")
            return

        participants = meeting["participants"]
        availability_sets = []
        
        # Gather availability information for all participants
        for user_id in participants:
            if user_id in self.users:
                availability_sets.append(set(self.users[user_id]["availability"]))
            else:
                print(f"User {user_id} not found in the system.")
                return

        # Determine common available times
        if availability_sets:
            common_times = set.intersection(*availability_sets)
            if common_times:
                preferences_scores = {time: 0 for time in common_times}

                # Weight based on user preferences
                for user_id in participants:
                    if user_id in self.users:
                        user_prefs = self.users[user_id]["preferences"]
                        for time, score in user_prefs.items():
                            if time in preferences_scores:
                                preferences_scores[time] += score
                
                # Suggest time with highest score
                suggested_time = max(preferences_scores, key=preferences_scores.get)
                print(f"Suggested time for meeting {meeting_id} is {suggested_time}")
            else:
                print(f"No common availability for meeting {meeting_id}.")
        else:
            print(f"No participants have availability set for meeting {meeting_id}.")

def main():
    scheduler = SmartScheduler()

    # Example users
    scheduler.add_user("user1", {"09:00": 2, "10:00": 3}, ["09:00", "10:00", "11:00"])
    scheduler.add_user("user2", {"09:00": 5, "11:00": 1}, ["09:00", "11:00", "12:00"])
    scheduler.add_user("user3", {"10:00": 4, "09:00": 2}, ["09:00", "10:00", "11:00"])

    # Example meeting
    scheduler.add_meeting("meeting1", ["user1", "user2", "user3"])

    # Suggest meeting time
    scheduler.suggest_meeting_times("meeting1")

if __name__ == "__main__":
    main()
```

### Explanation:

1. **SmartScheduler Class:**
   - Handles user and meeting data.
   - Users are stored with preferences and availability.
   - Meetings store participant IDs and scheduled time (initially `None`).

2. **Error Handling:**
   - Checks for existing users and meetings when adding new ones.
   - Checks if user exists before retrieving preference and availability data.

3. **Method:**
   - `add_user`: Adds a user to the system.
   - `add_meeting`: Adds a meeting with the specified participants.
   - `suggest_meeting_times`: Determines the best time for a meeting based on the overlapping availability and users' preferences.

This code serves as a starting point, and a more advanced system would require better handling of real-time data, integration with calendar APIs, and more sophisticated preference analysis.