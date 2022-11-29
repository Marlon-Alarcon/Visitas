<template>
  <h1>Editar a Personas</h1>
  <br>
  <br>
      <form >
          <!--<td>
              <input type="text" id="id" name="id" v-model="Lista.id">
          </td>-->
          <div class="form-group row justify-content-center">
            <label for="input" class="col-sm-2 col-form-label">Ingrese el nombre</label>
          <div class="col-sm-4">
              <input type="text" class="form-control" id="pers_nombre" name="pers_nombre" v-model="Lista.pers_nombre" required/>
          </div>
          </div>
          <br>
          <div class="form-group row justify-content-center">
            <label for="input" class="col-sm-2 col-form-label">Ingrese el apellido</label>
          <div class="col-sm-4">
              <input type="text" class="form-control" id="pers_apellido" name="pers_apellido" v-model="Lista.pers_apellido" required/>
          </div>
          </div>
          <br>
          <div class="form-group row justify-content-center">
            <label for="input"  class="col-sm-2 col-form-label ">Ingrese la el numero de Identificacion</label>
          <div class="col-sm-4" style="margin-top:10px;">
              <input type="text" class="form-control" id="pers_identificacion" name="pers_identificacion" v-model="Lista.pers_identificacion" required/>
          </div>
          </div>
          <br>
          <div class="form-group row justify-content-center">
            <label for="input"  class="col-sm-2 col-form-label ">Tipo de Identificacion</label>
            <div class="col-sm-4">
              <select class="form-select" v-model="Lista.tipo_identificacion" aria-label="Default select example" required>
              <option selected disabled value="">Tipo de Identificacion</option>
              <option value="2">Cedula</option>
              <option value="3">Tarjeta de Identidad</option>
              <option value="4">Registro Civil</option>
            </select>
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
name: "Edit",
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
          "pers_nombre": this.Lista.pers_nombre,
          "pers_apellido": this.Lista.pers_apellido,
          "pers_identificacion": this.Lista.pers_identificacion,
          "tipo_identificacion": this.Lista.tipo_identificacion,
      }
      axios.put("http://localhost:8000/api/persona/" + this.$route.params.id + "/", post).then(result => {
          console.log(result);
          Swal.fire({
            icon: 'success',
            title: 'Datos Editados',
            text: 'Correctamente',
            timer: 3000,
          })
          //this.Lista.id="";
          this.Lista.pers_nombre="";
          this.Lista.pers_apellido="";
          this.Lista.pers_identificacion="";
          this.Lista.tipo_identificacion="";

      })
  },
  salir(){
    this.$router.push("/persona");
  },
},

mounted() {
  let id = this.$route.params.id;
  let direccion = "http://localhost:8000/api/persona/"
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