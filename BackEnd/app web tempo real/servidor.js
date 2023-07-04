var http = require('http');
var fs = require('fs');

var server = http.createServer(function(request, response){
    response.writeHead(200, {"Content-Type": "text/html"});
    if(request.url == "/"){
        fs.readFile(__dirname + '/contato.html', function(erro, html){
            response.writeHeader(200, {'Content-Type': 'text/html'});
            response.write(html);
            response.end();});
    } 
    else if(request.url == "/artigo"){
        fs.readFile(__dirname + '/artigo.html', function(erro, html){
            response.writeHeader(200, {'Content-Type': 'text/html'});
            response.write(html);
            response.end();});
    } 
    else { 
        fs.readFile(__dirname + '/erro.html', function(erro, html){
            response.writeHeader(200, {'Content-Type': 'text/html'});
            response.write(html);
            response.end();});
    }
});

server.listen(3000, ()=>{console.log("Servidor Rodando!")});