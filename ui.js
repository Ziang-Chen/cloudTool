// UI file


// initialize the elements binding

sourceButton= document.getElementsByClassName("sourceButton")[0]
targetButton= document.getElementsByClassName("targetButton")[0]
uploadButton= document.getElementsByClassName("uploadButton")[0]
downloadButton= document.getElementsByClassName("downloadButton")[0]
patternButton= document.getElementsByClassName("patternButton")[0]
ruleButton= document.getElementsByClassName("ruleButton")[0]
refreshButoon= document.getElementsByClassName("refreshButton")[0]

networkdashboard= document.getElementsByClassName("networkdashboard")[0]

run= document.getElementsByClassName("run")[0]
cli= document.getElementsByClassName("cli")[0]
filelists=document.getElementsByClassName("filelists")[0]

let response=null

// send command
run.addEventListener("click",function(){
    c_buff=document.getElementsByTagName("input")[0].value
    fetch("/run", {
                        method: "POST",
                        body: JSON.stringify({
                        command:c_buff
                        }),
                    headers: {  "Content-type": "application/json; charset=UTF-8"}
                }).then((response) => 
                    response.text() 
                ).then((text)=> {
                    networkdashboard.innerHTML=text
                })
                    
});
    


// initialize information update 

fetch("/information", {
    method: "POST",
    body: JSON.stringify({
        content:"init"
    }),
    headers: {  "Content-type": "application/json; charset=UTF-8"}
}).then(function(response) { 
    networkdashboard.innerHTML=response.text()
    });


// get file list

fetch("/filelist").then((response)=> response.text()).then((text)=> {
    filelists.innerHTML=text
    });
    


//test code for async on both frontend and backend

async function test_async_sub(arg){
    const pre=new Date()
    const ID=Date.now()
    console.log(ID, pre.getSeconds())
    fetch(arg).then(function(response) {
        const current=new Date()
        console.log(ID, current.getSeconds() )
    });
};

function test_async(){
    test_async_sub("/async_test");
    test_async_sub("/async_test_2");
    test_async_sub("/async_test_3");
};