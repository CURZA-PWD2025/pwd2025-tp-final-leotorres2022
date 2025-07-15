
import { defineStore } from "pinia"
import { ref } from "vue"
import ApiService from "@/services/ApiService"
import type  {Socios}   from '@/interfaces/Socios'

const useSociosStore = defineStore('socios', () => {
  const socios = ref<Array<Socios>>([])
  const socio= ref<Socios>({
    id: 0,
    nombre: '',
    direccion: '',
    email: '',
    telefono: ''
  })
const url = 'socios'
  async function getAll()
  {
    const data = await ApiService.getAll(url)
    if (data) {
      socios.value = data
              }
  }
  async function create(socio: Socios) {
    const response = await ApiService.create(url, socio)
    if (response) {
           return response
    }

  }

 async function update(socio: Socios) {
    if (socio.id) {
    const data = await ApiService.update(url +'/',socio.id, socio)
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
return { socios,socio , getAll, destroy, create, update }

})

export default useSociosStore
