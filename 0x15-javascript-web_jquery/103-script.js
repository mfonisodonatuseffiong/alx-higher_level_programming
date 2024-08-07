$(document).ready(function() {
    // Function to fetch and display the translation
    function fetchHello() {
        const languageCode = $('#language_code').val();
        
        // Fetch the translation from the API
        $.getJSON(`https://www.fourtonfish.com/hellosalut/hello/?lang=${languageCode}`, function(data) {
            $('#hello').text(data.hello);
        }).fail(function() {
            $('#hello').text('Error: Unable to fetch translation.');
        });
    }

    // Handle button click event
    $('#btn_translate').click(function() {
        fetchHello();
    });

    // Handle ENTER key press event in the input field
    $('#language_code').keypress(function(event) {
        if (event.which === 13) { // ENTER key code
            fetchHello();
        }
    });
});
