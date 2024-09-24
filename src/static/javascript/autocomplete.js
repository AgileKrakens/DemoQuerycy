let nomes = ['Amélia Naomi', 'Fabião Zagueiro', 'Júnior Da Farmácia', 'Marcão Da Academia', 'Rafael Pascucci', 'Roberto Chagas', 'Thomaz Henrique', 'Dr José Cláudio', 'Dulce Rita', 'Fernando Petiti', 'Juvenil Silvério', 'Juliana Fraga', 'Lino Bispo', 'Marcelo Garcia', 'Milton Vieira Filho', 'Renato Santiago', 'Robertinho Da Padaria', 'Roberto Do Eleven', 'Rogério Da Acasem', 'Walter Hayashi', 'Zé Luís']
const resultsBox = document.querySelector('.result-box');
const inputBox = document.getElementById('input-box');

inputBox.onkeyup = function() {
  let result = [];
  let input = inputBox.value;
  if (input.length){
    result = nomes.filter((keyword)=>{
      return keyword.toLowerCase().includes(input.toLowerCase());

    });
    // console.log(result)
  }
  display(result)
  if (!result.length){
    resultsBox.innerHTML = '';
  }
}

function display(result){
  const content = result.map((list)=>{
    return "<li onclick=selectInput(this)>"+ list + "</li>";
  })
  resultsBox.innerHTML = "<ul>" + content.join('') + "</ul>";
}

function selectInput(list){
  inputBox.value = list.innerHTML;
  resultsBox.innerHTML = '';
}