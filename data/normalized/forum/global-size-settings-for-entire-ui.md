# Global size settings for entire UI?

## Question

**And** asked on 18 Apr 2022

Hello, Is there a way to set the size of input/button elements globally on app startup instead of setting it individually on each button/combobox/etc (Telerik.Blazor.ThemeConstants.*.Size)?

## Answer

**Dimo** answered on 21 Apr 2022

Hello Andrei, Currently, there is no built-in functionality to configure global settings in any of our components. However, there are ways to achieve this: Use a separate component that will nest our component and will provide all default parameters. Update the source code of our components and set the default values. Regards, Dimo
