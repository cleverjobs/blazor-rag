# First Steps with UI for Blazor

## Question

**bur** asked on 10 Apr 2019

I am following the instructions on the doc "First Steps with UI for Blazor" ([https://docs.telerik.com/blazor/getting-started/first-steps.html#add-to-existing-project).](https://docs.telerik.com/blazor/getting-started/first-steps.html#add-to-existing-project).) In the section titled "Add to Existing Project", the first instruction states: Activate a trial by visiting the following link: [https://www.telerik.com/download-trial-file/v2-b/ui-for-blazor](https://www.telerik.com/download-trial-file/v2-b/ui-for-blazor) When I do this, a file named "Telerik.UI.for.Blazor.0.4.0" is downloaded to my machine. What do I do with this file? William Burrows

## Answer

**Pavlina** answered on 10 Apr 2019

Hi William, Thank you for your feedback about the First steps article for Blazor. I agree with you that we can add one additional step after the first one that explains in more details what to do with this file. Therefore, we will update the topic and the addition will be available until the end of the week. Meanwhile, you can refer to the info below: When you download the "Telerik UI for Blazor 0.4.0" a trial license for this product is created and the Blazor package appears in your account. This also activates the Telerik Private Nuget feed from where you can install the Blazor Nuget as described in the next steps. For more information about how to use the Telerik Private Nuget feed as package source you can refer to the article below: [https://docs.telerik.com/aspnet-mvc/getting-started/nuget-install#the-telerik-private-nuget-feed](https://docs.telerik.com/aspnet-mvc/getting-started/nuget-install#the-telerik-private-nuget-feed) Let me know if you need additional assistance. Regards, Pavlina

### Response

**burrows@uw.edu** answered on 11 Apr 2019

Thanks for the quick response. However, I am still confused. When I click on the link "[https://www.telerik.com/download-trial-file/v2-b/ui-for-blazor",](https://www.telerik.com/download-trial-file/v2-b/ui-for-blazor",) I am prompted to open the file as a zip file or download it. I am not sure what to do here. Note that after clicking on the link, I am NOT seeing the Telerik.UI.for.Blazor package. Sorry - I must be having a bad day. Thanks for the help.

### Response

**Pavlina** answered on 17 Apr 2019

Hi William, Please excuse me for the long delay. In order to be able to install the Telerik UI for Blazor components, you need to make sure that the following steps are completed. After you click the download link you should save the file let's say on your Desktop as shown in the screenshot below: [https://www.screencast.com/t/NKJzGjfCGGZj](https://www.screencast.com/t/NKJzGjfCGGZj) Once it is downloaded you have to open your existing Blazor app in Visual Studio 2019 or create a new one as described in this section from the documentation. Then you need to create a new entry for telerik.com in the package source that points to your Desktop as a Source: [https://www.screencast.com/t/MKJouAlkia](https://www.screencast.com/t/MKJouAlkia) When this is done you should go to the Browse tab in VS where Telerik.UI.for.Blazor will appear and now you should be able to install our components. [https://www.screencast.com/t/V96vKZ6pxnDg](https://www.screencast.com/t/V96vKZ6pxnDg) In addition, I have recorded a video while creating the Blazor app and installing our components, so you can rely on it in order to see all the steps in action. [https://www.screencast.com/t/QF6RH4wuX](https://www.screencast.com/t/QF6RH4wuX) Please try to follow them and let me know if you still encounter any difficulties running the Telerik Blazor components. Regards, Pavlina Progress for Blazor

### Response

**burrows@uw.edu** answered on 18 Apr 2019

Thanks Pavlina ... the video did the trick. I got it to work. Thanks for all your help on this. bill burrows
