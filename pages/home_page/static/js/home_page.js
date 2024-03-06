// Block out dates before the current date
const today = new Date();
const minDay = today.toISOString().split("T")[0];

document.getElementById('date').setAttribute('min', minDay);

//check endTime does not proceed startTime
const startTimeInput = document.getElementById("startTime");
const endTimeInput = document.getElementById("endTime");

startTimeInput.addEventListener("change", function () {
    const startTime = startTimeInput.value;

    if (this.value) {
        endTimeInput.removeAttribute('disabled');
        endTimeInput.setAttribute('min', `${startTime}:00`);
    }
});

endTimeInput.addEventListener("change", function () {
    const startTime = startTimeInput.value;
    const endTime = this.value;

    if (startTime > endTime) {
        alert("End time cannot be before start time.");
        this.value = startTime;
    }
});
// document.getElementById("movieForm").addEventListener("submit", function (event) {
//     event.preventDefault();
//
//     const formData = new FormData(event.target);
//     const date = formData.get("date");
//     const movie = formData.get("movie");
//     const city = formData.get("city");
//     const startTime = formData.get("startTime");
//     const endTime = formData.get("endTime");
//
//     //validate all fields have been filled out
//     if (date === "" || movie === "" || city === "") {
//         alert("Please fill out all fields.");
//         return false;
//     }
//
//     console.log("Date:", date);
//     console.log("Movie:", movie);
//     console.log("City:", city);
//     console.log("Start Time:", startTime);
//     console.log("End Time:", endTime);
//
//     window.location.href = `movie_screenings.html?date=${date}&movie=${movie}&city=${city}&stateTime=${startTime}&endTime=${endTime}`;
//
// });
