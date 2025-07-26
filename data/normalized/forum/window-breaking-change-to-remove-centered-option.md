# Window Breaking Change to Remove Centered Option

## Question

**Sco** asked on 21 May 2025

Why did you remove the centered option in the window in place of Top and Left positions in 9.0.0?! The programmer will now have to manually figure out the top/left corner location based on the browser size and the size of the window. I have 20+ of your window controls and all of them are skewed out of the browser window when I set them to 50%, 50%. This makes centering of a window a completely manual process and VERY difficult.

## Answer

**Dimo** answered on 21 May 2025

Hello Scott, To center the Window, simply set the Top and Left parameter values to an empty string at any time. The Centered parameter did not work after the initial Window display. Removing the parameter actually made the component setup and management simpler. Otherwise the app should also reset Top and Left explicitly when setting Centered="true" programmatically. Regards, Dimo Progress Telerik

### Response

**Scott** commented on 21 May 2025

Works great. Thank you for the help and explanation.
