// src/validators/validateLoginForm.ts
import { loginSchema } from '@/schemas/loginSchema'
import { ZodSafeParseResult } from 'zod/v4'

export async function validateLoginForm(values: {
  email: string
  password: string
}) {
  const result: ZodSafeParseResult<{
    email: string
    password: string
  }> = loginSchema.safeParse({
    email: values.email.trim(),
    password: values.password.trim(),
  })

  if (!result.success) {
    const errors: Record<string, { message: string }> = {}
    for (const issue of result.error.issues) {
      errors[String(issue.path[0])] = { message: issue.message }
    }
    return { valid: false, errors }
  }

  return { valid: true, errors: {} }
}
