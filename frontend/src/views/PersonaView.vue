<template>

<div class="container center">
        <div class="row container">
              
              <h2 class="text-center animate__animated animate__heartBeat"> Administracion de datos Personas </h2>
 
        </div>

        <div class="col-12 text-center">
              <button type="button" class="btn btn-outline-primary" data-bs-toggle="modal" data-bs-target="#exampleModal">
                <i class="material-icons material-icons-outlined">add_circle</i> Agregar
              </button>

              <!-- Modal -->
              <div class="modal fade" id="exampleModal" tabindex="-1" aria-labelledby="exampleModalLabel" aria-hidden="true">
                <div class="modal-dialog">
                  <div class="modal-content">
                    <div class="modal-header">
                      <h5 class="modal-title container-center" id="exampleModalLabel">Ingresar Datos</h5>
                      <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
                    </div>
                    <br>
                    <div class="modal-body">
                      <div class="input-group flex-nowrap">
                        <input type="text" class="form-control" placeholder="Id" aria-describedby="addon-wrapping" id="id" name="id" v-model="id">
                      </div>
                      <br>
                      <div class="input-group flex-nowrap">
                        <input type="text" class="form-control" placeholder="Nombre" aria-label="pers_nombre" aria-describedby="addon-wrapping" id="pers_nombre" name="pers_nombre" v-model="pers_nombre">
                      </div>
                      <br>
                      <div class="input-group flex-nowrap">
                        <input type="text" class="form-control" placeholder="Apellido" aria-describedby="addon-wrapping" id="pers_apellido" name="pers_apellido" v-model="pers_apellido">
                      </div>
                      <br>
                      <div class="input-group flex-nowrap">
                        <input type="text" class="form-control" placeholder="N° Identificacion" aria-describedby="addon-wrapping" id="pers_identificacion" name="pers_identificacion" v-model="pers_identificacion">
                      </div>
                      <br>
                      <div class="input-group flex-nowrap">
                          <select class="form-select" v-model="tipo_identificacion" aria-label="Default select example" required>
                            <option selected disabled value="">Tipo de Identificacion</option>
                            <option value="2">Cedula</option>
                            <option value="3">Tarjeta de Identidad</option>
                            <option value="4">Registro Civil</option>
                          </select>
                        <!--<input type="text" class="form-control" placeholder="Tipo Identificacion" aria-describedby="addon-wrapping" id="tipo_identificacion" name="tipo_identificacion" v-model="tipo_identificacion">-->
                      </div>
                    </div>
                    <div class="modal-footer">
                      <button type="button" class="btn btn-outline-danger" data-bs-dismiss="modal">Salir</button>
                      <button type="button" class="btn btn-outline-success"  v-on:click="registrar()">Guardar</button>
                    </div>
                  </div>
                </div>
              </div>
            </div>
                
                <div class="col-md-12">
                  <br>
                  <br>
                    <table class="table table-primary table-striped table-bordered table-hover table-responsive">
                      <thead>
                        <tr>
                          <th class="text-center">ID</th>
                          <th class="text-center">NOMBRE</th>
                          <th class="text-center">APELLIDO</th>
                          <th class="text-center">CEDULA</th>
                          <th class="text-center">TIPO DE IDENTIFICACION</th>
                          <th class="text-center">EDITAR</th>
                          <th class="text-center">ELIMINAR</th>
                        </tr>
                      </thead>
                      <tbody v-for="i in Lista" :key="i.id">
                          <tr>
                              <td class="text-center">{{i.id}}</td>
                              <td class="text-center">{{i.pers_nombre}}</td>
                              <td class="text-center">{{i.pers_apellido}}</td>
                              <td class="text-center">{{i.pers_identificacion}}</td>
                              <td class="text-center">{{i.tipo_identificacion}}</td>
                              <td class="text-center">
                                <button type="button" class="btn btn-primary" v-on:click="editar(i.id)">
                                    <i class="material-icons material-icons-outlined">edit</i>
                                </button>
                              </td>
                              <td class="text-center">
                                <button type="button" class="btn btn-primary" v-on:click="eliminar(i.id)">
                                    <i class="material-icons material-icons-outlined">person_remove</i>
                                </button>
                              </td>
                          </tr>
                      </tbody>
                    </table>
                </div>
</div>

</template>

<script>

import axios from 'axios';
import Swal from 'sweetalert2'

export default{
  name: 'PersonaView',
  data() {
    return{
      Lista: null,
      id: "",
      pers_nombre: "",
      pers_apellido: "",
      pers_identificacion: "",
      tipo_identificacion: "",
    }
  },
  methods: {
    registrar(){
      let post = {
      "id": this.id,
      "pers_nombre": this.pers_nombre,
      "pers_apellido": this.pers_apellido,
      "pers_identificacion": this.pers_identificacion,
      "tipo_identificacion": this.tipo_identificacion,
      }
      axios.post('http://localhost:8000/api/persona/', post)
        .then(result => {
          this.id="";
          this.pers_nombre="";
          this.pers_apellido="";
          this.pers_identificacion="";
          this.tipo_identificacion="";
          
          Swal.fire({
            icon: 'success',
            title: 'Excelente',
            text: 'Datos agregados correctamente!',
          })

          this.updated()

          console.log(result)
        })
    },
    editar(id) {
      console.log(id)
      this.$router.push('Edit/' + id);
    },
    eliminar(id) {
      console.log(id)
      Swal.fire({
      title: 'Desea eliminarlo?',
      text: "Esta acción es irreversible!",
      icon: 'warning',
      showCancelButton: true,
      confirmButtonColor: '#3085d6',
      cancelButtonColor: '#d33',
      confirmButtonText: 'Si, Eliminar!'
        }).then((result) => {
          if (result.isConfirmed) {
            axios.delete("http://localhost:8000/api/persona/" + id + "/").then(result => {
              this.updated()
              console.log(result);
        })
            Swal.fire(
              'Eliminado!',
              'Dato eliminado correctamente.',
              'success'
            )
          }
        })

    },
    updated() {
      let direccion = "http://localhost:8000/api/persona/";
      axios.get(direccion).then(data => {
        this.Lista = data.data
      })
    }
  },
  mounted(){
        axios.get('http://localhost:8000/api/persona/').then(data => {
          this.Lista = data.data;
          //console.log( data.data);
        })
      },
}

</script>