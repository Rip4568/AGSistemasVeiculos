async function renderUpdateForm(registroId) {
  try {
    const response = await fetch(`/render_form_update/${registroId}/`);
    const html = await response.text();

    // Encontre o elemento do modal e substitua o conteúdo interno
    const editModal = document.getElementById(`edit_modal`);
    const contentForm = editModal.querySelector('.content-form');
    contentForm.innerHTML = html;

    // Exiba o modal
    editModal.show();
  } catch (error) {
    console.log('Erro ao renderizar o formulário de atualização:', error);
  }
}

function addListnerFormSubmit() {
  const form = document.getElementById('filtrar-form');
  form.addEventListener('submit', (event) => {
    event.preventDefault();
    renderTableRegister(form);
  })
}

async function renderTableRegister(form) {
  const data = Object.fromEntries(new FormData(form));
  console.log(data);
  const response = await fetch('/render_table_list/', {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
      'X-CSRFToken': getCookie('csrftoken')
    },
    body: JSON.stringify({data})
  });
  const html = await response.text();
  const tableListControle = document.getElementById('table-list-controle');
  tableListControle.innerHTML = html;
}

function getCookie(cookieName) {
  const name = cookieName + "=";
  const decodedCookie = decodeURIComponent(document.cookie);
  const cookieArray = decodedCookie.split(';');
  for(let i = 0; i < cookieArray.length; i++) {
      let cookie = cookieArray[i];
      while (cookie.charAt(0) === ' ') {
          cookie = cookie.substring(1);
      }
      if (cookie.indexOf(name) === 0) {
          return cookie.substring(name.length, cookie.length);
      }
  }
  return "";
}

function getCookieSimple(cookieName='csrftoken') {
  window.document.cookie.split(';').forEach((cookie) => {
    if (cookie.includes(cookieName)) {
      return cookie.split('=')[1];
    }
  });
}
addListnerFormSubmit()