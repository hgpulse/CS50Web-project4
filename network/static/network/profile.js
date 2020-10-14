document.addEventListener('DOMContentLoaded', function() {

    console.log("hello")

     //get the current profile
     const name = document.getElementById("profile").value;
     // By current User
     const cuser = document.getElementById("currentUser").value;

    setbtn(name, cuser);
   
})

function setbtn(name, cuser){
    //select the div
    const app = document.querySelector(`#follow-view`);
    
    // add follow btn object
    var followBtn = document.createElement('button');
    followBtn.innerHTML = "Follow";
    followBtn.id = 'followBtn';
    followBtn.className='btn btn-success btn-rounded text-white text-uppercase font-14';

    followBtn.addEventListener('click', function() {
        profile(name, cuser)
      });

    app.appendChild(followBtn)
    
}

function profile(name, cuser) {
    console.log(cuser)
    console.log(name)
    fetch(`/profileapi/${name}`)
    .then(response => response.json())
    .then(profiles => {
        // Print profile
        console.log(profiles);
    
        // ... do something else with profile ...
    });

    fetch(`/profileapi/${name}`, {
        method: 'PUT',
        body: JSON.stringify({
            follow: cuser
        })
      })
      return true;
    
    

}

