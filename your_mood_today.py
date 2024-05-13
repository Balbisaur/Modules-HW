def mood_response(mood):
    if mood in moods:
        return moods[mood]
    else:
        return "I'm not sure how to respond to that mood. Maybe try 'happy', 'sad', or 'okay'?"

from moody import moods

mood = input("How are you feeling today? ")
print(mood_response(mood))

