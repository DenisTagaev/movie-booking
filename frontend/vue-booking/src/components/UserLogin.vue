<script setup lang="ts">
import { reactive, watch } from 'vue'
import { useToast } from "primevue/usetoast";
import { Form, FormField } from '@primevue/forms';
import InputText  from 'primevue/inputtext'
import Password from 'primevue/password'
import Button from 'primevue/button'
import { FloatLabel, ToastServiceMethods, Message } from 'primevue'

import { validateLoginForm } from '@/validators/validateLoginForm'

const toast: ToastServiceMethods = useToast();

const initialLoginValues: {
    email: string;
    password: string;
} = reactive({
  email: '',
  password: ''
})
const errors: {
    email: null | string;
    password: null | string;
} = reactive({
  email: null,
  password: null
})

watch(() => [initialLoginValues.email, initialLoginValues.password], async () => {
  const result = await validateLoginForm(initialLoginValues)
  errors.email = result.errors.email?.message || null
  errors.password = result.errors.password?.message || null
}, { immediate: true })

const handleLogin: () => void = 
() => {
  // TODO: actual login logic
}

const onFormSubmit = ({ valid }: 
{valid: boolean}) => {
    if (valid) {
        toast.add({ severity: 'success', summary: 'Login Successful!', life: 2000 });
    }
};
</script>

<template>
    <main class="login-container">
      <Form 
        v-slot="$form"   
        :model="initialLoginValues"
        class="login-form" 
        @submit.prevent="handleLogin"
      >
        <h2 class="login-title">Sign in</h2>
        <p class="login-subtitle">to continue to Movie Booking App</p>
  
        <FormField class="form-group">
          <FloatLabel variant="on">
              <InputText
                v-model="initialLoginValues.email"
                id="email"
                type="email"
                autocomplete="email"
                style="width: 100%;"
                required
              />
              <label for="email">Email</label>
          </FloatLabel>
          <Message v-if="$form.email?.invalid" severity="error" size="small" variant="simple">{{ $form.email.error?.message }}</Message>
        </FormField>
  
        <FormField class="form-group password-field">
          <FloatLabel variant="on">
            <Password
              v-model="initialLoginValues.password"
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
          <Message v-if="$form.password?.invalid" severity="error" size="small" variant="simple">{{ $form.password.error?.message }}</Message>
        </FormField>
  
        <Button
          type="submit"
          label="Login"
          class="p-button p-button-primary login-btn"
          />
          <!-- :disabled="!$form.email.valid || !$form.password.valid" -->
      </Form>
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
  