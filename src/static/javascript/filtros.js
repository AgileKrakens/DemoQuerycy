let nomes = ['Amélia Naomi', 'Fabião Zagueiro', 'Júnior Da Farmácia', 'Marcão Da Academia', 'Rafael Pascucci', 'Roberto Chagas', 'Thomaz Henrique', 'Dr José Cláudio', 'Dulce Rita', 'Fernando Petiti', 'Juvenil Silvério', 'Juliana Fraga', 'Lino Bispo', 'Marcelo Garcia', 'Milton Vieira Filho', 'Renato Santiago', 'Robertinho Da Padaria', 'Roberto Do Eleven', 'Rogério Da Acasem', 'Walter Hayashi', 'Zé Luís'];
let nomesOrganizados = nomes.sort()
const container = document.getElementById('checkboxContainer');

        
        nomes.forEach((nome, index) => {
            
            const checkbox = document.createElement('input');
            checkbox.type = 'checkbox';
            checkbox.id = index;
            checkbox.name = nome;
            checkbox.value = nome;
            checkbox.class = 'checkbox';

            
            const label = document.createElement('label');
            label.htmlFor = index;
            label.textContent = nome;

            
            container.appendChild(checkbox);
            container.appendChild(label);

            
            container.appendChild(document.createElement('br'));
        });