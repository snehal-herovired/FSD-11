// // What is api ?
// // what is http requests?
// // types of requests : get, post, put, delete
// // what is postman?
// // what is JSON?
// // Monolithic and microservices ?
// //use or benefit of async code in http request?
// // what is client and server?

// //client ===frontend 
// //server==backend

// // Requests ==> client : give me on info iphone
// // Server => has a port(ear)=>reponse=>to client ;
// // http://localhost:5000 ;
// // 

// // JSON : js  object notation : data intermedieary : 
// // Object : JSON ()
// // 
// let obj={
//     name:"Snehal",
//     age:24
// }

// // JS object JSON or string format : 


// // localstorage.setitems('obj',"value")
// //localstorage.getitems('obj')
// //localstorage.deleteitems

// //[object object]

// const JSONobj =JSON.stringify(obj);
// localStorage.setItem('info',JSONobj);

// const datafromLocal =localStorage.getItem('info');

// const validJSObj =JSON.parse(datafromLocal);
// console.log(validJSObj,"data from localstorage");
// validJSObj.address ="Gurugram";
// console.log(validJSObj,"data manipulation");


// How to make get and post req using ajax, xhr
// basic understaning of async .

//Es6 : promises and async -await : Fetch API;

//Blocking code : sycnhronous code ,

// hi
// 123
// 12345 : 3 min executed : non-blocking code :asycnhronous code ;
//end

// JS : single-threaded and sychrnous code ;

//  Frontend : scroll :(event):-> function call : it is asking server amazon
//  to share the product data : DOM tree population;

// Web worker API;-> handling the asychronous code;

// Asychrnous code : Callbacks and Promises ;

// domelement.addeventlisterner('click',function(){

// })

//  Function in Javascript are Special : they are treated as first class 
// citizen and first class object in js.

// functions in js, they can be stored in variables ,or they can be passed as an
// argument to another function or they can returned from a function.


// sychronous callback ;
//asychrnous callback :we need help setTimeout () method.
console.log("start");

function parent(a,b,callback){
    setTimeout(()=>{
        // main logic block
        callback(a,b)
    },0)
}

 parent(2,3,child)
//  console.log(returnedvalue);

function child(a,b){
    let c= a+b;
    console.log("value of child function",c)

}

console.log("end");

// 