<template>

    <div class="container center">
            <div class="row container">
                  
                  <h2 class="text-center animate__animated animate__heartBeat">Administracion Visitas</h2>
     
            </div>
    
            <div class="col-12">
              <br>
              <div class="row">
                <div class="col clearfix">
                    <button type="button" class="btn btn-outline-primary" data-bs-toggle="modal" data-bs-target="#exampleModal">
                      <i class="material-icons material-icons-outlined">add_circle</i> Agregar
                    </button>
                </div>
              <div class="col clearfix">
                <button @click="exportToPDF" type="button" class="btn btn-outline-warning" >Exportar como PDF</button>
              </div>
          </div>
                  
                  <!-- Modal -->
                  <div class="modal fade" id="exampleModal" tabindex="-1" aria-labelledby="exampleModalLabel" aria-hidden="true">
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
                          <br>
                          <div class="input-group flex-nowrap">
                            <input type="time" class="form-control" placeholder="Hora de Ingreso" aria-label="visi_h_ingreso" aria-describedby="addon-wrapping" id="visi_h_ingreso" name="visi_h_ingreso" v-model="visi_h_ingreso">
                          </div>
                          <br>
                          <div class="input-group flex-nowrap">
                            <input type="time" class="form-control" placeholder="Hora de salida" aria-describedby="addon-wrapping" id="visi_h_salida" name="visi_h_salida" v-model="visi_h_salida">
                          </div>
                          <br>
                          <div class="input-group flex-nowrap">
                            <input type="date" class="form-control" placeholder="Fecha" aria-describedby="addon-wrapping" id="visi_fecha" name="visi_fecha" v-model="visi_fecha">
                          </div>
                          <br>
                          <div class="input-group flex-nowrap">
                            <input type="text" class="form-control" placeholder="Id de Visitante" aria-describedby="addon-wrapping" id="visitante" name="visitante" v-model="visitante">
                          </div>
                          <br>
                          <div class="input-group flex-nowrap">
                            <input type="text" class="form-control" placeholder="Id de Estudiante" aria-describedby="addon-wrapping" id="estudiante" name="estudiante" v-model="estudiante">
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
                    
                    <div class="col-md-12" ref="document">
                      <br>
                      <br>
                      <div id="element-to-convert">
                        <table class="table table-primary table-striped table-bordered table-hover table-responsive">
                          <thead>
                            <tr>
                              <th class="text-center">ID</th>
                              <th class="text-center">HORA INGRESO</th>
                              <th class="text-center">HORA SALIDA</th>
                              <th class="text-center">FECHA</th>
                              <th class="text-center">VISITANTE</th>
                              <th class="text-center">ESTUDIANTE</th>
                              <th class="text-center">ELIMINAR</th>
                              <th class="text-center">EDITAR</th>
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
    </div>
    
    </template>
    
<script>
import axios from 'axios';
import Swal from 'sweetalert2'
import html2pdf from "html2pdf.js";


export default {
  name: 'VisitanteView',
  data() {
    return {
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
    registrar() {
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
          this.id = "";
          this.visi_h_ingreso = "";
          this.visi_h_salida = "";
          this.visi_fecha = "";
          this.visitante = "";
          this.estudiante = "";
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
      this.$router.push('editVisita/' + id);
    },
    exportToPDF() {
      const Swal = require('sweetalert2')
        Swal.fire({
        position: 'top-end',
        icon: 'success',
        title: 'PDF GENERADO',
        showConfirmButton: false,
        timer: 1500
      })

      html2pdf(document.getElementById("element-to-convert"), {
				margin: 1,
  			filename: "List Visita.pdf",
        jsPDF: { unit: 'in', format: 'A3', orientation: 'landscape' }
			});
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
          axios.delete("http://localhost:8000/api-v/Visita/" + id + "/").then(result => {
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
      let direccion = "http://localhost:8000/api-v/Visita/";
      axios.get(direccion).then(data => {
        this.Lista = data.data
      })
    }
  },
  mounted() {
    axios.get('http://localhost:8000/api-v/Visita/').then(data => {
      this.Lista = data.data;
      //console.log( data.data);
    })
  },
}

</script>