import { defineStore } from 'pinia'
import { ref } from 'vue'
import ApiService from '@/services/ApiService'
import type { Categorias } from '@/interfaces/Categorias'

const useCategoriasStore = defineStore('categorias', () => {
  const categorias = ref<Array<Categorias>>([])
  const categoria = ref<Categorias>({
    id: 0,
    nombre: '',
  })
  const url = 'categorias'
  async function getAll() {
    const data = await ApiService.getAll(url)
    if (data) {
      categorias.value = data
    }
  }
  async function create(categoria: Categorias) {
    const response = await ApiService.create(url, categoria)
    if (response) {
      return response
    }
  }

  async function update(categoria: Categorias) {
    if (categoria.id) {
      const data = await ApiService.update(url + '/', categoria.id, categoria)
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
  return { categorias, categoria, getAll, destroy, create, update }
})

export default useCategoriasStore
