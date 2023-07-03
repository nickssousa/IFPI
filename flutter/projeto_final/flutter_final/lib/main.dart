import 'package:cloud_firestore/cloud_firestore.dart';
import 'package:firebase_core/firebase_core.dart';
import 'package:flutter/material.dart';
import 'package:flutter_final/extra/home.dart';
import 'package:flutter_final/viwers/add_contato.dart';
import 'package:flutter_final/firebase_options.dart';
import 'package:firebase_database/firebase_database.dart';



import 'viwers/login.dart';
import 'viwers/editarcontato.dart';
import 'viwers/cadastrar.dart';
import 'viwers/inicial.dart';
import 'viwers/tela2.dart';
import 'widget/mapa.dart';
import 'viwers/contatos.dart';

void main() async{
  WidgetsFlutterBinding.ensureInitialized();
  await Firebase.initializeApp(
    options: DefaultFirebaseOptions.currentPlatform,
  );
  
  
  runApp(const MyApp());

  FirebaseFirestore firestore = FirebaseFirestore.instance;
}

class MyApp extends StatelessWidget {
  const MyApp({super.key});

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      debugShowCheckedModeBanner: false,
      title: "Projeto Final",
      theme: ThemeData(
        colorScheme: ColorScheme.fromSeed(seedColor: Colors.green),
        useMaterial3: true,
      ),
      initialRoute: '/',
      routes: {
        "/": (ctx) => const Login(),
        "/inicial": (ctx) => const Inicial(),
        "/cadastrar": (ctx) => const Cadastrar(),
        "/tela2" : (ctx) => const Tela2(),
        "/mapa" : (ctx) => const Mapa(),
        "/contatos" : (ctx) => const Contatos(),
        "/addcontatos" : (ctx) => const Add_Contato(),
        "/extra1" : (ctx) => const App(),
      },
    );
  }
}
