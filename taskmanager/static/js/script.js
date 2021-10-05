// from Materialize
  document.addEventListener('DOMContentLoaded', function() {
    // for mobile sidenav
    let sidenav = document.querySelectorAll('.sidenav');
    // for modal to confirm deletion of category
    let modal = document.querySelectorAll('.modal');
    // initialise them
    M.Sidenav.init(sidenav);
    M.Modal.init(modal);
  });