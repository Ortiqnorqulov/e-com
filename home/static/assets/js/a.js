const star_labels= document.querySelectorAll(".star1")
const star_inputs = document.querySelectorAll(".star_input")
const label_images= document.querySelectorAll(".label_image")

let rating = 0

for(let i = 0; i < star_inputs.length; i++){
    star_inputs[i].addEventListener("change", (e)=>{
        for(let n = 0; n<=4; n++ ){
            if(n<=i){
                label_images[n].setAttribute("src","/static/assets/imgs/icon-star.png")
            }else if(n>=i){
                label_images[n].setAttribute("src", "/static/assets/imgs/white-star.png")
            }
        }
        rating = i+1
        console.log(rating)
    })
}
