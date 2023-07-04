import 'package:flutter/material.dart';
import 'package:google_maps_flutter/google_maps_flutter.dart';
import 'package:geolocator/geolocator.dart';

class Mapa extends StatefulWidget {
  @override
  State<Mapa> createState() => MapaState();
}

class MapaState extends State<Mapa> {
  late GoogleMapController mapController;

  final LatLng _center = const LatLng(-5.088641218688359, -42.81186970076059);

  void _onMapCreated(GoogleMapController controller){
    mapController = controller;
  }

  _localizacaoAtual() async{
    Position position = await Geolocator.getCurrentPosition(
      desiredAccuracy: LocationAccuracy.high,
    );
    print('Localização: ' + position.toString());
  }


  @override
  void initState() {
    // TODO: implement initState
    super.initState();
    _localizacaoAtual();
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: Text('Mapa'),
        backgroundColor: Colors.green,
      ),
      body: GoogleMap(
        myLocationEnabled: true,
        mapType: MapType.normal,
        onMapCreated: _onMapCreated,
        initialCameraPosition: CameraPosition(
          target: _center,
          zoom: 15.0
        ),
        
      ),
      
    );
  }
}
