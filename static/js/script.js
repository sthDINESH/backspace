
document.addEventListener("DOMContentLoaded", function () {
    console.log("Hello from JS");
});

// ===============================
// JS FOR MY BOOKINGS PAGE TEMPLATE 
// ===============================

/* Modal handling for editing bookings */
function openEditModal(bookingId) {
    fetch(`/booking/${bookingId}/edit-form/`)
        .then(response => response.text())
        .then(html => {
            document.getElementById('editBookingBody').innerHTML = html;
            document.getElementById('editBookingModal').style.display = 'block';
            document.getElementById('editBookingForm').onsubmit = function(e) {
                e.preventDefault();
                let formData = new FormData(this);
                fetch(`/booking/${bookingId}/update/`, {
                    method: 'POST',
                    body: formData,
                    headers: {'X-CSRFToken': formData.get('csrfmiddlewaretoken')}
                })
                .then(response => response.json())
                .then(data => {
                    if (data.success) {
                        alert('Booking updated!');
                        location.reload();
                    } else {
                        alert(data.message);
                    }
                });
            };
        });
}
/* close Edit Booking Modal */
function closeEditModal() {
    document.getElementById('editBookingModal').style.display = 'none';
}
/* Cancel Booking Function */
function cancelBooking(bookingId) {
    if (confirm('Are you sure you want to delete this booking?')) {
        fetch(`/booking/${bookingId}/cancel/`, {method: 'POST'})
            .then(response => response.json())
            .then(data => {
                if (data.success) {
                    alert('Booking cancelled!');
                    location.reload();
                } else {
                    alert(data.message);
                }
            });
    }
}


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
      el.addEventListener('click', async (e) => {
        const workspaceId = el.getAttribute('data-workspace-id');
        const workspaceTitle=el.id;

        if(!el.classList.contains("reserved") && bookingModal){
            bookingModalEl.querySelector(".modal-title").innerText=`Reserve ${workspaceTitle}?`;
            // Set data-workspace-id on the form
            const bookingForm = bookingModalEl.querySelector('form[data-type="new-booking"]');
            if (bookingForm) {
                bookingForm.setAttribute('data-workspace-id', workspaceId);

                // Get values from check-bookings form
                const checkForm = document.querySelector('#check-bookings form');
                const date = checkForm.querySelector('[name="date"]').value;
                const startTime = checkForm.querySelector('[name="start_time"]').value;
                const endTime = checkForm.querySelector('[name="end_time"]').value;

                // Fetch workspace details via AJAX
                let workspaceDetails = null;
                try {
                  const resp = await fetch(`/booking/workspace/${workspaceId}`);
                  const data = await resp.json();
                  if (data.success) {
                    // Display workspace details in modal
                    workspaceDetails = `
                      <div class='workspace'>
                        <h3><span>${data.workspace.name}</span></h3>
                        <p>Location: <span>${data.workspace.location}</span></p>
                        <p>Capacity: <span>${data.workspace.capacity}</span></p>
                        <p>Type: <span>${data.workspace.workspace_type}</span></p>
                        <p>Status: <span>${data.workspace.status}</span></p>
                        <p>Amenities: <span>${data.workspace.amenities.join(', ')}</span></p>
                        <p>Description: <span>${data.workspace.description}</span></p>
                      </div>
                    `;
                  } else {
                    workspaceDetails = "Workspace not found.";
                  }
                } catch (err) {
                  workspaceDetails = "Error loading workspace details.";
                }
                
                bookingModalEl.querySelector(".workspace-details").innerHTML=`
                  <div class='reservation-details'>
                    <h3> Reservation details: </h3>
                    <p>Date: <span>${date}</span></p>
                    <p>Time: <span>${startTime} - ${endTime}</span></p>
                  </div>
                  ${workspaceDetails}
                  `;

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
              // Fetch booking details via AJAX
              try {
                  const resp = await fetch(`/booking/booking/${bookingId}`);
                  const data = await resp.json();
                  if (data.success) {
                      cancelModalEl.querySelector(".booking-details").innerHTML = `
                        <div class='booking-details'>
                          <h3>Booking details:</h3>
                          <p>Workspace: <span>${data.booking.workspace_name}</span></p>
                          <p>Date: <span>${data.booking.booking_date}</span></p>
                          <p>Time: <span>${data.booking.start_time} - ${data.booking.end_time}</span></p>
                          <p>Status: <span>${data.booking.status}</span></p>
                          <p>Purpose: <span>${data.booking.purpose}</span></p>
                          <p>Notes: <span>${data.booking.notes}</span></p>
                        </div>
                      `;
                  } else {
                      cancelModalEl.querySelector(".booking-details").textContent = "Booking not found.";
                  }
              } catch (err) {
                  cancelModalEl.querySelector(".booking-details").textContent = "Error loading booking details.";
              }
          }
          cancelModal.show();
        }
        console.log("Clicked");
      });
    });
});
