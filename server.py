from flask import Flask
import sqlite3
import Levenshtein

# start Flask app
app = Flask(__name__)
startingDistance = 1000
approvedDistance = 10

# fetch known phrases from database
conn = sqlite3.connect('primes')
c= conn.cursor()
c.execute('SELECT * FROM known_phrases')
knownPhrases = c.fetchall()

# index page
@app.route('/')
def index():
    return 'Silence is gold!'

def get_closest(phrase, id):
    minDistance = startingDistance
    matchPhrase = False

    # search for relative phrase based on Levenshtein distance
    for known in knownPhrases:
        distance = Levenshtein.distance(phrase, known[2])
        if (distance < minDistance):
            minDistance = distance
            matchPhrase = known

    print("Distance: "+str(minDistance))
    print("Closest: "+matchPhrase[2])

    if (minDistance < approvedDistance):
        return matchPhrase
    else:
        return False


# create add function
# import a new phrase in the database
@app.route('/add/<phrase>')
def add(phrase):
    # connect to database
    conn = sqlite3.connect('primes')
    c= conn.cursor()

    # find closest phrase
    closest = get_closest(phrase, c.lastrowid)

    # insert to db if found
    if (closest != False):
        pending = 1
        videoId = closest[3]
    else:
        pending = 0
        videoId = 0

    value = "('" + str(phrase) + "', " + str(pending) + ", " + str(videoId) + ")"
    c.execute("INSERT INTO incoming_phrases (description, pending, videoId) VALUES " + value)
    conn.commit()

    return "OK"

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
