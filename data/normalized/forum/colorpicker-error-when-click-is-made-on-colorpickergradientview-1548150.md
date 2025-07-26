# ColorPicker: Error when click is made on ColorPickerGradientView

## Question

**Cip** asked on 04 Jan 2022

Hi everybody, I'm trying to use the ColorPicker into my project but when I make a click on the ColorPickerGradientView I get the error bellow: Is there a way to fix this issue? Best regards, Cipri

### Response

**Ciprian Daniel** commented on 06 Jan 2022

If it helps I can give you some more informations: My application is a Blazor Server Application and the version of Telerik Components is 2.28.0. I don't know if this info can help you, but I was thinking that the ColorPicker may work only for a Blazor WebAssambly Application. I don't know what to say I just can't select the color with the mouse.

## Answer

**Ciprian Daniel** answered on 11 Jan 2022

What details do you need from me in order to have a solution for my problem?

### Response

**Matthias** answered on 11 Jan 2022

Hello, First create a project with a single page and check if the error still occurs. If yes, then post the source code here. I'm happy to take a look and see if I can reproduce it tomorrow best regards Matthias

### Response

**Ciprian Daniel** commented on 12 Jan 2022

Hello Matthias Thank you for helping. I've created a new Blazor project and I have added the Telerik Color Picker on the Counter Page, the error is still occurring. I post the project here so you can look at it. I'm using .Net Core 3.1 I don't know if that info counts.

### Response

**Ciprian Daniel** commented on 12 Jan 2022

This zip file contains a gif where you can see what happens when trying to pick a color.

### Response

**Matthias** answered on 12 Jan 2022

Hi, Unfortunately I don't have 3.1 on the computer anymore, but I think that after the changes it should also work for you. Here it goes now without problems. Previously I also had an error message. But I'm pretty sure that the solution should also run with 3.1. I have made the following changes: _Host.cshtml <link rel="stylesheet" href="_content/Telerik.UI.for.Blazor/css/kendo-theme-default/all.css" /> <script src="_content/Telerik.UI.for.Blazor/js/telerik-blazor.js"> </script> You had implemented "body" twice. Once in TelerikLayout and once in MainLayout. So it should be enough that you delete one of them for it to work. MainLayout: @inherits LayoutComponentBase <TelerikRootComponent> <div class="sidebar"> <NavMenu /> </div> <div class="main"> <div class="top-row px-4"> <a href="[https://docs.microsoft.com/aspnet/"](https://docs.microsoft.com/aspnet/") target="_blank"> About </a> </div> <div class="content px-4"> @Body </div> </div> </TelerikRootComponent> Example: @page "/" <h1> Hello, world! </h1> Welcome to your new app. <SurveyPrompt Title="How is Blazor working for you?" /> @* Blazor ColorPicker *@<TelerikColorPicker @bind-Value="@Color" /> @code {
string Color { get; set; }="rgb(40, 47, 137)";
} If you still have questions, just write! Have a nice time and greetings from Berlin Matthias

### Response

**Ciprian Daniel** answered on 13 Jan 2022

Hi Matthias, I made the changes you suggested but that issue is still present, I can't select the color using the ColorPicker. Thank you for your help. Cipri

### Response

**Matthias** commented on 13 Jan 2022

Hello, if you like, I can send you the whole project. But as .net 6.

### Response

**Ciprian Daniel** commented on 13 Jan 2022

I'm taking in consideration to change the .Net Core version from 3.1 to .Net Core 5 or .Net Core 6 maybe that will fix the issue.

### Response

**Matthias** commented on 13 Jan 2022

well possible and the switch to .net 6 has other advantages as well.

### Response

**Ciprian Daniel** commented on 13 Jan 2022

I've made another blank project using .Net Core 5 where I've added the ColorPicker and now that issue is not present anymore, the ColorPicker is working fine but in this situation it seams that the ColorPicker is not working on projects based on .Net Core 3.1
