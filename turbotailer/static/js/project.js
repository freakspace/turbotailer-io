import '../sass/project.scss';

document.addEventListener('DOMContentLoaded', function() {
    // Open menu mobile
    var button = document.getElementById('dropdownButton');
    var dropdown = document.getElementById('dropdownMenu');

    button.addEventListener('click', function() {
        var isHidden = dropdown.hasAttribute('hidden');
        if (isHidden) {
            dropdown.removeAttribute('hidden');
        } else {
            dropdown.setAttribute('hidden', '');
        }
    });
});
