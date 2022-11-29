<template>
<link href="https://maxcdn.bootstrapcdn.com/font-awesome/4.3.0/css/font-awesome.min.css" rel="stylesheet">
<br>
    <div class=" container center">
        <h2>CONSULTAS</h2>
    </div>
<br>
<div class="container">
    <div class="row">
        <div class="col-sm-6">
            <div class="card bg-c-green order-card">
            <div class="card-block">
                <h5 class="card-title">Consulta 1</h5>
                <p class="card-text">Visitantes en un rango de hora determinado</p>
                <button type="button" class="btn btn-primary" v-on:click="consulta()">Ir a consulta</button>
            </div>
            </div>
        </div>
        <div class="col-sm-6">
            <div class="card bg-c-blue order-card">
            <div class="card-block">
                <h5 class="card-title">Consulta 2</h5>
                <p class="card-text">Discriminar Tipos de visitantes</p>
                <button type="button" class="btn btn-primary" v-on:click="consulta2()">Ir a consulta</button>
            </div>
            </div>
        </div>
        <div class="col-sm-6">
            <div class="card bg-c-yellow order-card">
            <div class="card-block">
                <h5 class="card-title">Consulta 3</h5>
                <p class="card-text">Estudiantes mayores</p>
                <button type="button" class="btn btn-primary" v-on:click="consulta3()">Ir a consulta</button>
            </div>
            </div>
        </div>
        <div class="col-sm-6">
            <div class="card bg-c-verde order-card">
            <div class="card-block">
                <h5 class="card-title">Consulta 4</h5>
                <p class="card-text">Estudiantes y su identificacion</p>
                <button type="button" class="btn btn-primary" v-on:click="consulta4()">Ir a consulta</button>
            </div>
            </div>
        </div>
	</div>
</div>
</template>
<script>
export default {
    methods:{
        consulta(){
            this.$router.push("/consulta");
        },
        consulta2(){
            this.$router.push("/consulta2");
        },
        consulta3(){
            this.$router.push("/consulta3");
        },
        consulta4(){
            this.$router.push("/consulta4");
        }
    }

}

</script>

<style>
.order-card {
    color: rgb(0, 0, 0);
}

.bg-c-blue {
    background: linear-gradient(45deg,#4099ff,#73b4ff);
}

.bg-c-green {
    background: linear-gradient(45deg,#2ed8b6,#59e0c5);
}

.bg-c-yellow {
    background: linear-gradient(45deg,#FFB64D,#ffcb80);
}

.bg-c-verde {
    background: linear-gradient(45deg,#00C897,#82CD47);
}


.card {
    border-radius: 5px;
    -webkit-box-shadow: 0 1px 2.94px 0.06px rgba(4,26,55,0.16);
    box-shadow: 0 1px 2.94px 0.06px rgba(4,26,55,0.16);
    border: none;
    margin-bottom: 30px;
    -webkit-transition: all 0.3s ease-in-out;
    transition: all 0.3s ease-in-out;
}

.card .card-block {
    padding: 25px;
}

.order-card i {
    font-size: 26px;
}

.f-left {
    float: left;
}

.f-right {
    float: right;
}
</style>