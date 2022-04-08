// search function
function SearchFunction() {
    let input, filter, div, item, i, txtValue
    input = document.getElementById("searchInput")
    filter = input.value.toUpperCase()
    tr = document.getElementsByTagName("tr")
    for (i = 0; i < tr.length; i++){
      item = tr[i]
      txtValue = item.textContent || item.innerText

      if (txtValue.toUpperCase().indexOf(filter) > -1){
        tr[i].style.display = ''
      }else{
        tr[i].style.display = 'none'
      }
    }
}