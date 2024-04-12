
let caution = document.querySelector('#main .container .back #caution')


let note = document.querySelector("#main .container .back #note2")
let backani = gsap.timeline()

backani.from(note,{

    // x:500,
    scale:0.1,
    // duration:.2,
})


// let text = document.querySelector("#main .container .back .text")
// new TypeIt(text, {
//     strings: "Please upload your CV!",
//     waitUntilVisible: true,
//     // statrDelay:10000,
//     speed: 75,
//     loop: false,
//     afterComplete: function (instance) {
//         instance.destroy();
//       }
//   }).go()
let form = document.querySelector("#form")
let fileInput = document.querySelector("#file")
function validFile(){
    let validLogo = document.querySelector('#main .container .formTaker #validFileLogo')
    let caution = document.querySelector('#main .container .formTaker #caution')
    validLogo.style.display = "block"
    caution.style.display = "none"
    fileInput.style.border = `1px solid #23F721`
}
form.addEventListener('submit',(e)=>{
    let caution = document.querySelector('#main .container .formTaker #caution')
    if(fileInput.value!=""){
        fileInput.style.border = `1px solid black`
        arrow.style.display  = `none`
        console.log("File is not empty ")
        form.action = "/upload"
    }else{
    e.preventDefault()
        caution.style.display = "block"
        fileInput.style.border = `1px solid #E72929`
    console.log("File is  empty ")
    }
})



let inputField = document.querySelectorAll('input')
let mouse = document.querySelector('#main .mouseDiv')
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
console.log(inputField)
inputField.forEach((ele)=>{
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

t1 = gsap.timeline();


let verifyBtn = document.querySelector('.verify')
verifyBtn.addEventListener('click',(e)=>{
    e.preventDefault();
   
    // t1.from("#main .container .formValidator",{
        

        


    // })
})

// function verifyBtnDisplayFunc(){
//     data = JSON.stringify({{answer|tojson}})??" hejk";
//     data = JSON.parse(data)
//     console.log(data)
//     console.log("reload")
//     console.log(jsonData.length)
//     let verifyBtn = document.querySelector("#main .container .btnDiv #verifyBtn");
//     let subBtn = document.querySelector("#main .container .btnDiv #subBtn");
//     if(jsonData.length!==0){
//         verifyBtn.style.display = "block"
        
//         subBtn.style.display = "none"
//     }else{
//         verifyBtn.style.display = "none"
        
//         subBtn.style.display = "block"
//     }
// }
// document.addEventListener("DOMContentLoaded", function() {
   

//     verifyBtnDisplayFunc()
// });

// let textAni = gsap.timeline()
// let texts = document.querySelectorAll('#main .container .back .text1')
// texts.forEach((text)=>{
//     function shuffle(array) { 
//         return array.sort( ()=>Math.random()-0.5 );
//      } 
// let quest = shuffle(["Tell me about yourself?","What’s your dream job?","What do you think we could do better or differently?","Sell me this pen.","What do you do when a decision is being made that you disagree with?","Walk me through your resume.","Why should we hire you?","What are your greatest strengths?","What motivates you?","Do you consider yourself successful?"])
// let questInd = Math.floor((Math.random() *quest.length) + 0);
// setInterval(()=>{
//     textAni.to(text,{
//         x: Math.floor((Math.random() *1200) + 50),
//         y: Math.floor((Math.random() * 600) + 50),
//         duration:5,
//         onstart:function(){
//             new TypeIt(text, {
//                 strings: quest[questInd],
//                 waitUntilVisible: true,
//                 // statrDelay:10000,
//                 speed: 10,
//                 loop: false,
//                 afterComplete: function (instance) {
//                     instance.destroy();
//                     setTimeout(()=>{
    
//                         // let text22 = document.querySelector(text)
//                         // text22.innerHTML = ""
//                         instance.reset()
//                        },5000)
                    
//                   }
//               }).go()
              

//         }
//     })
  
// },1000)
// })

function dataRec(data = ""){
    jsonData = []
     jsonData = JSON.parse(data);
   if(jsonData.length===undefined){
   
    new TypeIt("#main .container .instructionDiv h3", {
        strings: "Please first submit form!",
        waitUntilVisible: true,
        // statrDelay:10000,
        speed: 75,
        loop: false,
        afterComplete: function (instance) {
            instance.destroy();
          }
      }).go()
    setTimeout(() => {
        let h3Div = document.querySelector('#main .container .instructionDiv h3').textContent = ""
    }, 4000);
    
      
   }else{
    t1.to("#main .container .formTaker",{
        
        scale:.7,
        x:-400,
        scrub:5,
        duration:.4,
        
     })
     
     let formValidator = document.querySelector('#main .container .formValidator')
     formValidator.style.display = "block"
       console.log(jsonData)
       let name = document.querySelector("#main .container .formValidator .nameDiv #name")
       let summary = document.querySelector("#main .container .formValidator .selfSummaryDiv #summary")
       let collegeNm = document.querySelector("#main .container .formValidator .collegeDiv #collegeNm")
       let degree = document.querySelector("#main .container .formValidator .degreeDiv #degree")
       
       let candidateData = jsonData[jsonData.length-1]
       // let candidateData = jsonData
       console.log(candidateData)
       // console.log(jsonData)
       //summary
       // console.log(summary)
       if(candidateData[0]!==""){
           name.value = candidateData[0]
           localStorage.setItem('name',name.value)
        }else{
            let nameDiv = document.querySelector("#main .container .formValidator .nameDiv")
            nameDiv.style.display = "none"
            
        }
        if(candidateData[1]!==""){
            summary.value = candidateData[1];
        }else{
            let summaryDiv = document.querySelector("#main .container .formValidator .selfSummaryDiv ")
            summaryDiv.style.display = "none"
        }
        if(candidateData[4]!==""){
            collegeNm.value = candidateData[4];
        }else{
            let collegeNmDiv = document.querySelector("#main .container .formValidator .collegeDiv ")
            collegeNmDiv.style.display = "none"
        }
        if(candidateData[5]!==""){
            degree.value = candidateData[5]
        }else{
            let degreeDiv = document.querySelector("#main .container .formValidator .degreeDiv ")
            degreeDiv.style.display = "none"
        }
        if(candidateData[2]!==""){
            
            let skillDiv  = document.querySelectorAll("#main .container .formValidator .skillDiv .skills li")
            let skillParentDiv  = document.querySelectorAll("#main .container .formValidator .skillDiv")
            console.log(skillDiv)
            
            for (let index = 0; index < (skillDiv.length>3?3:skillDiv.length); index++) {
            skillDiv[index].textContent= candidateData[2][index];
            
        }
    }else{
        skillParentDiv.style.display = "none"
    }
 
    }   

    
}


