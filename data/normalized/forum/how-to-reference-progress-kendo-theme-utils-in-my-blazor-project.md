# How to reference @Progress/kendo-theme-utils in my Blazor Project

## Question

**Sha** asked on 20 Feb 2025

I'm trying to use the Telerik and Kendo UI Accessibility Utilities in my Blazor application. I've followed the instructions at [https://www.telerik.com/design-system/docs/utils/get-started/installation/](https://www.telerik.com/design-system/docs/utils/get-started/installation/) to install the npm package, it I'm unclear how to access this from my Blazor application. Looks like I need to add a stylesheet link, but I can't figure out the syntax.

## Answer

**Dimo** answered on 20 Feb 2025

Hi Shawn, One option is to copy the CSS file manually from node_modules to the wwwroot folder of your app. Or, you can use LibMan for a more automated and easy use of CSS files that are installed through npm. This is a generic approach that is not coupled with the CSS utilities specifically. Another option is to simply load the CSS file from CDN. The last URL on the page will always load the latest version. Regards, Dimo Progress Telerik

### Response

**Shawn** commented on 20 Feb 2025

I figured out how to use LibMan. I need my application to be self contained, so using the CDN is not an option for me. I would appreciate if the documentation at the [https://www.telerik.com/design-system/docs/utils/get-started/installation/](https://www.telerik.com/design-system/docs/utils/get-started/installation/) and [https://www.telerik.com/blazor-ui/documentation/styling-and-themes/overview](https://www.telerik.com/blazor-ui/documentation/styling-and-themes/overview) could be enhanced to present this option. In addition to adding the library with LibMan, I had to add a reference to the stylesheet in my app: <link rel="stylesheet" href="~/lib/progress/kendo-theme-utils/dist/all.css" /> None of this was clear from that documentation. Now that the kendo-theme-utils are no longer included in the Blazor themes, I want to request that there be clearer documentation for Telerik UI for Blazor users on how to do this. The link you provided to Using Telerik Blazor Themes with LibMan did not mention the kendio-theme-utils. Since I have used NuGet package for accessing the base theme, I didn't think this applied to me. Better documentation would have saved me a lot of time.

### Response

**Dimo** commented on 20 Feb 2025

The Telerik CSS utilities are not part of Telerik UI for Blazor and are not used by our Blazor components. Explaining how to install them in the Telerik UI for Blazor documentation doesn't make much sense. Nevertheless, I agree that the CSS utilities documentation itself can be improved to me clearer, so I passed your feedback to the team. Sorry about the extra time that you had to invest in this.
