import 'package:cloud_firestore/cloud_firestore.dart';
import 'package:flutter/material.dart';
import 'package:flutter_final/viwers/editarcontato.dart';
import '../widget/construtor.dart';



class Contatos extends StatefulWidget {
  const Contatos({super.key});

@override
 _ContatosState createState() => _ContatosState();

}

class _ContatosState extends State<Contatos> {
  final firestore = FirebaseFirestore.instance;
    
  mostrarDetalhes(Objeto objeto){
      Navigator.push(context, MaterialPageRoute(
        builder: (_) => EditarContato(objeto: objeto),
        ),
        );
  }
  

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        backgroundColor: Colors.green,
        titleTextStyle: TextStyle(fontSize: 20, color: Colors.white),
        title: const Text('Contatos'),
        centerTitle: true,
      ),
      body: Center(
        child: Column(
          mainAxisAlignment: MainAxisAlignment.center,
          children: [
            StreamBuilder<QuerySnapshot>(
      stream: FirebaseFirestore.instance.collection("Contatos").snapshots(),
      builder: (BuildContext context, AsyncSnapshot<QuerySnapshot> snapshot) {
        if (!snapshot.hasData) {
          return Center(
            child: CircularProgressIndicator(),
          );

        }
        return Container(
          height: 250,
          width: 500,
          child: ListView(
            children: snapshot.data!.docs.map((DocumentSnapshot document) {
                 
                  return Card(
                    child: ListTile(
                        title: Text(document['Nome'].toString()),
                        subtitle: Text(document['Email'].toString()),
                        trailing: const Icon(Icons.edit),
                        onTap: () { 
                          Objeto banco = Objeto(
                            document["Nome"], 
                            document["Email"], 
                            document["Latitude"],
                            document["Longitude"],
                            );
                          mostrarDetalhes(banco);
                          },
                          
                         /* Navigator.pushNamed(context, "/edcontatos",
                          arguments: banco(nome: document["Nome"], email: document["Email"], latitude: document["Latitude"], longitude: document["Longitude"])
                          );*/


                        
                        onLongPress:(){
                          firestore.collection("Contatos").doc(document.id).delete();
                        },
                    ),
                  );
                }).toList()
                .cast(),
          ),
        );
      },
    )
    ],
        ),
      ),

      floatingActionButton: FloatingActionButton(
        onPressed: () {
            Navigator.pushNamed(context, "/addcontatos");
            },
        tooltip: 'Adicionar',
        child: const Icon(Icons.add),
      ), // This trailing comma makes auto-formatting nicer for build methods.

      );
  }}