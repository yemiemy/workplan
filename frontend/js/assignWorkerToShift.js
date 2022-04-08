function handleFormMsg(msg, display){
    let formMsgElement = document.getElementById("create-form-msg")
    if (formMsgElement !== null){
        if (display === true){
            formMsgElement.setAttribute("class", "alert alert-success alert-dismissible fade show")
            formMsgElement.innerHTML = `
                <strong>Success</strong> ${msg}
            ` 
        } else{
            formMsgElement.setAttribute("class", "alert alert-danger alert-dismissible fade show")
            formMsgElement.innerHTML = `
                <strong>Oops</strong> ${msg}
            ` 
        }
    }
}

function handleAssignMent(event) {
    event.preventDefault()
    const myForm = event.target
    const myFormData = new FormData(myForm)
    const method = myForm.getAttribute("method")
    const url = `http://127.0.0.1:8000/api/add-worker-to-shift/`
    
    const xhr = new XMLHttpRequest()
    xhr.open(method, url)
    xhr.setRequestHeader("HTTP_X_REQUESTED_WITH", "XMLHttpRequest")
    xhr.setRequestHeader("X-Requested-With", "XMLHttpRequest")
    xhr.onload = function (){
        if (xhr.status === 200){
            handleFormMsg("Workers added successfully.", true)
            handleDetail(id)
            myForm.reset()
        }else if(xhr.status === 404){
            console.log(xhr.status, xhr.response)
            handleFormMsg(xhr.response, true)
            alert(xhr.response)
        }else{
            console.log(xhr.status, xhr.response)
            alert("There was a server error, please try again.")
        }
    }
    xhr.onerror = function () {
        alert("An error occurred. Please try again.")
    }
    xhr.send(myFormData)
}



const assignWorkerForm = document.getElementById("add-worker-form")
assignWorkerForm.addEventListener("submit", handleAssignMent)
