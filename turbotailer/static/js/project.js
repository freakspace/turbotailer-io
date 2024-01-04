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

    /* // Get the modal
    var modal = document.getElementById("myModal");

    // Get the button that opens the modal
    var btn = document.getElementById("myBtn");

    // Get the <span> element that closes the modal
    var span = document.getElementsByClassName("close")[0];

    btn.addEventListener('click', function() {
        console.log("TESTER")
        modal.style.display = "block";
    });

    // When the user clicks on the button, open the modal
    btn.onclick = function() {
        console.log("TESTER")
        modal.style.display = "block";
    }

    // When the user clicks on <span> (x), close the modal
    span.onclick = function() {
        modal.style.display = "none";
    }

    // When the user clicks anywhere outside of the modal, close it
    window.onclick = function(event) {
        if (event.target == modal) {
            modal.style.display = "none";
        }
    }  */
});

class Modal {
    constructor(modalId, triggerButtonId, closeButtonClass) {
        this.modal = document.getElementById(modalId);
        this.triggerButton = document.getElementById(triggerButtonId);
        this.closeButton = document.querySelector(`.${closeButtonClass}`);
        this.isMandatory = false; // default behavior

        this.init();
    }

    init() {
        // Open modal event
        this.triggerButton.addEventListener('click', () => {
            this.open();
        });

        // Close modal event
        this.closeButton.addEventListener('click', () => {
            if (!this.isMandatory) {
                this.close();
            }
        });

        // Click outside to close
        window.addEventListener('click', (event) => {
            if (event.target === this.modal && !this.isMandatory) {
                this.close();
            }
        });
    }

    open() {
        this.modal.style.display = 'block';
    }

    close() {
        this.modal.style.display = 'none';
    }

    setMandatory(mandatory) {
        this.isMandatory = mandatory;
    }
}

const typicalModal = new Modal("myModal", "myBtn", "close");
