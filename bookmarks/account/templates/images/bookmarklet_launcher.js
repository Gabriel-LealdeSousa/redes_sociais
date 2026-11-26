(function(){
    bookmarklet_js = document.body.appendChild(document.createElement);
    bookmarklet_js.src = '//127.0.0.1:8000/static/js/bookmarklet';
    window.bookmarklet = true;

}
else{
    bookmarkletLaunch();
}
}) ();