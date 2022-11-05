<template>
    <h1>Editar Visitante</h1>
        <form>
            <!--<td>
                <input type="text" id="id" name="id" v-model="Lista.id">
            </td>-->
            <div class="form-group row justify-content-center">
              <label for="input" class="col-sm-2 col-form-label">Ingrese el telefono</label>
              <div class="col-sm-4">
                <input type="text" class="form-control" id="visit_telefono" name="visit_telefono" v-model="Lista.visit_telefono" required>
              </div>
          </div>
            <br>
            <div class="form-group row justify-content-center">
              <label for="input" class="col-sm-2 col-form-label">Ingrese el lugar de procedencia</label>
              <div class="col-sm-4">
                <input type="text" class="form-control" id="visit_procedencia" name="visit_procedencia" v-model="Lista.visit_procedencia" required>
              </div>
          </div>
            <br>
            <div class="form-group row justify-content-center">
              <label for="input" class="col-sm-2 col-form-label">Ingrese el Id de personas</label>
              <div class="col-sm-4">
                <input type="text" class="form-control" id="persona" name="persona" v-model="Lista.persona" required>
              </div>
          </div>
            <br>
            <div class="form-group row justify-content-center">
              <label for="input"  class="col-sm-2 col-form-label ">Tipo de Parentesco </label>

              <div class="col-sm-4">
                <select class="form-select" v-model="Lista.tipo_parentesco" aria-label="Default select example" required>
                <option selected disabled value="">Parentesco</option>
                <option value="6">Padre</option>
                <option value="7">Madre</option>
                <option value="8">Hermanos</option>
                <option value="9">Otros</option>
              </select>
              </div>
            </div>
            <br>
            <div class="form-group row justify-content-center">
              <label for="input"  class="col-sm-2 col-form-label ">Tipo de Sexo </label>

              <div class="col-sm-4">
                <select class="form-select" v-model="Lista.tipo_sexo" aria-label="Default select example" required>
                <option selected disabled value="">Sexo</option>
                <option value="15">Masculino</option>
                <option value="16">Femenino</option>
              </select>
              </div>
            </div>
            <br>
            <div class="form-group row justify-content-center">
              <label for="input"  class="col-sm-2 col-form-label ">Tipo de Visitante </label>

              <div class="col-sm-4">
                <select class="form-select" v-model="Lista.tipo_visitante" aria-label="Default select example" required>
                <option selected disabled value="">Visitante</option>
                <option value="18">Interno</option>
                <option value="19">Externo</option>
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
  name: "EditarVisitante",
  data() {
    return {
      Lista: [],
    }
  },
  methods: {
    editar() {
        let post = {
            //"id": this.Lista.id,
            "visit_telefono": this.Lista.visit_telefono,
            "visit_procedencia": this.Lista.visit_procedencia,
            "persona": this.Lista.persona,
            "tipo_parentesco": this.Lista.tipo_parentesco,
            "tipo_sexo": this.Lista.tipo_sexo,
            "tipo_visitante": this.Lista.tipo_visitante,
        }
        axios.put("http://localhost:8000/api/visitante/" + this.$route.params.id + "/", post).then(result => {
            console.log(result);
            //this.Lista.id="";
            Swal.fire({
              icon: 'success',
              title: 'Datos Editados',
              text: 'Correctamente',
            })

            this.Lista.visit_telefono="";
            this.Lista.visit_procedencia="";
            this.Lista.persona="";
            this.Lista.tipo_parentesco="";
            this.Lista.tipo_sexo="";
            this.Lista.tipo_visitante="";
        })
    },
      salir(){
      this.$router.push("/visitante");
    },
  },
  
  mounted() {
    let id = this.$route.params.id;
    let direccion = "http://localhost:8000/api/visitante/"
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