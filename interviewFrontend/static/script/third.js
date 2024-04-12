// let http = require('http');
// const { dataSend } = require('../script/cv_parser.js');
// import { dataSend } from "./cv_parser";
let canName = localStorage.getItem('name')
let loaderText = document.querySelector('#loaderText')
new TypeIt(loaderText, {
    strings: `Hello ${canName} , Goodluck to your Interview`,
    speed: 60,
    waitUntilVisible: true,
}).go();
// console.log(dataSend.name)
let loaderVisibility = true;
document.addEventListener('keydown', function(event) {
    // Check if the pressed key has a specific keycode
    if (event.keyCode === 13 && loaderVisibility) {
        loaderVisibility = false;
        console.log("run")
        let loader = document.querySelector('.loader')
        gsap.to(loader,{
            y:-1000,
            duration:2,
            scrub:5,
        })
        let container = document.querySelector('.container')
        container.style.display = 'flex'
    }
});
let mouse = document.querySelector(' .mouseDiv')
let container = document.querySelector('#main .container')
let btn  = document.querySelectorAll('button')
btn.forEach((ele)=>{
    ele.addEventListener("mousemove",()=>{
        gsap.to(mouse,{
            scale:.5,
            border:`3px solid black`,
            x:-5,
            y:-5,
        })
    })
    ele.addEventListener("mouseleave",()=>{
        gsap.to(mouse,{
            scale:1,
            border:`1px solid black`,
            x:5,
            y:5,
        })
    })
})

container.addEventListener("mouseleave",(e)=>{
    
    mouse.style.display = "none";
    
    
})
container.addEventListener("mousemove",(e)=>{
    mouse.style.display = "block";
    let x = e.clientX;
    let y= e.clientY;
    mouse.style.top= `${y-10}px`
    mouse.style.left = `${x-10}px`
    
    console.log(x,y)
    
})
 
