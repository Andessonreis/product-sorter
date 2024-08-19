const apiUrl = 'http://127.0.0.1:5000';

async function adicionarProduto() {
    const nome = document.getElementById('nomeProduto').value;
    const avaliacao = document.getElementById('avaliacaoProduto').value;
    const preco = document.getElementById('precoProduto').value;

    const response = await fetch(`${apiUrl}/add_product`, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ nome, avaliacao, preco })
    });

    if (response.ok) {
        exibirProdutos() // Exibe os produtos imediatamente após a adição
    }
}

async function ordenarProdutos() {
    const estrategia = document.getElementById('estrategiaOrdenacao').value;

    const response = await fetch(`${apiUrl}/sort_products`, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ estrategia })
    });
    const sortedProducts = await response.json();
    exibirProdutos(sortedProducts);
}

async function exibirProdutos(produtos = null) {
    const listaProdutos = document.getElementById('listaProdutos');
    listaProdutos.innerHTML = '';

    if (!produtos) {
        const response = await fetch(`${apiUrl}/get_products`, {
            method: 'GET',
            headers: { 'Content-Type': 'application/json' }
        });
        produtos = await response.json();
    }

    produtos.forEach(produto => {
        const itemProduto = document.createElement('li');
        itemProduto.textContent = `${produto.nome} - Avaliação: ${produto.avaliacao} - Preço: R$ ${produto.preco}`;
        listaProdutos.appendChild(itemProduto);
    });
}

document.addEventListener('DOMContentLoaded', exibirProdutos); // Exibe os produtos ao carregar a página
