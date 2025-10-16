document.addEventListener("DOMContentLoaded", function () {
    console.log("Hello from JS");

    function openBookingModal(tableId) {
      currentTableId = tableId;
      modalTitle.textContent = `Reserve Table ${tableId}`;
      vendorNameInput.value = '';
      vendorContactInput.value = '';
      modalMsg.style.display = 'none';
      modalBackdrop.style.display = 'flex';
      vendorNameInput.focus();
    }

    const bookingModalEl = document.querySelector("#booking-modal");
    let bookingModal = null;
    if(bookingModalEl){
        bookingModal = new bootstrap.Modal(bookingModalEl);
    }

    const cancelModalEl = document.querySelector("#cancel-modal");
    let cancelModal = null;
    if(cancelModalEl){
        cancelModal = new bootstrap.Modal(cancelModalEl);
    }
    
    
    document.querySelectorAll('.workspace').forEach(el => {
      el.addEventListener('click', (e) => {
        const workspaceId = el.getAttribute('data-workspace-id');
        const workspaceTitle=el.id;

        if(!el.classList.contains("reserved") && bookingModal){
            bookingModalEl.querySelector(".modal-title").innerText=`Reserve ${workspaceTitle}?`;
            bookingModalEl.querySelector(".workspace-details").innerText=`Need to populate details for ${workspaceTitle}`;
            // Set data-workspace-id on the form
            const bookingForm = bookingModalEl.querySelector('form[data-type="new-booking"]');
            if (bookingForm) {
                bookingForm.setAttribute('data-workspace-id', workspaceId);

                // Get values from check-bookings form
                const checkForm = document.querySelector('#check-bookings form');
                const date = checkForm.querySelector('[name="date"]').value;
                const startTime = checkForm.querySelector('[name="start_time"]').value;
                const endTime = checkForm.querySelector('[name="end_time"]').value;

                // Set values in booking modal form
                bookingForm.querySelector('[name="workspace"]').value = workspaceId;
                bookingForm.querySelector('[name="booking_date"]').value = date;
                bookingForm.querySelector('[name="start_time"]').value = startTime;
                bookingForm.querySelector('[name="end_time"]').value = endTime;
            }
            bookingModal.show();
        } else if(el.classList.contains("editable") && cancelModal){
          cancelModalEl.querySelector(".modal-title").innerText=`Cancel booking?`;
          const bookingId = el.getAttribute("data-booking-id");
          const cancelForm = cancelModalEl.querySelector('form[data-type="cancel-booking"]');
          if (cancelForm && bookingId) {
              cancelForm.setAttribute('action', `/booking/${bookingId}/cancel`);
          }
          cancelModal.show();
        }
        console.log("Clicked");
      });
    });
});
