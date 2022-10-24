<template>

    <div class="container center">
            <div class="row container">
                  
                  <h2 class="text-center">Administracion de datos Visitantes</h2>
     
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
                            <input type="text" class="form-control" placeholder="Id" aria-describedby="addon-wrapping" id="id" name="id" v-model="id">
                          </div>
                          <div class="input-group flex-nowrap">
                            <input type="text" class="form-control" placeholder="Telefono" aria-label="visit_telefono" aria-describedby="addon-wrapping" id="visit_telefono" name="visit_telefono" v-model="visit_telefono">
                          </div>
                          <div class="input-group flex-nowrap">
                            <input type="text" class="form-control" placeholder="Lugar de Procedencia" aria-describedby="addon-wrapping" id="visit_procedencia" name="visit_procedencia" v-model="visit_procedencia">
                          </div>
                          <div class="input-group flex-nowrap">
                            <input type="text" class="form-control" placeholder="ID Persona" aria-describedby="addon-wrapping" id="pers_identificacion" name="pers_identificacion" v-model="persona">
                          </div>
                          <div class="input-group flex-nowrap">
                              <select class="form-select" v-model="tipo_parentesco" aria-label="Default select example" required>
                                <option selected disabled value="">Parentesco</option>
                                <option value="6">Padre</option>
                                <option value="7">Madre</option>
                                <option value="8">Hermanos</option>
                                <option value="9">Otros</option>
                              </select>
                          </div>

                          <div class="input-group flex-nowrap">
                              <select class="form-select" v-model="tipo_sexo" aria-label="Default select example" required>
                                <option selected disabled value="">Sexo</option>
                                <option value="15">Masculino</option>
                                <option value="16">Femenino</option>
                              </select>
                          </div>

                          <div class="input-group flex-nowrap">
                              <select class="form-select" v-model="tipo_visitante" aria-label="Default select example" required>
                                <option selected disabled value="">Visitante</option>
                                <option value="18">Interno</option>
                                <option value="19">Externo</option>
                              </select>
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
                              <th class="text-center">TELEFONO</th>
                              <th class="text-center">PROCEDENCIA</th>
                              <th class="text-center">NOMBRE</th>
                              <th class="text-center">TIPO PARENTESCO</th>
                              <th class="text-center">SEXO</th>
                              <th class="text-center">TIPO VISITANTE</th>
                              <th class="text-center">ELIMINAR</th>
                            </tr>
                          </thead>
                          <tbody v-for="i in Lista" :key="i.id">
                              <tr>
                                  <td class="text-center">{{i.id}}</td>
                                  <td class="text-center">{{i.visit_telefono}}</td>
                                  <td class="text-center">{{i.visit_procedencia}}</td>
                                  <td class="text-center">{{i.persona}}</td>
                                  <td class="text-center">{{i.tipo_parentesco}}</td>
                                  <td class="text-center">{{i.tipo_sexo}}</td>
                                  <td class="text-center">{{i.tipo_visitante}}</td>
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
      name: 'VisitanteView',
      data() {
        return{
          Lista: null,
          id: "",
          visit_telefono: "",
          visit_procedencia: "",
          persona: "",
          tipo_parentesco: "",
          tipo_sexo: "",
          tipo_visitante: "",
        }
      },
      methods: {
        registrar(){
          let post = {
          "id": this.id,
          "visit_telefono": this.visit_telefono,
          "visit_procedencia": this.visit_procedencia,
          "persona": this.persona,
          "tipo_parentesco": this.tipo_parentesco,
          "tipo_sexo": this.tipo_sexo,
          "tipo_visitante": this.tipo_visitante,
          }
          axios.post('http://localhost:8000/api/visitante/', post)
            .then(result => {
              this.id="";
              this.visit_telefono="";
              this.visit_procedencia="";
              this.persona="";
              this.tipo_parentesco="";
              this.tipo_sexo="";
              this.tipo_visitante="";
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
            axios.delete("http://localhost:8000/api/visitante/" + id + "/").then(result => {
            this.updated()
            console.log(result);
             })
         }
         
        },
        updated() {
          let direccion = "http://localhost:8000/api/visitante/";
          axios.get(direccion).then(data => {
            this.Lista = data.data
          })
        }
      },
      mounted(){
        axios.get('http://localhost:8000/api/visitante/').then(data => {
          this.Lista = data.data;
          //console.log( data.data);
        })
      },
    }
    
    </script>