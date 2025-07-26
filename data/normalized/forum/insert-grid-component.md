# Insert Grid component

## Question

**Dav** asked on 31 Mar 2021

Hi, Does anyone know if it is possible to insert a grid component (that is currently rendered on screen) into the editor? My thoughts are that it should be possible to "convert" the grid into HTML code using the table tags. Appreciate any thoughts or advice. Cheers

## Answer

**Marin Bratanov** answered on 01 Apr 2021

Hello David, If you can plug logic similar to unit testing or framework rendering to get the rendered HTML, you could add it to the field that your editor users. Another option might be to take that HTML as a string from the DOM with JS Interop and pass it back to the C# code. As far as I know, there is no built-in facility in the Blazor framework for you to get the rendered code and markup from a component or from a template. Regards, Marin Bratanov
