function getRadioValue(){
    let posi_nega = document.getElementsByName('posi_nega');
    let max_len = posi_nega.length;
    let checkValue = '';
  
    for (let i = 0; i < max_len; i++){
      if (posi_nega.item(i).checked){
        checkValue = posi_nega.item(i).value;
      }
    }
    return checkValue;
  }
let btnA = document.getElementById('btnA');
let btnB = document.getElementById('btnB');
let btnC = document.getElementById('btnC');

btnA.addEventListener('click', () => {
    let radio_value = getRadioValue();
    let resultA = document.querySelector('input[name="resultA"]');
    resultA.value = parseInt(resultA.value) + 1 * parseInt(radio_value);
    let resultTotal = document.querySelector('input[name="resultTotal"]');
    resultTotal.value = parseInt(resultTotal.value) + 1 * parseInt(radio_value);
});

btnB.addEventListener('click', () => {
    let radio_value = getRadioValue();
    let resultB = document.querySelector('input[name="resultB"]');
    resultB.value = parseInt(resultB.value) + 1 * parseInt(radio_value);
    let resultTotal = document.querySelector('input[name="resultTotal"]');
    resultTotal.value = parseInt(resultTotal.value) + 2 * parseInt(radio_value);
});

btnC.addEventListener('click', () => {
    let radio_value = getRadioValue();
    let resultC = document.querySelector('input[name="resultC"]');
    resultC.value = parseInt(resultC.value) + 1 * parseInt(radio_value);
    let resultTotal = document.querySelector('input[name="resultTotal"]');
    resultTotal.value = parseInt(resultTotal.value) + 3 * parseInt(radio_value);
});