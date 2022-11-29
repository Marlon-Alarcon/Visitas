<template>
    <div class="contenedor container center">
        <h3>CONSULTA 3<span class="cursor">|</span> </h3>
    </div>
    <div class="container center">
        <div class="row container">
              <h6 class="text-center"> <small> A continuacion se muestra la consulta </small> </h6>
        </div>
    </div>
    <br>
    <div class="form-group row justify-content-center">
        <label for="input" class="col-sm-2 col-form-label">Edad Mayor a</label>
        <div class="col-sm-4">
            <input type="text" class="form-control" placeholder="Edad" aria-label="edad" aria-describedby="addon-wrapping" id="edad" name="edad" v-model="edad">
        </div>
    </div>
    <br>
    <button type="button" class="btn btn-outline-danger" data-bs-dismiss="modal" v-on:click="mostrar()">Mostrar Datos</button>

    <div class="col-md-12">
            <br>
            <br>
            <table class="table table-primary table-striped table-bordered table-hover table-responsive" v-if="Lista.lent!=0">
                <thead>
                <tr>
                    <th class="text-center">ID</th>
                    <th class="text-center">Nombre</th>
                    <th class="text-center">Apellido</th>
                    <th class="text-center">Edad</th>
                    <th class="text-center">Estado</th>
                </tr>
                </thead>
                <tbody v-for="i in Lista" :key="i.id">
                    <tr>
                        <td class="text-center">{{i.id}}</td>
                        <td class="text-center">{{i.persona__pers_nombre}}</td>
                        <td class="text-center">{{i.persona__pers_apellido}}</td>
                        <td class="text-center">{{i.estu_edad}}</td>
                        <td class="text-center">{{i.tipo_estado__maes_nombre}}</td>
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
        persona__pers_nombre: "",
        persona__pers_apellido: "",
        estu_edad: "",
        tipo_estado__maes_nombre: "",
        edad: "",
        }
    },
    methods: {
        mostrar (){
            let post = {
                "edad" : this.edad,
            }
            axios.post('http://localhost:8000/api-v/consulta3/', post)
            .then(result => {
                this.Lista= result.data.data;

                console.log(result.data.data)
            }).catch(error => {
                console.log(error)
            })
        }
    },
    mounted(){
    axios.get('http://localhost:8000/api-v/consulta3/').then(data => {
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