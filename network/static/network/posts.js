document.addEventListener('DOMContentLoaded', function() {
    // Use buttons to toggle between views
    // document.querySelector('#edit').addEventListener('click', () => edit(user,postId));

    
    // document.querySelector('#edit').addEventListener('click', () => load_mailbox('inbox'));
    
    console.log("hello")
    // By default, follow btn
    
})

function edit(user, postId) {
   
 
    console.log(user)
    console.log(postId)
   
//select the post
//get input
const post = document.getElementById(`${postId}`);
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
input.id = "inputlg";
input.rows = "6";
input.cols="30";
//btn config
btn.id="save"
btn.type="submit"
btn.innerHTML="save";
btn.className='btn btn-success btn-rounded text-white text-uppercase font-14';

post.appendChild(input); //appendChild
post.appendChild(btn); //appendChild
content.remove();
editBtn.remove();



console.log(postValue)
// in post change p element to textarea
// add save btn
// add onclick action with fetch -->PUT


//    let content = app.document.getElementById("content").value;

//    console.log(content)
  




}


