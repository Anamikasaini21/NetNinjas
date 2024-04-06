
function logSubmit(event) {
  event.preventDefault();
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
      'X-RapidAPI-Key': '9e6b36bf4dmshd72ea913fac4e08p114e85jsn2d125e094240',
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
        //  const ur='"'+u+'"';
        let d=document.querySelector("#res");
        d.setAttribute("src",u);
        var imageUrl =u; 
      
      });
      
        console.log("url is printed");

      console.log("call request end");
  } catch (error) {
    console.error(error);
  }
}
const form = document.getElementById("images");
form.addEventListener("submit", logSubmit);






