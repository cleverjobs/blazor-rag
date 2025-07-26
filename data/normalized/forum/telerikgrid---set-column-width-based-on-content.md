# TelerikGrid - Set column width based on content

## Question

**Ale** asked on 05 Jun 2023

I'm trying out Telerik in an existing Blazor WebAssembly project. In order to try it out, I'm adding Telerik components next to the existing HTML elements so I can see how they compare. I have a question about how to set the column width in TelerikGrid. I'd like to set the width based on whichever is larger: the content or the header title. I tried setting Width="auto" but that didn't work. I tried setting Width to a fixed width, but I'd like to avoid hardcoding the width like that. Please see the attached image. It shows two tables: 1. The existing table using a regular HTML table with Bootstrap classes "table table-striped". Notice how the columns have different widths. 2. The TelerikGrid with the same headers and data. Notice how the columns are all the same width.

## Answer

**Nadezhda Tacheva** answered on 08 Jun 2023

Hi Alejandro, To achieve this result, you may use the autofit functionality of the Grid. You can programmatically autofit the columns using the exposed methods. If you need to perform this on initialization of the component, please see the specifics here: Autofit All Grid Columns on Initial Load. I hope you will find the above information and linked resources useful. Please let us know if any other questions appear. Regards, Nadezhda Tacheva
