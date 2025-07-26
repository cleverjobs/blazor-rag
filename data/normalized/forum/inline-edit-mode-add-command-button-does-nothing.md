# Inline edit mode: Add command button does nothing

## Question

**And** asked on 28 May 2019

I directly copy your example code from: [https://demos.telerik.com/blazor-ui/grid/editing-incell](https://demos.telerik.com/blazor-ui/grid/editing-incell) into a server-side Blazor page using .Net Core 3 preview 5. Telerik UI for Blazor 0.5.0. I run the app and the grid works perfectly apart from the "Add Employee" button. When I click it, it does nothing. No new blank row is added. Please note that the other grid command buttons work fine including "Delete" and "Edit".

## Answer

**Marin Bratanov** answered on 28 May 2019

Hi Andrew, The first official 1.0.0 version brought some changes in the command names, and the documentation is for the latest version (which is 1.1.0 at the time of writing, and I strongly advise that you upgrade to it). You can find the old command names in the following KB article: [https://docs.telerik.com/blazor-ui/knowledge-base/grid-update-from-0-5-to-1-0.](https://docs.telerik.com/blazor-ui/knowledge-base/grid-update-from-0-5-to-1-0.) The demos also run on the latest version and thus their code would no longer work on the 0.5.0 pre-release version. Regards, Marin Bratanov

### Response

**Andrew** answered on 28 May 2019

Wow! I had no idea 1.1.0 had been released. For some reason the private NuGet feed I setup as per [https://docs.telerik.com/blazor-ui/installation/nuget](https://docs.telerik.com/blazor-ui/installation/nuget) is still showing 0.5.0 as the only available version. I downloaded the .zip archive from my "Downloads" page and the "Add" button now works. So thank you for that! However it would be great to hear any tips on why my private nuget feed is still just showing 0.5.0...

### Response

**Marin Bratanov** answered on 28 May 2019

Hi Andrew, It's good to hear you have things working. On the feed and versions - we are investigating such a problem at the moment, we had a few similar reports. Could you let me know what happens when you: remove the Telerik feed restart the PC re-add the feed by following the "Store Credentials in Clear Text for the Telerik NuGet feed" section from this article: [https://docs.telerik.com/blazor-ui/installation/nuget](https://docs.telerik.com/blazor-ui/installation/nuget) Can you then see the 1.1.0 version? Regards, Marin Bratanov

### Response

**Andrew** answered on 28 May 2019

Yes, that does seem to have fixed it. Is there another source (like a blog or webpage) I can manually watch to ensure I learn about new versions, just in case the nuget feed again doesn't update for me for some reason?

### Response

**Marin Bratanov** answered on 28 May 2019

Thanks for getting back to me, Andrew. We tend to publish blogs for new releases, and the release notes list will show a new version: [https://www.telerik.com/support/whats-new/blazor-ui/release-history.](https://www.telerik.com/support/whats-new/blazor-ui/release-history.) Regards, Marin Bratanov

### Response

**Marin Bratanov** answered on 03 Jun 2019

A quick follow-up, Andrew, We just created an RSS feed for new releases and here's a direct link: [https://www.telerik.com/feeds/ui-for-blazor-whats-new](https://www.telerik.com/feeds/ui-for-blazor-whats-new) Regards, Marin Bratanov

### Response

**Andrew** answered on 03 Jun 2019

Fab. Have subscribed!!
