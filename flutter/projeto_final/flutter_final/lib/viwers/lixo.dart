import 'package:cloud_firestore/cloud_firestore.dart';

FirebaseFirestore db = FirebaseFirestore.instance;

nemsei() {
  db.collection("cities").get().then(
  (querySnapshot) {
    print("Successfully completed");
    for (var docSnapshot in querySnapshot.docs) {
      print('${docSnapshot.id} => ${docSnapshot.data()}');
    }
  },
  onError: (e) => print("Error completing: $e"),
);
}