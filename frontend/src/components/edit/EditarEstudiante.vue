<template>
  <h1>Editar Estudiante</h1>
  <br>
      <form>
          <!--<td>
              <input type="text" id="id" name="id" v-model="Lista.id">
          </td>-->
          <div class="form-group row justify-content-center">
            <label for="input" class="col-sm-2 col-form-label">Edite la edad </label>
            <div class="col-sm-4">
              <input type="text" class="form-control" id="estu_edad" name="estu_edad" v-model="Lista.estu_edad">
            </div>
          </div>
          <br>
          <div class="form-group row justify-content-center">
            <label for="input" class="col-sm-2 col-form-label">Edite el Id de la Persona </label>
            <div class="col-sm-4">
              <input type="text" class="form-control" id="persona" name="persona" v-model="Lista.persona">
            </div>       
          </div>
          <br>
          <div class="form-group row justify-content-center">
            <label for="input" class="col-sm-2 col-form-label">Seleccione el estado </label>
            <div class="col-sm-4">
              <select class="form-select" v-model="Lista.tipo_estado" aria-label="Default select example" required>
                <option selected disabled value="">Tipo de estado</option>
                <option value="11">Activo</option>
                <option value="12">Inactivo</option>
                <option value="13">Suspendido</option>
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
import Swal from 'sweetalert2'

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
          Swal.fire({
            icon: 'success',
            title: 'Datos Editados',
          })

          this.Lista.estu_edad="";
          this.Lista.persona="";
          this.Lista.tipo_estado="";
      })
  },
  salir(){
    this.$router.push("/estudiante");
  }
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

<style>
.space {
  width: 10px;
  height: auto;
  display: inline-block;
}
</style>