# How can I use local SVG files with Grid or Command buttons in a Blazor WASM application?

## Question

**Mic** asked on 22 Jul 2023

I would like to use a third party set of SVG images for buttons. I was hoping I could do something like: <GridCommandButton Command="View" Icon="@/assets/magnifying_glass.svg"> View </GridCommandButton>

## Answer

**Georgi** answered on 26 Jul 2023

Hello, Michael I am pasting here the answer you got in the private ticket so that the community can benefit from it too.=========================================Generally speaking, the 'GridCommandButton' 'Icon' parameter modifies the content of the button, rendering an SVG tag (icon) within the <button> tag. However, if you want to include your custom icon, you can declare it using a <img> or <svg> tag directly within the 'GridCommandButton' body. Here is a REPL example that demonstrates this approach: [https://blazorrepl.telerik.com/wxEBGzaq09Im5oFS52](https://blazorrepl.telerik.com/wxEBGzaq09Im5oFS52) Please review the example and let me know if this solution meets your requirements or if further assistance is needed.=========================================Regards, Georgi Progress Telerik
