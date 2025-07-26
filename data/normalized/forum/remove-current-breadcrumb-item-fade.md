# Remove current Breadcrumb item fade

## Question

**Pet** asked on 03 May 2023

By default the Breadcrumb appears to fade the last item (page you're currently on) as seen on the screenshot attached. Is there anyway to remove this affect, I would like it instead to have the text bolded to represent the current breadcrumb. Is this possible to remove and if so, how?

## Answer

**Radko** answered on 04 May 2023

Hi Peter, The default behavior of the component is to render the last item as a disabled one, which indicates the item is not focusable/interactable. If your scenario requires it, you can change this by overriding the CSS styling applied to said item. The fade that you have mentioned is done through the opacity attribute, thus overriding that should get the desired result. Here is a simple example of such an override: [https://blazorrepl.telerik.com/GdYpYyYf59A9JCMS48](https://blazorrepl.telerik.com/GdYpYyYf59A9JCMS48) Regards, Radko Progress Telerik
