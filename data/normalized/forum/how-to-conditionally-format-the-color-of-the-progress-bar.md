# How to Conditionally format the color of the progress bar

## Question

**Pat** asked on 14 Jun 2022

Is there a way to format the color of TelerikProgressBar based off data? I see you can set the Class on that item, however it does not apply background-color to the fill of the bar. I've found that I can modify all bars by setting the following css: .k-progressbar .k-state-selected { background-color:green; } Thanks!

### Response

**Benjamin** commented on 16 Jun 2022

Have you tried using the Class-Attribute of the ProgressBar-Component? You can add any class you want, like bg-green/bg-red/... (if bootstrap installed) You can define the css classes to use one line before ... @{ var defaultClass="bg-green"; if(mymodel.amount> 3) defaultClass="bg-red"; } <TelerikProgressBar Value="@model.Progress" Class="@defaultClass">...</TelerikProgressBar>

### Response

**Patrick** commented on 16 Jun 2022

Yes, if I apply the background-color attribute in a custom class and conditionally apply it to the element it changes the background fill color and not the color of the bar.

### Response

**Benjamin** commented on 16 Jun 2022

Gotcha :) You have the "highlighted" (e.g. blue) bar and the progressbar itself (usually grey). The highlighted bar has css-classes .k-progressbar .k-state-selected, while the progressbar is just the .k-progressbar. You can reach the goal with css selectors (same approach as above), just add additional css like: .k-progressbar.bg-green { background-color: lawngreen; } .k-progressbar.bg-green .k-state-selected { background-color: green; } output: It would be much better to have a property for this, but afaik there is no such (yet). I'd suggest you to throw an suggestion in the box: [https://feedback.telerik.com/blazor?listMode=Recent&categoryId=2231:)](https://feedback.telerik.com/blazor?listMode=Recent&categoryId=2231:))

### Response

**Patrick** commented on 16 Jun 2022

Thanks Benjamin! I'll definitely throw a suggestion for adding a property. I had to modify it slightly to get it to work for me, but you definitely pointed me in the right direction. Posted bellow the modified css needed and a picture the inspector and rendered HTML .bg-green .k-state-selected { background-color: green; }

## Answer

**Patrick** answered on 22 Jun 2022

1. Set custom class on TelerikProgressBar @customClass='bg-green' <TelerikProgressBar Value="@model.Progress" Class="@customClass">...</TelerikProgressBar> 2. Add Css to overwrite the background-color when YourCustomClass .k-state-selected. bg-green.k-state-selected { background-color: green; }

### Response

**Ivan** commented on 22 Jun 2022

Since 3.4.0 version, this feature not workig with custom Saas Theme Buider See attachments _Layout.cshtml @*<link href="@Url.Content("lib/blazor-ui/swatches/default-ocean-blue.css")" rel="stylesheet" type="text/css" />*@<link href="@Url.Content("css/telerik-light/telerik-light.css")" rel="stylesheet" type="text/css" />

### Response

**Nadezhda Tacheva** commented on 27 Jun 2022

Hi Ivan, It looks like the issue here is specifically theme related as I did not manage to reproduce it with the built-in themes using UI for Blazor 3.4.0. I will open a dedicated ticket on the matter, so we can revise it with our front-end engineers.

### Response

**W.** commented on 01 Jul 2022

We experience the same problem since 3.40 Bootstrap Theme (made with Saas theme builder .. .months ago) after updating the CSS the problem solved !

### Response

**Nadezhda Tacheva** commented on 05 Jul 2022

Hi W., The issue occurred as the themes in the ThemeBuilder were not accordingly updated, so this caused a mismatch between the latest component rendering and the themes generated through the ThemeBuilder. Our front-end engineers managed to address this quickly and indeed, generating the desired theme anew is expected to solve the problem.

### Response

**Nadezhda Tacheva** answered on 27 Jun 2022

Hi all, We now have a feature request for adding Property to set color of Progress Bar that Patrick opened. I just wanted to link it here, so any other interested parties might easily find and follow it. Regards, Nadezhda Tacheva

### Response

**Ivan** commented on 27 Jan 2023

Hi Nadezhda! v 4.0.0 - has same bug again Progress doesn't showing with any custom theme

### Response

**Nadezhda Tacheva** commented on 01 Feb 2023

Hi Ivan, You are correct. UI for Blazor 4.0.0 was released on January 18, however, some additional time was needed for releasing the ThemeBuilder with the new version of the themes. At this stage, it references the old version of the themes. Please excuse us for the trouble caused in this regard. The new ThemeBuilder version release is planned for today. You may then try generating your custom theme anew. Please let us know if you are experiencing any difficulties with that. Generally speaking, our goal is to publish the new ThemeBuilder version immediately after each product release, so we do not hit such an issue. My colleagues are working on a process, that will produce a new ThemeBuilder release together with each product release.

### Response

**Ivan** commented on 01 Feb 2023

Hi, Nadezhda! I fully support your decision. And it turns out that when updating to a new release of the main components, the project turns out to be not working in some cases. Built-in themes are good, but I'm sure most use custom themes.

### Response

**Nadezhda Tacheva** commented on 01 Feb 2023

Hi Ivan, I agree with you that custom themes are vastly used. The initiative we've started for releasing the new ThemeBuilder version along with the product release will hopefully take effect from the next release. Once this process is settled, one will be able to seamlessly generate and use their custom theme after the product upgrade.

### Response

**Ivan** commented on 03 Feb 2023

Hi Nadezhda! "Today" is two days ago, but the component still doesn't work when using a custom theme.

### Response

**Nadezhda Tacheva** commented on 08 Feb 2023

Hi Ivan, My colleagues have informed me that the new ThemeBuilder version was released on February 2nd. Can you please test generating your theme again and let me know if you are still experiencing issues with it? If so, you may open a dedicated ticket and send us a reproduction, so we can investigate further. Please accept my apologies for the inconvenience.

### Response

**Ivan** commented on 08 Feb 2023

Nadezhda, I'm happy to report that everything is ok. The only condition is that you need to completely recreate the theme, since the names of class variables have changed.

### Response

**Nadezhda Tacheva** commented on 09 Feb 2023

Hi Ivan, Thank you for providing an update! I am happy to find out that the custom theme is now successfully applied. Indeed, it has to be recreated due to the changes in the variables. The good news in this regard is that my colleagues will be working on an improvement of this process to allow for easier migration to new themes.
