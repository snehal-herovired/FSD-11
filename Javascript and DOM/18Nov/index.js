// getElementbyId :element directly.
// getElementbyClassName
// const getdivs =document.getElementsByClassName('sample');
// console.log(getdivs);  htmlCollections []

//getElementsbyTagName;
// const getdivs =document.getElementsByTagName('div');
// console.log(getdivs);  HTMLCollections []


//querySelectors and querSelectorALL.

// let divwithId =document.querySelector('#sample');
// console.log(divwithId)
// let divwithClass =document.querySelector('.sample');
// console.log(divwithClass);

// let Alldivs =document.querySelectorAll('div');
// console.log(Alldivs);  NodeLists[]

// differnce btw NodeLists and HTMLCollections ? ********

// Events : onclick, onChange, onLoad, scroll, keypress, submit ;

//addEventListener('eventtype',function)

// Click event
let mydiv = document.querySelector(".sample");
let innerDivValue = 0;
let newBtn =document.createElement('button');
newBtn.textContent="increment counter";



mydiv.addEventListener('click', function () {
    // alert("your div has been clicked")
    // mydiv.style.color="red"
    mydiv.style.height = "200px"
    mydiv.style.width = "200px"
    // on click sample1 text should be replaced with herovired
    //    mydiv.innerText ="Herovired"
    mydiv.innerHTML = `<div id="redbox" style='background-color: red;height: 50px;width: 50px;'>
  ${innerDivValue}
  </div>
  
  
  <button id="btn">Increment</button>
  `
  const btn =document.getElementById('btn');
  console.log(btn);
  btn.addEventListener('click',function(){
    alert("btn is clicked")
    //update the counter logic
  })

  //we are going to attach the global btn we created , inside body;
  document.body.appendChild(newBtn)

  newBtn.addEventListener('click',function(){
    const redboxDiv =document.querySelector('#redbox');
    console.log(redboxDiv.innerText);
    redboxDiv.innerText =parseInt(redboxDiv.innerText) + 1;
   

   //updation of counter value;
})
}) 
// btn should be outside of whole blue box ;

//mouseover Event; hover effect
//mouseleave
// &&
//mouseenter
//mouseout

// let hoverme =document.querySelector(".hoverme");
// hoverme.addEventListener('mouseenter',function(){
//     hoverme.style.backgroundColor="lightpink"
//     hoverme.classList.add('hoverDiv')
//     //box shadow
// })

// hoverme.addEventListener("mouseout",function(){
//     hoverme.style.backgroundColor="blue"
//     hoverme.classList.remove('hoverDiv')
// })


// scroll 
// let Scroller =document.querySelector(".sroller");
// Scroller.addEventListener("scroll",function(){
//     console.log("i am scrolling here");
// })


// Change Event
const Vehicle =document.getElementById('vehicle');
Vehicle.addEventListener("change",function(event){
    console.log(event.target.name ,":",event.target.value)
})

// const input =document.querySelector("input");
// input.addEventListener('change',function(event){
// console.log(event.target.name,":",event.target.value);
// })

//Pick your Subjects : make a checkbox : give 4 subjects
// Pick your Gender : Male and female :radio btn


//Keypress
const btnA =document.querySelector("#btn-a");
btnA.addEventListener("keypress",function(event){
    // console.log(event.key);
    if(event.key=="a"){
  console.log("person should go left");
    }
    if(event.key=="d"){
        console.log("person should go right");
    }
    if(event.key=="Enter"){
        ///logic
    }

})

const form =document.querySelector("form");
form.addEventListener('submit',function(event){
  event.preventDefault();
})

// create 2 boxes one red  and one green.
// in red box you have input box and submit btn
// when you write in input box and click on btn ;
//the value of input box should get populated in green box in ul;