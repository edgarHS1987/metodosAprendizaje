function checkForm(formulario){
    var modal = new bootstrap.Modal(document.getElementById("capturaTodas"), {});
    
    let error = false;
    
    for (let i = 1; i < 17; i++) {
        error = false;
        var radios = document.getElementsByName("radios"+i);
        for (let index = 0; index < radios.length; index++) {
            if(radios[index].checked){
                console.log(radios[index].value);
                error = true;
            }
        }
        if (error == false) {
            modal.show();
            return false;
        }
        
    }
    return true;
}