<template>
<div class="container center">
    <div class="row container">
          <h2 class="text-center animate__animated animate__heartBeat">DATOS ACTUALIZADOS EN PERSONA</h2>
          <h6 class="text-center"> <small> A continuacion se muestran los datos que alguna vez han sido actualizados en la tabla personas </small> </h6>
    </div>
</div>
<div class="col-md-12">
                  <br>
                  <br>
                  <div class="d-flex justify-content-between align-items-center">
                    <button @click="salir" type="button" class="btn btn-outline-success">
                        <i class="material-icons material-icons-outlined">keyboard_return</i> Regresar
                    </button>
                  </div>
                  <br>
                    <table class="table table-primary table-striped table-bordered table-hover table-responsive ">
                      <thead>
                        <tr>
                          <th class="text-center">ID</th>
                          <th class="text-center">FECHA DE MODIFICACION</th>
                          <th class="text-center">PERSONA</th>
                          <th class="text-center">ACCION</th>
                        </tr>
                      </thead>
                      <tbody v-for="i in Lista" :key="i.id">
                          <tr>
                              <td class="text-center">{{i.id}}</td>
                              <td class="text-center">{{i.fecha}}</td>
                              <td class="text-center">{{i.pers}}</td>
                              <td class="text-center">{{i.accion}}</td>
                          </tr>
                      </tbody>
                    </table>
                </div>

</template>

<script>
import axios from 'axios';

export default{
    name: 'ActualizandoView',
    data() {
        return{
        Lista: null,
        id: "",
        fecha: "",
        accion: "",
        pers: "",
        }
    },
    
    methods:{
        salir(){
        this.$router.push("/persona");
      },
    },

    mounted(){
    axios.get('http://localhost:8000/api/actupersona/').then(data => {
      this.Lista = data.data;
      //console.log( data.data);
    })
  },
}
</script>
