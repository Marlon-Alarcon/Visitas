<template>
    <h1>Editar</h1>
    <br>
    <form class="content">
        <div class="mb-8">
            <label for="exampleInputEmail1" class="form-label">Ingrese la Edad </label>
            <input type="text"  placeholder="Edad" id="estu_edad" name="estu_edad" v-model="Lista.estu_edad">
        </div>
        <div class="mb-8">
            <label for="exampleInputEmail1" class="form-label">Ingrese la el nombre </label>
            <input type="text"  placeholder="persona" id="persona" name="persona" v-model="Lista.persona">
        </div>
        <div class="mb-8">
            <label for="exampleInputEmail1" class="form-label">Ingrese el tipo de estado </label>
            <input type="text"  placeholder="tipo_estado" id="tipo_estado" name="tipo_estado" v-model="Lista.tipo_estado">
        </div>
        <button type="submit" class="btn btn-primary" v-on:click="editar()">Editar</button>
    </form>
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
            "id": this.Lista.id,
            "estu_edad": this.Lista.estu_edad,
            "persona": this.Lista.persona,
            "tipo_estado": this.Lista.tipo_estado,
        }
        axios.put("http://localhost:8000/api/persona/" + this.$route.params.id + "/", post).then(result => {
            console.log(result);
            this.Lista.id="";
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
