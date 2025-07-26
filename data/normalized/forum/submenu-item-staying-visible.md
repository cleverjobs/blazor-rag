# Submenu item staying visible

## Question

**Eri** asked on 31 Mar 2020

Hello, I am using the menu component and am noticing that submenus can remain visible after moving the mouse cursor off them. An example: [https://raw.githubusercontent.com/austineric/StaticAssets/master/Example1.gif](https://raw.githubusercontent.com/austineric/StaticAssets/master/Example1.gif) (The example uses sample code from [https://demos.telerik.com/blazor-ui/menu/index)](https://demos.telerik.com/blazor-ui/menu/index)) I've had users move their mouse that way by chance and it makes the navigation confusing. Is there anything I can do differently to avoid the behavior? Thanks, Eric

## Answer

**Marin Bratanov** answered on 31 Mar 2020

Hi Eric, Such behavior is something that can be observed in a Server-side BLazor app when the user has a high latency to the server. It's an inherent problem in this scenario and we've done what can be done to alleviate it. Server-side Blazor is not suitable for public facing sites (such as our demos, by the way) and perhaps such an app needs to be hosted on Azure so it can be close to your users, or you should migrate it to a WASM app to eliminate the SIgnalR latency altogether. That said, can you reproduce this problem in a low-latency environment (not like our demos)? Regards, Marin Bratanov

### Response

**Eric** answered on 31 Mar 2020

Hi Marin, That example is actually from a project running locally on my machine. Thanks for the explanation, that makes sense.

### Response

**Marin Bratanov** answered on 31 Mar 2020

Hi Eric, I tried the demo locally and I could not reproduce such behavior. Does this work fine for you in a WASM app? If yes, then it is definitely a SignalR mixup due to latency (where that latency would be coming from on localhost is beyond me, though). Regards, Marin Bratanov

### Response

**Aditya** answered on 15 Mar 2021

I am having this same issue with Blazor Server Side app. Instead of displaying the sub-menus on hover, will it be possible to show the submenus only upon explicitly clicking on the top menu or a drop down indicator? Something similar to this=> Check "Show Item on Click" option [https://blazor.syncfusion.com/demos/menu-bar/api?theme=bootstrap4](https://blazor.syncfusion.com/demos/menu-bar/api?theme=bootstrap4)

### Response

**Marin Bratanov** answered on 15 Mar 2021

Hello Aditya, The good news is that this issue with the menu items staying open should be fixed in our next release: [https://feedback.telerik.com/blazor/1428330-multiple-parent-menu-items-can-be-expanded-at-the-same-time](https://feedback.telerik.com/blazor/1428330-multiple-parent-menu-items-can-be-expanded-at-the-same-time) As for showing menu sub-items on click - it will be possible when this feature gets implemented: [https://feedback.telerik.com/blazor/1428333-show-menu-items-on-click-instead-of-hover](https://feedback.telerik.com/blazor/1428333-show-menu-items-on-click-instead-of-hover) You may also find interesting this one: [https://feedback.telerik.com/blazor/1476204-hide-event-for-the-menu-not-hide-on-mouseout](https://feedback.telerik.com/blazor/1476204-hide-event-for-the-menu-not-hide-on-mouseout) I've added your Vote on your behalf for both to raise their priority, and you can click the Follow button on those pages to get email status updates. Regards, Marin Bratanov

### Response

**Aditya** answered on 15 Mar 2021

Thank you Marin ...is there a tentative release date for the next version (2.23.0)?

### Response

**Marin Bratanov** answered on 16 Mar 2021

Hi Aditya, We are aiming at the end of March or early April. Regards, Marin Bratanov
