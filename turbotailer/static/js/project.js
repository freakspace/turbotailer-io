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


document.addEventListener('DOMContentLoaded', () => {
    const navItems = document.querySelectorAll('.nav-item');

    // Scroll to section on nav item click
    navItems.forEach(item => {
        item.addEventListener('click', () => {
            const targetId = item.getAttribute('data-target');
            const targetSection = document.getElementById(targetId);
            targetSection.scrollIntoView({ behavior: 'smooth', block: 'start' });
        });
    });

    // Change nav item appearance on scroll
    window.addEventListener('scroll', () => {
        let currentSection = '';
        document.querySelectorAll('.priceplan').forEach(section => {
            const sectionTop = section.offsetTop;
            if (window.scrollY >= sectionTop - 50) {
                currentSection = section.getAttribute('id');
            }
        });
        navItems.forEach(item => {
            // Remove multiple classes
            item.classList.remove('border', 'bg-white', 'rounded-xl', 'shadow-lg');

            // Check if the item's data-target matches the current section
            if (item.getAttribute('data-target') === currentSection) {
                // Add multiple classes
                item.classList.add('border', 'bg-white', 'rounded-xl', 'shadow-lg');
            }
        });

    });
});
