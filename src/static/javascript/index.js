const hidePlaceholder = document.getElementById('input-txt');
hidePlaceholder.addEventListener('focus', function(){
    this.placeholder = '';
})
hidePlaceholder.addEventListener('blur', function(){
    this.placeholder = 'O que deseja procurar ?';
});