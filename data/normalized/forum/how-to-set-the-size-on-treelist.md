# How to set the size on TreeList?

## Question

**Cip** asked on 01 Feb 2023

Hello, Now the TelerikTreeList component is rendered by default with the css class k-grid-md. On the TelerikGrid component the Size can be set so the grid can be rendered with the css class k-grid-sm. I would need the possibility to set on TelerikTreeList component the css class k-grid-sm. How can that be achieved now? Best regards, Cipri

## Answer

**Justin** answered on 03 Feb 2023

This answer was using information regarding a different component and as such it was incorrect and has been removed. Regards, Justin

### Response

**Rob** commented on 19 Apr 2023

I'm using the latest release of the components; if I add your suggested Size="sm" the treelist disappears from the rendered view. It also doesn't seem to be recognised by visual studio as a valid property. I simply want consistency between grid and treelist row size. I'm rendering a hierarchical data set if that matters. Thanks Rob

### Response

**Rob** commented on 19 Apr 2023

crit: Microsoft.AspNetCore.Components.WebAssembly.Rendering.WebAssemblyRenderer[100] Unhandled exception rendering component: Object of type 'Telerik.Blazor.Components.TelerikTreeList`1[[Metre2.Snowdrop.Shared.Schema.Estimating.EstimateNode, Metre2.Snowdrop.Shared, Version=1.0.0.0, Culture=neutral, PublicKeyToken=null]]' does not have a property matching the name 'Size'. System.InvalidOperationException: Object of type 'Telerik.Blazor.Components.TelerikTreeList`1[[Metre2.Snowdrop.Shared.Schema.Estimating.EstimateNode, Metre2.Snowdrop.Shared, Version=1.0.0.0, Culture=neutral, PublicKeyToken=null]]' does not have a property matching the name 'Size'.

### Response

**Justin** answered on 23 Apr 2023

Hello Rob, Yes, the previous answer was incorrect. I apologize for any inconvenience that this may have caused. The TreeList component does not currently have a Size parameter. That being said, you may manually adjust the CSS to create consistency between the size of the Treelist and a Grid that is set to Size="sm". To help with this see our article on how to Override Theme Styles. Also, I have created an example in this REPL, that uses inline CSS to override the default size of the Treelist in order to be consistent with the size of a small grid. Regards, Justin Progress Telerik
