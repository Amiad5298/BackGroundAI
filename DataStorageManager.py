import firebase_admin
from firebase_admin import credentials, firestore, storage
import uuid

class DataStorageManager:
    def __init__(self, firebase_credentials_path, storage_bucket_name):
        # Initialize Firebase app
        cred = credentials.Certificate(firebase_credentials_path)
        firebase_admin.initialize_app(cred, {
            'storageBucket': storage_bucket_name
        })
        self.db = firestore.client()
        self.bucket = storage.bucket()

    def upload_image(self, image_url, file_name):
        try:
            # Generate a unique file name
            unique_file_name = f"{uuid.uuid4()}_{file_name}"
            
            # Download the image to a temporary location
            image_blob = self.bucket.blob(unique_file_name)
            image_blob.upload_from_string(image_url)
            image_blob.make_public()

            return image_blob.public_url
        except Exception as e:
            print(f"Error uploading image: {e}")
            return None

    def save_metadata(self, collection_name, document_id, data):
        try:
            doc_ref = self.db.collection(collection_name).document(document_id)
            doc_ref.set(data)
            print("Data saved successfully.")
        except Exception as e:
            print(f"Error saving metadata: {e}")

    def get_metadata(self, collection_name, document_id):
        try:
            doc_ref = self.db.collection(collection_name).document(document_id)
            doc = doc_ref.get()
            if doc.exists:
                return doc.to_dict()
            else:
                print("No such document!")
                return None
        except Exception as e:
            print(f"Error retrieving metadata: {e}")
            return None
