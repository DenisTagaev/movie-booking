<script setup lang="ts">
import { reactive, watch } from 'vue'
import { Router, useRouter } from 'vue-router'
import { useToast } from "primevue/usetoast"
import { Form, FormField } from '@primevue/forms'
import InputText  from 'primevue/inputtext'
import Password from 'primevue/password'
import Button from 'primevue/button'
import { FloatLabel, ToastServiceMethods, Message } from 'primevue'

import debounce from '@/utils/debounce'
import { validateSignUpForm } from '@/validators/validateSignUpForm'

const router: Router = useRouter()
const toast: ToastServiceMethods = useToast();

const SignUpValues: {
    email: string;
    password: string;
    confirmPassword: string;
} = reactive({
  email: '',
  password: '',
  confirmPassword: ''
})

const errors: {
    email: null | string;
    password: null | string;
    confirmPassword: null | string;
} = reactive({
  email: '',
  password: '',
  confirmPassword: ''
})

const focusedField: {
    email: boolean;
    password: boolean;
    confirmPassword: boolean;
} = reactive(
  {
    email: false,
    password: false,
    confirmPassword: false,
  }
)

watch(() => [SignUpValues.email, SignUpValues.password, SignUpValues.confirmPassword], 
  debounce(async () => {
    const { errors: validationErrors } = await validateSignUpForm(SignUpValues)
    errors.email =  validationErrors.email?.message || null
    errors.password =  validationErrors.password?.message || null
    errors.confirmPassword = validationErrors.confirmPassword?.message || null
  }, 300), { immediate: true })

async function handleSignUp() {
  const result = await validateSignUpForm(SignUpValues)

  if (result.valid) {
    // TODO: send data to backend
    // router.push('/')
  }
}

</script>

<template>
    <main class="signup-container">
      <Form
        :model="SignUpValues"
        class="signup-form"
        @submit.prevent="handleSignUp"
      >
        <h2 class="form-title">Create your account</h2>
  
        <FormField class="form-group">
          <FloatLabel variant="on">
            <InputText
              v-model="SignUpValues.email"
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
  
        <FormField class="form-group">
          <FloatLabel variant="on">
            <Password
              v-model="SignUpValues.password"
              id="password"
              inputId="password"
              :feedback="false"
              style="width: 100%;"
              :input-style="{ width: '100%' }"
              @focus="focusedField.password = true"
              @blur="focusedField.password = false"
              required
            />
            <label for="password">Password</label>
          </FloatLabel>
          <Message v-if="focusedField.password && errors.password" severity="error" size="small" variant="simple">{{ errors.password }}</Message>
        </FormField>

        <FormField class="form-group">
            <FloatLabel variant="on">
                <Password
                    v-model="SignUpValues.confirmPassword"
                    id="confirm-password"
                    inputId="confirm-password"
                    :feedback="false"
                    style="width: 100%;"
                    :input-style="{ width: '100%' }"
                    @focus="focusedField.confirmPassword = true"
                    @blur="focusedField.confirmPassword= false"
                    required
                />
                <label for="confirm-password">Confirm Password</label>
            </FloatLabel>
            <Message v-if="errors.confirmPassword" severity="error" size="small" variant="simple">
                {{ errors.confirmPassword }}
            </Message>
        </FormField>
  
        <Button
          type="submit"
          label="Sign Up"
          class="p-button p-button-primary signup-btn"
        />
  
        <p class="login-link">
          Already have an account? <RouterLink to="/">Log in</RouterLink>
        </p>
      </Form>
    </main>
  </template>

<style scoped lang="scss">
.signup-container {
  display: flex;
  justify-content: center;
  align-items: center;
  min-height: 100vh;
  padding: 2rem;
}

.signup-form {
  border-radius: 12px;
  padding: 2rem;
  max-width: 400px;
  width: 100%;
  box-shadow: 0 4px 12px rgba(0, 0, 0, 0.1);
}
.form-title {
  margin-bottom: 1rem;
  text-align: center;
}
.form-group {
    border: none;
    padding: 0;
    display: flex;
    flex-direction: column;
    margin-bottom: 1.25rem;
  }

.login-link {
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