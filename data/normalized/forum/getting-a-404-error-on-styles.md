# Getting a 404 error on styles

## Question

**Pau** asked on 31 Mar 2020

Hi, I'm getting a 404 error on the static resource styles from the assembly "Telerik.UI.for.Blazor.Trial" My path is "_content/Telerik.UI.for.Blazor.Trial/css/kendo-theme-default/all.css" as per your online guide. ([https://docs.telerik.com/blazor-ui/getting-started/what-you-need)](https://docs.telerik.com/blazor-ui/getting-started/what-you-need)) The styles for my own RCL are served just fine using the same methodology. I'm trying to assess the viability of the toolset for a customer and this isn't a great start...

## Answer

**Marin Bratanov** answered on 31 Mar 2020

Hello Paul, We recently added the themes as static assets, so if you are not on the latest version (2.9.0 at the moment), they may not work that way. In such a case, you can try using them from the CDN: [https://docs.telerik.com/blazor-ui/themes/overview#cdn](https://docs.telerik.com/blazor-ui/themes/overview#cdn) or as local dependencies: [https://docs.telerik.com/blazor-ui/themes/overview#libman](https://docs.telerik.com/blazor-ui/themes/overview#libman) Regards, Marin Bratanov
