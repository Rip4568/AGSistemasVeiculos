function renderUpdateForm(registroId) {
  fetch(`/controle/update/${registroId}/`)
    .then(response => response.text())
    .then(html => {
      // Encontre o elemento do modal e substitua o conteúdo interno
      const editModal = document.getElementById(`edit_modal_${registroId}`);
      editModal.innerHTML = html;

      // Exiba o modal
      editModal.showModal();
    })
    .catch(error => {
      console.error('Erro ao renderizar o formulário de atualização:', error);
    });
}