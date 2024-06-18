function search() {
    console.log('Função de pesquisa chamada!');
    var inputSearch = document.getElementById('inputSearch');
    var query = inputSearch.value.toLowerCase(); // Obtenha o valor da entrada e converta para minúsculas
    var table = document.getElementById('estoque'); // Obtenha a tabela

    var rows = table.getElementsByTagName('tr'); // Obtenha todas as linhas da tabela

    // Itere sobre as linhas da tabela e mostre/oculte com base na consulta
    for (var i = 1; i < rows.length; i++) { // Comece em 1 para ignorar o cabeçalho
        var nome = rows[i].getElementsByTagName('td')[1]; // Obtém o conteúdo da segunda coluna (nome)

        if (nome) {
            var nomeText = nome.textContent || nome.innerText;
            if (nomeText.toLowerCase().indexOf(query) > -1) {
                rows[i].style.display = ''; // Mostrar a linha se a consulta for encontrada
            } else {
                rows[i].style.display = 'none'; // Ocultar a linha se a consulta não for encontrada
            }
        }
    }
}