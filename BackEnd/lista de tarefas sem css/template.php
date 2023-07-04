<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Gerenciador de Tarefas</title>
</head>
<body>
    <head>
        <title>Gerenciador de Tarefas</title>
    </head>
        <h1>Gerenciador de Tarefas</h1>

    <form>
        <fieldset>
            <legend>Nova Tarefa</legend>
            <label>
                Nome:
                <input type="text" name="nome" /><br><br>
                Telefone:
                <input type="number" name="telefone"><br><br>
                e-mail:
                <input type="email" name="email"><br><br>
                Descrição:
                <textarea name='descricao'></textarea><br><br>
                Data:
                <input type="date" name="data"><br><br>
                <input type="checkbox" name="favorito" value="sim">
                <label for="favorito">favorito</label><br>

            </label>
            <br><br><input type="submit" value="Cadastrar">
        </fieldset>
    </form>

    <table>
            <tr>
                <th>Nome</th>
                <th>Telefone</th>
                <th>E-mail</th>
                <th>Descrição</th>
                <th>Data</th>
                <th>Favorito</th>
            </tr>
            
        <? foreach ($lista_tarefas as $tarefa) : ?>
                <tr>
                    <td><? echo $tarefa['nome']; ?></td>
                    <td><? echo $tarefa['telefone']; ?></td>
                    <td><? echo $tarefa['email']; ?></td>
                    <td><? echo $tarefa['descricao']; ?></td>
                    <td><? echo $tarefa['data']; ?></td>
                    <td><? echo $tarefa['favorito']; ?></td>
                </tr>
        <? endforeach; ?>
    </table>

</body>
</html>