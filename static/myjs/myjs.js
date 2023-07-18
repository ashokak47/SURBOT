$('#login_btn').click(function(){
    var email = $("#email").val();
    var password = $("#password").val();
    $.ajax(
    {
        type:"POST",
        url: "/login",
        data:{
            "email": email,
            "password": password,
        },
        success: function( data ) 
        {
            alert("Login Button clicked")
        }
    })
});


$('#signup_btn').click(function(){
    var email = $("#email").val();
    var password = $("input[name=password]").val();
    var name = $("input[name=name]").val();
    var contact =$("input[name=contact]").val();
    var dob = $("input[name=dob]").val();
    var doa =$("input[name=doa]").val();
    var address = $("input[name=address]").val();

    $.ajax(
    {
        type:"POST",
        url: "/SBT/signup/",
        csrfmiddlewaretoken: '{{ csrf_token }}',
        data:{
            "email": email,
            "password": password,
            "name": name,
            "contact": contact,
            "dob": dob,
            "doa": doa,
            "address": address,
        },
        success: function( data ) 
        {
            if(data.result =='success'){
                alert("Signup successful.")
            }else{
                alert("Something went wrong.")
            }
            
        }
    })
});

