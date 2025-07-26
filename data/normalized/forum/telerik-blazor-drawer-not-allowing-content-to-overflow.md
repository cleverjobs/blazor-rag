# Telerik Blazor drawer not allowing content to overflow

## Question

**Chr** asked on 15 Jun 2022

Hello, I'm currently using the Telerik drawer as a static menu on the left of our project. We're using the template to customize the components being loaded into the drawer and would like the upper most component (profile image) to extend about 50% out of the drawer and into our header. You can view the look we want to accomplish from the drawerWant image and view the behavior we're currently getting from the drawerHave image.

### Response

**Benjamin** commented on 16 Jun 2022

Looks like an z-index issue for me. Have you tried adding the css attribute z-index for your image to a higher one than the z-index of the profile image?

## Answer

**Christopher** answered on 16 Jun 2022

I was able to fix this issue by setting overflow: visible for each of the following selectors (k-drawer, k-drawer-wrapper, k-drawer-item)
