<template>
  <div>
    <form @submit.prevent="crear">
      <div >
       <label>Nombre de Socio</label>
          <select v-model="compra.socio" required>
         <option v-for="socio in socios" :key="socio.id" :value="socio">
         {{ socio.nombre }}
         </option>
        </select>
        <label for="" >Descripcion del Articulo</label>
        <p >{{ compra.descripcion }}</p>
        <label for="" >Precio</label>
          <p >{{ compra.precio }}</p>
        <label for="" >cantidad</label>
        <input type="text" name="" v-model="compra.cantidad">
        <label for="" >Talle</label>
         <select v-model="compra.talle" required>
        <option v-for="talle in talles" :key="talle.id" :value="talle">
          {{ talle.nombre }}
        </option>
      </select>
        <label for="" >Categoria</label>
      <select v-model="compra.categoria" required>
        <option v-for="categoria in categorias" :key="categoria.id" :value="categoria">
          {{ categoria.nombre }}
        </option>
      </select>
       </div>
      <button type="submit">Crear</button>
    </form>

  </div>
<div class="volver" >
          <router-link :to="{name:'tienda'}"><i class="pi pi-arrow-circle-left" style="font-size: 2rem"></i></router-link>
    </div>
</template>

<script setup lang="ts">
import { toRefs} from 'vue'
import UseComprasStore from '../../stores/compras'
import UseTallesStore from '../../stores/talles'
import UseSociosStore from '../../stores/socios'
import  UseCategoriasStore from '../../stores/categorias'
const limpiar = () => {
  compra.value.cantidad = 1
  compra.value.talle = undefined
  compra.value.categoria = undefined
  compra.value.socio = undefined
}

const { talles, getAll: getAllTalles } = UseTallesStore()
const { socios, getAll: getAllSocios } = UseSociosStore()
const { categorias, getAll: getAllCategorias } = UseCategoriasStore()
const {compra:compra} = toRefs(UseComprasStore())
const {create} = UseComprasStore()



import { onMounted } from 'vue'
onMounted(async () => {
await getAllTalles()
await getAllSocios()
await getAllCategorias()

limpiar()

})

const crear = async ()=> {
  if (!compra.value.descripcion) {
    alert('La descripcion de la es obligatoria')
    }
  else if (compra.value.precio <= 0) {
    alert('El precio debe ser mayor a 0')
  }
  else if (compra.value.cantidad < 0) {
    alert('la cantidad no puede ser negativo')
  }
  else if (!compra.value.talle) {
    alert('Debe seleccionar un Talle')
  }
  else if (!compra.value.categoria) {
     alert('Debe seleccionar una categoria')
  }
   else if (!compra.value.socio){
     alert('Debe ingresar un Nro de Socio')
  }

else {
    const cantidad = Number(compra.value.cantidad)
  const precioUnitario = Number(compra.value.precio)
    const articulo_json = {
      descripcion: compra.value.descripcion,
      precio: precioUnitario* cantidad,
      cantidad: Number(compra.value.cantidad),
      talle_id: compra.value.talle?.id,
      categoria_id: compra.value.categoria?.id,
      socio_id: compra.value.socio?.id,

    }
    console.log('Articulo a crear:', articulo_json)
    try {
      await create(articulo_json)
      console.log(' creada correctamente:', articulo_json)
      alert('Compra creada correctamente')
      // Resetear los campos del formulario
      compra.value.descripcion= ''
      compra.value.precio= 0
      compra.value.cantidad= 0
      compra.value.talle= undefined
      compra.value.categoria= undefined
      compra.value.socio= undefined

    } catch (error) {
      console.error('Error al crear compra:', error)
      alert('Error al crear compra. Revisa la consola para más detalles.')
    }
  }
}

</script>

<style scoped>
form {
  background-color: #fff;
  padding: 2rem;
  border-radius: 12px;
  max-width: 600px;
  margin: auto;
  box-shadow: 0 6px 20px rgba(0, 0, 0, 0.1);
}

label {
  display: block;
  margin-top: 1rem;
  font-weight: bold;
  color: #333;
  font-size: 1rem;
}

select,
input[type="text"] {
  width: 100%;
  padding: 0.75rem 1rem;
  margin-top: 0.3rem;
  border: 1px solid #ccc;
  border-radius: 8px;
  font-size: 1rem;
  transition: border-color 0.3s;
}

select:focus,
input[type="text"]:focus {
  border-color: #169d3e;
  outline: none;
}

p {
  background-color: #f0f0f0;
  padding: 0.75rem 1rem;
  border-radius: 8px;
  font-size: 1rem;
  color: #444;
  margin-top: 0.3rem;
  margin-bottom: 1rem;
}




.volver{
  display: flex;
  justify-content: center;
  align-items: center;
  height: 20vh;
}

</style>


