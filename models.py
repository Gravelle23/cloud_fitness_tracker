from datetime import datetime

#users
def create_user(db, name, email):
    #create a new user and return the user ID
    doc_ref = db.collection("users").document()
    doc_ref.set({
        "name": name,
        "email": email,
        "created_at": datetime.utcnow().isoformat()
    })
    return doc_ref.id

def get_all_users(db):
    #get all users from the database
    users = []
    for doc in db.collection("users").stream():
        data = doc.to_dict()
        data["id"] = doc.id
        users.append(data)
    return users

def get_user_by_id(db, user_id):
    #get a user by their ID
    doc = db.collection("users").document(user_id).get()
    if not doc.exists:
        return None
    data = doc.to_dict()
    data["id"] = doc.id
    return data

def delete_user(db, user_id):
    #delete a user by their ID
    db.collection("users").document(user_id).delete()


#Entries
def create_entry(db, user_id, entry_type, title, calories=None, duration=None):
    #crete a new entry for a user
    doc_ref = db.collection("entries").document()

    entry_data = {
        "userId" : user_id.strip(),
        "type" : entry_type.strip(),
        "title" : title.strip(),
        "created_at" : datetime.utcnow().isoformat()
    }

    if calories is not None:
        entry_data["calories"] = calories

    if duration is not None:
        entry_data["duration"] = duration

    doc_ref.set(entry_data)
    return doc_ref.id

def get_entries(db, user_id = None):
    #get all entries, optionally filtered by user ID
    entries = []

    query = db.collection("entries")
    if user_id:
        query = query.where("userId", "==", user_id.strip())

    for doc in query.stream():
        data = doc.to_dict()
        data["id"] = doc.id
        entries.append(data)

    #newest first
    entries.sort(key=lambda e: e.get("created_at", ""), reverse=True)
    return entries

def update_entry(db, entry_id, updates):
    #update an entry by its ID
    updates["updates_at"] = datetime.utcnow().isoformat()
    db.collection("entries").document(entry_id).update(updates)

def delete_entry(db, entry_id):
    #delete an entry by its ID
    db.collection("entries").document(entry_id).delete()