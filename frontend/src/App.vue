<template>
  <div class="d-flex" id="wrapper">

    <!-- Sidebar -->
    <div class="bg-light border-right" id="sidebar-wrapper">
      <div class="sidebar-heading text-center">
        <h1 class="text-gradient text-center"><b>Vue Sidebar</b></h1>
      </div>
      <br>
      
      <div class="list-group list-group-flush">
        <a>
          <router-link to="/" class="list-group-item list-group-item-action bg-light "><i
              class="material-icons material-icons-outlined icono">home</i> Home</router-link>
        </a>

        <div class="accordion accordion-flush " id="accordionFlushExample">
          <div class="accordion-item bg-light">
            <h2 class="accordion-header" id="flush-headingOne ">
              <button class="accordion-button collapsed bg-light" type="button" data-bs-toggle="collapse"
                data-bs-target="#flush-collapseOne" aria-expanded="false" aria-controls="flush-collapseOne">
                <i class="material-icons material-icons-outlined icono">groups</i><a> Personas</a>
              </button>
            </h2>
            <div id="flush-collapseOne" class="accordion-collapse collapse" aria-labelledby="flush-headingOne"
              data-bs-parent="#accordionFlushExample">
              <a>
                <router-link to="/persona" class="list-group-item list-group-item-action bg-light"><i
                    class="material-icons material-icons-outlined icono">person</i> Personas</router-link>
              </a>
              <a>
                <router-link to="/estudiante" class="list-group-item list-group-item-action bg-light "><i
                    class="material-icons material-icons-outlined icono">school</i> Estudiante</router-link>
              </a>
              <a>
                <router-link to="/visitante" class="list-group-item list-group-item-action bg-light "><i
                    class="material-icons material-icons-outlined icono">hail</i> Visitantes</router-link>
              </a>
            </div>
          </div>
        </div>
        <a>
          <router-link to ="/visita" class="list-group-item list-group-item-action bg-light"><i class="material-icons material-icons-outlined icono">diversity_3</i>  Visita</router-link>
        </a>
        <a>
          <router-link to ="/maestra" class="list-group-item list-group-item-action bg-light "><i class="material-icons material-icons-outlined icono">settings_suggest</i>  Maestra</router-link>
        </a>
      </div>
    </div>
    <!-- /#sidebar-wrapper -->

    <!-- Page Content - Contenido -->
    <div id="page-content-wrapper">

      <nav class="navbar navbar-expand-lg navbar-light bg-light border-bottom">
        <button class="btn btn-success" id="menu-toggle">
          <i class="material-icons material-icons-outlined">vertical_split</i>
        </button>

        <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
          <span class="navbar-toggler-icon"></span>
        </button>

        <div class="collapse navbar-collapse" id="navbarSupportedContent">
          <ul class="navbar-nav ml-auto mt-2 mt-lg-0">
            <li class="nav-item active">
              <a class="nav-link" href="#">Home <span class="sr-only">(current)</span></a>
            </li>
            <li class="nav-item">
              <a class="nav-link" href="#">Link</a>
            </li>
            <li class="nav-item dropdown">
              <a class="nav-link dropdown-toggle" href="#" role="button" data-bs-toggle="dropdown" aria-expanded="false">
                Dropdown
              </a>
              <div class="dropdown-menu dropdown-menu-right" aria-labelledby="navbarDropdown">
                <a class="dropdown-item" href="#">Action</a>
                <a class="dropdown-item" href="#">Another action</a>
                <div class="dropdown-divider"></div>
                <a class="dropdown-item" href="#">Something else here</a>
              </div>
            </li>
          </ul>
        </div>
      </nav>

      <div class="container-fluid text-center">
        <router-view></router-view>
      </div>
    </div>
    <!-- /#page-content-wrapper -->

    
  </div>

  <!-- /#wrapper -->
</template>

<style>
 /*App.css*/ 
 .icono{
  color: #66BFBF;
}
</style>

<script>
//Bootstrap y librerias jQuery

import 'bootstrap/dist/css/bootstrap.min.css';
import 'bootstrap/dist/js/bootstrap.min.js';
import 'popper.js/dist/umd/popper.min.js';

import 'jquery/dist/jquery.min.js';


import $ from 'jquery'; 
import './assets/App.css';


export default {
 
  mounted(){
    //toggle sidebar
    $("#menu-toggle").click(function(e) {
      e.preventDefault();
      $("#wrapper").toggleClass("toggled");
    });
  },
  
}
</script>