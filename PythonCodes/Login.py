import firebase_admin
from firebase_admin import credentials, firestore
from pandas import read_excel
# SDK ayarlamaları
credentialData = credentials.Certificate("credentials.json")
firebase_admin.initialize_app(credentialData)
# Firestore instance  oluşturma
firestoreDb = firestore.client()
# Veri Ekleme
firestoreDb.collection(u'testCollection').add({'yazar':'Orhan Veli'})
# Veri Okuma
snapshots = list(firestoreDb.collection(u'testCollection').get())
for snap in snapshots:
 print(snap.to_dict())


