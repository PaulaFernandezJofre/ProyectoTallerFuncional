document.addEventListener('DOMContentLoaded', function() {
  var audioPlayer = document.getElementById('audioPlayer');

  // Enfocar el reproductor de audio al presionar Shift + Tab al inicio de la página
  document.addEventListener('keydown', function(event) {
    if (event.shiftKey && event.key === 'Tab') { // Verificar Shift + Tab usando event.key
      event.preventDefault(); // Prevenir el comportamiento predeterminado
      audioPlayer.focus(); // Enfocar el reproductor de audio
    }
  });
});


  
