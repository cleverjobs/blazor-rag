# Menu problems

## Question

**Alb** asked on 04 Sep 2019

I am testing the new menu component but found some issues: 1. when you move the mouse over the menu options sometimes more than one menu remains openned. (attached screenshot) 2. when you click a submenu option the submenu is not closed/hidden. 3. add option to show/open submenus only when clicking in the menu option, not when passing mouse over it.

## Answer

**Marin Bratanov** answered on 05 Sep 2019

Hi Alberto, To each separate question: when you move the mouse over the menu options sometimes more than one menu remains openned. (attached screenshot) - we are aware of this, and we are working on it. I made the following Feedback portal page so you can Follow its progress: [https://feedback.telerik.com/blazor/1428330-multiple-parent-menu-items-can-be-expanded-at-the-same-time.](https://feedback.telerik.com/blazor/1428330-multiple-parent-menu-items-can-be-expanded-at-the-same-time.) when you click a submenu option the submenu is not closed/hidden. - I created the following Feature Request page so you can track its status, and if you have any other comments or ideas on this, feel free to post them there: [https://feedback.telerik.com/blazor/1428332-add-method-to-hide-the-menu.](https://feedback.telerik.com/blazor/1428332-add-method-to-hide-the-menu.) The menu' primary function is navigation and it will hide when its view disposes when navigation occurs. It also hides on mouseout. add option to show/open submenus only when clicking in the menu option, not when passing mouse over it. - Here's a request page to track this feature: [https://feedback.telerik.com/blazor/1428333-show-menu-items-on-click-instead-of-hover.](https://feedback.telerik.com/blazor/1428333-show-menu-items-on-click-instead-of-hover.) Regards, Marin Bratanov

### Response

**Alberto** answered on 19 Sep 2019

I have updated to 2.0 that is suppose to fix the problem but still same problem and multiple menus are left open. Menu FIXED Multiple parent menu items can be expanded at the same time.

### Response

**Marin Bratanov** answered on 20 Sep 2019

Hi Alberto, Can you reproduce this when running our demos locally, or on your own local project? I am asking this because it seems that the large latency to our live demos may still be causing this, even though there shouldn't be an issue in a local environment (which is what Server-side Blazor is suitable for). That said, I have reopened the issue and we will look into it further. Regards, Marin Bratanov

### Response

**Pedro** answered on 28 Oct 2020

We are having the same problem, we use Telerik.UI.for.Blazor. 2.17.0, I am attaching an example. it's become really problematic.

### Response

**Marin Bratanov** answered on 28 Oct 2020

Hi Pedro, You can Follow this here [https://feedback.telerik.com/blazor/1428330-multiple-parent-menu-items-can-be-expanded-at-the-same-time.](https://feedback.telerik.com/blazor/1428330-multiple-parent-menu-items-can-be-expanded-at-the-same-time.) It has been reopened for a while but the sync had failed, but I fixed that now. This is by far not a trivial issue to debug, investigate and fix. Regards, Marin Bratanov

### Response

**Mirano** answered on 23 Nov 2020

Using Blazor controls 2.18, the problems reported in September 2019 are still there and nothing has changed, so this persists for more than a year. When are you going to fix this?

### Response

**Marin Bratanov** answered on 23 Nov 2020

Hi Mirano, The key issue with this particual problem is that it is un-debuggable. To manifest, it requires a large latency. This requires a remote server. At the same time, WebAssembly debugging is still not good enough. We've investigated this and improved some things a few times already. That said the best way to know when something happens is to Follow the

### Response

**Aleksandr** answered on 23 Nov 2020

+1 have similar issues, would love to have it fixed, repro 100%

### Response

**Marin Bratanov** answered on 24 Nov 2020

Hi Aleksandr, Your vote is already in and you can Follow the progress of that issue in the portal too. Regards, Marin Bratanov

### Response

**Mirano** answered on 24 Nov 2020

I have to say I have no idea what you are talking about. First webassembly, then debugging, then that you need some server... Let's make this short: add 3 menus, each menu with 10 sub-items with some long names, then fire it up and go with mouse over them, they will open randomly on mouse over (I have no idea why the menus would drop down if I did not click on them, this behavior does not exist anywhere in the universe), they would not collapse and soon you will get all three menus going over each other making a mess on the screen. Very easy to reproduce and it sure not working properly, so either fix it or remove this component out of the suite, that's all.

### Response

**Todd** answered on 18 Dec 2020

+1 as well. Seems somewhat more likely when moving the mouse quickly - but end users will do what end users do, right?

### Response

**Marin Bratanov** answered on 19 Dec 2020

Hello Todd, Moving the mouse quickly over a menu is more likely to cause this, yes. You can Follow a fix here. Regards, Marin Bratanov
