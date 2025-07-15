
import { defineStore } from "pinia"
import { ref } from "vue"
import ApiService from "@/services/ApiService"
import type  {Talles}   from '@/interfaces/Talles'

const useTallesStore = defineStore('talles', () => {
  const talles = ref<Array<Talles>>([])
  const talle= ref<Talles>({
    id: 0,
    nombre: '',
  })
const url = 'talles'
  async function getAll()
  {
    const data = await ApiService.getAll(url)
    if (data) {
      talles.value = data
              }
  }
  async function create(talle:Talles) {
    const response = await ApiService.create(url, talle)
    if (response) {
           return response
    }

  }

 async function update(talle: Talles) {
    if (talle.id) {
    const data = await ApiService.update(url +'/',talle.id, talle)
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
return { talles: talles,talle: talle , getAll, destroy, create, update }

})

export default useTallesStore
