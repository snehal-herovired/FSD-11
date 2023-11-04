// const sampleArr = [1, 2, 3, 4, 5];
// console.log("start")
// //map, filter and reduce

// //map()=> returns an array which is same size as that of original array;
// //original array is not affected.

// // let mappedArray=sampleArr.map((currentValue,index,originalarray)=>{
// //     // console.log("current value:",currentValue,index,originalarray)
// //     if(currentValue%2==0){

// //         return currentValue;
// //     }
// // })

// // console.log("mappedArray:",mappedArray);

// //filter()

// // setTimeout(()=>{
// //     let filteredArr =sampleArr.filter((currentValue,index,originalArray)=>{
// //         //conditional statement;
// //         console.log("inside filter callback")
// //         if(currentValue%2==0){
// //             return currentValue;
// //         }

// //     })
// //     console.log("filteredArr :",filteredArr)
// // },1000)

// // console.log("originalArray:",sampleArr);
// // console.log("filteredArray:",filteredArr);

// // why filter is not working same as that of Callback (setTimeput).

// // console.log("end")


// // //reduce();
// // const reducevalue= sampleArr.reduce((accumulator,number)=>{
// //   //summation of all the array element values
// //   const sum =accumulator+number;
// //   return sum;
// // },0)

// // console.log(reducevalue,"reducedValue");

// // Js objects:

// let obj = {
//     name: "Snehal",
//     dob: "24-01-2021",
//     age: 23
// }

// //object dot notation
// // obj.age=23;
// // obj.name="Earth"
// // "my name is"
// // obj["my name is"]="Snehal"


// // console.log(obj["dob"])

// // // inbuilt  function:keys(),values() and entries();
// // const allkeys =Object.keys(obj);
// // console.log(allkeys);
// // // ["","",""]
// // //dynamic access to values of objects;
// // const allValues=allkeys.map((currentKey)=>{
// //   console.log(obj[currentKey])
// //   return obj[currentKey]
// // })

// // console.log("allvalues of Obj :",allValues);

// // const alldirectvalues =Object.values(obj);
// // console.log("obj values",alldirectvalues)

// const objValues = Object.entries(obj);
// // console.log("all object entries:", objValues);

// // objValues =[[],[],[]];
// const returnobj = objValues.map(([key, value], index) => {
//     // console.log("key:",key ,"value:",value ,index);
//     const keyValuepair = {
//         [key]: value
//     }
//     return keyValuepair
// })

// // destructing :Es6 version (ecmascript v6)
// //map,filter and reduce : ES6
// //arrow function:es6
// //let and const :es6

// // const arr =[1,2,3]
// // const [arr1,arr2,arr3]=[1,2,3]
// console.log(returnobj)