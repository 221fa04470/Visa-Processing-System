document.getElementById("applyNowBtn").addEventListener("click", function() {
    const form = document.getElementById("visaApplicationForm");
    if (form.style.display === "none" || form.style.display === "") {
        form.style.display = "block";  // Show the form
        document.getElementById("applyNowBtn").innerText = "Hide Form";
    } else {
        form.style.display = "none";   // Hide the form
        document.getElementById("applyNowBtn").innerText = "Apply Now";
    }
});
