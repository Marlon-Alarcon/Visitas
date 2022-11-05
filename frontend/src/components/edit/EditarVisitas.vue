<template>
    <h1>Editar Visias</h1>
    <br>
        <form>
            <!--<td>
                <input type="text" id="id" name="id" v-model="Lista.id">
            </td>-->
            <div class="form-group row justify-content-center">
              <label for="input" class="col-sm-2 col-form-label">Edite la hora de ingreso </label>
              <div class="col-sm-4">
                <input type="time" class="form-control" id="visi_h_ingreso" name="visi_h_ingreso" v-model="Lista.visi_h_ingreso">
              </div>
            </div>
            <br>
            <div class="form-group row justify-content-center">
              <label  for="input" class="col-sm-2 col-form-label">Edite la hora de salida </label>
              <div class="col-sm-4">
                <input type="time" class="form-control" id="visi_h_salida" name="visi_h_salida" v-model="Lista.visi_h_salida">
              </div>
            </div>
            <br>
            <div class="form-group row justify-content-center">
              <label for="input" class="col-sm-2 col-form-label">Edite la fecha </label>
              <div class="col-sm-4">
                <input type="date" class="form-control" id="visi_fecha" name="visi_fecha" v-model="Lista.visi_fecha">
              </div>
            </div>
            <br>
            <div class="form-group row justify-content-center">
              <label for="input" class="col-sm-2 col-form-label"> Ingrese el Id de visitante </label>
              <div class="col-sm-4">
                <input type="text" class="form-control"  id="visitante" name="visitante" v-model="Lista.visitante">
              </div>
            </div>
            <br>
            <div class="form-group row justify-content-center">
              <label for="input" class="col-sm-2 col-form-label"> Ingrese el Id de estudiante </label>
              <div class="col-sm-4">
                <input type="text" class="form-control" id="estudiante" name="estudiante" v-model="Lista.estudiante">
              </div>
            </div>
        </form>
        <br>
    <button type="submit" class="btn btn-outline-success" v-on:click="editar()">Editar</button>
    <div class="space"></div>

    <button type="button" class="btn btn-outline-danger" v-on:click="salir()">Salir</button>
  </template>
  
  <script>
  import axios from 'axios';
  
  export default {
  name: "EditarVisita",
  data() {
    return {
      Lista: [],
    }
  },
  methods: {
    editar() {
      const Swal = require('sweetalert2')
        let post = {
            //"id": this.Lista.id,
            "visi_h_ingreso": this.Lista.visi_h_ingreso,
            "visi_h_salida": this.Lista.visi_h_salida,
            "visi_fecha": this.Lista.visi_fecha,
            "visitante": this.Lista.visitante,
            "estudiante": this.Lista.estudiante,
        }
        axios.put("http://localhost:8000/api-v/Visita/" + this.$route.params.id + "/", post).then(result => {
            console.log(result);
            //this.Lista.id="";
            Swal.fire({
              icon: 'success',
              title: 'Datos Editados',
              text: 'Correctamente',
              timer: 3000,
            })
            this.Lista.visi_h_ingreso="";
            this.Lista.visi_h_salida="";
            this.Lista.visi_fecha="";
            this.Lista.visitante="";
            this.Lista.estudiante="";
        })
    },
      salir(){
      this.$router.push("/visita");
    },
  },
  
  mounted() {
    let id = this.$route.params.id;
    let direccion = "http://localhost:8000/api-v/Visita/"
    axios.get(direccion + id).then(data => {
        this.Lista = data.data;
    })
  },
  }
  </script>

<style>
.space {
  width: 10px;
  height: auto;
  display: inline-block;
}
</style>