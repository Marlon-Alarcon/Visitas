<template>
    <div class="container center">
        <div class="row container">
              <h2 class="text-center animate__animated animate__heartBeat">CONSULTA 2</h2>
              <h6 class="text-center"> <small>Consulta discriminando el tipo de Visitante</small> </h6>
        </div>
    </div>
    <br><br>
    <div class="form-group row justify-content-center">
        <label for="input" class="col-sm-2 col-form-label">Tipo de visitante</label>
        <div class="col-sm-4">
            <input type="text" class="form-control" placeholder="Tipo de visitante" aria-label="regis" aria-describedby="addon-wrapping" id="regis" name="regis" v-model="regis">
        </div>
    </div>
    <br>

    <br>
    <div class="col-12">
          <br>
        <div class="row">
            <div class="col clearfix">
                <button type="button" class="btn btn-outline-danger" data-bs-dismiss="modal" v-on:click="mostrar()">mostrar</button>
            </div>
            <div class="col clearfix">
                <button type="button" class="btn btn-outline-danger" data-bs-dismiss="modal" v-on:click="exportToPDF()">Generar PDF</button>
            </div>
        </div>
    </div>
    
    <div class="col-md-12" id="pdf">
            <br>
            <br>
            <table class="table table-primary table-striped table-bordered table-hover table-responsive " v-if="Lista.lent!=0">
                <thead>
                <tr>
                    <th class="text-center">ID</th>
                    <th class="text-center">Nombre Visitante</th>
                    <th class="text-center">Apellido Visitante</th>
                    <th class="text-center">Parentesco</th>
                    <th class="text-center">Sexo</th>
                    <th class="text-center">Tipo Visitante</th>
                </tr>
                </thead>
                <tbody v-for="i in Lista" :key="i.id">
                    <tr>
                        <td class="text-center">{{i.id}}</td>
                        <td class="text-center">{{i.persona__pers_nombre}}</td>
                        <td class="text-center">{{i.persona__pers_apellido}}</td>
                        <td class="text-center">{{i.tipo_parentesco__maes_nombre}}</td>
                        <td class="text-center">{{i.tipo_sexo__maes_nombre}}</td>
                        <td class="text-center">{{i.tipo_visitante__maes_nombre}}</td>
                    </tr>
                </tbody>
            </table>
    </div>
    
</template>

<script>

import axios from 'axios';
import html2pdf from "html2pdf.js";

export default{
    name: 'Consulta2View',
    data() {
        return{
        Lista: [],
        persona__pers_nombre: "",
        persona__pers_apellido: "",
        tipo_parentesco__maes_nombre: "",
        tipo_sexo__maes_nombre: "",
        tipo_visitante__maes_nombre: "",
        regis: "",
        }
    },
    methods: {
        mostrar (){
            let post = {
                "regis" : this.regis,
            }
            axios.post('http://localhost:8000/api-v/consulta2/', post)
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
    axios.get('http://localhost:8000/api-v/consulta2/').then(data => {
      this.Lista = data.data;
      //console.log( data.data);
    })
  },
}
</script>