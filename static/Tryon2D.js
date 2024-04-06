function logSubmit(event) {
  event.preventDefault();
  let load=document.getElementById("loader");
  load.style.display='block';
  const data = new FormData(event.target);  

  console.log(event.target)
  const files = [...(data.entries())];
  console.log("data",(data.entries()))
  console.log(files)
  const person = files[0][1];
  const clothes = files[1][1];
  console.log(person);
  
  const dataSend = new FormData();
  dataSend.append("personImage", person);
  dataSend.append("clothImage", clothes);
  console.log("request");
  const url = "https://virtual-try-on2.p.rapidapi.com/clothes-virtual-tryon";
  const options = {
    method: "POST",
    headers: {
      'X-RapidAPI-Key': '4b83f54d28msh516b2eedb96aa43p19897ajsn44ac150d3011',
      'X-RapidAPI-Host': 'virtual-try-on2.p.rapidapi.com'
    },
    body: dataSend,
  };
  try {
    console.log("fetch call");
    fetch(url, options)
      .then((val) => {
        // console.log(val);
        return val.json();
      })
      .then((result) => {
        console.log("inside")
         console.log(result);
         const key='response';
         console.log(result[key]);
         result = result[key];
         const k='ouput_path_img';
         const u=result[k];
              
         console.log(u);
         let load=document.getElementById("loader");
  load.style.display='none';
         document.getElementById("loader").style.display = "none";

        //  const ur='"'+u+'"';
        let d=document.querySelector("#res");
        d.setAttribute("src",u);
        var imageUrl =u; 
        
      });
      
        console.log("url is printed");

      console.log("call request end");
  } catch (error) {
    console.error(error);
    let er=document.getElementById("msg");
    er.innerHTML="error in fetching";
  }
}
const form = document.getElementById("images");
form.addEventListener("submit", logSubmit);