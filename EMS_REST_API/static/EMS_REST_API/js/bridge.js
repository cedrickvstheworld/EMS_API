// $(document).on('submit', '#updatethis', function (e) {
//         e.preventDefault();
//         $.ajax({
//                 xhrFields: {
//                     withCredentials: true
//                 },
//                 headers: {
//                     'Authorization': 'Basic ' + btoa('cedrick:longview048')
//                 },
//             type: 'POST',
//             url: '/updateEmployee/',
//             dataType: 'json',
//             data:{
//                 first_name: $('#first_name').val(),
//                 middle_name: $('#middle_name').val(),
//                 last_name: $('#last_name').val(),
//                 csrfmiddlewaretoken: $('input[name=csrfmiddlewaretoken]').val()
//             },
//             success: function () {
//                 $('#employeeUpdate').load(' #employeeUpdate')
//             }
//
//             });
//
//     });

    //
    // $(document).on('submit', '#updateEmployee', function (e) {
    //     e.preventDefault();
    //     $.ajax({
    //
    //         type: 'POST',
    //         url: '/emswebext/employeeUpdate/',
    //         data:{
    //             emp_id: $('#email').val(),
    //             first_name: $('#first_name').val(),
    //             middle_name: $('#middle_name').val(),
    //             last_name: $('#last_name').val(),
    //             position: $('#position').val(),
    //             status: $('#status').val(),
    //             address: $('#address').val(),
    //             birthday: $('#birthday').val(),
    //             csrfmiddlewaretoken: $('input[name=csrfmiddlewaretoken]').val()
    //         },
    //         success: function () {
    //             $('#profilediv').load(' #profilediv')
    //         }
    //
    //         });
    //
    // });
    //
