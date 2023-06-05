import 'package:flutter/material.dart';
import 'package:google_maps_flutter/google_maps_flutter.dart';
import 'package:geolocator/geolocator.dart';

class Mapa extends StatefulWidget {
  const Mapa({super.key});

  @override
  State<Mapa> createState() => _MapaState();
}

class _MapaState extends State<Mapa> {
  late GoogleMapController mapController;
  final LatLng _center = LatLng(-22.9129, -43.4399);
  Set<Marker> _marks = {};

  void _onMapCreated(GoogleMapController controller) {
    mapController = controller;
  }

  _localizacaoAtual() async {
    LocationPermission permission;

    bool ativado = await Geolocator.isLocationServiceEnabled();
    if (!ativado) {
      return Future.error('Por favor habilite localização');
    }
    if (permission == LocationPermission.denied) {
      permission = await Geolocator.requestPermission();
      if (permission == LocationPermission.denied) {
        return Future.error('Por favor autorize o acesso.');
      }
    }

    Position position = await Geolocator.getCurrentPosition(
      desiredAccuracy: LocationAccuracy.high,
    );
    print('Localização: ' + position.toString());
  }

  void _loadMarks() {
    Set<Marker> localMarks = {};
    Marker markerRiver = Marker(
      markerId: MarkerId('River Clube'),
      position: LatLng(-5.19426273177079, -42.73528131491655),
      infoWindow: InfoWindow(
        title: 'River Clube',
      ),
    );
    Marker markerVasco = Marker(
      markerId: MarkerId('Vasco Clube'),
      position: LatLng(-23.99093595287719, -46.3040735453277),
      infoWindow: InfoWindow(title: 'Vasco Clube'),
    );
    Marker markerAtletico = Marker(
      markerId: MarkerId('Atletico Clube'),
      position: LatLng(-25.52328262251824, -49.26830370646951),
      infoWindow: InfoWindow(title: 'Athletico Clube'),
    );
    localMarks.add(markerRiver);
    localMarks.add(markerVasco);
    localMarks.add(markerAtletico);
    setState(() {
      _marks = localMarks;
    });
  }

  @override
  void initState() {
    _loadMarks();
    super.initState();
    _loadMarks();
    _localizacaoAtual();
  }

  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: Text('Tela do mapa'),
      ),
      body: (GoogleMap(
        myLocationEnabled: true,
        onMapCreated: _onMapCreated,
        initialCameraPosition: CameraPosition(target: _center, zoom: 11.0),
        markers: _marks,
      )),
    );
  }
}
