# Issue with Grid filter

## Question

**And** asked on 20 Oct 2020

when I click on the filter icon of the grid I get this error Microsoft.JSInterop.JSException: Could not find 'showAnimationGroupAsync' in 'window.TelerikBlazor'. Error: Could not find 'showAnimationGroupAsync' in 'window.TelerikBlazor'. I am using Telerik.UI.forBlazor 2.17.0 and i am referencing the local JS file _content/Telerik.UI.for.Blazor/js/telerik-blazor.js I am not sure what is causing this error, any help would be appreciated Thanks

## Answer

**Marin Bratanov** answered on 20 Oct 2020

Hello Andrew, The following article summarizes the known reasons and solutions for such problems: [https://docs.telerik.com/blazor-ui/troubleshooting/js-errors](https://docs.telerik.com/blazor-ui/troubleshooting/js-errors) If going through them does not help, I recommend you open a support ticket and send us a small runnable sample that shows the problem so we can take a look at the concrete situation. Regards, Marin Bratanov

### Response

**Andrew** answered on 20 Oct 2020

thanks, I will try to... I have noticed this issue only happens when running locally from Visual Studio

### Response

**Marin Bratanov** answered on 21 Oct 2020

Hi Andrew, In such a case, it is likely that there is a timing issue due to the extremely low latency of the localhost "connection" and perhaps removing the "defer" attribute from the script will help with that. It is not a mandatory thing, we add it to the documentation with the hope to speed up people's pages a bit. Regards, Marin Bratanov
