import 'package:flutter/cupertino.dart';
import 'package:flutter/material.dart';

void main() {
  runApp(const MyApp());
}

class MyApp extends StatelessWidget {
  const MyApp({Key? key}) : super(key: key);

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'Flutter Demo',
      theme: ThemeData(
        primarySwatch: Colors.green,
      ),
      home: const MyHomePage(title: 'Flutter Demo Home Page'),
    );
  }
}

class MyHomePage extends StatefulWidget {
  const MyHomePage({Key? key, required this.title}) : super(key: key);

  final String title;

  @override
  State<MyHomePage> createState() => _MyHomePageState();
}

class _MyHomePageState extends State<MyHomePage> {
  final TextEditingController _textEditingControllerPeso =
      TextEditingController();
  final TextEditingController _textEditingControllerAltura =
      TextEditingController();

  var resultado = '';

  int _counter = 0;

  void _incrementCounter() {
    setState(() {
      _counter++;
    });
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: Text("Calculadora de IMC"),
        centerTitle: true,
        actions: [
          IconButton(
            onPressed: () {
              setState(() {
                _textEditingControllerAltura.text = '';
                _textEditingControllerPeso.text = '';
                resultado = '';
              });
            },
            icon: Icon(Icons.refresh),
          )
        ],
      ),
      body: SingleChildScrollView(
        padding: EdgeInsets.fromLTRB(40.0, 0.0, 40.0, 0.0),
        child: Column(
          crossAxisAlignment: CrossAxisAlignment.stretch,
          children: [
            Icon(
              Icons.person_outline,
              size: 150.0,
              color: Colors.green,
            ),
            SizedBox(
              height: 20.0,
            ),
            TextField(
                keyboardType: TextInputType.number,
                textAlign: TextAlign.center,
                controller: _textEditingControllerPeso,
                decoration: InputDecoration(
                    label: Text("Peso (kg)"),
                    labelStyle:
                        TextStyle(color: Colors.green, fontSize: 25.0))),
            SizedBox(
              height: 20.0,
            ),
            TextField(
                keyboardType: TextInputType.number,
                textAlign: TextAlign.center,
                controller: _textEditingControllerAltura,
                decoration: InputDecoration(
                    label: Text("Altura (m)"),
                    labelStyle:
                        TextStyle(color: Colors.green, fontSize: 25.0))),
            SizedBox(
              height: 20.0,
            ),
            Container(
              height: 50.0,
              child: ElevatedButton(
                onPressed: () {
                  setState(() {
                    resultado = (double.parse(_textEditingControllerPeso.text) /
                            (double.parse(_textEditingControllerAltura.text) *
                                double.parse(
                                    _textEditingControllerAltura.text)))
                        .toStringAsFixed(2);
                    print("O IMC é " + resultado);
                    texto = "Seu IMC é " + resultado;
                  });
                },
                child: Text(
                  "Calcular",
                  style: TextStyle(color: Colors.white, fontSize: 35.0),
                ),
              ),
            ),
            SizedBox(
              height: 20.0,
            ),
            Text(
              resultado,
              textAlign: TextAlign.center,
              style: TextStyle(color: Colors.green, fontSize: 25.0),
            ),
          ],
        ),
      ),
    );
  }
}
