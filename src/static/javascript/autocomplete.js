let nomes = ['Amélia Naomi', 'Fabião Zagueiro', 'Júnior Da Farmácia', 'Marcão Da Academia', 'Rafael Pascucci', 'Roberto Chagas', 'Thomaz Henrique', 'Dr José Cláudio', 'Dulce Rita', 'Fernando Petiti', 'Juvenil Silvério', 'Juliana Fraga', 'Lino Bispo', 'Marcelo Garcia', 'Milton Vieira Filho', 'Renato Santiago', 'Robertinho Da Padaria', 'Roberto Do Eleven', 'Rogério Da Acasem', 'Walter Hayashi', 'Zé Luís'];


// Objeto para mapear nomes a URLs
const urls = {
  'Amélia Naomi': 'http://127.0.0.1:5000/perfil/2',
  'Fabião Zagueiro': 'http://127.0.0.1:5000/perfil/5',
  'Júnior Da Farmácia': 'http://127.0.0.1:5000/perfil/8',
  'Marcão Da Academia': 'http://127.0.0.1:5000/perfil/11',
  'Rafael Pascucci': 'http://127.0.0.1:5000/perfil/14',
  'Roberto Chagas': 'http://127.0.0.1:5000/perfil/17',
  'Thomaz Henrique': 'http://127.0.0.1:5000/perfil/20',
  'Dr José Cláudio': 'http://127.0.0.1:5000/perfil/3',
  'Dulce Rita': 'http://127.0.0.1:5000/perfil/4',
  'Fernando Petiti': 'http://127.0.0.1:5000/perfil/6',
  'Juvenil Silvério': 'http://127.0.0.1:5000/perfil/9',
  'Juliana Fraga': 'http://127.0.0.1:5000/perfil/7',
  'Lino Bispo': 'http://127.0.0.1:5000/perfil/10',
  'Marcelo Garcia': 'http://127.0.0.1:5000/perfil/12',
  'Milton Vieira Filho': 'http://127.0.0.1:5000/perfil/13',
  'Renato Santiago': 'http://127.0.0.1:5000/perfil/15',
  'Robertinho da Padaria': 'http://127.0.0.1:5000/perfil/16',
  'Roberto Do Eleven': 'http://127.0.0.1:5000/perfil/18',
  'Rogério Da Acasem': 'http://127.0.0.1:5000/perfil/19',
  'Walter Hayashi': 'http://127.0.0.1:5000/perfil/21',
  'Zé Luís': 'http://127.0.0.1:5000/perfil/22',
};

const resultsBox = document.querySelector('.result-box');
const inputBox = document.getElementById('input-box');

inputBox.onkeyup = function() {
  let result = [];
  let input = inputBox.value;
  if (input.length){
    result = nomes.filter((keyword)=>{
      return keyword.toLowerCase().includes(input.toLowerCase());
    });
    display(result)
  }
  if (!result.length){
    resultsBox.innerHTML = '';
  }
}

function display(result){
  const content = result.map((list)=>{
    const url = urls[list] || ''; // Verifica se o URL existe antes de usar
    return `<li onclick="redirectToUrl('${url}')">${list}</li>`;
  })
  resultsBox.innerHTML = "<ul>" + content.join('') + "</ul>";
}

function redirectToUrl(url) {
  if (url) { // Verifica se o URL é válido antes de redirecionar
    window.location.href = url;
  } else {
    // Opcional: Exibir uma mensagem de erro caso o URL não seja encontrado
    alert('URL não encontrado para este nome.');
  }
}