<template>
    <h1>Editar Visitante</h1>
        <form>
            <!--<td>
                <input type="text" id="id" name="id" v-model="Lista.id">
            </td>-->
            <div class="mx-auto"  style="width: 300px;">
              <label for="exampleInputEmail1" class="form-label">Ingrese el telefono </label>
                <input type="text" id="visit_telefono" name="visit_telefono" v-model="Lista.visit_telefono">
            </div>
            <br>
            <div class="mx-auto"  style="width: 300px;">
              <label for="exampleInputEmail1" class="form-label">Ingrese el lugar de procedencia </label>
                <input type="text" id="visit_procedencia" name="visit_procedencia" v-model="Lista.visit_procedencia">
            </div>
            <br>
            <div class="mx-auto"  style="width: 300px;">
              <label for="exampleInputEmail1" class="form-label">Ingrese el Id de personas </label>
                <input type="text" id="persona" name="persona" v-model="Lista.persona">
            </div>
            <br>
            <div class="mx-auto input-group flex-nowrap"  style="width: 300px;">
              <select class="form-select" v-model="Lista.tipo_parentesco" aria-label="Default select example" required>
                <option selected disabled value="">Parentesco</option>
                <option value="6">Padre</option>
                <option value="7">Madre</option>
                <option value="8">Hermanos</option>
                <option value="9">Otros</option>
              </select>
            </div>
            <br>
            <div class="mx-auto input-group flex-nowrap"  style="width: 300px;">
              <select class="form-select" v-model="Lista.tipo_sexo" aria-label="Default select example" required>
                <option selected disabled value="">Sexo</option>
                <option value="15">Masculino</option>
                <option value="16">Femenino</option>
              </select>
            </div>
            <br>
            <div class="mx-auto input-group flex-nowrap"  style="width: 300px;">
              <select class="form-select" v-model="Lista.tipo_visitante" aria-label="Default select example" required>
                <option selected disabled value="">Visitante</option>
                <option value="18">Interno</option>
                <option value="19">Externo</option>
              </select>
            </div>
        </form>
        <br>
    <button type="submit" class="btn btn-primary" v-on:click="editar()">Editar</button>
  </template>
  
  <script>
  import axios from 'axios';
  
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
            this.Lista.visit_telefono="";
            this.Lista.visit_procedencia="";
            this.Lista.persona="";
            this.Lista.tipo_parentesco="";
            this.Lista.tipo_sexo="";
            this.Lista.tipo_visitante="";
        })
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