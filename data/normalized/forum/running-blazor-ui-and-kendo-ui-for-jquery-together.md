# Running Blazor UI and Kendo UI for JQuery together

## Question

**Dav** asked on 01 Aug 2023

I'm updating an older ASP.Net program (.Net 2; Bootstrap 3; Telerik / Kendo stuff from 2018) and some of the components are just proving easier to rewrite completely than to try and update. I have a proof-of-concept where I've replaced one of our TabStrips with a Blazor UI Tabstrip -- holy crap, Blazor is nice -- but I think the definitions in telerik-blazor.js are overriding the Kendo UI for JQuery definitions. I'm already only importing the JQuery definitions I need and bundling with Webpack -- is there any way to do the same thing with the Blazor UI stuff short of building a stripped release from source?

## Answer

**Dimo** answered on 04 Aug 2023

Hi Dave, There is a feature request to use the JS files for our Blazor components separately. Currently, we don't support it out-of-the-box, but in theory you can implement and configure this ability manually, as you mentioned. We also have a KB article on how to use Kendo UI widgets in a Blazor app. Generally, this should be done as a last resort, because the widgets are not true Blazor components and you will need to wrap them in Razor components to make them behave like ones. Finally, we haven't come across a problem with the two products messing up their scripts. This should not happen, as the two products don't share JavaScript types. The only things that come to my mind are: The possibility for the same HTML element to be initialized as a Kendo UI TabStrip and as a Blazor TabStrip. I believe this can happen only if a jQuery statement in the app targets a Blazor TabStrip by mistake. Two different TabStrips are nested in one another. Regards, Dimo Progress Telerik
