
import { defineStore } from "pinia"
import { ref } from "vue"
import ApiService from "@/services/ApiService"
import type  {Socios}   from '@/interfaces/Socios'
import type {Talles} from '@/interfaces/Talles'
import type {Categorias} from '@/interfaces/Categorias'
import type {Compras} from '@/interfaces/Compras'

const useComprasStore = defineStore('compras', () => {
  const compras = ref<Array<Compras>>([])
  const compra = ref<Compras>({
    id: 0,
    descripcion: '',
    precio: 0,
    cantidad: 0,
    talle: {} as Talles,
    categoria: {} as Categorias,
    socio: {} as Socios
  })
const url = 'compras'
  async function getAll()
  {
    const data = await ApiService.getAll(url)
    if (data) {
      compras.value = data
       console.log('Compras cargadas:', data)
              }
  }
  async function create(compra: Compras) {
    const response = await ApiService.create(url+'/', compra)
    if (response) {
           return response
    }

  }



 async function update(compra: Compras) {
    if (compra.id) {
    const data = await ApiService.update(url + '/',compra.id, compra)
    if (data) {
      return data
    }
  }
  }

  async function destroy(id: number) {
    const data = await ApiService.destroy(url + '/', id)
    if (data) {
      return data
          }
  }

function seleccionarProducto(producto: { descripcion: string; precio: number }) {
  compra.value.descripcion = producto.descripcion
  compra.value.precio = producto.precio
}


return { compra, compras, getAll, destroy, create, update , seleccionarProducto  }

})




export default useComprasStore
