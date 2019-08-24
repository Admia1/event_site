$(document).ready(function(){


    


    $('input[name="detail_type"]').change(function(){
        if($(this).val() == "0")
        {
            $("#a6").css({"display":"block"});
            $("#a7").css({"display":"block"});
            $("#a8").css({"display":"none"});
            $("#a9").css({"display":"none"});
            $("#a10").css({"display":"none"});
            $("#a11").css({"display":"none"});
            $("#a12").css({"display":"none"});
            $("#a13").css({"display":"none"});
            // $("#a14").css({"display":"none"});
        }

        if($(this).val() == "1")
        {
            $("#a6").css({"display":"none"});
            $("#a7").css({"display":"none"});
            $("#a8").css({"display":"block"});
            $("#a9").css({"display":"block"});
            $("#a10").css({"display":"block"});
            $("#a11").css({"display":"none"});
            $("#a12").css({"display":"none"});
            $("#a13").css({"display":"none"});
            // $("#a14").css({"display":"none"});
        }

        if($(this).val() == "2")
        {
            $("#a6").css({"display":"none"});
            $("#a7").css({"display":"none"});
            $("#a8").css({"display":"none"});
            $("#a9").css({"display":"none"});
            $("#a10").css({"display":"none"});
            $("#a11").css({"display":"block"});
            $("#a12").css({"display":"block"});
            $("#a13").css({"display":"none"});
            // $("#a14").css({"display":"none"});
        }

        if($(this).val() == "3")
        {
            $("#a6").css({"display":"none"});
            $("#a7").css({"display":"none"});
            $("#a8").css({"display":"none"});
            $("#a9").css({"display":"none"});
            $("#a10").css({"display":"none"});
            $("#a11").css({"display":"none"});
            $("#a12").css({"display":"block"});
            $("#a13").css({"display":"block"});
            // $("#a14").css({"display":"block"});
        }

        if($(this).val() == "4")
        {
            $("#a6").css({"display":"none"});
            $("#a7").css({"display":"none"});
            $("#a8").css({"display":"none"});
            $("#a9").css({"display":"none"});
            $("#a10").css({"display":"none"});
            $("#a11").css({"display":"none"});
            $("#a12").css({"display":"none"});
            $("#a13").css({"display":"none"});
            // $("#a14").css({"display":"none"});
        }

    });






    var t = "<i class='paper plane icon' id='iconsubmit'></i>";
    var s = function f()
    {
        $("#b1").css({
           "color":"black" 
        });
        
    }

    var u = function f()
    {
        $("#b1").empty();
        $("#b1").append(t);
    }


    $("#b1").mouseenter(function(){
        $(this).empty();
        $(this).css({
        // "border-color":"cadetblue",
        "color":"cadetblue",
        "background-position":"left bottom",
        });

        $(this).append(t);
    });

    $("#b1").mouseleave(function(){
        {
            $(this).empty();
            $(this).css({
                "background-position":"right bottom",
                // "border-color":"rgb(9, 119, 55)",
                "color":"black",
                });
            $(this).append("ثبت نام");
        }

    });



});

$('.ui.form')
  .form
({
    

    fields:
    {
        first_name:
        {
            identifier: 'first_name',
            rules:
            [
                {
                    type   : 'empty',
                    prompt : 'لطفا نام خود را وارد کنید'
                },

                {
                    type   : 'minLength[2]',
                    prompt : 'نام حداقل باید شامل دو حرف باشد'                  
                }

            ],
        },


        last_name:
        {
            identifier: 'last_name',
            rules:
            [
                {
                    type   : 'empty',
                    prompt : 'لطفا نام خانوادگی خود را وارد کنید'
                },

                {
                    type   : 'minLength[2]',
                    prompt : 'نام خانوادگی حداقل باید شامل دو حرف باشد'
                }

            ],
        },


        identify_number:
        {
            identifier: 'identify_number',
            rules:
            [
                {
                    type   : 'exactLength[10]',
                    prompt : 'کد ملی شامل 10 رقم می باشد'
                },

                {
                    type   : 'integer',
                    prompt : 'کد ملی یک عدد 10 رقمی می باشد'
                }
            ],
        },

        activity:
        {
            identifier: 'activity',
            rules:
            [
                {
                    type   : 'empty',
                    prompt : 'لطفا حیطه ی فعالیت خود را وارد کنید'
                }
            ],
        },

        email:
        {
            identifier  : 'email',
            rules:
            [
                {
                    type   : 'email',
                    prompt : 'لطفا یک ایمیل معتبر وارد کنید'
                }
            ],
        },

        phone:
        {
            identifier  : 'phone',
            rules:
            [
                {
                    type   : 'empty',
                    prompt : 'لطفا شماره تماس خود را وارد کنید'
                }
            ],
        },


    }
})
.submit(function(event){
//   if( $('.ui.form').form('is valid')) {
    // event.preventDefault();
    if($('input[name="activity"]').val()=="0" && $('input[name="code"]').val()=="")
    {
        event.preventDefault();
        // $("#validation-message").children[0].append("<li>لطفا کد راهنمای خود را وارد کنید<li>");
        // $(".ui.list").append("<li>لطفا کد راهنمای خود را وارد کنید<li>");
        var node = document.createElement("LI");
        var textnode = document.createTextNode("لطفا کد راهنمای خود را وارد کنید");
        // node.style.backgroundColor("color: #9f3a38;");
        document.getElementById("code").style.backgroundColor = "#fff6f6";
        document.getElementById("code").style.borderColor = "#e0b4b4";
        document.getElementById("code").style.color = "#9f3a38";
        node.appendChild(textnode);
        document.getElementById("validation-message").childNodes[0].appendChild(node);
    }
    
//   }
});