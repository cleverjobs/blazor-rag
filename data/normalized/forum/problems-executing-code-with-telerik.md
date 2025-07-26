# Problems executing code with Telerik

## Question

**Aks** asked on 09 Dec 2019

Hello I have in the latest months tested Blazor with Telerik components. Friday, my code worked as intended with Telerik DataSource 1.3.0 and Telerik UI for Blazor 2.2.1. Today, the calendar was shown as friday, but the days were unselectable, and the TelerikCharts were invisible. What can I do to prevent it? I have tried to edit the reference to css and js files to older editions, but without effect. Thank you in advance Aksel

## Answer

**Marin Bratanov** answered on 09 Dec 2019

Hello Aksel, Are you, by chance, using a client-side (WASM) type of project? If so, there are new workarounds for the new Linker issues from WASM Preview 4 that you can find here: [https://docs.telerik.com/blazor-ui/getting-started/what-you-need#client-side-project-considerations.](https://docs.telerik.com/blazor-ui/getting-started/what-you-need#client-side-project-considerations.) Also, make sure that you have followed the information here, especially the JS Interop asset versioning if you are using the CDN: [https://docs.telerik.com/blazor-ui/upgrade/overview.](https://docs.telerik.com/blazor-ui/upgrade/overview.) If this does not help, please post here the errors that you get, or, preferrably, open a private ticket where you can send me the problematic project so I can take a look. Regards, Marin Bratanov

### Response

**Aksel** answered on 09 Dec 2019

The project is made in Blazor server-side with the Telerik extension. I have tried to use "_content/telerik.ui.for.blazor/js/telerik-blazor.js" and online with current version code, but noone helped. It is impossible to send any error message, due to it doesn't return anything, other than the console in Chrome says "Uncaught (in promise) undefined".

### Response

**Marin Bratanov** answered on 09 Dec 2019

Hi Aksel, Try opening the console, clearing it, and then reloading the app. You can also keep an eye on the Network tab to see if all requests return successfully (they must). Then, if you get an error, you should be able to see some more details in the console so you can send them to me. If you don't, you may have to enable the detailed errors in the app, here's how to do it: [https://stackoverflow.com/questions/57514541/how-to-turn-on-circuitoptions-detailederrors](https://stackoverflow.com/questions/57514541/how-to-turn-on-circuitoptions-detailederrors) On a side note, can you confirm that you have:.NET Core 3.1.0 RTM installed the Telerik UI for Blazor 2.5.0 package (I do not see a license in your account so if the project can't restore it, a lot of things can go wrong) Regards, Marin Bratanov

### Response

**Aksel** answered on 09 Dec 2019

I do not get any errors neither in network tab, console tab in Chrome nor output from Visual Studio. The component .NET Core 3.1 SDK is also installed, and the latest package is too. The components worked fine friday, but today, it wouldn't work.

### Response

**Marin Bratanov** answered on 10 Dec 2019

Hi Aksel, If the same project worked a few days ago, but not now, the most likely problem is that something happened to the machine - for example, the .NET installation is broken and needs a repair/reinstall, or something went wrong with the nuget cache and clearing it may help. Since I don't see any license on your account (not even a trial) I suspect the problem may be that your machine can't restore our packages. Perhaps the license holder at your company moved the licenses around and you may need to talk to them to get assigned a license again. That said, I'd advise that you open a support ticket and send me the project so I can see what's wrong with it. Regards, Marin Bratanov
