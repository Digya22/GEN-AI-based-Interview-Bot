let cnt = document.querySelector('#cnt')
let after = document.querySelector("#line3")
let t1 = gsap.timeline();
function counterFuntion(){
    let num = 0;
    let counterInterval = setInterval(()=>{
        cnt.innerHTML = `${num++}`;
        
        if(num==101){
            clearInterval(counterInterval)
        }
    },25)
}


let btnDiv = document.querySelector("#main .container .btnDiv")


function loaderAnimation(){

t1.from(".loader",{
    display:"block"
})
t1.from(".loader .text .line h1",{
    y:'200px',
    duration:1,
    stagger:0.4,
    scrub:5
})
t1.from(".loader .counter",{
    scale:0,
    // duration:1,
    stagger:1,
    onStart:function(){
        counterFuntion();
    }
})
t1.to(".loader",{
    opacity:0,
    delay:2.8,
    
    zIndex:100,
    display:"none"
})
}
mainPageAnimation();
// loaderAnimation();
function mainPageAnimation(){

    t1.to("#main",{
        display:"block",
        delay:.2
    })
    // gsap.from("#main .container .background",{
    //     y:1000
    // })
    t1.from("#main .container .header",{
        // opacity:0,
        y:-300,
        scale:0,
        stagger:.6,
        duration:.5,
        scrub:5
    })
    
let btnDiv = document.querySelector(".btnDiv")
t1.from("#main .container .btnDiv ",{
    opacity:0,
    scale:0,
})
t1.from("#main .container .quotes",{
    y:200,
    opacity:0,
    scale:.3
})

quotes = ["Doing the best at this moment puts you in the best place for the next moment.","Success is no accident. It is hard work, perseverance, learning, studying, sacrifice and most of all, love of what you are doing or learning to do.","The only thing standing between you and outrageous success is continuous progress you need discipline.","Most of the important things in the world have been accomplished by people who have kept on trying when there seemed to be no hope at all.","There are no secrets to success. It is the result of preparation, hard work, and learning from failure." ,"Don't spend time beating on a wall, hoping to transform it into a door. ","The future depends on what you do today.", "Only those who dare to fail greatly can ever achieve greatly.","It is hard to fail, but it is worse never to have tried to succeed." ]
function quotesGen(){
    let x = Math.floor(Math.random() * quotes.length);
    console.log(x)
    console.log(quotes[x])
    let quotesText = document.querySelector("#main .container .quotes .text")
    quotesText.innerHTML = quotes[x];
    
 

}
setTimeout(()=>{
   
    new TypeIt("#main .container .header #innerHeading", {
        // strings: "This is my string!",
        waitUntilVisible: true,
        statrDelay:10000,
        speed: 75,
        loop: false,
        afterComplete: function (instance) {
            instance.destroy();
          }
      }) .type("Intrvew", { delay: 200 })
      .move(-2, { delay: 100 })
      .type("i", { delay: 400 })
      .move(-3,{delay:100})
      .type("e",{delay:400})
      .move(null, { to: "END", instant: true, delay: 300 })
      .type(" Platform.")
      .go();
},2000)

quotesGen()

  

}

let mouse = document.querySelector('#main .mouseDiv')
let btn  = document.querySelectorAll('button')
btn.forEach((ele)=>{
    ele.addEventListener("mousemove",()=>{
        gsap.to(mouse,{
            scale:.5,
            border:`3px solid white`,
            x:-5,
            y:-5,
        })
    })
    ele.addEventListener("mouseleave",()=>{
        gsap.to(mouse,{
            scale:1,
            border:`1px solid white`,
            x:5,
            y:5,
        })
    })
})
let container = document.querySelector('#main .container')

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

let cir2 = document.querySelector("#main .container .background #cir2")
let codeLogo = document.querySelector("#main .container .background #codeLogo")
let svgLogo = document.querySelector("#main .container .background #arrow")
let svgLogoPath = document.querySelector("#main .container .background #arrow #path")
// 
console.log(svgLogo)
gsap.to(codeLogo,{
    scale:1.6,
    rotate:20,
})
gsap.to(cir2,{
    // scale:.8,
    // x:200,
    rotate:360,
    duration:7,

    repeat:-1,
    repeatDelay:.03
    // duration:100,

})

gsap.from("#motoText",{
    x:-900,
    duration:1,
    scrub:5,
    

})

setTimeout(function(){
    let erase = document.querySelector('#erase')
    erase.style.display = "block"
     new Vivus(
        'erase',
        {
          type: 'delayed',
          duration: 600,
          animTimingFunction: Vivus.EASE_OUT_BOUNCE,
        },
        // myCallback
        
      );
      
},2000)


const ani1 = new Vivus(
    'rectline',
    {
      type: 'oneByOne',
      duration: 600,
      animTimingFunction: Vivus.EASE,
    
    },
);
setInterval(() => {
    // setTimeout(()=>{
        // },5000)
        // ani.reset()
        ani1.play()
        
        
        ani1.finish().play(-1)
        if(ani1.getStatus()=='end'){
            ani1.reset()
            ani1.play()
        }
        // ani.play(1)
}, 6000);

const ani = new Vivus(
    'wavyline',
    {
      type: 'oneByOne',
      duration: 400,
      animTimingFunction: Vivus.EASE_OUT,
    
    },
);
setInterval(() => {
    // setTimeout(()=>{
        // },5000)
        // ani.reset()
        ani.play()
        ani.finish().play(-1)
        if(ani.getStatus()=='end'){
            ani.reset()
            ani.play()
        }
        // ani.play(1)
}, 4000);
const ani3 = new Vivus(
    'back3',
    {
      type: 'oneByOne',
      duration: 600,
      animTimingFunction: Vivus.EASE_OUT,
    
    },
);
setInterval(() => {
    // setTimeout(()=>{
        // },5000)
        // ani.reset()
        ani3.play()
        ani3.finish().play(-1)
        if(ani3.getStatus()=='end'){
            ani3.reset()
            ani3.play()
        }
        // ani.play(1)
}, 5000);

// const cirSVG = new Vivus(
//     'cirSVG',
//     {
//       type: 'oneByOne',
//       duration: 700,
//       animTimingFunction: Vivus.EASE_OUT_BOUNCE,
    
//     },
// );
// setInterval(() => {
//     // setTimeout(()=>{
//         // },5000)
//         // ani.reset()
//         cirSVG.play()
//         cirSVG.finish().play(-1)
//         if(cirSVG.getStatus()=='end'){
//             cirSVG.reset()
//             cirSVG.play()
//         }
//         // ani.play(1)
// }, 6000);

const rect3 = new Vivus(
    'rect3',
    {
      type: 'oneByOne',
      duration: 200,
      animTimingFunction: Vivus.EASE_OUT_BOUNCE,
    
    },
);
setInterval(() => {
    // setTimeout(()=>{
        // },5000)
        // ani.reset()
        rect3.play()
        rect3.finish().play(-1)
        if(rect3.getStatus()=='end'){
            rect3.reset()
            rect3.play()
        }
        // ani.play(1)
}, 2500);
// console.log(`aiute${ani.getStatus()}`)



  
    



// new TypeIt("#motoText", {
//     strings: "Say Goodbye to Traditional Interviews: Welcome to the Future of Hiring",
//     // ... other options
//   }).go();