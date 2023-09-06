new Vue({
    el: '#hairs_app',
    data: {
    orders:[]
    },
    created: function(){
        const vm = this;
        axios.get('/api/hairs')
        .then(function(response){
        console.log(response.data)
        })
    }
}

)