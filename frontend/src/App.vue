<template>
  <div class="d-flex" id="wrapper">

    <!-- Sidebar -->
    <div class="bg-light border-right" id="sidebar-wrapper">
      <div class="sidebar-heading text-center"><h1 class="text-gradient text-center" ><b>Vue Sidebar</b></h1></div>
      <br>
      <div class="list-group list-group-flush">
        <a>
          <router-link to ="/" class="list-group-item list-group-item-action bg-light">Home</router-link>
        </a>
        <a>
          <router-link to ="/persona" class="list-group-item list-group-item-action bg-light">Personas</router-link>
        </a>
        <a>
          <router-link to ="/estudiante" class="list-group-item list-group-item-action bg-light">Estudiante</router-link>
        </a>
        <a>
          <router-link to ="/visitante" class="list-group-item list-group-item-action bg-light">Visitantes</router-link>
        </a>
        <a>
          <router-link to ="/visita" class="list-group-item list-group-item-action bg-light">Visita</router-link>
        </a>
        <a>
          <router-link to ="/maestra" class="list-group-item list-group-item-action bg-light">Maestra</router-link>
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