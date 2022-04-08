const shiftInfo = document.getElementById("shift-detail")
const workersList = document.getElementById("workers-list")
const selectWorkers = document.getElementById("id_select_workers")
const shiftFormDetails = document.getElementById("shift-form-details")

const getAvailableWorkers = () => {
    const xhr = new XMLHttpRequest()
    const method ="GET"
    const url = "http://127.0.0.1:8000/api/workers-list/"
    const responseType = "json"

    xhr.responseType = responseType
    xhr.open(method, url)
    xhr.onload = function(){
        if(xhr.status === 200){
            const listedWorkers = xhr.response
            
            let selectItemStr = ""
            for (let i = 0; i < listedWorkers.length; ++i){
                let worker = listedWorkers[i]
                if(worker.is_available){
                    selectItemStr +=
                    `
                    <option value="${worker.id}">${worker.first_name} ${worker.last_name}</option>
                    `
                }
            } 
            selectWorkers.innerHTML = selectItemStr

        }
        else{
            console.log(xhr.status, xhr.response)
            alert("An error has occured. Please refresh the page.")
        }
    }
    xhr.onerror = function () {
        alert("An error occurred. Please try again.")
    }
    xhr.send()
}


const handleDetail = (id) => {
    const url = `http://127.0.0.1:8000/api/shift/${id}/`
    const method = "GET"
    const xhr = new XMLHttpRequest()
    xhr.responseType =  "json"
    xhr.open(method, url)
    xhr.onload = function () {
        if (xhr.status === 200){
            let shift = xhr.response
            shiftInfo.innerHTML = `
                <h1>${shift.name}</h1>
                <p>Duration: <b>${shift.start_time}</b> - <b>${shift.end_time}</b></p>
            `
            shiftFormDetails.innerHTML += `
            <input type="hidden" name="id" value="${shift.id}">
            <input type="hidden" name="name" value="${shift.name}">
            <input type="hidden" name="start_time" value="${shift.start_time}">
            <input type="hidden" name="end_time" value="${shift.end_time}">
            `
            let contentStr = ""
            if (shift.workers.length == 0){
                contentStr +=
                `
                <tr>
                    <td colspan="2">No workers on duty yet.</td>
                </tr>
                `
            } 
            for (let i = 0; i < shift.workers.length; ++i){
                let worker = shift.workers[i]
                contentStr +=
                `
                <tr>
                    <th scope="row">${i+1}</th>
                    <td>${worker.first_name} ${worker.last_name}</td>
                </tr>
                `
            }
            workersList.innerHTML = contentStr
            getAvailableWorkers()
        }else if(xhr.status === 404){
            alert(`There is no shift with ${id} present.`)
            let link = window.location.href
            link = link.substring(0, link.lastIndexOf("/")+1)
            link+="index.html"
            window.location.href = link
        }else{
            console.log(xhr.status, xhr.response)
            alert("An error occured. Please try again.")
        }
    }
    xhr.onerror = function () {
        alert("An error occurred. Please try again.")
    }
    xhr.send()
}

id = localStorage.getItem("id")
handleDetail(id)