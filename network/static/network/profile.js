document.addEventListener('DOMContentLoaded', function() {

    console.log("hello")
    //get the current profile
    const name = document.getElementById("btn-follow").value;
    // By current User
    const cuser = document.getElementById("currentUser").value;
    // current user
    profile(name, cuser);
})

function profile(name, cuser) {
    console.log(cuser)
    console.log(name)
    fetch(`/profileapi/${name}`)
    .then(response => response.json())
    .then(profiles => {
        // Print emails
        console.log(profiles);
    
        // ... do something else with emails ...
    });
    

}

