import 'package:flutter/material.dart';

class Login extends StatefulWidget {
  static var routeName = '/login';

  const Login({Key? key}) : super(key: key);

  @override
  State<Login> createState() => _LoginState();
}

class _LoginState extends State<Login> {
  final _usuarioController = TextEditingController();
  final _senhaController = TextEditingController();

  @override
  void dispose() {
    _usuarioController.dispose();
    _senhaController.dispose();
    super.dispose();
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        backgroundColor: Colors.green,
        titleTextStyle: TextStyle(fontSize: 20, color: Colors.white),
        title: const Text('Tela de Login'),
        centerTitle: true,
      ),
      body: Column(children: [
        Padding(
          padding: const EdgeInsets.all(16.0),
          child: Column(
            crossAxisAlignment: CrossAxisAlignment.stretch,
            children: [
              Container(
                  alignment: Alignment.center,
                  height: 200,
                  width: 180,
                  child: Image.asset('images/ifpi.png')),
              Padding(
                padding: const EdgeInsets.all(20.0),
                child: TextField(
                  controller: _usuarioController,
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
                  controller: _senhaController,
                  obscureText: true,
                  decoration: const InputDecoration(
                    border: OutlineInputBorder(),
                    labelText: 'Senha',
                  ),
                ),
              ),
              Padding(
                padding: const EdgeInsets.fromLTRB(25, 8, 25, 8),
                child: Row(
                  mainAxisAlignment: MainAxisAlignment.center,
                  children: [
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
              ),
              TextButton(
                onPressed: () {
                  Navigator.pushNamed(context, "/cadastrar");
                },
                child: const Text('Cadastrar'),
              ),
              Container(
                width: 15,
                child: TextButton(
                  onPressed: () {},
                  child: const Text('Recuperar senha?'),
                ),
              ),
            ],
          ),
        ),
      ]),
    );
  }
}
