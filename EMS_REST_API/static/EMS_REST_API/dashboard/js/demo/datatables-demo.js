// Call the dataTables jQuery plugin
$(document).ready(function() {
  $('#dataTable').DataTable({
            responsive: true,
        });
});


$(document).ready(function() {
  $('#dataTable-salary').DataTable({
        responsive: true,
        "order": [ 14, "desc" ],
    } );
});

$(document).ready(function() {
  $('#dataTable-salary-all').DataTable({
        responsive: true,
        "order": [ 16, "desc" ],
    } );
});

$(document).ready(function() {
  $('#dataTable-attendance').DataTable({
        responsive: true,
        "order": [ 2, "desc" ],
    } );
});

$(document).ready(function() {
  $('#dataTable-attendance-all').DataTable({
        responsive: true,
        "order": [ 4, "desc" ],
    } );
});