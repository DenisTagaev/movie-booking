import { signUpSchema } from '@/schemas/signUpSchema'
import { ZodSafeParseResult } from 'zod/v4'

export async function validateSignUpForm(values: {
  email: string
  password: string
  confirmPassword: string
}) {
  const result: ZodSafeParseResult<{
    email: string
    password: string
    confirmPassword: string
  }> = signUpSchema.safeParse({
    email: values.email.trim(),
    password: values.password.trim(),
    confirmPassword: values.confirmPassword.trim(),
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
