<?php
session_start();
require "banco.php";
require "ajudantes.php";
$exibir_tabela = true;

$tem_erros = false;
$erros_validacao = [];

if (tem_post()) {

    $tarefa = [
        'id' => $_POST['id'],
        'nome' => $_POST['nome'],
        'descricao' => '',
        'prazo' => '',
        'prioridade' => $_POST['prioridade'],
        'concluida' => 0
    ];

    if (array_key_exists('descricao', $_POST)) {
        $tarefa['descricao'] = $_POST['descricao'];
    } 
    if (array_key_exists('prazo', $_POST) && strlen($_POST['prazo']) > 0) {
        if (validar_data($_POST['prazo'])) {
            $tarefa['prazo'] = traduz_data_para_banco($_POST['prazo']);
        } else {
            $tem_erros = true;
            $erros_validacao['prazo'] = 'O prazo não é uma data válida';
        }
    } else {
        $tem_erros = true;
        $erros_validacao['prazo'] = 'O prazo não é uma data válida';
    }
    
        $tarefa['prioridade'] = $_POST['prioridade'];
    if (array_key_exists('concluida', $_POST)) {
        $tarefa['concluida'] = $_POST['concluida'];
    }         

    if (tem_post()){
        $tarefa = [
                'id' => $_POST['id'],
                'nome' => $_POST['nome'],
                'descricao' => $_POST['descricao'],
                'prazo' => (isset($_POST['prazo'])) ? traduz_data_para_banco($_POST['prazo']) : '',
                'prioridade' => $_POST['prioridade'],
                'concluida' => 0
                ];

        if (strlen($tarefa['nome']) == 0 ){
                $tem_erros = true;
                $erros_validacao['nome'] = 'O nome da tarefa é orbigatorio!';
            }
        }


        if (! $tem_erros){
            gravar_tarefa($conexao,$tarefa);
            header('Location: tarefas.php');
            die();
        }
}
    
    $lista_tarefas = buscar_tarefas($conexao);

	include "./teste.php"; //opcional para incluir uma imagem no topo
    
    $tarefa = [
        'id' => 0,
        'nome' => $_POST['nome'] ?? '',
        'descricao' => $_POST['descricao'] ?? '',
        'prazo' => $_POST['prazo'] ?? '',
        'prioridade' => (isset($_POST['prazo'])) 
                    ? traduz_data_para_banco($_POST['prazo']) : '',
        'concluida' => $_POST['concluida'] ?? ''
        ];

    
    include "./template.php";
?>