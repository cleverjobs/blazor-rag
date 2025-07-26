# Change the way negative numbers show

## Question

**BobBob** asked on 15 Apr 2021

I want negative #'s to show as -9999 not (9999). Is there any way to do this? I could do it with the Kendo controlsby putting kendo.culture().numberFormat.currency.pattern[0]="-$n"; in the document.ready function but I can't see to figure out how to do it with Blazor controls. Thanks.

## Answer

**Marin Bratanov** answered on 16 Apr 2021

Hello Bob, The format in Blazor numeric textbox is determined by the thread culture, you can read more about the behavior of our components with globalization and cultures in the dedicated article: [https://docs.telerik.com/blazor-ui/globalization/overview.](https://docs.telerik.com/blazor-ui/globalization/overview.) So, in the common case, the format will be simply a minus in front of the number. I am attaching here one localization sample modified to also have a numeric textbox so you can see the behavior when the culture is changed. Regards, Marin Bratanov

### Response

**Bob** answered on 16 Apr 2021

I did read that article, but I didn't see anything that said I could change Globalization options, only localization which appears to only be the wording within controls. However, on that note, I wanted to change the Options in the Confirm Dialog to be "Yes" & "No" instead of "OK" and "Cancel". I looked that the resx file in the Demos folder like the localization article said but could not find anything in it for the Dialog control. I have the latest version of controls as well. I will check out your video and the link you attached and hopefully they will help.

### Response

**Marin Bratanov** answered on 16 Apr 2021

Hi Bob, Try the project, ensure you have set an explicit culture on the threads and see how things go. The numeric textbox basically does a .ToString(Format) and thus .NET generates the string based on the format settings of the culture. You may also want to check if your application overrides the number format. As for the dialog buttons - you can use localization, the keys for those buttons are "Dialog_Ok" and "Dialog_Cancel". If you do not see them in the messages file in our demos, then the demos you are reviewing are for an older version. You need to make sure to check them out from the 2.23.0 version, the previous ones don't have the dialog component. It is important to keep in mind that localization is a subset of globalization, just like number and date formats are subsets of globalizing an app. Regards, Marin Bratanov

### Response

**Bob** answered on 16 Apr 2021

Sorry, but I don't really understand what you mean by "ensure
you have set an explicit culture on the threads"? I see where you add the localization in the Startup.cs but I don't see anything about Globalization being set anywhere. Sorry, I a new to this globalization & localization stuff.

### Response

**Marin Bratanov** answered on 16 Apr 2021

Hi Bob, The localization middleware does that for you in a server-side blazor app, based on the cookie and the controller action that makes it. You can also explore the WASM sample where the culture setting through a culture chooser UI is much more explicit: [https://github.com/telerik/blazor-ui/tree/master/common/localization/ClientLocalizationResx](https://github.com/telerik/blazor-ui/tree/master/common/localization/ClientLocalizationResx) - see this in Program.cs: [https://github.com/telerik/blazor-ui/blob/master/common/localization/ClientLocalizationResx/Client/Program.cs#L34-L45](https://github.com/telerik/blazor-ui/blob/master/common/localization/ClientLocalizationResx/Client/Program.cs#L34-L45) I also recommend you review the MSDN documentation about globalizing Blazor as a first step in this journey: [https://docs.microsoft.com/en-us/aspnet/core/blazor/globalization-localization?view=aspnetcore-5.0](https://docs.microsoft.com/en-us/aspnet/core/blazor/globalization-localization?view=aspnetcore-5.0) [https://docs.microsoft.com/en-us/aspnet/core/fundamentals/localization?view=aspnetcore-5.0](https://docs.microsoft.com/en-us/aspnet/core/fundamentals/localization?view=aspnetcore-5.0) Regards, Marin Bratanov

### Response

**Bob** answered on 16 Apr 2021

Got the localization working. For the Globalization, it took me some time, but I finally figured out I had to add the following line in my startup.cs to get it to work when I am formatting the value as "C". supportedCultures.First().NumberFormat.CurrencyNegativePattern=1; (Note, I am only using one culutre, "en-US" so using .First() works just fine for me)

### Response

**Marin Bratanov** answered on 16 Apr 2021

Glad to see you have solved this, Bob! --Marin
