import 'package:flutter/material.dart';

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
          
          Row(
            
            children: [
              ElevatedButton(
                          style: OutlinedButton.styleFrom(
                            backgroundColor: Colors.green,
                          ),
                          onPressed: () {
                            Navigator.pushNamed(context, "/contatos");
                          },
                          child: const Text(
                            'Contatos',
                            style: TextStyle(color: Colors.white),
                          ),
                        ),
           

          ElevatedButton(
                      style: OutlinedButton.styleFrom(
                        backgroundColor: Colors.green,
                      ),
                      onPressed: () {
                        Navigator.pushNamed(context, "/mapa");
                      },
                      child: const Text(
                        'Mapa',
                        style: TextStyle(color: Colors.white),
                      ),
                    ),
             ],
          ),

          Row(
            children: [
              ElevatedButton(
                          style: OutlinedButton.styleFrom(
                            backgroundColor: Colors.green,
                          ),
                          onPressed: () {
                            Navigator.pushNamed(context, "/extra1");
                          },
                          child: const Text(
                            'API #1',
                            style: TextStyle(color: Colors.white),
                          ),
                        ),
            

          ElevatedButton(
                      style: OutlinedButton.styleFrom(
                        backgroundColor: Colors.green,
                      ),
                      onPressed: () {},
                      child: const Text(
                        'Extra',
                        style: TextStyle(color: Colors.white),
                      ),
                    ),
                    ],
          ),
        ],
      ),
    );
  }
}