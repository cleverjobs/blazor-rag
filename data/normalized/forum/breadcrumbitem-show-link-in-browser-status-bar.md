# BreadcrumbItem show link in browser status bar

## Question

**Adr** asked on 20 Nov 2022

Is it possible to have the BreadcrumbItem show the link in the browser status bar when a user hovers over it, like a regular anchor tag? I tried using an ItemTemplate and wrapping the content in an anchor tag with the onclick set to return false, but I couldn't see any way to do this without losing all the existing styling. It seems like I'd have to pretty much rewrite the entirety of the BreadcrumbItem to get access to things like the Root or Last property in order to render the items correctly.

## Answer

**Hristian Stefanov** answered on 23 Nov 2022

Hi Adrian, I confirm that the desired result is possible. Indeed, using the ItemTemplate is the easiest way to make things work. Here is an example I have prepared for you that seems to cover the scenario needs: REPL link. Please run and test it to see the result. Let me know if you face any difficulties when testing. Regards, Hristian Stefanov

### Response

**Adrian** commented on 24 Nov 2022

Thanks, that gave me enough to work with, got it working now.
