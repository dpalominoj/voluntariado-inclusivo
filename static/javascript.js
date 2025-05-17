// Menú móvil
const btnPhone = document.getElementById('mobileMenuBtn');
const menuPhone = document.getElementById('mobileMenu');        
btnPhone.addEventListener('click', () => {
    menuPhone.classList.toggle('active');	
});

// Menú móvil (Cerrar al elegir menú)
const menuItems = mobileMenu.querySelectorAll('a, button');
  menuItems.forEach(item => {
    item.addEventListener('click', () => {
      mobileMenu.classList.remove('active');
    });
});

// Funcionalidad modo oscuro
let oscuro  = false;
function modoOscuro(){
	const body = document.body;
	const btnModo = document.getElementById('m-oscuro');
	const navbar = document.getElementById('navbar');
	const impacto = document.getElementsByClassName('impacto')[0] ;
	const testimcards = document.getElementsByClassName('test-card');
	const contentform = document.getElementsByClassName('cont_frm');
	
	if(oscuro){
		//modo claro
		body.style.backgroundColor = "#f8f9fa";
		body.style.color = "black";
		navbar.style.background = "white";
        btnModo.textContent = "🌙";
	}else{
		//modo oscuro
		body.style.backgroundColor = "black";
		body.style.color = "white";
		navbar.style.background = "black";
		impacto.style.color = "black";
		for(let card of testimcards){
			card.style.color = "black";
		}
		for(let frm of contentform){
			frm.style.color = "black";
		}
        btnModo.textContent = "🌞";
	}
	oscuro = !oscuro;
}

// Funcion Abrir Inicio de Sesión
function abrirLogin(){
	const formLogin = document.getElementById('signInModal');
	const formReg = document.getElementById('signUpModal');
	formLogin.style.display = "flex";
	formReg.style.display = "none";
}

// Funcion Abrir Registro
function abrirRegistro(){
	const formReg = document.getElementById('signUpModal');
	const formLogin = document.getElementById('signInModal');
	formReg.style.display = 'flex';
	formLogin.style.display = 'none';
}
// Cerrar Modal
function cerrarMod(){
	const formLogin = document.getElementById('signInModal');
	const formRegis = document.getElementById('signUpModal');
	formLogin.style.display = "none";
	formRegis.style.display = "none";
}

// Funcionalidad lista desplegable
const listaselect = document.getElementById('selDisc');
document.querySelector('.rpta').onchange = 
    () => listaselect.style.display = disc_si.checked ? 'inline-block' : 'none';

// Scroll con tecla espacio (bajar) y tecla shift+espacio (subir)
document.addEventListener('keydown', function(event) {
  if (event.code === 'Space') {
    event.preventDefault();
    const scrollAmount = event.shiftKey ? -window.innerHeight * 0.8 : window.innerHeight * 0.8;
    window.scrollBy({
      top: scrollAmount,
      behavior: 'smooth'
    });
  }
});
	
