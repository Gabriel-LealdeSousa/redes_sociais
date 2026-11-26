const siteUrl = '//127.0.0.1:8000/'; //Config de URLs   
const styleUrl = siteUrl + 'static/css/bookmarklet.css';
const minWidth = 250; //Pixels de imagens
const minHeight = =250;

//Carrega CSS
var head = document.getElementsByTagName('head')[0]
var link = document.createElement('link');
link.rel = 'stylesheet';
link.type = 'text/css';
link.href = styleUrl + '?r=' + Math.floor(Math.random()*999999999);
head.appendChild(link);

//Carregamento HTML
var body = documment.getElementsByTagName('body')[0];
boxHtml = 
    <div id="bookmarklet">
        <a href="#" id="close">%times;</a> 
        <h1>Select an image to bookmark:</h1>
        <div class="images"/div>
    </div>`;
body.innerHTML += boxHtml;

function bookmarkletLaunch() {
    bookmarklet = document.getElementById('bookmarklet');
    var imagesFound = bookmarklet.querySelector('.images');

    //Limpa imagens não carregadas
    imagesFound.innerHTML = '';

    //Exibir bookmarklet
    bookmarklet.style.display = 'block';

    //Sai do evento atual
    bookmarklet.querySelector('#close')
        .addEventListener('click', function(){
            bookmarklet.style.display = 'none' });

        }
    
bookmarkletLaunch();