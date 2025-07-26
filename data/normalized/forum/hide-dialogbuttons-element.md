# Hide DialogButtons element

## Question

**Cla** asked on 11 Sep 2023

I have a TelerikDialog who host a component, when some logic occurs on component i would like to hide the dialog buttons, now i can do this for each button inside DialogButtons element, but this cause the dialog to show some empty space with a separation line. I would like to hide entirely the DialogButtons element to prevent showing empty space, i tried with hidden html attribute or @if statement but it's not supported. There is a workaround? It woud be glad to have a Visible property on DialogButtons component in future releases.

## Answer

**Georgi** answered on 14 Sep 2023

Hello, Claudio, Yes, it is possible to conditionally hide the DialogButtons. A custom CSS class selector can be used on the TelerikDialog to achieve this. <style>.customClass.k-dialog>.k-dialog-actions { display: none;
} </style> This way, the style will be applied only to Dialog components with the customClass. To conditionally apply the CSS class selector, a boolean flag and a ternary operator can be used: <TelerikDialog @ref="DialogRef" Class="@(!Visible ? " customClass ": "")" Title="@Title" Visible="true"> Additionally, use the Dialog's Refresh method to re-render the component after the new changes. An a wait Task.Delay(1) might be needed before calling the Refresh method to give Blazor time to refresh the UI and pass the class to the component. I have prepared a REPL example to show the result. Let me know if additional questions arise. Regards, Georgi Progress Telerik
