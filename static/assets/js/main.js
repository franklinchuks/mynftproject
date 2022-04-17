// Changing Image

document.getElementById('id_image_group').onclick = function (event) {
    document.getElementById('id_image_file').click();
};
function readURL(input) {
    var reader = new FileReader();
    reader.onload = function (e) {
        $('#id_mage_display').attr('src', e.target.result)
    };
    reader.readAsDataURL(input.files[0]);
}