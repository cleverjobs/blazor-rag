# Telerik Media Query Error

## Question

**Jef** asked on 06 Oct 2023

Hi, When migrating a WebAssembly Blazor App, this error happens: Could not find 'TelerikBlazor.initMediaQuery' ('TelerikBlazor' was undefined). Thanks,

## Answer

**JeffSM** answered on 06 Oct 2023

The Telerik Blazor Js reference was missing: <script src="_framework/blazor.webassembly.js"> </script> <script src="_content/Telerik.UI.for.Blazor/js/telerik-blazor.js"> </script> #jefferson2020

### Response

**Hristian Stefanov** commented on 09 Oct 2023

Hi Jefferson, I'm happy to see you quickly found the solution on your own. Thank you for sharing it here, publicly, so other developers can benefit from it. Kind Regards, Hristian

### Response

**Jonathan** commented on 31 Oct 2023

Thanks for posting this as this resolved the same issue that we had too! Regards, Jonathan
