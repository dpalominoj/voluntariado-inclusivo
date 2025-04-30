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
        btnModo.textContent = "🌞";
	}
	oscuro = !oscuro;
}

/* --Var Botones y Modal
const btnLogin = document.getElementById('signInBtn');
const btnRegis = document.getElementById('signUpBtn');
const formLogin = document.getElementById('signInModal');
const formRegis = document.getElementById('signUpModal');

// Abrir Modal Login/Registro
btnLogin.onclick = function(){
	formLogin.style.display = "flex";
}
btnRegis.onclick = function(){
	formRegis.style.display = "flex";
}*/

// Funcion Abrir Inicio de Sesión
function abrirLogin(){
	const formLogin = document.getElementById('signInModal');
	formLogin.style.display = "flex";
}

// Funcion Abrir Registro
function abrirRegistro(){
	const formReg = document.getElementById('signUpModal');
	formReg.style.display = 'flex';
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
	