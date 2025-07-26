# How I Change the expended collapse icon from TelerikTreeView

## Question

**Sam** asked on 22 Jun 2024

HI: How Can I change the expanded i/collapsed con from TelerikTreeView? There is a demo in the documentation but is for the main icon, not for the collapse/expanded icon. Thanks in advance.

## Answer

**Sami** answered on 22 Jun 2024

I change the styles, and is working, but I'm not sure if is the right way, ¿Could you please give me and advise? .k-i-caret-alt-right::before { content: "\e11f"; } .k-i-caret-alt-down::before { content: "\e122"; }

### Response

**Nadezhda Tacheva** answered on 26 Jun 2024

Hi Sami, To change the expand/collapse icons of the TreeView I would also recommend using custom CSS. The solution you have implemented is correct. I just want to add an important note. These styles will work only if the TreeView uses Font icons. This was by default up to UI for Blazor 4.3.0. After that, the default icon type was changed to SVG and you will need different styling for that. Here is an example: [https://blazorrepl.telerik.com/GoYUmKbv15GO0B3v44.](https://blazorrepl.telerik.com/GoYUmKbv15GO0B3v44.) Regards, Nadezhda Tacheva Progress Telerik
