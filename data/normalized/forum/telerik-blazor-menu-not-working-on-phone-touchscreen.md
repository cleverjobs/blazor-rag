# Telerik Blazor Menu not working on phone touchscreen

## Question

**Ind** asked on 27 Aug 2021

Hi I tried your blazor-ui demo, the Menu component to find out how it can collapse the sub-menu when user click outside of them. Tested on android phone and the menu with sub-menu is not working. When I touch the menu with sub-menu, nothing happened. [https://demos.telerik.com/blazor-ui/menu/images](https://demos.telerik.com/blazor-ui/menu/images) [https://demos.telerik.com/blazor-ui/menu/overview](https://demos.telerik.com/blazor-ui/menu/overview) [https://demos.telerik.com/blazor-ui/menu/template](https://demos.telerik.com/blazor-ui/menu/template) I tried with 2 browser just to make sure.

## Answer

**Hristian Stefanov** answered on 01 Sep 2021

Hi Indra, I see here two possible scenarios that you might have: You have a collapsed menu, and upon clicking/touching, the sub-menu is not opening. You have an expanded menu, and upon clicking/touching, the sub-menu is not closing. Can you please confirm the actual situation, and did you test on different phones? These details will be helpful in the process of investigating the undesired behavior. I also tested the demos on two different android phones, and it seems the sub-menu opens/closes as expected on my devices. Thank you. Regards, Hristian Stefanov

### Response

**Indra** commented on 02 Sep 2021

Ok, I think it is browser issue; I tested with chrome browser using 2 android phone: huawei and xiaomi, your menu demo page works, the menu can expand and collapse But when I use adblock browser on 2 android phone and huawei stock browser on huawei phone, the initial collapsed menu is not expanding to show the sub-menu when clicked.

### Response

**Hristian Stefanov** answered on 07 Sep 2021

Hi Indra, It seems that this behavior depends on the AdBlock in your phone's browser. The ad-blocker might be detecting the pop-up as an advertisement. I can confirm that we are not aware of any workarounds except disabling or try changing the ad-blocker. If you have any other questions, I would be glad to help. Regards, Hristian Stefanov
