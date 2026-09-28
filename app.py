from flask import Flask, jsonify

app = Flask(__name__)

events = [
    {
        "id": 1,
        "name": "Tech Fest",
        "date": "10 October 2026",
        "venue": "College Auditorium"
    },
    {
        "id": 2,
        "name": "Sports Day",
        "date": "20 October 2026",
        "venue": "College Ground"
    }
]


@app.route("/")
def home():
    return """
    <h1>College Event Manager</h1>
    <p>Welcome to the College Event Manager!</p>
    <p>Upcoming Events:</p>
    <ul>
        <li>Tech Fest - 10 October 2026</li>
        <li>Sports Day - 20 October 2026</li>
    </ul>
    <a href="/events">View All Events</a>
    """


@app.route("/events")
def get_events():
    return jsonify(events)


@app.route("/events/<int:event_id>")
def event_details(event_id):
    for event in events:
        if event["id"] == event_id:
            return jsonify(event)

    return jsonify({"error": "Event not found"}), 404


@app.route("/health")
def health():
    return jsonify({"status": "healthy"})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)