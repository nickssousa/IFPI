import 'package:cloud_firestore/cloud_firestore.dart';
import 'package:flutter_final/widget/construtor.dart';

final firestore = FirebaseFirestore.instance;

mostrarDetalhes(Objeto objeto){
  
}



void retrieveSubCol(){
  final docRef = firestore.collection("Contatos");
  docRef.snapshots();
}

coisar(){
  firestore.collection("Contatos").get().then((value) {
    value.docs.forEach((event) {
      firestore.collection("Contatos").doc(event.id).snapshots();
    });
});

}