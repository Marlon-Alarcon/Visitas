<template>
  <h1>Editar Estudiante</h1>
      <form>
          <!--<td>
              <input type="text" id="id" name="id" v-model="Lista.id">
          </td>-->
          <div class="mx-auto"  style="width: 300px;">
            <label for="exampleInputEmail1" class="form-label">Ingrese la edad </label>
              <input type="text" id="estu_edad" name="estu_edad" v-model="Lista.estu_edad">
          </div>
          <br>
          <div class="mx-auto"  style="width: 300px;">
            <label for="exampleInputEmail1" class="form-label">Ingrese el Id de Persona </label>
              <input type="text" id="persona" name="persona" v-model="Lista.persona">
          </div>
          <br>
          <div class="mx-auto input-group flex-nowrap"  style="width: 300px;">
            <select class="form-select" v-model="Lista.tipo_estado" aria-label="Default select example" required>
              <option selected disabled value="">Tipo de estado</option>
              <option value="11">Activo</option>
              <option value="12">Inactivo</option>
              <option value="13">Suspendido</option>
            </select>
          </div>
      </form>
  <button type="submit" class="btn btn-primary" v-on:click="editar()">Editar</button>
</template>

<script>
import axios from 'axios';

export default {
name: "EditarEstudiante",
data() {
  return {
    Lista: [],
  }
},
methods: {
  editar() {
      let post = {
          //"id": this.Lista.id,
          "estu_edad": this.Lista.estu_edad,
          "persona": this.Lista.persona,
          "tipo_estado": this.Lista.tipo_estado,
      }
      axios.put("http://localhost:8000/api/estudiante/" + this.$route.params.id + "/", post).then(result => {
          console.log(result);
          //this.Lista.id="";
          this.Lista.estu_edad="";
          this.Lista.persona="";
          this.Lista.tipo_estado="";
      })
  },
},

mounted() {
  let id = this.$route.params.id;
  let direccion = "http://localhost:8000/api/estudiante/"
  axios.get(direccion + id).then(data => {
      this.Lista = data.data;
  })
},
}
</script>