<template>
    <h1>Editar Visias</h1>
        <form>
            <!--<td>
                <input type="text" id="id" name="id" v-model="Lista.id">
            </td>-->
            <div class="mx-auto"  style="width: 300px;">
              <label for="exampleInputEmail1" class="form-label">Edite la hora de ingreso </label>
                <input type="time" id="visi_h_ingreso" name="visi_h_ingreso" v-model="Lista.visi_h_ingreso">
            </div>
            <br>
            <div class="mx-auto"  style="width: 300px;">
              <label for="exampleInputEmail1" class="form-label">Edite la hora de salida </label>
                <input type="time" id="visi_h_salida" name="visi_h_salida" v-model="Lista.visi_h_salida">
            </div>
            <br>
            <div class="mx-auto"  style="width: 300px;">
              <label for="exampleInputEmail1" class="form-label">Edite la fecha </label>
                <input type="date" id="visi_fecha" name="visi_fecha" v-model="Lista.visi_fecha">
            </div>
            <br>
            <div class="mx-auto"  style="width: 300px;">
              <label for="exampleInputEmail1" class="form-label"> Ingrese el Id de visitante </label>
                <input type="text" id="visitante" name="visitante" v-model="Lista.visitante">
            </div>
            <br>
            <div class="mx-auto"  style="width: 300px;">
              <label for="exampleInputEmail1" class="form-label"> Ingrese el Id de estudiante </label>
                <input type="text" id="estudiante" name="estudiante" v-model="Lista.estudiante">
            </div>
        </form>
        <br>
    <button type="submit" class="btn btn-primary" v-on:click="editar()">Editar</button>
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
            this.Lista.visi_h_ingreso="";
            this.Lista.visi_h_salida="";
            this.Lista.visi_fecha="";
            this.Lista.visitante="";
            this.Lista.estudiante="";
        })
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