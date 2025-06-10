import { z } from "zod/v4";
import { loginSchema } from "./loginSchema";

export const signUpSchema = loginSchema
  .extend({
    confirmPassword: z.string(),
  })
  .refine(data => data.password === data.confirmPassword, {
    message: 'Passwords do not match.',
    path: ['confirmPassword'],
  })