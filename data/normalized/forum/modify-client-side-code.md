# Modify client-side code

## Question

**SOJ** asked on 07 Jan 2021

How will we modify client side code? (Need the application to crawled by search engine)

## Answer

**Marin Bratanov** answered on 07 Jan 2021

Hello, There are a couple different ways to do this and you can download our demos to see one of them - we render a component in the <head> section of the page that takes care of the SEO metadata. You should also make sure to use server pre-rendering (both with the server-side flavor and with WebAssembly) so that all the content comes down from the server in the first response. Regards, Marin Bratanov
