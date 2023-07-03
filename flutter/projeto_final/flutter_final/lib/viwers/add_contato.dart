import 'package:cloud_firestore/cloud_firestore.dart';
import 'package:flutter/material.dart';


class Add_Contato extends StatefulWidget {
  const Add_Contato({super.key});

  @override
  State<Add_Contato> createState() => _Add_ContatoState();
}

class _Add_ContatoState extends State<Add_Contato> {
  late TextEditingController nomeController;
  late TextEditingController emailController;
  late TextEditingController marcador1Controller;
  late TextEditingController marcador2Controller;

  final firestore = FirebaseFirestore.instance;


  @override
  void initState() {
    super.initState();
    nomeController = TextEditingController();
    emailController = TextEditingController();
    marcador1Controller = TextEditingController();
    marcador2Controller = TextEditingController();
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        backgroundColor: Colors.green,
        titleTextStyle: TextStyle(fontSize: 20, color: Colors.white),
        title: const Text('Adicionar Contato'),
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
                  keyboardType: TextInputType.number,
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
                  keyboardType: TextInputType.number,
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
                        firestore.collection("Contatos").doc("${nomeController.text}").set({
                              'Nome': nomeController.text,
                              'Email': emailController.text,
                              'Latitude': marcador1Controller.text,
                              'Longitude': marcador2Controller.text,
                            });

                        Navigator.pop(context);
                      },
                      child: const Text(
                        'Salvar',
                        style: TextStyle(color: Colors.white),
                      ),
                    ),
        ],
      ),
    );
  }
}