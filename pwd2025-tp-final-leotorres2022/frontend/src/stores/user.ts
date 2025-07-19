import { defineStore } from 'pinia'

const useUserStore = defineStore('userMode', {
  state: () => ({
    modo: 'usuario' // 'usuario' o 'admin'
  }),
  actions: {
    setModo(nuevoModo: string) {
      this.modo = nuevoModo
    }
  }
})
export default useUserStore
