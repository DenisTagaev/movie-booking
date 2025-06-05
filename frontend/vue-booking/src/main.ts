import './assets/main.css'

import { createApp } from 'vue'
import { createPinia } from 'pinia'
import PrimeVue from 'primevue/config'
import Material from '@primeuix/themes/material'
import ToastService from 'primevue/toastservice'
import 'primeicons/primeicons.css'

import App from './App.vue'
import router from './router'

const app = createApp(App)

app.use(createPinia())
app.use(PrimeVue, {
    theme: {
        preset: Material,
        options: {
            darkModeSelector: 'system',
            cssLayer: true
        }
    }
})
app.use(ToastService)
app.use(router).mount('#app')
