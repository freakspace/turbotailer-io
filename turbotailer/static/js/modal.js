export class Modal {
    constructor(modalId, triggerButtonId, closeButtonClass) {
        this.modal = document.getElementById(modalId);
        this.triggerButton = document.getElementById(triggerButtonId);
        this.closeButton = document.querySelector(`.${closeButtonClass}`);
        this.isMandatory = false;
        this.init();
    }
    init() {

        // Open modal event
        if(this.triggerButton){
            this.triggerButton.addEventListener('click', () => {
                this.open();
            });
        }
        if(this.closeButton){
            // Close modal event
            this.closeButton.addEventListener('click', () => {
                if (!this.isMandatory) {
                    this.close();
                }
            });
        }

        // Click outside to close
        window.addEventListener('click', (event) => {
            if (event.target === this.modal && !this.isMandatory) {
                this.close();
            }
        });
    }

    open() {
        this.modal.style.display = 'block';
        document.body.classList.add('overflow-hidden');
    }

    close() {
        this.modal.style.display = 'none';
        document.body.classList.remove('overflow-hidden');
    }

    setMandatory(mandatory) {
        this.isMandatory = mandatory;
    }
}
