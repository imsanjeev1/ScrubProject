$(document).on('submit','#post-file',function(e) {
    e.preventDefault();
    $.ajax({
            type: "POST",
            data: {data_file: $('#file_id').get(0).files[0].name,csrfmiddlewaretoken:$('input[name=csrfmiddlewaretoken]').val()},
            // data: content,
            url: '/file_upload',
            success: function (response) {
                if (response == true) {
                    console('true');
                    //window.location.href="/home/sanjeeev/templates/home.html"
                    // location.href = '/index.html';
                }
                else {
                    alert('Error Occur');
                }
                //window.console.log(response);
            }, error: function (xhr, status, err) {
                console.log(status, err);
            }
        });
})
//
// function file_upload() {
//     console.log("create post is working!") // sanity check
//     var file_get = $('#file_id').val();
//     console.log("File_Value",file_get);
//     $.ajax({
//         url : "hma/portal/register1/", // the endpoint
//         type : "POST", // http method
//         data : { the_post : $('#post-text').val() }, // data sent with the post request
//
//         // handle a successful response
//         success : function(json) {
//             $('#post-text').val(''); // remove the value from the input
//             console.log(json); // log the returned json to the console
//             console.log("success"); // another sanity check
//         },
//
//         // handle a non-successful response
//         error : function(xhr,errmsg,err) {
//             $('#results').html("<div class='alert-box alert radius' data-alert>Oops! We have encountered an error: "+errmsg+
//                 " <a href='#' class='close'>&times;</a></div>"); // add the error to the dom
//             console.log(xhr.status + ": " + xhr.responseText); // provide a bit more info about the error to the console
//         }
//     });
// };