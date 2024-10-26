let nomes = ['Amélia Naomi', 'Fabião Zagueiro', 'Júnior Da Farmácia', 'Marcão Da Academia', 'Rafael Pascucci', 'Roberto Chagas', 'Thomaz Henrique', 'Dr José Cláudio', 'Dulce Rita', 'Fernando Petiti', 'Juvenil Silvério', 'Juliana Fraga', 'Lino Bispo', 'Marcelo Garcia', 'Milton Vieira Filho', 'Renato Santiago', 'Robertinho Da Padaria', 'Roberto Do Eleven', 'Rogério Da Acasem', 'Walter Hayashi', 'Zé Luís'];


// Objeto para mapear nomes a URLs
const urls = {
  'Amélia Naomi': 'http://127.0.0.1:5000/perfil/ver._amélia_naomi',
  'Fabião Zagueiro': 'http://127.0.0.1:5000/perfil/ver._fabião_zagueiro',
  'Júnior Da Farmácia': 'http://127.0.0.1:5000/perfil/ver._júnior_da_farmácia',
  'Marcão Da Academia': 'http://127.0.0.1:5000/perfil/ver._marcão_da_academia',
  'Rafael Pascucci': 'http://127.0.0.1:5000/perfil/ver._rafael_pascucci',
  'Roberto Chagas': 'http://127.0.0.1:5000/perfil/ver._roberto_chagas',
  'Thomaz Henrique': 'http://127.0.0.1:5000/perfil/ver._thomaz_henrique',
  'Dr José Cláudio': 'http://127.0.0.1:5000/perfil/ver_dr._josé_cláudio',
  'Dulce Rita': 'http://127.0.0.1:5000/perfil/ver._dulce_rita',
  'Fernando Petiti': 'http://127.0.0.1:5000/perfil/ver._fernando_petiti',
  'Juvenil Silvério': 'http://127.0.0.1:5000/perfil/ver._juvenil_silvério',
  'Juliana Fraga': 'http://127.0.0.1:5000/perfil/ver._juliana_fraga',
  'Lino Bispo': 'http://127.0.0.1:5000/perfil/ver._lino_bispo',
  'Marcelo Garcia': 'http://127.0.0.1:5000/perfil/ver._marcelo_garcia',
  'Milton Vieira Filho': 'http://127.0.0.1:5000/perfil/ver._milton_vieira_filho',
  'Renato Santiago': 'http://127.0.0.1:5000/perfil/ver._renato_santiago',
  'Robertinho da Padaria': 'http://127.0.0.1:5000/perfil/ver._robertinho_da_padaria',
  'Roberto Do Eleven': 'http://127.0.0.1:5000/perfil/ver._roberto_do_eleven',
  'Rogério Da Acasem': 'http://127.0.0.1:5000/perfil/ver._rogério_da_acasem',
  'Walter Hayashi': 'http://127.0.0.1:5000/perfil/ver._walter_hayashi',
  'Zé Luís': 'http://127.0.0.1:5000/perfil/ver._zé_luis',
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