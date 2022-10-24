<template>
    <h1>editar</h1>
    <table>
        <tr>
            <!--<td>
                <input type="text" id="id" name="id" v-model="Lista.id">
            </td>-->
            <td>
                <input type="text" id="pers_nombre" name="pers_nombre" v-model="Lista.pers_nombre">
            </td>
            <td>
                <input type="text" id="pers_apellido" name="pers_apellido" v-model="Lista.pers_apellido">
            </td>
            <td>
                <input type="text" id="pers_identificacion" name="pers_identificacion" v-model="Lista.pers_identificacion">
            </td>
            <td>
                <input type="text" id="tipo_identificacion" name="tipo_identificacion" v-model="Lista.tipo_identificacion">
            </td>
        </tr>
    <button type="submit" class="btn btn-primary" v-on:click="editar()">Editar</button>
    </table>
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
