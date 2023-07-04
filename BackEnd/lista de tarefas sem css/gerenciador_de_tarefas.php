<? session_start() ?>

<?
            if (array_key_exists('nome', $_GET) && $_GET['nome'] != '') {
                $tarefa = [
                    'nome' => $_GET['nome'],
                    'telefone' => $_GET['telefone'],
                    'email' => $_GET['email'],
                    'descricao' => $_GET['descricao'],
                    'data' => $_GET['data'],
                    'favorito' => $_GET['favorito'],
                ];
                if (array_key_exists('telefone', $_GET)) {
                    $tarefa['telefone'] = $_GET['telefone'];
                }

                if (array_key_exists('email', $_GET)) {
                    $tarefa['email'] = $_GET['email'];
                }
    
                if (array_key_exists('descricao', $_GET)){
                    $tarefa['descricao'] = $_GET['descricao'];
                }

                if (array_key_exists('data', $_GET)){
                    $tarefa['data'] = $_GET['data'];
                }

                if (array_key_exists('favorito', $_GET)){
                    $tarefa['favorito'] = $_GET['favorito'];
                }
                $_SESSION['lista_tarefas'][] = $tarefa;
            }

            $lista_tarefas = [];
            if (array_key_exists('lista_tarefas', $_SESSION)) {
                $lista_tarefas = $_SESSION['lista_tarefas'];
            }

          

    include 'template.php';
    ?>


