$(function() {
  $('#user-input').on("submit", async function(e) {
    e.preventDefault();
    const testWord = $('#test-word').val();
    await checkWord(testWord);
  })
  
  async function checkWord(word) {
    const response = await axios.post(`/test-word`, { word });
    console.log(response.data.response);
  }
})
