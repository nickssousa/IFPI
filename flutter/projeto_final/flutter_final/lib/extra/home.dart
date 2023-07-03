import 'package:flutter/material.dart';
import 'package:flutter_final/extra/movies.dart';


class App extends StatelessWidget {
  const App({super.key});

  @override
  build(context) {
    return const MaterialApp(
      debugShowCheckedModeBanner: false,
      title: 'Filmes',
      home: MoviesListView(),
    );
  }
}