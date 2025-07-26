# Could not find 'initGrid' in 'window.TelerikBlazor'.

## Question

**And** asked on 29 Aug 2019

Hi, Marin. Today I spotted some problem in console. My be it's appeared after new 1.6.0 version. Path to java script was not changed long time and this path was taken from [https://docs.telerik.com/blazor-ui/getting-started/client-blazor](https://docs.telerik.com/blazor-ui/getting-started/client-blazor) <script src="_content/telerik.ui.for.blazor.trial/js/telerik-blazor.js" defer></script>

## Answer

**Marin Bratanov** answered on 29 Aug 2019

Hi Andriy, The error indicates that the JS Interop file is either missing, or references a wrong version. Since you are using static assets, the most likely problem is that they are not enabled on the server project that hosts the blazor app. I am attaching here a small sample I made for you that has a grid that works fine for me so you can compare against it. Regards, Marin Bratanov

### Response

**Marin Bratanov** answered on 29 Aug 2019

And I am attaching here one that uses the trial package, because I forgot to change that from my local test app. If comparing against those samples does not help, please modify either of them to showcase the problem. Alternatively, send me another project that I can run and inspect. Regards, Marin Bratanov

### Response

**Andriy** answered on 29 Aug 2019

Hi, Marin. Thank you for your quick answer. Your project works fine. I don't now what I did wrong, but after several manipulations (restore changesets from Team Foundation Server and restore telerik blazor version 1.5.0) project starts normally. After restore last version of my project and upgrade to component 1.6.0 all works normally too. Tell me please, when project starts, this link always download java scripts from telerik server? <script src="_content/telerik.ui.for.blazor.trial/js/telerik-blazor.js" defer></script> Or this java script is a part of telerik libriry on my computer?

### Response

**Marin Bratanov** answered on 29 Aug 2019

Hi Andriy, This URL points to a local file that is in our nuget package. The build of the project copies such static assets to the _content/<packageName> folder. Regards, Marin Bratanov

### Response

**Andriy** answered on 30 Aug 2019

I found, how to fix this exception. In Visual Studio need to clean solution in Buld Menu. Today I got the same error for popup windows. After cleaning all works fine.

### Response

**Marin Bratanov** answered on 01 Sep 2019

Thanks for sharing your solution with the community, Andriy. I marked your post as an answer to the thread as well. Regards, Marin Bratanov

### Response

**Andriy** answered on 10 Oct 2019

History of my issue have some continue. Today I made first publication of our site on our server. After fixing several problems I found, thatTelerik Blazor Java script not working. I get old good message "Could not find 'initGrid' in 'window.TelerikBlazor'.". And I ask myself "wtf". After 5 minuts researches I found this: 1. My root publish folder is C:\Program Files\ANDRIY.CO\Base2BaseSite 2. Index.html was plased into C:\Program Files\ANDRIY.CO\Base2BaseSite\Base2BaseSite2019\dist 3. But Blazor Java scripts was plased into C:\Program Files\ANDRIY.CO\Base2BaseSite\wwwroot\_content\Telerik.UI.for.Blazor\js I don't know why. I used standard way to publish my app into folder by Visual Studio Publish wizard. Why Publish wizard send java script into wwwroot folder, I don't know. After manual move "_content" folder (with sub folders) into C:\Program Files\ANDRIY.CO\Base2BaseSite\Base2BaseSite2019\dist all works normally.

### Response

**Marin Bratanov** answered on 10 Oct 2019

Hi Andriy, When I right click> Publish the server-side project in the solution, I get the same folder structure - the client app has its own folder with the dist folder in there, but the static assets are copied by the framework into the ~/wwwroot folder, because that's where the .exe of the server project will look for them, and that works properly for me. You shouldn't need to move folders yourself. Recently we've received some feedback about weird problems when apps get published, and they were all around the WASM flavor (even though they related to issues with wrong .dll files being copied by publish builds). At the moment, I'd say that there's something in the framework that's not quite right in this regard yet. Are you using a client-side app? I can also suggest you take a look at the following article that lists the problems around the JS Interop file that we've found so far, their causes and solutions: [https://docs.telerik.com/blazor-ui/troubleshooting/js-errors.](https://docs.telerik.com/blazor-ui/troubleshooting/js-errors.) Regards, Marin Bratanov

### Response

**Andriy** answered on 10 Oct 2019

Hi, Marin Thank you for you answer. Yes, I'm using client side app (web assembly).

### Response

**Marin Bratanov** answered on 11 Oct 2019

Hi Andriy, Is it a sefl-hosted (static site), or an ASP.NET Core hosted? If it is ASP.NET Core hosted there shouldn't be issues. If it is a self-hosted static site - you can't use static assets in it, because MS have not fixed that yet (I hope they do). Does trying the other steps from the article I linked help? Regards, Marin Bratanov

### Response

**almostEric** answered on 12 Nov 2020

Hi, I am getting this same error but with a server based Blazor App. (using the Blazor demo and .net 5.0) I assume it is some simple config setting, but not seeing it

### Response

**Marin Bratanov** answered on 12 Nov 2020

Hello, Could you try following the ideas from the Microsoft.JSInterop.JSException: Could not find ... section of our docs? If the versions are correct and the file returns successfully, then removing the "defer" attribute is likely to fix this. Regards, Marin Bratanov

### Response

**almostEric** answered on 12 Nov 2020

Hi, I went through that doc - my project is using Blazor.Trial 2.19. StaticAssets are enabled. Where is the defer attribute that I should remove?

### Response

**Marin Bratanov** answered on 12 Nov 2020

It's in the index file of your app - where you register the Telerik JS Interop file. Change it from <script src="_content/Telerik.UI.for.Blazor.Trial/js/telerik-blazor.js" defer></script> to <script src="_content/Telerik.UI.for.Blazor.Trial/js/telerik-blazor.js"></script> Regards, Marin Bratanov

### Response

**almostEric** answered on 12 Nov 2020

OK, found it - it was actually in the _Host.cshtml file (in the Telerik demo project). The script line was actually missing in my project. Is there some documentation for manually adding Telerik controls to an existing project? It seems like you assume we will start from the Telerik.Blazor template. I also had to add the link to kendoCss Thanks for the help

### Response

**Marin Bratanov** answered on 12 Nov 2020

Hello, The following article explains the manual steps: [https://docs.telerik.com/blazor-ui/getting-started/what-you-need](https://docs.telerik.com/blazor-ui/getting-started/what-you-need) Regards, Marin Bratanov
