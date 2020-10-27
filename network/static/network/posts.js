document.addEventListener('DOMContentLoaded', function() {
    // Use buttons to toggle between views
    // document.querySelector('#edit').addEventListener('click', () => edit(user,postId));

    
    // document.querySelector('#edit').addEventListener('click', () => load_mailbox('inbox'));
    
    console.log("hello")
    // By default, follow btn
    
})

function edit(postId) {
   

    
    console.log(postId)
   
//select the post
//get input
post = document.getElementById(`${postId}`);
console.log(post)
//get edit btn
const editBtn = document.querySelector('#edit');


//select p content
const content = post.querySelector("#content");
//save the value
let postValue = content.textContent;
//create textarea element 
let input = document.createElement("TEXTAREA");
// create btn
let btn = document.createElement("button");
//add precend value to the input
input.textContent = postValue;
input.class = "btn btn-success btn-rounded text-white text-uppercase font-14";
input.id = "write-content";
input.rows = "6";
input.cols="30";
input.placeholder ="content";
//btn config
btn.id="save"
btn.type="submit"
btn.innerHTML="save";
btn.className='btn btn-success btn-rounded text-white text-uppercase font-14';

btn.addEventListener('click', function() {




    console.log(`post to save:${postId}`)
    console.log(`content:${postId}`)
    save(postId)
  });

post.appendChild(input); //appendChild
post.appendChild(btn); //appendChild
// content.remove();
// editBtn.remove();
// Hide content and edit BTN
content.style.display = 'none';
editBtn.style.display = 'none';



console.log(postValue)
}


function save(postId) {
    //let content = document.getElementById(`write-content`).value;
     //clean post dom 
    const post = document.getElementById(`${postId}`);
    
    content.innerHTML = '';
    content = post.querySelector(`#write-content`).value;
    console.log(`post to save${postId}`)
    console.log(`content to save : ${content}`)

    

    fetch(`/postapi/${postId}`, {
            method: 'PUT',
            body: JSON.stringify({
            content: content
            })
        })
        //update DOM
        post.querySelector("#content").textContent = content;
        
        
        
        //hide edit
        
        post.querySelector(`#write-content`).style.display = 'none';
        post.querySelector("#save").style.display = 'none';
        
        //show p content and btn view
        post.querySelector("#content").style.display = 'block';
        post.querySelector('#edit').style.display = 'block';
        
       
        

     return true;

}

function like(postId, user) {
   
    const post = document.getElementById(`${postId}`);
    let likeBtn = post.querySelector(`#like`);
    
    //GET THE ACTUAL USER
    console.log(`post to like : ${postId}`)
    console.log(`user to add or remove : ${user}`)
    
    // first update list
    fetch(`/postapi/${postId}`, {
        method: 'PUT',
        body: JSON.stringify({
        user: user
        })
    })
    
    
    // fetch Async to wait for the updated response
    
    async function fetchlikesJSON() {
        const response = await fetch(`/postapi/${postId}`);
        const post = await response.json();  return post;
      }
      
      fetchlikesJSON().then( post => {
        likeCount = likeBtn.querySelector('#likecount');

       likeCount.innerHTML = post.likes;
        // Print emails
        console.log(post.likes);
        // ... do something else with emails ...
        
      });

  
    
    
    


       
    
        
    
        //update DOM
        //post.querySelector("#content").textContent = content;
        
        //show p content and btn view
        // post.querySelector("#content").style.display = 'block';
        // post.querySelector('#edit').style.display = 'block';
        
       
        

     return true;

}
function thumb(x) {
    x.classList.toggle("fa-thumbs-down");
  } 
