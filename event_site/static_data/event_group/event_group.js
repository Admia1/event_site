$(document).ready(function(){

    new Vue({
        el: '#main',
        data: {
            events: [
                {
                    location: 'تهران',
                    price: 100000,
                },
                {
                    location: 'شیراز',
                    price: 200000,
                }
            ],
            discountPercent: null,
            loading: false,
            discountCode: null,
            discountError: null,
        },
        methods: {
            discountValidation(){
                if(this.discountCode){
                    this.loading = true;
                    axios.post('http://academic-events.ir/api/discount_check/1/',{
                        discount_code: this.discountCode
                    }).then(function(response) {
                        console.log(response.data)

                        // if(response.result == 'ok'){
                        //     this.discountPercent = response.percent;
                        // } else {
                        //     this.discountError = response.error;
                        // }
                        this.loading = false;
                    })
                }
            }
        }
    });

    $(".ui.button.goto_discount").click(function(){
        $('.ui.modal')
        .modal('show');
    });


});