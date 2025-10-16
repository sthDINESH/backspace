
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


