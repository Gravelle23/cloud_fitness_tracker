import firebase_admin
from firebase_admin import credentials, firestore


def get_db(service_account_path="serviceAccountKey.json"):
    """
    Connect to Firestore and return a database client.
    Only initializes Firebase once.
    """
    if not firebase_admin._apps:
        cred = credentials.Certificate(service_account_path)
        firebase_admin.initialize_app(cred)

    return firestore.client()
