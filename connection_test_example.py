import firebase_admin
from firebase_admin import credentials, firestore

# Initialize Firebase
cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred)

# Connect to Firestore
db = firestore.client()

# Test insert
doc_ref = db.collection("test").document()
doc_ref.set({
    "message": "Connection successful"
})

print("Data written successfully!")
