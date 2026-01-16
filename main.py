import functions_framework
from google.cloud import firestore

# Connect to the DB
db = firestore.Client()

@functions_framework.http
def receive_data(request):
    # 1. Get the JSON sent by your script
    request_json = request.get_json(silent=True)

    # 2. Extract info (default to UNKNOWN if missing)
    plate = request_json.get('plate', 'UNKNOWN')
    status = request_json.get('status', 'Unknown')

    # 3. Save to Firestore
    db.collection('parking_logs').add({
        'plate': plate,
        'status': status,
        'timestamp': firestore.SERVER_TIMESTAMP
    })

    return 'Success: Data Saved', 200
