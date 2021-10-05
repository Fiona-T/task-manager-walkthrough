// from Materialize
  document.addEventListener('DOMContentLoaded', function() {
    // mobile sidenav
    let sidenav = document.querySelectorAll('.sidenav');
    // initialization
    M.Sidenav.init(sidenav);
    // for modal to confirm deletion of category
    let modal = document.querySelectorAll('.modal');
    // initialization
    M.Modal.init(modal);
    // datepicker on add task form
    let datepicker = document.querySelectorAll('.datepicker');
    // initialization - options: date format, text on done btn
    M.Datepicker.init(datepicker, {
      format: "dd mmmm, yyyy",
      i18n: {done: "Select"}
    });
    // dropdown list (select element) on add task form
    let selects = document.querySelectorAll('select');
    // initialization
    M.FormSelect.init(selects);

  });