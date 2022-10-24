<template>

    <div class="container center">
            <div class="row container">
                  
                  <h2 class="text-center">Administracion Visitas</h2>
     
            </div>
    
            <div class="col-12 text-center">
                  <button type="button" class="btn btn-primary" data-bs-toggle="modal" data-bs-target="#exampleModal">
                    Agregar
                  </button>
                  
                  <!-- Modal -->
                  <div class="modal fade modal-dialog modal-lg" id="exampleModal" tabindex="-1" aria-labelledby="exampleModalLabel" aria-hidden="true">
                    <div class="modal-dialog">
                      <div class="modal-content">
                        <div class="modal-header">
                          <h5 class="modal-title container-center" id="exampleModalLabel">Ingresar Datos</h5>
                          <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
                        </div>
                        <div class="modal-body">
                          <div class="input-group flex-nowrap">
                            <input type="text" class="form-control" placeholder="id" aria-describedby="addon-wrapping" id="id" name="id" v-model="id">
                          </div>
                          <div class="input-group flex-nowrap">
                            <input type="text" class="form-control" placeholder="Hora de Ingreso" aria-label="visi_h_ingreso" aria-describedby="addon-wrapping" id="visi_h_ingreso" name="visi_h_ingreso" v-model="visi_h_ingreso">
                          </div>
                          <div class="input-group flex-nowrap">
                            <input type="text" class="form-control" placeholder="Hora de salida" aria-describedby="addon-wrapping" id="visi_h_salida" name="visi_h_salida" v-model="visi_h_salida">
                          </div>
                          <div class="input-group flex-nowrap">
                            <input type="date" class="form-control" placeholder="Fecha" aria-describedby="addon-wrapping" id="visi_fecha" name="visi_fecha" v-model="visi_fecha">
                          </div>
                          <div class="input-group flex-nowrap">
                            <input type="text" class="form-control" placeholder="Id de Visitante" aria-describedby="addon-wrapping" id="visitante" name="visitante" v-model="visitante">
                          </div>
                          <div class="input-group flex-nowrap">
                            <input type="text" class="form-control" placeholder="Id de Estudiante" aria-describedby="addon-wrapping" id="estudiante" name="estudiante" v-model="estudiante">
                          </div>
                        </div>
                        <div class="modal-footer">
                          <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">Salir</button>
                          <button type="button" class="btn btn-primary"  v-on:click="registrar()">Guardar</button>
                        </div>
                      </div>
                    </div>
                  </div>
                </div>
                    
                    <div class="col-md-12">
                      <br>
                      <br>
                        <table class="table table-primary table-striped table-bordered table-hover">
                          <thead>
                            <tr>
                              <th class="text-center">ID</th>
                              <th class="text-center">HORA INGRESO</th>
                              <th class="text-center">HORA SALIDA</th>
                              <th class="text-center">FECHA</th>
                              <th class="text-center">VISITANTE</th>
                              <th class="text-center">ESTUDIANTE</th>
                              <th class="text-center">ELIMINAR</th>
                            </tr>
                          </thead>
                          <tbody v-for="i in Lista" :key="i.id">
                              <tr>
                                  <td class="text-center">{{i.id}}</td>
                                  <td class="text-center">{{i.visi_h_ingreso}}</td>
                                  <td class="text-center">{{i.visi_h_salida}}</td>
                                  <td class="text-center">{{i.visi_fecha}}</td>
                                  <td class="text-center">{{i.visitante}}</td>
                                  <td class="text-center">{{i.estudiante}}</td>
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
    
    export default{
      name: 'VisitaView',
      data() {
        return{
          Lista: null,
          id: "",
          visi_h_ingreso: "",
          visi_h_salida: "",
          visi_fecha: "",
          visitante: "",
          estudiante: "",
        }
      },
      methods: {
        registrar(){
          let post = {
          "id": this.id,
          "visi_h_ingreso": this.visi_h_ingreso,
          "visi_h_salida": this.visi_h_salida,
          "visi_fecha": this.visi_fecha,
          "visitante": this.visitante,
          "estudiante": this.estudiante,
          }
          axios.post('http://localhost:8000/api-v/Visita/', post)
            .then(result => {
              this.id="";
              this.visi_h_ingreso="";
              this.visi_h_salida="";
              this.visi_fecha="";
              this.visitante="";
              this.estudiante="";
              this.updated()
    
              console.log(result)
            })
        },
        editar(id) {
          console.log(id)
          this.$router.push('editVisitante/' + id);
        },
        eliminar(id) {
          console.log(id)

            var op = window.confirm('¿Desea Eliminar al Visitante?')

            if (op){
            axios.delete("http://localhost:8000/api-v/Visita/" + id + "/").then(result => {
            this.updated()
            console.log(result);
             })
         }
         
        },
        updated() {
          let direccion = "http://localhost:8000/api-v/Visita/";
          axios.get(direccion).then(data => {
            this.Lista = data.data
          })
        }
      },
      mounted(){
        axios.get('http://localhost:8000/api-v/Visita/').then(data => {
          this.Lista = data.data;
          //console.log( data.data);
        })
      },
    }
    
    </script>