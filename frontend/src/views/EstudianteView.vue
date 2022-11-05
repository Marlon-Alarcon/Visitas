<template>
<div class="container center">
        <div class="row container">
              <h2 class="text-center animate__animated animate__heartBeat">Administracion de datos Estudiante</h2>
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
                        <h1 class="modal-title fs-5 container center" id="exampleModalLabel">AGREGAR ESTUDIANTE</h1>
                        <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
                      </div>
                      <div class="modal-body">
                          <div class="input-group flex-nowrap">
                            <input type="text" class="form-control" placeholder="Id" aria-describedby="addon-wrapping" id="id" name="id" v-model="id">
                          </div>
                          <br>
                          <div class="input-group flex-nowrap">
                            <input type="text" class="form-control" placeholder="Edad de estudiante" aria-label="estu_edad" aria-describedby="addon-wrapping" id="pers_nombre" name="estu_edad" v-model="estu_edad">
                          </div>
                          <br>
                          <div class="input-group flex-nowrap">
                            <input type="text" class="form-control" placeholder="ID de Persona" aria-label="persona" aria-describedby="addon-wrapping" id="persona" name="persona" v-model="persona">
                          </div>
                          <br>
                          <select class="form-select" v-model="tipo_estado" aria-label="Default select example">
                            <option selected disabled value="">Tipo de Estado</option>
                            <option value="11">Activo</option>
                            <option value="12">Inactivo</option>
                            <option value="13">Suspendido</option>
                          </select>
                      </div>
                      <div class="modal-footer">
                        <button type="button" class="btn btn-outline-danger" data-bs-dismiss="modal">Cerrar</button>
                        <button type="button" class="btn btn-outline-success" v-on:click="registrar()">Guardar</button>
                      </div>
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
                          <th class="text-center">EDAD</th>
                          <th class="text-center">NOMBRE</th>
                          <th class="text-center">ESTADO</th>
                          <th class="text-center">EDITAR</th>
                          <th class="text-center">ELIMINAR</th>
                        </tr>
                      </thead>
                      <tbody v-for="i in Lista" :key="i.id">
                          <tr>
                              <td class="text-center">{{i.id}}</td>
                              <td class="text-center">{{i.estu_edad}}</td>
                              <td class="text-center">{{i.persona}}</td>
                              <td class="text-center">{{i.tipo_estado}}</td>
                              <td class="text-center">
                                <button type="button" class="btn btn-outline-primary" v-on:click="editar(i.id)">
                                    <i class="material-icons material-icons-outlined">edit</i>
                                </button>
                              </td>
                              <td class="text-center">
                                <button type="button" class="btn btn-outline-primary" v-on:click="eliminar(i.id)">
                                    <i class="material-icons material-icons-outlined">person_remove</i>
                                </button>
                              </td>
                          </tr>
                      </tbody>
                    </table>
                </div>
</template>

<script>
import axios from 'axios';
import Swal from 'sweetalert2'

export default{
  name: 'EstudianteView',
  data() {
    return{
      Lista: null,
      id: "",
      estu_edad: "",
      persona: "",
      tipo_estado: "",
    }
  },
  methods: {
    registrar(){
      let post = {
      "id": this.id,
      "estu_edad": this.estu_edad,
      "persona": this.persona,
      "tipo_estado": this.tipo_estado,
      }
      axios.post('http://localhost:8000/api/estudiante/', post)
        .then(result => {
          this.id="";
          this.estu_edad="";
          this.persona="";
          this.tipo_estado="";

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
      this.$router.push('editar/' + id);
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
            axios.delete("http://localhost:8000/api/estudiante/" + id + "/").then(result => {
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
      let direccion = "http://localhost:8000/api/estudiante/";
      axios.get(direccion).then(data => {
        this.Lista = data.data
      })
    }
  },
  mounted(){
    axios.get('http://localhost:8000/api/estudiante/').then(data => {
      this.Lista = data.data;
      //console.log( data.data);
    })
  },
}
</script>