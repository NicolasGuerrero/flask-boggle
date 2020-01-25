$(function() {
  let currentScore = 0;

  let timer = $('#timer').text();
  timeInterval = setInterval(updateTimer, 1000);
  
  $('#user-input').on("submit", async function(e) {
    e.preventDefault();
    const testWord = $('#test-word').val();
    const result = await checkWord(testWord);
    const feedback = interpretResponse(result, testWord);
    $('#response').text(feedback);
    $('#test-word').val('');
  })
  
  async function checkWord(word) {
    const response = await axios.post(`/test-word`, { word });
    const result = response.data.result;
    return result;
  }

  function interpretResponse(response, word){
    if (response === 'ok'){
      feedback = `Added: ${word}`;
      updateScore(word);
    } else if(response === "not-on-board"){
      feedback = `${word} is not a valid word on board`;
    } else if (response === "not-word") {
      feedback = `${word} is not a valid english word`;
    }
    return feedback;
  }

  function updateScore(validWord){
    currentScore += validWord.length;
    $('#score').text(currentScore);
  }

  function updateTimer(){
    timer--;
    $('#timer').text(timer);
    
    if(timer === 0){
      sendScore();
      $('#user-input').remove();
      clearInterval(timeInterval);
    }
  }

  async function sendScore(){
    const response = await axios.post(`/add-score`, { score: currentScore });
    console.log("High Score: ", response.data.highScore);
    console.log("Attempts: ", response.data.attempts);
  }
})
