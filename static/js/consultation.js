const note = document.getElementById('notes');
const doctorNotes = document.getElementById('doctor-notes');
note.addEventListener('click', event => {
  event.preventDefault();
  if (note.innerHTML === 'Show Notes') {
    doctorNotes.style.display = 'block';
    note.innerHTML = 'Hide Notes';
  } else {
    doctorNotes.style.display = 'none';
    note.innerHTML = 'Show Notes';
  }
});

