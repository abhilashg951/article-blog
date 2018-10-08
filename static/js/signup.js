$(document).ready(function(){
$('#edit_article').hide();
});

function signup(){
first_name = document.getElementById('first_name').value
last_name = document.getElementById('last_name').value
phone_no = document.getElementById('phone_no').value
dob = document.getElementById('dob').value
email = document.getElementById('email').value
password = document.getElementById('password').value
confirm_password = document.getElementById('confirm_password').value

if (password != confirm_password){

alert("Password Not Match")
return false;
}

$.ajax({
url: '/signup_post/',
type: 'POST',
data: {'first_name': first_name, 'last_name': last_name, 'phone_no': phone_no, 'dob': dob, 'email': email, 'password': password},
success:function(req){
if(req.success === true){
window.location.href = '/login_get/';
}
else{
window.location.href = '/signup_get/';
}
}
});
}

function login(){
$('.container-main-text').html('');
email = document.getElementById('email').value
password = document.getElementById('password').value

$.ajax({
url: '/login/',
type: 'POST',
data: {'email': email, 'password': password},
success:function(req){
if(req.success === true){
if(req.email == ''){
var html1 = '<a class="right signup-next" href="/signup_get/">&nbsp Register</a><a class=" right" href="/login_get/">Login / </a>';
}
else{
var html1 = '<a class=" right" href="/logout_get/">Logout / </a>';
}
$('.container-main-text').append(html1);
window.location.href = '/article_dashboard/';
}
else{
window.location.href = '/login_get/';
}
}
});
}

function add_article(){
var formdata = new FormData();
name = document.getElementById('article_name').value;
alert(name);
description = document.getElementById('article_desc').value;
category = document.getElementById('category').value;
tag = document.getElementById('tag').value;
img = document.getElementById('img').files[0];
formdata.append('name',name);
formdata.append('description', description);
formdata.append('category', category);
formdata.append('tag', tag);
formdata.append('img', img);
jQuery.ajax({
url:'/add_article_post/',
type:'POST',
processData:false,
contentType:false,
data: formdata,
success:function(req){
if(req.success === true){
window.location.href = '/article_dashboard/';
}
}
});
}

function del_article(id)
{
$.ajax({
url:'/del_article/',
type:'POST',
data:{'id':id},
success:function(req){
alert('Your id has been deleted');
window.location.href = '/article_dashboard/';
}
});
}

function edit_article(id)
{
$.ajax({
url:'/edit_article_get/',
type:'GET',
data:{'id':id},
success:function(req){
$('#main-div').hide();
$('#edit_article').show();
$('#edit_article').html('');
//window.location.href = '/Edit_article/';
console.log(req.data.article_name);
//$('#article_name').val(req.data.article_name);
//$('#article_desc').val(req.data.article_desc);
//$('#category').val(req.data.category);
//$('#tag').val(req.data.tag);
var id = req.data.id;
var html = '<h4>Edit the Article</h4>'+
'<input type="text" value="'+ req.data.article_name +'" id="article_name" placeholder="Name">'+
    '<input type="text" value="'+ req.data.article_desc +'" id="article_desc" placeholder="Description">'+
    '<input type="text" value="'+ req.data.category +'" id="category" placeholder="Category">'+
    '<input type="text" value="'+ req.data.tag +'" id="tag" placeholder="Title">'+
//    <input type="file" value="" id="img">'
    '<input type="submit" value="Submit" onclick="add_article_post('+ id +')"/>';
    $('#edit_article').append(html);
}
});
}

function add_article_post(id)
{
var formdata = new FormData();
name = document.getElementById('article_name').value;
description = document.getElementById('article_desc').value;
category = document.getElementById('category').value;
tag = document.getElementById('tag').value;
//img = document.getElementById('img').files[0];
formdata.append('name',name);
formdata.append('description', description);
formdata.append('category', category);
formdata.append('tag', tag);
formdata.append('id', id);
//formdata.append('img', img);
jQuery.ajax({
url:'/edit_article_get/',
type:'POST',
processData:false,
contentType:false,
data: formdata,
success:function(req){
if(req.success === true){
window.location.href = '/article_dashboard/';
}
}
});
}