import 'package:flutter/material.dart';
import 'package:flutter_activity/mapa.dart';
import 'package:flutter_activity/tela2.dart';

void main() {
  runApp(const MyApp());
}

class MyApp extends StatelessWidget {
  const MyApp({super.key});

  // This widget is the root of your application.
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'Flutter Demo',
      theme: ThemeData(
        primarySwatch: Colors.blue,
      ),
      home: const MyHomePage(title: 'Flutter Demo Home Page'),
      routes: {
        '/a': (context) => MyApp(),
        '/tela2': (context) => Tela2(),
        '/mapa': (context) => Mapa()
      },
    );
  }
}

class MyHomePage extends StatefulWidget {
  const MyHomePage({super.key, required this.title});

  final String title;

  @override
  State<MyHomePage> createState() => _MyHomePageState();
}

class _MyHomePageState extends State<MyHomePage> {
  @override
  Widget build(BuildContext context) {
    return Scaffold(
        appBar: AppBar(
          title: Text(widget.title),
        ),
        body: Column(
          crossAxisAlignment: CrossAxisAlignment.stretch,
          children: [
            Icon(
              Icons.person_2_outlined,
              size: 500,
            ),
            ElevatedButton(
              onPressed: () {
                Navigator.pushNamed(context, '/tela2');
              },
              child: Text('Login'),
            ),
            ElevatedButton(
                onPressed: () {
                  Navigator.pushNamed(context, '/mapa');
                },
                child: Text('Mapa')),
          ],
        ));
  }
}
