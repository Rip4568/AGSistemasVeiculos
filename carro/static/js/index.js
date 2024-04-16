function getCookie(cookieName='csrftoken') {
  window.document.cookie.split(';').forEach((cookie) => {
    if (cookie.includes(cookieName)) {
      return cookie.split('=')[1];
    }
  });
}

async function renderFormToUpdate(veiculoId) {
  const modal = document.getElementById('edit_modal');
  modal.show()
  modal.querySelector('.content-form').innerHTML = 'Carregando...'
  const response = await fetch(`/render_form_update_car/${veiculoId}/`);
  modal.querySelector('.content-form').innerHTML = await response.text();
}

async function renderModalToDelete(veiculoId) {
  const modal = document.getElementById(`delete_modal`);
  modal.show()
  modal.querySelector('.content-form').innerHTML = 'Carregando...'
  const response = await fetch(`/render_form_delete_car/${veiculoId}/`);
  modal.querySelector('.content-form').innerHTML = await response.text();
}