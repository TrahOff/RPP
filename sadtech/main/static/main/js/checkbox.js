const masterCheckbox = document.getElementById('masterCheckbox');

// Получаем ссылки на все остальные checkbox
const checkboxes = document.querySelectorAll('input[type="checkbox"]');

// Назначаем обработчик события при изменении состояния главного checkbox
masterCheckbox.addEventListener('change', function() {
  // Проходимся по всем checkbox и устанавливаем их состояние в соответствии с состоянием главного checkbox
  checkboxes.forEach(function(checkbox) {
    checkbox.checked = masterCheckbox.checked;
  });
});