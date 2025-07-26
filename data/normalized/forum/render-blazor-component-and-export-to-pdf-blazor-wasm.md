# Render Blazor component and export to pdf. (Blazor Wasm)

## Question

**Len** asked on 11 Oct 2022

Hi, I'm looking into rendering a TelerikGrid component (including hierarchy) to a pdf using the Telerik Pdf processing library. I'm a bit lost on what is and is not supported in the pdf-/word processing suite in Blazor (Wasm). Is there any way to render a Blazor component and export it to pdf?

## Answer

**Dimo** answered on 14 Oct 2022

Hello Lennert, Currently there are two ways to export a Grid to PDF: The first one uses the Grid data and will work with a single Grid instance and our PDF Processing library. The other uses the page HTML markup and will work with multiple Grid instances and our Kendo UI Drawing library. Hierarchy involves multiple Grid instances, so you will need the second option. Also see the following page: Export Grid to PDF - feature request with discussion and workarounds Regards, Dimo Progress Telerik
