# NuGet Feed for Latest Version?

## Question

**Adr** asked on 19 Aug 2019

Is the latest package available from a nuget feed anywhere? I don't see it on any public feed, nor on the private nuget feed that was setup when I first installed. In the private feed, I only see v1.0 Am I missing something?

## Answer

**Marin Bratanov** answered on 19 Aug 2019

Hi Adrian, You can download the zip archive from your account and set up a local feed, as shown in this article: [https://docs.telerik.com/blazor-ui/installation/zip](https://docs.telerik.com/blazor-ui/installation/zip) Generally, the new versions are also available from our authenticated NuGet feed online, but with trial licenses that have had a previous trial so soon, the system may cut off access as a general licensing behavior. We have taken extra steps to allow trials to be downloaded for Blazor in such short timeframes, considering it is a new and still experimental technology, but retrofitting that into the live feed could break something for the hundreds of other packages we have, and we have not taken this risk. Regards, Marin Bratanov
