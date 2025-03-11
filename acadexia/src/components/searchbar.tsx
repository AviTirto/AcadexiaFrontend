import { Button } from "@/components/ui/button"
import { Input } from "@/components/ui/input"
import { zodResolver } from "@hookform/resolvers/zod"
import { useForm } from "react-hook-form"
import { z } from "zod"
import {
  Form,
  FormControl,
  FormDescription,
  FormField,
  FormItem,
  FormLabel,
  FormMessage,
} from "@/components/ui/form"
import { useState } from "react"

interface SearchBarProps {
  placeholder?: string,
  onSearch: (prevQuery: string, query: string) => void
}

const FormSchema = z.object({
  query: z.string().min(1, {
    message: "Search query cannot be empty.",
  }),
})

export function SearchBar({ placeholder, onSearch}: SearchBarProps) {
  const form = useForm<z.infer<typeof FormSchema>>({
    resolver: zodResolver(FormSchema),
    defaultValues: {
      query: "",
    },
  })

  const [prevQuery, setPrevQuery] =  useState("")

  function handleSearch(data: z.infer<typeof FormSchema>) {
    onSearch(prevQuery, data.query)
    setPrevQuery(data.query)
  }

  return (
    <Form {...form}>
      <form onSubmit={form.handleSubmit(handleSearch)} className="w-full space-y-6">
        <div className="flex">
          <FormField
            control={form.control}
            name="query"
            render={({ field }) => (
              <FormItem className="w-full mr-2">
                <FormControl>
                  <Input placeholder={placeholder} {...field} />
                </FormControl>
                <FormMessage />
              </FormItem>
            )}
          />
          <Button type="submit">Search</Button>
        </div>
      </form>
    </Form>
      // <Input type="text" placeholder={placeholder} ref={ query } />
      // <Button type="submit">Search</Button>
  )
}
