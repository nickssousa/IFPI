import 'package:cloud_firestore/cloud_firestore.dart';
import 'package:flutter/material.dart';
import 'package:flutter_final/widget/construtor.dart';

class EditarContato extends StatefulWidget {
  final Objeto objeto;
  const EditarContato({super.key, required this.objeto});

  @override
  State<EditarContato> createState() => _EditarContatoState();
}

class _EditarContatoState extends State<EditarContato> {
  late TextEditingController idController;
  late TextEditingController nomeController;
  late TextEditingController emailController;
  late TextEditingController marcador1Controller;
  late TextEditingController marcador2Controller;

  final firestore = FirebaseFirestore.instance;

  existe(){
    Objeto objeto =  widget.objeto;
    idController.text = objeto.nome;
    nomeController.text = objeto.nome;
    emailController.text = objeto.email;
    marcador1Controller.text = objeto.marcador1;
    marcador2Controller.text = objeto.marcador2;
  }

  @override
  void initState() {
    super.initState();
    idController = TextEditingController();
    nomeController = TextEditingController();
    emailController = TextEditingController();
    marcador1Controller = TextEditingController();
    marcador2Controller = TextEditingController();

    existe();
  }


  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        backgroundColor: Colors.green,
        titleTextStyle: TextStyle(fontSize: 20, color: Colors.white),
        title: Text(widget.objeto.nome),
        centerTitle: true,
      ),
      body: Column(
        children: [
          Padding(
                padding: const EdgeInsets.all(20.0),
                child: TextField(
                  controller: nomeController,
                  keyboardType: TextInputType.name,
                  decoration: const InputDecoration(
                    border: OutlineInputBorder(),
                    labelText: 'Usuario',
                    //hintText: '${banco.nome}',
                  ),
                ),
              ),
          Padding(
                padding: const EdgeInsets.fromLTRB(20, 0, 20, 20),
                child: TextField(
                  controller: emailController,
                  keyboardType: TextInputType.name,
                  decoration: const InputDecoration(
                    border: OutlineInputBorder(),
                    labelText: 'Email',
                  ),
                ),
              ),
          Padding(
                padding: const EdgeInsets.fromLTRB(20, 0, 20, 20),
                child: TextField(
                  controller: marcador1Controller,
                  keyboardType: TextInputType.name,
                  decoration: const InputDecoration(
                    border: OutlineInputBorder(),
                    labelText: 'Latitude',
                  ),
                ),
              ),
          Padding(
                padding: const EdgeInsets.fromLTRB(20, 0, 20, 20),
                child: TextField(
                  controller: marcador2Controller,
                  keyboardType: TextInputType.name,
                  decoration: const InputDecoration(
                    border: OutlineInputBorder(),
                    labelText: 'Longitude',
                  ),
                ),
              ),
          ElevatedButton(
                      autofocus: true,
                      style: OutlinedButton.styleFrom(
                        backgroundColor: Colors.green,
                      ),
                      onPressed: () {
                        firestore.collection("Contatos").doc("${idController.text}").update({
                              'Nome': nomeController.text,
                              'Email': emailController.text,
                              'Latitude': marcador1Controller.text,
                              'Longitude': marcador2Controller.text,
                            });

                        Navigator.pop(context);
                      },
                      child: const Text(
                        'Atualizar',
                        style: TextStyle(color: Colors.white),
                      ),
                    ),
        ],
      ),
    );
  }
}