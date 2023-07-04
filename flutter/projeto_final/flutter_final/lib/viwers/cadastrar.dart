import 'package:cloud_firestore/cloud_firestore.dart';
import 'package:flutter/material.dart';

class Cadastrar extends StatefulWidget {
  const Cadastrar({super.key});

  @override
  State<Cadastrar> createState() => _CadastrarState();
}

class _CadastrarState extends State<Cadastrar> {
  late TextEditingController usuarioController;
  late TextEditingController senhaController;

  final firestore = FirebaseFirestore.instance;

@override
  void initState() {
    // TODO: implement initState
    super.initState();
    usuarioController = TextEditingController();
    senhaController = TextEditingController();
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        backgroundColor: Colors.red,
        title: Text('Tela de Cadastro'),
        centerTitle: true,
      ),
      body: Column(
        children: [
          Container(
                  alignment: Alignment.center,
                  height: 200,
                  width: 180,
                  child: Image.asset('images/ifpi.png')),
          Padding(
                padding: const EdgeInsets.all(20.0),
                child: TextField(
                  controller: usuarioController,
                  keyboardType: TextInputType.name,
                  decoration: const InputDecoration(
                    border: OutlineInputBorder(),
                    labelText: 'Usuario',
                    hintText: 'Fulano de Tal',
                  ),
                ),
              ),
          Padding(
                padding: const EdgeInsets.fromLTRB(20, 0, 20, 20),
                child: TextField(
                  controller: senhaController,
                  keyboardType: TextInputType.name,
                  decoration: const InputDecoration(
                    border: OutlineInputBorder(),
                    labelText: 'Senha',
                  ),
                ),
              ),
          Padding(
                padding: const EdgeInsets.fromLTRB(20, 0, 20, 20),
                child: TextField(
                  keyboardType: TextInputType.name,
                  decoration: const InputDecoration(
                    border: OutlineInputBorder(),
                    labelText: 'Repetir Senha',
                  ),
                ),
              ),
          ElevatedButton(
                      autofocus: true,
                      style: OutlinedButton.styleFrom(
                        backgroundColor: Colors.green,
                      ),
                      onPressed: () {
                        firestore.collection("Usuario").add({
                              'Usuario': usuarioController.text,
                              'Senha': senhaController.text,
                        });
                        Navigator.pushNamed(context, '/inicial');
                      },
                      child: const Text(
                        'ENTRAR',
                        style: TextStyle(color: Colors.white),
                      ),
                    ),
        ],
      ),
    );
  }
}
