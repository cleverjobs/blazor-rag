# TelerikMenu not functioning in the Blazor Project Template

## Question

**Doo** asked on 20 Jan 2020

Hi! I just used the Telerik Extension to create a Server-Side Grid Demo project using .Net Core 3.1 on VS Enterprise 16.4.3. The project runs properly but I noticed that the menu is not behaving properly at all: - I always has the Home element highlighted - The Menu Items are not functioning after clicking so I cannot navigate to /counter or my custom /company page - Console in Edge and Chrome do not register any activity when I click on a MenuItem - Inspecting the Menu Item doesn't show the internal <a> with a proper href set - I'm running site on IIS Express with HTTPS self-signed certificate

## Answer

**DoomerDGR8** answered on 20 Jan 2020

Here is a working project showing the issue I'm facing: [https://1drv.ms/u/s!AniVX60enXnSvM4ACXdBL7akOH4aOA?e=BdeEpl](https://1drv.ms/u/s!AniVX60enXnSvM4ACXdBL7akOH4aOA?e=BdeEpl)

### Response

**Marin Bratanov** answered on 20 Jan 2020

Hello Hassan, The provided link does not open so I can only guess, yet here is what I can surmise for each issue: I always has the Home element highlighted - this is a bug in the keyboard navigation of the menu - it always gets focused when the page loads, we will fix that. This applies only to the focus outline on my end, though, and does not break anything. The Menu Items are not functioning after clicking so I cannot navigate to /counter or my custom /company page - generally, this looks like an error that was thrown and broke the app. Console in Edge and Chrome do not register any activity when I click on a MenuItem - this also indicates an error. Inspecting the Menu Item doesn't show the internal <a> with a proper href set - this indicates an issue in the customized template or another error. I'm running site on IIS Express with HTTPS self-signed certificate - you need to make sure that all network requests return successfully so the app can run Generally, if you see the menu outline this means that you are using 2.6.0 or later, which indicates that you have updated the project template (the default one from the VS gallery still carries 2.5.1). Please make sure that you have upgraded it correctly and try deleting the bin and obj folders in all projects. If this does not help, please open a support ticket and send me the problematic project so I can investigate. Regards, Marin Bratanov

### Response

**DoomerDGR8** answered on 21 Jan 2020

Going with the default VS template and upgrading to Telerik works. Also, point 4, I meant to say that I CAN see the <a> with a proper href.

### Response

**Marin Bratanov** answered on 21 Jan 2020

Hello Hassan, It is good to hear you have a project working. If you find issue in our template or in our components, don't hesitate to reach out. Adding a runnable sample of the problematic behavior helps a lot in the investigation as it lets me debug instead of guess, which results in more accurate answers. Regards, Marin Bratanov
