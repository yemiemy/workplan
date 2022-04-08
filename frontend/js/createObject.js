const closeModalBtn = document.querySelectorAll('#close-btn')

// Create Form Handling
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

function handleCreateFormSubmit(event) {
    event.preventDefault()
    const myForm = event.target
    const myFormData = new FormData(myForm)
    const url = myForm.getAttribute("action")
    const method = myForm.getAttribute("method")
    
    let objectToCreate = "";
    if (url.includes("worker")){
        objectToCreate = "Worker" 
    }else{
        objectToCreate = "Shift" 
    }

    const xhr = new XMLHttpRequest()
    const responseType = "json"
    xhr.responseType = responseType
    xhr.open(method, url)
    xhr.setRequestHeader("HTTP_X_REQUESTED_WITH", "XMLHttpRequest")
    xhr.setRequestHeader("X-Requested-With", "XMLHttpRequest")
    xhr.onload = function () {
        if (xhr.status === 201){
            handleFormMsg(`${objectToCreate} added successfully.`, true)
            if (objectToCreate === "Worker"){
                loadWorkers(workersContainerElement)
            }else{
                loadShifts(shiftsContainerElement)
            }
            myForm.reset()
            closeModalBtn.forEach((close)=> {
                close.click()
            })
        } else if (xhr.status === 400) {
            console.log(xhr.status, xhr.response)
            const errorJson = xhr.response
            const contentError = errorJson.detail
            let contenErrorMsg;
            if (contentError){
                contenErrorMsg = contentError
            } else {
                alert("An error occured. Please try again.")
            }
            handleFormMsg(contenErrorMsg, false)
            closeModalBtn.forEach((close)=> {
                close.click()
            })
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

const workerCreateForm = document.getElementById('worker-create-form')
workerCreateForm.addEventListener("submit", handleCreateFormSubmit)

const shiftCreateForm = document.getElementById('shift-create-form')
shiftCreateForm.addEventListener("submit", handleCreateFormSubmit)
// --- END Create Form