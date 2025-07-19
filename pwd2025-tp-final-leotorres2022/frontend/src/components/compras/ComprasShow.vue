<template>
<div class="detalle-socio">
  <h2><i class="pi pi-id-card" style="margin-right: 8px"></i>Detalle de la Compra</h2>
  <p><i class="pi pi-pencil" style="margin-right: 8px"></i><strong></strong> <span class="dato">{{ compra.descripcion}}</span></p>
  <p><i class="pi pi-dollar" style="margin-right: 8px"></i><strong></strong> <span class="dato">{{ compra.precio }}</span></p>
  <p><i class="pi pi-user" style="margin-right: 8px"></i><strong></strong> <span class="dato">{{ compra.socio?.nombre}}</span></p>
  <p><i class="pi pi-sort-numeric-up" style="margin-right: 8px"></i><strong></strong> <span class="dato">{{ compra.cantidad}}</span></p>
    <p><i class="pi pi-th-large" style="margin-right: 8px"></i><strong></strong> <span class="dato">{{ compra.categoria?.nombre}}</span></p>
        <p><i class="pi pi-tag" style="margin-right: 8px"></i><strong></strong> <span class="dato">{{ compra.talle?.nombre}}</span></p>
  <p><i class="pi pi-hash" style="margin-right: 8px"></i><strong>ID:</strong> <span class="dato">{{ compra.id }}</span></p>
</div>


   <div class="volver" >
          <router-link :to="{name:'compras_list'}"><i class="pi pi-arrow-circle-left" style="font-size: 2rem"></i></router-link>
    </div>

</template>
<script setup lang="ts">
import { toRefs } from 'vue';
import  UseComprasStore from '../../stores/compras'
import { useRoute} from 'vue-router';
import { onMounted } from 'vue';
const route = useRoute()
const { compra: compra,compras: compras} = toRefs(UseComprasStore())
onMounted(async () => {
const id = route.params.id
const encontrada= compras.value.find(compra =>compra.id == parseInt(id as string))
compra.value =  encontrada ?? { descripcion: '' , cantidad: 0, categoria:undefined, socio: undefined,talle: undefined, precio: 0,id:0 }

  if (!encontrada) {
    console.error('Compra no encontrada')
  }


if (!compra.value) {
    console.error('socio no encontrado')
  }

}
)

</script>

<style scoped>
.detalle-socio {
  max-width: 600px;
  margin: 2rem auto;
  padding: 2rem;
  background-color: #ffffff;
  border-radius: 12px;
  box-shadow: 0 8px 16px rgba(0,0,0,0.1);
  color: #333;
  font-family: 'Segoe UI', sans-serif;
}

.detalle-socio h2 {
  text-align: center;
  color: #444;
  margin-bottom: 1.5rem;
}

.detalle-socio p {
  margin: 1rem 0;
  font-size: 1.1rem;
  display: flex;
  align-items: center;
}

.dato {
  margin-left: 8px;
  color: #007BFF;
  font-weight: bold;

}

.volver{
  display: flex;
  justify-content: center;
  align-items: center;
  height: 20vh;
}
</style>
