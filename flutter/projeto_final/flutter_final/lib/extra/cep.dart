import 'package:flutter/material.dart';
import 'package:http/http.dart' as http;
import 'dart:convert';



class Extra2 extends StatefulWidget {
  const Extra2({super.key});

  @override
  State<Extra2> createState() => _Extra2State();
}

class _Extra2State extends State<Extra2> {
  final cepController = TextEditingController();
  String logradouro = "";
  String bairro = "";
  String cidade = "";
  String estado = "";

  _buscarCep() async{
    var url = Uri.parse('https://viacep.com.br/ws/64005450/json/');
    http.Response response;

    response = await http.get(url);
    //print('Resposta' + response.statusCode.toString());
    //print('Resposta' + response.body);

    Map<String, dynamic> retorno = json.decode(response.body);
    
    setState(() {
      logradouro = " " + retorno["logradouro"];
      bairro = "Bairro " + retorno['bairro'];
      cidade = "Cidade " + retorno['localidade'];
      estado = "UF - " + retorno['uf'];
    });
  }

  


  @override
  Widget build(BuildContext context) {
    return Scaffold( 
      appBar: AppBar(
        backgroundColor: Colors.green,
        titleTextStyle: TextStyle(fontSize: 20, color: Colors.white),
        title: const Text('Endereço Pelo C.E.P.'),
        centerTitle: true,
      ),
    body: Column(
      children: [
        Padding(
          padding: EdgeInsets.fromLTRB(150.0, 30, 150, 30 ),
          child: TextField(
                    controller: cepController,
                    keyboardType: TextInputType.number,
                    decoration: const InputDecoration(
                      border: OutlineInputBorder(),
                      hintText: 'XXXXX-XXX',
                    ),
                  ),
        ),
        Container(
          alignment: Alignment.center,
          padding: EdgeInsets.fromLTRB(100.0, 0, 100, 30 ),
                child: Column(children: [
            ElevatedButton(
              onPressed:() {
              _buscarCep();
              
            },
            child: Text ('Buscar Cep', style: TextStyle(color: Colors.white),),
            style: 
            ElevatedButton.styleFrom(backgroundColor: Colors.green,
            minimumSize: Size(100, 75),
            shape: const RoundedRectangleBorder(
              borderRadius: BorderRadius.all(Radius.circular(20)),
            
            )
            ),
        
            ),
            SizedBox(height: 30.0),
            Text('$logradouro \n $bairro \n $cidade \n $estado' ,
                 style:TextStyle(color:Colors.green, fontSize: 15.0), ),
              
          ],
          ),
        ),
      ],
    ),

    );
  }
}



