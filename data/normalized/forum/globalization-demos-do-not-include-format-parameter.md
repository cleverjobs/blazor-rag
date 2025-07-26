# Globalization Demos do not include Format parameter

## Question

**Jef** asked on 23 Feb 2021

The Format="d" parameter for the demo site is not in use and does not pick up different cultures appropriately from browser. Also: the en-GB format does not get applied to the date format when the browser language preference is set to English-United Kingdom

## Answer

**Marin Bratanov** answered on 23 Feb 2021

Hi Fritz, Our demos aren't designed to read the browser culture, there is a chooser for a few example ones in a dropdown, such as here where we have German, Spanish, Bulgarian and US English: [https://demos.telerik.com/blazor-ui/daterangepicker/globalization](https://demos.telerik.com/blazor-ui/daterangepicker/globalization) I'm attaching here a sample app that seems to work fine for me and renders things as expected when the culture is set on the app correctly, which is something the app needs to do, our components cannot presume to do that instead of the developer, and we simply use what the framework gives us. Am I missing something in the setup? Does it work as expected for you? Regards, Marin Bratanov

### Response

**Marin Bratanov** answered on 24 Feb 2021

Here is also a WASM version that seems to also work as expected (the range picker is in the Counter page) when the .NET default thread culture is set. Regards, Marin Bratanov

### Response

**Marin Bratanov** answered on 24 Feb 2021

And here is a version where Blazor sets the culture as per the browser preferred language (you need <BlazorWebAssemblyLoadAllGlobalizationData>true</BlazorWebAssemblyLoadAllGlobalizationData> in the csproj for that to work properly). This sample is the same one but without the culture chooser in the UI and without the explicit setting for the culture in Program.cs. Regards, Marin Bratanov

### Response

**Jeff Fritz** answered on 24 Feb 2021

That was the issue -- I was missing the BlazorWebAssemblyLoadAllGlobalizationData entry in csproj. Once that was added... Dates were formatted properly.

### Response

**Marin Bratanov** answered on 24 Feb 2021

Happy to see you moving forward! I've also marked your post as the answer to the thread for anyone else having a similar mishap. Regards, Marin Bratanov
