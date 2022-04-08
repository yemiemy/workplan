// Workers List Handling
function loadWorkers(workersElement){
    const xhr = new XMLHttpRequest()
    const method ="GET"
    const url = "http://127.0.0.1:8000/api/workers-list/"
    const responseType = "json"

    xhr.responseType = responseType
    xhr.open(method, url)
    xhr.onload = function(){
        if(xhr.status === 200){
            const listedWorkers = xhr.response
            let finalListStr = ""
            for (let i = 0; i < listedWorkers.length; ++i){
                let worker =  listedWorkers[i]
                finalListStr += formatWorkersElement(worker, i+1)
            }

            workersElement.innerHTML = finalListStr
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


function formatWorkersElement(worker, i) {
    let formatted =
    `

        <tr>
            <th scope="row">${i}</th>
            <td>${worker.first_name}</td>
            <td>${worker.last_name}</td>
            <td>${worker.email}</td>
            <td>${worker.is_available ? "Available" : "Not Available"}</td>
        </tr>
        ` 
    return formatted
}




const workersContainerElement = document.getElementById('workers-list')
loadWorkers(workersContainerElement)

