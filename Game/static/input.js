submit_btn = document.getElementById('btn-ok')

async function csrf() {
    const response1 = await fetch('/bnc/getcsrf/')
    body = await response1.json()

    console.log(body.result)
    token = body.result

    
}
var csrf_token = csrf()


async function check() {
    game_field = document.getElementById('input_field')
    input = game_field.value
    console.log(input)
    
      body_r = {
        'X-CSRFToken' : csrf_token,
        input: input,
  
    }
   
    
    var response = await fetch('/bnc/check/', {
        headers: {
            'Content-Type': 'application/json'

          },
        body: JSON.stringify(body_r),
        method: "POST",
        credentials: 'same-origin',

    })
    if (response.status == 200) {
        body = await response.json()
        if(body.Ntry!=-1){
            console.log(body.all)
            console.log(body.result)
            console.log(body.place)
            console.log(body.Ntry)
            var win = body.place
            var Ntry = body.Ntry
            
            if(win == 4){
                location.href = '/bnc/win/'
            }
            value = ["Угадал:" + body.all + "\nНа своем месте:" + body.place + "\nВаш вариант:" + body.result + "\n"]
            document.getElementById("input_field").value = "";
            document.getElementById("Game-answer").value += value
            document.getElementById("Ntry").value = Ntry
        }   
        else {
            location.href = '/main/'
        }
        
        
        
    } else {
        body = await response.json()
        console.log(body.result)
    }
} 

submit_btn.addEventListener('click', check, csrf) 