<template>
    <div class="contenedor container center">
        <h3>CONSULTA 4<span class="cursor">|</span> </h3>
    </div>
    <div class="container center">
        <div class="row container">
              <h6 class="text-center"> <small> A continuacion se muestra la consulta </small> </h6>
        </div>
    </div>
    <br>

    <div class="col-md-12">
            <br>
            <br>
            <table class="table table-primary table-striped table-bordered table-hover table-responsive">
                <thead>
                <tr>
                    <th class="text-center">ID</th>
                    <th class="text-center">Nombre</th>
                    <th class="text-center">Apellido</th>
                    <th class="text-center">Identificacion</th>
                    <th class="text-center">Tipo de Identificacion</th>
                </tr>
                </thead>
                <tbody v-for="i in Lista" :key="i.id">
                    <tr>
                        <td class="text-center">{{i.id}}</td>
                        <td class="text-center">{{i.estu_edad}}</td>
                        <td class="text-center">{{i.persona__pers_nombre}}</td>
                        <td class="text-center">{{i.persona__pers_identificacion}}</td>
                        <td class="text-center">{{i.persona__tipo_identificacion__maes_valor}}</td>
                    </tr>
                </tbody>
            </table>
    </div>
    
</template>


<script>

import axios from 'axios';

export default{
    name: 'Consulta4View',
    data() {
        return{
        Lista: [],
        estu_edad: "",
        persona__pers_nombre: "",
        persona__pers_identificacion: "",
        persona__tipo_identificacion__maes_valor: "",
        }
    },
    mounted(){
    axios.get('http://localhost:8000/api-v/consulta4/').then(data => {
      this.Lista = data.data;
      //console.log( data.data);
    })
  },
}
</script>

<style>
.contenedor {
    font-size: xx-large;
    display: block;
    font-family: monospace;
    white-space: nowrap; /* los espacios en blanco no rompen la línea */        
    width: 20ch; /* el ancho será el número de caracteres que tiene nuestra línea */
    animation: escribiendo 2s steps(20);          
    overflow: hidden;
  }

  .cursor{
    color: #18BDEC;
    animation: 0.6s parpadeo-cursor infinite;
  }

  @keyframes escribiendo {
    from {
      width: 0;
    }
  }

  @keyframes parpadeo-cursor {
    50% {
      opacity: 0;
    }
  }
</style>