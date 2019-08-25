$(document).ready(function(){


    $("#dp").focus(function(){

        $(this).css({
            "border-radius":"0px"
        });

        // $("#dp_menu").css({
        //     "border-radius":"0px"
        // });
    });

    $("#dp").blur(function(){

        $(this).css({
            "border-radius":"20px"
        });

        // $("#dp_menu").css({
        //     "border-radius":"0px"
        // });
    });
    


    $('input[name="detail_type"]').change(function(){

        $("#dp").css({
            "border-radius":"20px"
        });

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


        national_id:
        {
            identifier: 'national_id',
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

        detail_type:
        {
            identifier: 'detail_type',
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

        phone_number:
        {
            identifier  : 'phone_number',
            rules:
            [
                {
                    type   : 'empty',
                    prompt : 'لطفا شماره تماس خود را وارد کنید'
                },

                {
                    type   : 'integer',
                    prompt : 'شماره تماس فقط شامل رقم می باشد'
                }
            ],
        },


    }
})
.submit(function(event){

    var valid_all = 1;
    
    if($('input[name="detail_type"]').val()=="1" && $('input[name="university"]').val()=="")
    {
        event.preventDefault();
        var node = document.createElement("LI");
        var textnode = document.createTextNode("لطفا نام دانشگاه را وارد کنید");
        document.getElementById("university").style.backgroundColor = "#fff6f6";
        document.getElementById("university").style.borderColor = "#e0b4b4";
        document.getElementById("university").style.color = "#9f3a38";
        node.appendChild(textnode);
        document.getElementById("validation-message").childNodes[0].appendChild(node);
        $("validation-message").css({'display':'block'})
        valid_uni = 0;
        valid_all = 0;
    }

    if($('input[name="detail_type"]').val()=="1" && $('input[name="study_field"]').val()=="")
    {
        event.preventDefault();
        var node = document.createElement("LI");
        var textnode = document.createTextNode("لطفا رشته ی تحصیلی خود را وارد کنید");
        document.getElementById("study_field").style.backgroundColor = "#fff6f6";
        document.getElementById("study_field").style.borderColor = "#e0b4b4";
        document.getElementById("study_field").style.color = "#9f3a38";
        node.appendChild(textnode);
        document.getElementById("validation-message").childNodes[0].appendChild(node);
        valid_stufield = 0;
        valid_all = 0;
    }

    if($('input[name="detail_type"]').val()=="1" && $('input[name="student_id"]').val()=="")
    {
        event.preventDefault();
        var node = document.createElement("LI");
        var textnode = document.createTextNode("لطفا شماره دانشجویی خود را وارد کنید");
        document.getElementById("student_id").style.backgroundColor = "#fff6f6";
        document.getElementById("student_id").style.borderColor = "#e0b4b4";
        document.getElementById("student_id").style.color = "#9f3a38";
        node.appendChild(textnode);
        document.getElementById("validation-message").childNodes[0].appendChild(node);
        valid_stuid = 0;
        valid_all = 0;
    }

    if($('input[name="detail_type"]').val()=="1" && $('input[name="student_id"]').val()!="")
    {
        var text = $('input[name="student_id"]').val();
        var e = 0;
        for(var i=0;i<text.length;i++)
        {
            if(text[i]!="1" && text[i]!="2" && text[i]!="3" && text[i]!="4" && text[i]!="5" && text[i]!="6" && text[i]!="7"
            && text[i]!="8" && text[i]!="9" && text[i]!="0")
            {
                e = 1;
            }
        }
        if(e == 1)
        {
            event.preventDefault();
            var node = document.createElement("LI");
            var textnode = document.createTextNode("شماره دانشجویی فقط شامل ارقام می باشد");
            document.getElementById("student_id").style.backgroundColor = "#fff6f6";
            document.getElementById("student_id").style.borderColor = "#e0b4b4";
            document.getElementById("student_id").style.color = "#9f3a38";
            node.appendChild(textnode);
            document.getElementById("validation-message").childNodes[0].appendChild(node);
            valid_stuid = 0;
            valid_all = 0;
        }
    }

    if($('input[name="detail_type"]').val()=="2" && $('input[name="agency"]').val()=="")
    {
        event.preventDefault();
        var node = document.createElement("LI");
        var textnode = document.createTextNode("لطفا نام آژانس خود را وارد کنید");
        document.getElementById("agency").style.backgroundColor = "#fff6f6";
        document.getElementById("agency").style.borderColor = "#e0b4b4";
        document.getElementById("agency").style.color = "#9f3a38";
        node.appendChild(textnode);
        document.getElementById("validation-message").childNodes[0].appendChild(node);
        valid_agency = 0;
        valid_all = 0;
    }

    if($('input[name="detail_type"]').val()=="2" && $('input[name="city"]').val()=="")
    {
        event.preventDefault();
        var node = document.createElement("LI");
        var textnode = document.createTextNode("لطفا نام شهر خود را وارد کنید");
        document.getElementById("city").style.backgroundColor = "#fff6f6";
        document.getElementById("city").style.borderColor = "#e0b4b4";
        document.getElementById("city").style.color = "#9f3a38";
        node.appendChild(textnode);
        document.getElementById("validation-message").childNodes[0].appendChild(node);
        valid_city = 0;
        valid_all = 0;
    }

    if($('input[name="detail_type"]').val()=="3" && $('input[name="hotel"]').val()=="")
    {
        event.preventDefault();
        var node = document.createElement("LI");
        var textnode = document.createTextNode("لطفا نام هتل خود را وارد کنید");
        document.getElementById("hotel").style.backgroundColor = "#fff6f6";
        document.getElementById("hotel").style.borderColor = "#e0b4b4";
        document.getElementById("hotel").style.color = "#9f3a38";
        node.appendChild(textnode);
        document.getElementById("validation-message").childNodes[0].appendChild(node);
        valid_hotel = 0;
        valid_all = 0;
    }

    if($('input[name="detail_type"]').val()=="3" && $('input[name="city"]').val()=="")
    {
        event.preventDefault();
        var node = document.createElement("LI");
        var textnode = document.createTextNode("لطفا نام شهر خود را وارد کنید");
        document.getElementById("city").style.backgroundColor = "#fff6f6";
        document.getElementById("city").style.borderColor = "#e0b4b4";
        document.getElementById("city").style.color = "#9f3a38";
        node.appendChild(textnode);
        document.getElementById("validation-message").childNodes[0].appendChild(node);
        valid_city = 0;
        valid_all = 0;
    }
    
  
    if(valid_all == 0)
    {
        event.preventDefault();
    }




});

$(document).ready(function(){
    $("#university").click(function(){

        if(valid_uni==0)
        {
            $(this).css({
                "border-color":"rgba(34,36,38,.15)",
                "background-color":"#fff",
                "color":"rgba(0,0,0,.87)"
            });
            valid_uni = 1;
        }
        
    });

    $("#study_field").click(function(){
        if(valid_stufield==0)
        {
            $(this).css({
                "border":"1px solid rgba(34,36,38,.15)",
                "background-color":"#fff",
                "color":"rgba(0,0,0,.87)"
            });
            valid_stufield = 1;
        }
        
    });

    $("#student_id").click(function(){
        if(valid_stuid==0)
        {
            $(this).css({
                "border":"1px solid rgba(34,36,38,.15)",
                "background-color":"#fff",
                "color":"rgba(0,0,0,.87)"
            });
            valid_stuid = 1;
        }
        
    });

    $("#agency").click(function(){
        if(valid_agency==0)
        {
            $(this).css({
                "border":"1px solid rgba(34,36,38,.15)",
                "background-color":"#fff",
                "color":"rgba(0,0,0,.87)"
            });
            valid_agency = 1;
        }
        
    });

    $("#hotel").click(function(){
        if(valid_hotel==0)
        {
            $(this).css({
                "border":"1px solid rgba(34,36,38,.15)",
                "background-color":"#fff",
                "color":"rgba(0,0,0,.87)"
            });
            valid_hotel = 1;
        }
        
    });

    $("#city").click(function(){
        if(valid_city==0)
        {
            $(this).css({
                "border":"1px solid rgba(34,36,38,.15)",
                "background-color":"#fff",
                "color":"rgba(0,0,0,.87)"
            });
            valid_city = 1;
        }
        
    });

});