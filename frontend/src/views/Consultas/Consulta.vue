<template>
    <div class="container center">
        <div class="row container">
              <h2 class="text-center animate__animated animate__heartBeat">Primera Consulta</h2>
              <h1></h1>
              <h5 class="text-center"> <small> Historial de visitantes y sus respectivos estudiantes, en un lapzo de tiempo </small> </h5>
        </div>
    </div>
    <br><br>
    <div class="form-group row justify-content-center">
        <label for="input" class="col-sm-2 col-form-label">Fecha de inicio</label>
        <div class="col-sm-4">
            <input type="Date" class="form-control" placeholder="Fecha1" aria-label="fecha1" aria-describedby="addon-wrapping" id="fecha1" name="fecha1" v-model="fecha1">
        </div>
    </div>
    <br>
    <div class="form-group row justify-content-center">
        <label for="input" class="col-sm-2 col-form-label">Fecha final</label>
        <div class="col-sm-4">
            <input type="Date" class="form-control" placeholder="fecha2" aria-label="fecha2" aria-describedby="addon-wrapping" id="fecha2" name="fecha2" v-model="fecha2">
        </div>
    </div>

    <div class="col-12">
          <br>
        <div class="row">
            <div class="col clearfix">
                <button type="button" class="btn btn-outline-danger" data-bs-dismiss="modal" v-on:click="mostrar()">mostrar</button>
            </div>

            <div class="col clearfix">
                <button type="button" class="btn btn-outline-danger" data-bs-dismiss="modal" v-on:click="exportToPDF()">PDF</button>
            </div>
        </div>
    </div>
    <div class="col-md-12" id="pdf">
            <br>
            <table class="table table-primary table-striped table-bordered table-hover table-responsive " v-if="Lista.lent!=0">
                <thead>
                <tr>
                    <th class="text-center">ID</th>
                    <th class="text-center">Ingreso</th>
                    <th class="text-center">Salida</th>
                    <th class="text-center">Fecha</th>
                    <th class="text-center">Nombre del visitante</th>
                    <th class="text-center">Procedencia</th>
                    <th class="text-center">Nombre estudiante</th>
                    <th class="text-center">Edad</th>
                    <th class="text-center">Tipo de estado</th>
                </tr>
                </thead>
                <tbody v-for="i in Lista" :key="i.id">
                    <tr>
                        <td class="text-center">{{i.id}}</td>
                        <td class="text-center">{{i.visi_h_ingreso}}</td>
                        <td class="text-center">{{i.visi_h_salida}}</td>
                        <td class="text-center">{{i.visi_fecha}}</td>
                        <td class="text-center">{{i.visitante__persona__pers_nombre}}</td>
                        <td class="text-center">{{i.visitante__visit_procedencia}}</td>
                        <td class="text-center">{{i.estudiante__persona__pers_nombre}}</td>
                        <td class="text-center">{{i.estudiante__estu_edad}}</td>
                        <td class="text-center">{{i.estudiante__tipo_estado__maes_nombre}}</td>
                    </tr>
                </tbody>
            </table>
    </div>
    
</template>

<script>

import axios from 'axios';
import html2pdf from "html2pdf.js";

export default{
    name: 'Consulta1View',
    data() {
        return{
        Lista: [],
        visi_h_ingreso: "",
        visi_h_salida: "",
        visi_fecha: "",
        visitante__persona__pers_nombre: "",
        visitante__visit_procedencia: "",
        estudiante__persona__pers_nombre: "",
        estudiante__estu_edad: "",
        estudiante__tipo_estado__maes_nombre: "",
        fecha1: "",
        fecha2: "",
        }
    },
    methods: {
        mostrar (){
            let post = {
                "fecha1" : this.fecha1,
                "fecha2" : this.fecha2,
            }
            axios.post('http://localhost:8000/api-v/consulta/', post)
            .then(result => {
                this.Lista= result.data.data;

                console.log(result.data.data)
            }).catch(error => {
                console.log(error)
            })
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
        html2pdf(document.getElementById("pdf"), {
                    margin: 1,
                filename: "List Historial.pdf",
            jsPDF: { unit: 'in', format: 'A3', orientation: 'landscape', text: 'hola' }
                });
        },
    },
    mounted(){
    axios.get('http://localhost:8000/api-v/consulta/').then(data => {
      this.Lista = data.data;
      //console.log( data.data);
    })
  },
}
</script>