// Workers List Handling
let loader = document.querySelectorAll("#loader")

function loadShifts(shiftElement){
    const xhr = new XMLHttpRequest()
    const method ="GET"
    const url = "http://127.0.0.1:8000/api/shift/list/"
    const responseType = "json"

    xhr.responseType = responseType
    xhr.open(method, url)
    xhr.onload = function(){
        if(xhr.status === 200){
            const listedShifts = xhr.response
            let finalListStr = ""
            for (let i = 0; i < listedShifts.length; ++i){
                let shift =  listedShifts[i]
                finalListStr += formatShiftElement(shift, i+1)
            }

            //puts off all loaders
            loader.forEach((element) => {
                element.style.display = "none"
            })
            
            shiftElement.innerHTML = finalListStr
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


function formatShiftElement(shift, i) {
    let formatted =
    `
        <tr>
            <th scope="row">${i}</th>
            <td>${shift.name}</td>
            <td>${shift.start_time}</td>
            <td>${shift.end_time}</td>
            <td>${shift.workers ? shift.workers.length : "0"}</td>
            <td><a href="../templates/shiftDetail.html" onclick="handleClick(${shift.id})">Add workers</td>
        </tr>
        ` 
    return formatted
}

function handleClick(id){
    localStorage.setItem("id", id)
}



const shiftsContainerElement = document.getElementById('shifts-list')
loadShifts(shiftsContainerElement)
