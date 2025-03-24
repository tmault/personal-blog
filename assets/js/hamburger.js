var body = document.querySelector('body');
var menuTrigger = document.querySelector('#menu-trigger');
var menuContainer = document.querySelector('#menu-container');
var hamburgerIcon = document.querySelector('.hamburger');

if (menuTrigger !== null) {
  menuTrigger.addEventListener('click', function(e) {
    menuContainer.classList.toggle('hidden');
    menuContainer.classList.toggle('flex');
    hamburgerIcon.classList.toggle('is-active');
    body.classList.toggle('lock-scroll');
  });
}
