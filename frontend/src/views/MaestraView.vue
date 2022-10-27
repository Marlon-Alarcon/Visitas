<template>

    <div class="container center">
            <div class="row container">
                  
                  <h2 class="text-center animate__animated animate__heartBeat">Administrar datos Maestros</h2>
     
            </div>
            
    
            <div class="col-12 text-center">
                  <button type="button" class="btn btn-outline-primary" data-bs-toggle="modal" data-bs-target="#exampleModal">
                    <i class="material-icons material-icons-outlined">add_circle</i> Agregar
                  </button>
                  
                  <!-- Modal -->
                  <div class="modal fade " id="exampleModal" tabindex="-1" aria-labelledby="exampleModalLabel" aria-hidden="true">
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
                            <input type="text" class="form-control" placeholder="Nombre" aria-label="maes_nombre" aria-describedby="addon-wrapping" id="maes_nombre" name="maes_nombre" v-model="maes_nombre">
                          </div>
                          <div class="input-group flex-nowrap">
                            <input type="text" class="form-control" placeholder="Valor" aria-describedby="addon-wrapping" id="maes_valor" name="maes_valor" v-model="maes_valor">
                          </div>
                          <div class="input-group flex-nowrap">
                            <input type="text" class="form-control" placeholder="Dependencia" aria-describedby="addon-wrapping" id="maes_dependencia" name="maes_dependencia" v-model="maes_dependencia">
                          </div>
                          <div class="input-group flex-nowrap">
                            <input type="text" class="form-control" placeholder="Estado" aria-describedby="addon-wrapping" id="maes_tipo_estado" name="maes_tipo_estado" v-model="maes_tipo_estado">
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
                              <th class="text-center">NOMBRE</th>
                              <th class="text-center">VALOR</th>
                              <th class="text-center">DEPENDENCIA</th>
                              <th class="text-center">ESTADO</th>
                              <th class="text-center">ELIMINAR</th>
                            </tr>
                          </thead>
                          <tbody v-for="i in Lista" :key="i.id">
                              <tr>
                                  <td class="text-center">{{i.id}}</td>
                                  <td class="text-center">{{i.maes_nombre}}</td>
                                  <td class="text-center">{{i.maes_valor}}</td>
                                  <td class="text-center">{{i.maes_dependencia}}</td>
                                  <td class="text-center">{{i.maes_tipo_estado}}</td>
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
      name: 'MaestraView',
      data() {
        return{
          Lista: null,
          id: "",
          maes_nombre: "",
          maes_valor: "",
          maes_dependencia: "",
          maes_tipo_estado: "",
        }
      },
      methods: {
        registrar(){
          let post = {
          "id": this.id,
          "maes_nombre": this.maes_nombre,
          "maes_valor": this.maes_valor,
          "maes_dependencia": this.maes_dependencia,
          "maes_tipo_estado": this.maes_tipo_estado,
          }
          axios.post('http://localhost:8000/api-m/maestra/', post)
            .then(result => {
              this.id="";
              this.maes_nombre="";
              this.maes_valor="";
              this.maes_dependencia="";
              this.maes_tipo_estado="";
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

            var op = window.confirm('¿Desea Eliminar un dato maestro?')

            if (op){
            axios.delete("http://localhost:8000/api-m/maestra/" + id + "/").then(result => {
            this.updated()
            console.log(result);
             })
         }
         
        },
        updated() {
          let direccion = "http://localhost:8000/api-m/maestra/";
          axios.get(direccion).then(data => {
            this.Lista = data.data
          })
        }
      },
      mounted(){
        axios.get('http://localhost:8000/api-m/maestra/').then(data => {
          this.Lista = data.data;
          //console.log( data.data);
        })
      },
    }
    </script>