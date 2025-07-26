# Telerik demo not working on ipad

## Question

**Hen** asked on 29 Dec 2020

Hi, trying the blazor demo on [https://demos.telerik.com/blazor-ui/grid/overview](https://demos.telerik.com/blazor-ui/grid/overview) with an ipad Air 2, ios 14.2, using safari or edge, results in error. Is this an unsupported environment? Brgds, Henri

## Answer

**Marin Bratanov** answered on 29 Dec 2020

Hello Henri, Safari and Chrome on iOS, as well as Edge on Windows are supported browsers, you can see the full details here: [https://docs.telerik.com/blazor-ui/browser-support.](https://docs.telerik.com/blazor-ui/browser-support.) In the current situation with Covid, it's hard to come by all possible devices, though, since we can't have them all at home. So, it would be helpful if you could run the demos locally to enable the detailed errors and post the error you get here - this might help us get an inkling on what might be happening. You can find them in the "demos" folder of your local Telerik UI for Blazor installation. On another note - if you are having issues with our demos on all browsers and platforms, it is possible that there is a connectivity problem - our demos are a server-side app and that poses more requirements on the network traffic. Perhaps the problem lies there (a srever-side app is not the best for hosting on the web, but is what had been available for about a year and we had to ship out demos like that). Does running the demos locally or trying the components in a local test project work as expected? Regards, Marin Bratanov
