# Drag and Drop is not working in MAUI

## Question

**Fab** asked on 01 Apr 2025

I have a blazor hybrid app with a basic FileSelect component. When I start the Windows Native MAUI app, the drag-and-drop feature of the component does not work at all. The drag of any file into the MAUI window shows a stop/not possible sign as the mouse pointer. In the Web version everything works as expected. There was also no note here that this might not work due to some restriction

## Answer

**Tsvetomir** answered on 03 Apr 2025

Hello Fabian, The encountered behavior seems to be related to the limitation that comes from the Blazor MAUI itself - BlazorWebView drag and drop does not work with MAUI Templates. So, I can recommend following the linked issue for any updates on it. In terms of the documentation, I will make sure to add this specific note in the Notes section. Thank you for bringing that to our attention. Your cooperation is highly valuable. Regards, Tsvetomir
