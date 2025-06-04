<script setup lang="ts">
import { Ref, ref } from 'vue'
import InputText  from 'primevue/inputtext'
import Password from 'primevue/password'
import Button from 'primevue/button'
import { FloatLabel } from 'primevue'

const email: Ref<string, string> = ref('')
const password: Ref<string, string> = ref('')

const handleLogin: () => void = 
() => {
  console.log('Attempting login with:', email.value, password.value)
  // TODO: actual login logic
}

</script>

<template>
    <main class="login-container">
      <form class="login-form" @submit.prevent="handleLogin">
        <h2 class="login-title">Sign in</h2>
        <p class="login-subtitle">to continue to Movie Booking App</p>
  
        <fieldset class="form-group">
          <FloatLabel variant="on">
              <InputText
                v-model="email"
                id="email"
                type="email"
                autocomplete="email"
                style="width: 100%;"
                required
              />
              <label for="email">Email</label>
          </FloatLabel>
        </fieldset>
  
        <fieldset class="form-group password-field">
          <FloatLabel variant="on">
            <Password
              v-model="password"
              id="password"
              inputId="password"
              style="width: 100%;"
              :input-style="{ width: '100%'}"
              :feedback="false"
              required
              >
            </Password>
            <label for="password">Password</label>
          </FloatLabel>
        </fieldset>
  
        <Button
          type="submit"
          label="Login"
          class="p-button p-button-primary login-btn"
          :disabled="!email || !password"
        />
      </form>
    </main>
  </template>
  
<style scoped lang="scss">
  .login-container {
    display: flex;
    justify-content: center;
    align-items: center;
    padding: 2rem;
    min-height: 100vh;
  }
  
  .login-form {
    padding: 2rem;
    border-radius: 12px;
    width: 100%;
    max-width: 400px;
    box-shadow: 0 4px 12px rgba(0, 0, 0, 0.5);
  }
  
  .login-title {
    font-size: 1.5rem;
    margin-bottom: 0.25rem;
  }
  
  .login-subtitle {
    font-size: 0.95rem;
    color: #777;
    margin-bottom: 1.5rem;
  }
  
  .form-group {
    border: none;
    padding: 0;
    display: flex;
    flex-direction: column;
    margin-bottom: 1.25rem;
  }
  
  .login-btn {
    width: 100%;
    font-weight: 600;
  }


</style>
  