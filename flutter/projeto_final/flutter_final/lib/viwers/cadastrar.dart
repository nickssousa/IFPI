import 'package:flutter/material.dart';

class Cadastrar extends StatefulWidget {
  const Cadastrar({super.key});

  @override
  State<Cadastrar> createState() => _CadastrarState();
}

class _CadastrarState extends State<Cadastrar> {
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
