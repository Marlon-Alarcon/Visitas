<template>
  <h1>Editar Persona</h1>
      <form>
          <!--<td>
              <input type="text" id="id" name="id" v-model="Lista.id">
          </td>-->
          <div class="mx-auto"  style="width: 300px;">
            <label for="exampleInputEmail1" class="form-label">Ingrese la el nombre </label>
              <input type="text" id="pers_nombre" name="pers_nombre" v-model="Lista.pers_nombre">
          </div>
          <br>
          <div class="mx-auto"  style="width: 300px;">
            <label for="exampleInputEmail1" class="form-label">Ingrese la el apellido </label>
              <input type="text" id="pers_apellido" name="pers_apellido" v-model="Lista.pers_apellido">
          </div>
          <br>
          <div class="mx-auto"  style="width: 300px;">
            <label for="exampleInputEmail1" class="form-label">Ingrese la el numero de identificacion </label>
              <input type="text" id="pers_identificacion" name="pers_identificacion" v-model="Lista.pers_identificacion">
          </div>
          <br>
          <div class="mx-auto input-group flex-nowrap"  style="width: 300px;">
            <select class="form-select" v-model="Lista.tipo_identificacion" aria-label="Default select example" required>
              <option selected disabled value="">Tipo de Identificacion</option>
              <option value="2">Cedula</option>
              <option value="3">Tarjeta de Identidad</option>
              <option value="4">Registro Civil</option>
            </select>
          </div>
      </form>
  <button type="submit" class="btn btn-primary" v-on:click="editar()">Editar</button>
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
      let post = {
          //"id": this.Lista.id,
          "pers_nombre": this.Lista.pers_nombre,
          "pers_apellido": this.Lista.pers_apellido,
          "pers_identificacion": this.Lista.pers_identificacion,
          "tipo_identificacion": this.Lista.tipo_identificacion,
      }
      axios.put("http://localhost:8000/api/persona/" + this.$route.params.id + "/", post).then(result => {
          console.log(result);
          //this.Lista.id="";
          this.Lista.pers_nombre="";
          this.Lista.pers_apellido="";
          this.Lista.pers_identificacion="";
          this.Lista.tipo_identificacion="";
      })
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