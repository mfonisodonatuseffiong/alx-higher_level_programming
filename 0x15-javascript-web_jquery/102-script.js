$(document).ready(function() {
    // Handle button click event
    $('#btn_translate').click(function() {
        // Get the value from the input field
        const languageCode = $('#language_code').val();
        
        // Fetch the translation from the API
        $.getJSON(`https://www.fourtonfish.com/hellosalut/hello/?lang=${languageCode}`, function(data) {
            // Update the content of the #hello div with the translation
            $('#hello').text(data.hello);
        }).fail(function() {
            // Handle errors (e.g., invalid language code)
            $('#hello').text('Error: Unable to fetch translation.');
        });
    });
});
