# Bootstrap dark theme with CSS static content

## Question

**Pie** asked on 08 Nov 2023

I'm using the bootstrap theme with CSS static content. <link rel="stylesheet" href="_content/Telerik.UI.for.Blazor/css/kendo-theme-bootstrap/all.css" /> I would like to change the theme to dark but I can't find the name of the bootstrap dark theme. Is it available for the static content CSS? If I use the CDN it works fine with both normal and dark modes but I'd prefer to use the static content.

## Answer

**Dimo** answered on 10 Nov 2023

Hi Pierluigi, Please notify us when you are posting the same question as a forum thread and a support ticket. This will avoid potential double work on our side. Thanks. Our Nuget package includes only the Main swatch of each theme, plus the Ocean Blue swatch of the Default theme. Here is the list: [https://docs.telerik.com/blazor-ui/styling-and-themes/overview#static-assets](https://docs.telerik.com/blazor-ui/styling-and-themes/overview#static-assets) For other swatches, please use our CDN. Alternatively, download the files and register them from the wwwroot folder. However, in this case, you will have to update them manually after each version update. Regards, Dimo Progress Telerik

### Response

**John** commented on 15 May 2024

Any chance of either including all the swatches in your nuget package or providing another optional/independent package (Telerik.UI.for.Blazor.Themes or something like that) to wrap them up in a single library? I want all the swatches locally (CDN isn't viable for my use-case) but am not interested in manually maintaining the static assets every time I upgrade Telerik.

### Response

**Dimo** commented on 17 May 2024

@John - This was not an option in the past, because each swatch CSS file included an icon font, which was a bit large. Now the icon font is in a separate file, so I raised a discussion in the team to consider adding all swatches to the existing or a separate NuGet package. I will appreciate if you provide the following information, which will help us: Do you use all swatches or just a few of them? Which ones? Do you use and switch multiple swatches in the same app or use different swatches in different apps? What is the reason that you prefer our swatches rather than your own custom themes and swatches? Do the swatch colors match your (customer's) corporate colors, or there is no need to match our component colors to any corporate colors? Thanks a lot!

### Response

**John** commented on 17 May 2024

Hey Dimo, In this specific app we offer all the swatches but don't collect metrics on which specific ones our users prefer to use. We allow the user to switch between any of your themes for aesthetic reasons and personal preferences. Some of our users have sharper eyes and like things compact, others have older eyes and prefer things to be bigger and obvious. However, for most other apps we deploy with just one theme and don't offer the ability to change it. I use your custom swatches because my teams are mainly full stack developers and using Telerik helps to reduce the UI burden since things are "done for me". That frees up time to focus on the more custom middle/backend code instead. I trust that you have folks dedicated to making sure things look good together for each swatch and my color vision isn't what it used to be so... Finally I have to be 508 compliant, so the Telerik tooling/colors helps me meet this requirement from the start. Having your documented compliance lets me check this box easily when I'm asked about it. The only custom theme I've bothered building is one meant for night time as the system is used in the dark as well. Some of your themes are close, but basically replacing colors with dim reds and greens (no whites or anything bright) to preserve night-vision. As that may be an unusual requirement I'm not surprised that I have to roll my own theme. Though we do have a org-wide style guide I don't conform to it much for sites using your tooling. It's mainly for public facing systems and the stuff we use Telerik for is more internally focused. Note obviously for an app without internet (otherwise I'd use your CDN) I have dedicated servers on a local LAN. File size is much less of a concern for me, the only impact I can think of would be slowing down the CI/CD pipeline every time it pulled your packages and even that is minimal since it's background work. Rambled on a bit but hopefully that addresses your questions.

### Response

**Dimo** commented on 17 May 2024

Great, thanks for all the details, John!
