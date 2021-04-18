  document.addEventListener('DOMContentLoaded', function() {
    var elems = document.querySelectorAll('.sidenav');
    var options = {
      menuWidth: 300, // Default is 300
      edge: 'left', // Choose the horizontal origin
      closeOnClick: false, // Closes side-nav on <a> clicks, useful for Angular/Meteor
      draggable: true // Choose whether you can drag to open on touch screens
    }
    var instances = M.Sidenav.init(elems, options);

    var tab_elems = document.querySelectorAll('.tabs');
    var tab_options = {
        duration: 300,
        swipeable: false,
    }
    var tab_instances = M.Tabs.init(tab_elems, tab_options);
  });