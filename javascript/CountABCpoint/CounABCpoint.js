// ラジオボタンの値取得処理
function getRadioValue(){
    // ラジオボタン要素取得
    let posi_nega = document.getElementsByName('posi_nega');
    // ラジオボタンの要素数取得
    let max_len = posi_nega.length;

    // 戻り値の初期値セット
    let checkValue = '';

    // ラジオボタンの要素数だけ繰り返し
    for (let i = 0; i < max_len; i++){
      // ラジオボタンが選択荒れていた場合
      if (posi_nega.item(i).checked){
        // valueの値を取得
        checkValue = posi_nega.item(i).value;
      }
    }
    // 戻り値：ラジオボタンのvalue値
    return checkValue;
  }

// ボタン要素の取得
let btnA = document.getElementById('btnA');
let btnB = document.getElementById('btnB');
let btnC = document.getElementById('btnC');

// [A]ボタン押下時の処理
btnA.addEventListener('click', () => {
  // ラジオボタンの値取得
  let radio_value = getRadioValue();

  // 出力用テキストから要素[A]を取得し、カウントを増減する
  let resultA = document.querySelector('input[name="resultA"]');
  resultA.value = parseInt(resultA.value) + 1 * parseInt(radio_value);

  // 出力用テキストから要素[Total]を取得し、計算・出力する
  let resultTotal = document.querySelector('input[name="resultTotal"]');
  resultTotal.value = parseInt(resultTotal.value) + 1 * parseInt(radio_value);
});

btnB.addEventListener('click', () => {
  // ラジオボタンの値取得
  let radio_value = getRadioValue();

  // 出力用テキストから要素[B]を取得し、カウントを増減する
  let resultB = document.querySelector('input[name="resultB"]');
  resultB.value = parseInt(resultB.value) + 1 * parseInt(radio_value);

  // 出力用テキストから要素[Total]を取得し、計算・出力する
  let resultTotal = document.querySelector('input[name="resultTotal"]');
  resultTotal.value = parseInt(resultTotal.value) + 2 * parseInt(radio_value);
});

btnC.addEventListener('click', () => {
  // ラジオボタンの値取得
  let radio_value = getRadioValue();

  // 出力用テキストから要素[B]を取得し、カウントを増減する
  let resultC = document.querySelector('input[name="resultC"]');
  resultC.value = parseInt(resultC.value) + 1 * parseInt(radio_value);

  // 出力用テキストから要素[Total]を取得し、計算・出力する
  let resultTotal = document.querySelector('input[name="resultTotal"]');
  resultTotal.value = parseInt(resultTotal.value) + 3 * parseInt(radio_value);
});