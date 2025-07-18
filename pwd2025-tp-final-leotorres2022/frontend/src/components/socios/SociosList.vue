<template>
  <h1 class="titulo">Socios Activos</h1>
  <div class="crear-container"></div>
  <table>
    <thead>
      <tr>
        <th>id</th>
        <th>nombre</th>
        <th>direccion</th>
        <th>telefono</th>
        <th>email</th>
        <th>acciones</th>
      </tr>
    </thead>
    <tbody>
      <tr v-for="socio in socios" :key="socio.id">
        <td>{{ socio.id }}</td>
        <td>{{ socio.nombre }}</td>
        <td>{{ socio.direccion }}</td>
        <td>{{ socio.telefono }}</td>
        <td>{{ socio.email }}</td>
        <td>
          <router-link :to="{ name: 'socios_update', params: { id: socio.id } }"
            ><i class="pi pi-pencil" style="font-size: 1.5rem"></i
          ></router-link>
          <router-link :to="{ name: 'socios_show', params: { id: socio.id } }"
            ><i class="pi pi-eye" style="font-size: 1.5rem"></i
          ></router-link>
          <button @click.prevent="eliminar(socio.id as number)">
            <i class="pi pi-trash" style="font-size: 1.5rem"></i>
          </button>
        </td>
      </tr>
    </tbody>
  </table>
</template>

<script setup lang="ts">
import { onMounted, toRefs } from 'vue'
import useSociosStore from '../../stores/socios'
const { socios } = toRefs(useSociosStore())
const { getAll, destroy } = useSociosStore()

onMounted(async () => {
  await getAll()
})
async function eliminar(id: number) {
  if (confirm('¿Estás seguro de eliminar el socio ' + id + '?')) {
    await destroy(id)
    await getAll()
  }
}
</script>

<style scoped>
.titulo {
  text-align: center;
  margin-top: 1rem;
}
.crear-container {
  display: flex;
  justify-content: center;
  margin-bottom: 1rem;
}
table {
  width: 100%;
  border-collapse: collapse;
  margin-top: 2rem;
  font-family: 'Segoe UI', sans-serif;
  font-size: 1.3rem;
  background-color: #fff;
  box-shadow: 0 4px 12px rgba(0, 0, 0, 0.1);
}

thead th {
  background-color: #007bff;
  color: white;
  padding: 1rem;
  text-align: left;
  font-weight: bold;
}

tbody td {
  padding: 1rem;
  border-top: 1px solid #eee;
}

tr:nth-child(even) {
  background-color: #f9f9f9;
}

td i {
  margin-right: 10px;
  color: #555;
  cursor: pointer;
  transition: color 0.3s ease;
}

td i:hover {
  color: #007bff;
}

.pi-pencil {
  cursor: pointer;
  color: #e5f41b;
}
</style>
