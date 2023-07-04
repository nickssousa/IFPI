import 'package:flutter/material.dart';
import 'package:flutter/services.dart';

class Inicial extends StatefulWidget {
  const Inicial({super.key});

  @override
  State<Inicial> createState() => _InicialState();
}

class _InicialState extends State<Inicial> {
  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        backgroundColor: Colors.green,
        titleTextStyle: TextStyle(fontSize: 20, color: Colors.white),
        title: const Text('Tela Inicial'),
        centerTitle: true,
      ),
      body: Column(
        children: [
          Container(
                  alignment: Alignment.center,
                  height: 200,
                  width: 180,
                  child: Image.asset('images/ifpi.png')),
          
          SizedBox(
            height: 150,
          ),
          
          Row(
            mainAxisAlignment: MainAxisAlignment.spaceAround,
            children: [
              Container(
                color: Colors.green,
                height: 60,
                width: 170.0,
                child: TextButton(
                            style: ButtonStyle(
                                backgroundColor:
                              MaterialStateProperty.all(Color.fromARGB(255, 76, 175, 80)),
                                textStyle: MaterialStateProperty.all(
                              const TextStyle(
                                  fontSize: 20, color: Colors.white))),
                            onPressed: () {
                              Navigator.pushNamed(context, "/contatos");
                            },
                            child: const Text(
                              'Contatos',
                              style: TextStyle(color: Colors.white),
                            ),
                          ),
              ),
           

          Container(
            color: Colors.green,
            height: 60,
            width: 170.0,
            child: TextButton(
                        style: ButtonStyle(
                          backgroundColor:
                              MaterialStateProperty.all(Color.fromARGB(255, 76, 175, 80)),
                                textStyle: MaterialStateProperty.all(
                              const TextStyle(
                                  fontSize: 20, color: Colors.white))),
                        onPressed: () {
                          Navigator.pushNamed(context, "/mapa");
                        },
                        child: const Text(
                          'Mapa',
                          style: TextStyle(color: Colors.white),
                        ),
                      ),
          ),
             ],
          ),

          SizedBox(
            height: 30,
          ),

          Row(
            mainAxisAlignment: MainAxisAlignment.spaceAround,
            children: [
              Container(
                color: Colors.green,
                height: 60,
                width: 170.0,
                child: TextButton(
                            style: ButtonStyle(
                          backgroundColor:
                              MaterialStateProperty.all(Color.fromARGB(255, 76, 175, 80)),
                                textStyle: MaterialStateProperty.all(
                              const TextStyle(
                                  fontSize: 20, color: Colors.white))),
                            onPressed: () {
                              Navigator.pushNamed(context, "/extra1");
                            },
                            child: const Text(
                              'API #1',
                              style: TextStyle(color: Colors.white),
                            ),
                          ),
              ),
            

          Container(
            color: Colors.green,
            height: 60,
            width: 170.0,

            child: TextButton(
                        style: ButtonStyle(
                          backgroundColor:
                              MaterialStateProperty.all(Color.fromARGB(255, 76, 175, 80)),
                                textStyle: MaterialStateProperty.all(
                              const TextStyle(
                                  fontSize: 20, color: Colors.white))),
                        onPressed: () {
                          Navigator.pushNamed(context, '/extra2');
                        },
                        child: const Text(
                          'API #2',
                          style: TextStyle(color: Colors.white),
                        ),
                      ),
          ),
                    ],
          ),
        ],
      ),
    );
  }
}