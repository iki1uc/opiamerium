document.getElementById('btnSound').addEventListener('click', toggleSound);
document.addEventListener('keydown', (e) => {
  if (e.key === 's' || e.key === 'S') toggleSound();
});
