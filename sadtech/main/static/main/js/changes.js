function changeSelectValue(value) {
    let selectElement = document.getElementById("id_delivery_method");
    let selectText = document.getElementById("method");

    const met  = document.querySelector('.dev_met');
    const btns = document.querySelectorAll('.btn');
    met.addEventListener('click', e => {
        btns.forEach(btn => {
        if(btn.getAttribute('id') === e.target.getAttribute('id'))
            btn.classList.add('active');
        else
            btn.classList.remove('active');
        });
    });

    // изменяем выбранное значение
    selectElement.value = value;
    selectText.value = value;
}