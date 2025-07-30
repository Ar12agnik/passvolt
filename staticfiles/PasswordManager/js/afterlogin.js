$(document).ready(()=>{
    const url= window.location.origin
    $("#pwds").DataTable();
    function generate_passwoord_now(){
        $("#generatedPassword").val("")

        $.ajax({
            type: "GET",
            url: `${url}/generate_password_page`,
            success: function (response) {
                $("#addPasswordSection").attr("hidden",true);
                $("#generatePasswordSection").removeAttr("hidden");
                $("#generatedPassword").val(response)
                $('#copyButton').click(function() {
                    var passwordInput = document.getElementById('generatedPassword');
                    passwordInput.select();
                    document.execCommand('copy');
                    alert('Password copied to clipboard!');

                  });

                
            }
        });
    }
    $("#generatePassword").on('click',generate_passwoord_now())
    $("#addpwd").on("click",()=>{
        $("#generatePasswordSection").attr("hidden",true);
        $("#addPasswordSection").removeAttr("hidden");
    })
    $("#generateBtn").on('click',()=>{
        
        generate_passwoord_now()

    })
    $("#switchToAdd").on("click",()=>{
        $("#generatePasswordSection").attr("hidden",true);
        $("#addPasswordSection").removeAttr("hidden");
    })
    
    $("#switchToGenerate").on("click",()=>{
        $("#addPasswordSection").attr("hidden",true);
        $("#generatePasswordSection").removeAttr("hidden");
    })

  })