<script setup lang="ts">
import { computed, ComputedRef, reactive, watch } from 'vue'
import { useToast } from "primevue/usetoast";
import { Form, FormField } from '@primevue/forms';
import InputText  from 'primevue/inputtext'
import Password from 'primevue/password'
import Button from 'primevue/button'
import { FloatLabel, ToastServiceMethods, Message } from 'primevue'

import debounce from '@/utils/debounce'
import { validateLoginForm } from '@/validators/validateLoginForm'

const toast: ToastServiceMethods = useToast();

const LoginValues: {
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
const focusedField: {
    email: boolean;
    password: boolean;
} = reactive(
  {
    email: false,
    password: false
  }
)
const isFormValid: ComputedRef<boolean> = 
  computed(() :boolean => {
    const hasNoErrors: boolean = !Object.values(errors).some(Boolean)
    const allFieldsFilled: boolean = Object.values(LoginValues).every(Boolean)
    return hasNoErrors && allFieldsFilled
});

watch(() => [LoginValues.email, LoginValues.password], 
  debounce(async (): Promise<void> => {
    const { errors: validationErrors } = await validateLoginForm(LoginValues)
    errors.email =  validationErrors.email?.message || null
    errors.password =  validationErrors.password?.message || null
  }, 300), { immediate: true })

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
        :model="LoginValues"
        class="login-form" 
        @submit.prevent="handleLogin"
      >
        <h2 class="login-title">Sign in</h2>
        <p class="login-subtitle">to continue to Movie Booking App</p>
  
        <FormField class="form-group">
          <FloatLabel variant="on">
              <InputText
                v-model="LoginValues.email"
                id="email"
                type="email"
                autocomplete="email"
                style="width: 100%;"
                @focus="focusedField.email = true"
                @blur="focusedField.email = false"
                required
              />
              <label for="email">Email</label>
          </FloatLabel>
          <Message v-if="focusedField.email && errors.email" severity="error" size="small" variant="simple">{{ errors.email }}</Message>
        </FormField>
  
        <FormField class="form-group password-field">
          <FloatLabel variant="on">
            <Password
              v-model="LoginValues.password"
              id="password"
              inputId="password"
              style="width: 100%;"
              :input-style="{ width: '100%'}"
              :feedback="false"
              @focus="focusedField.password = true"
              @blur="focusedField.password = false"
              required
              >
            </Password>
            <label for="password">Password</label>
          </FloatLabel>
          <Message v-if="focusedField.password && errors.password" severity="error" size="small" variant="simple">{{ errors.password }}</Message>
        </FormField>
  
        <Button
          type="submit"
          label="Login"
          class="p-button p-button-primary login-btn"
          :disabled="!isFormValid"
        />
        <p class="register-link">
          <span>Don't have an account?</span>
          <RouterLink to="/signup">Sign up</RouterLink>
        </p>
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
  .register-link {
    margin-top: 1.5rem;
    text-align: center;
    font-size: 0.875rem;
    color: #777;

    a {
      color: var(--p-button-primary-background); 
      text-decoration: none;
      font-weight: 600;
      margin-left: 0.25rem;
      transition: color 0.2s ease;
      
      &:hover {
        color: var(--p-button-primary-hover-background);
        text-decoration: underline;
      }
    }
  }
</style>