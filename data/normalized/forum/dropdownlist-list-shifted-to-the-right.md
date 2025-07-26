# Dropdownlist list shifted to the right

## Question

**Nei** asked on 27 May 2024

What could cause this appearance? Background: I'm upgrading a Blazor Server site from .NET Core 3.1 and Bootstrap 4 to .NET 8 and Bootstrap 5. Upgraded the Telerik Blazor nuget package and regenerated the CSS file using ThemeBuilder. Razor markup is: <TelerikDropDownList TextField="Key" ValueField="Value" Data="@Sizes" @bind-Value="@Size" Width="150px"><DropDownListSettings><DropDownListPopupSettings Height="auto"></DropDownListPopupSettings></DropDownListSettings></TelerikDropDownList> The shift starts if the viewport is greater than 1500px in width. If it's 1500px or less I see: <div class="k-animation-container telerik-blazor" data-id="d53dbb0d-7b8c-49d1-bb05-a173229fa149" role="region" aria-label="Options list" id="7b6577ed-d3c0-4d2c-b473-0ea9fa03f32d" dir="ltr" style="height: auto; left: 12px; top: 99px; width: 150px; z-index: 10002; display: none;"> 1600px shows: <div class="k-animation-container telerik-blazor k-animation-container-shown" data-id="d53dbb0d-7b8c-49d1-bb05-a173229fa149" role="region" aria-label="Options list" id="7b6577ed-d3c0-4d2c-b473-0ea9fa03f32d" dir="ltr" style="height: auto; left: 56px; top: 99px; width: 150px; z-index: 10002;"> The inline left property increases in value as the viewport increases in width.

## Answer

**Nansi** answered on 29 May 2024

Hi Neil, Thank you for the screenshot and the code examples. The <div> class k-animation-container telerik-blazor k-animation-container-shown is generated when the DropDownList popup opens. The k-animation-container telerik-blazor is when the popup is closed. I am not sure that this indicates the misalignment in the DropDownList popup. I tested and created a .NET8 app with Bootstrap 5. I cannot reproduce the issue. Initially, my viewport is set to match the device width. <meta name="viewport" content="width=device-width, initial-scale=1.0" /> And after that, I tested with 1500px and 1600px. The popup appears where it should be. Please review our wrong popup position troubleshooting article and make sure that everything in the application is set correctly. If the problem persists, please send me an isolated runnable example with dummy data for inspection. Regards, Nansi Progress Telerik

### Response

**Neil N** commented on 29 May 2024

Thank you very much. The troubleshooting article led to a solution. Replaced: <app class="app container-fluid"> <component type="typeof(App)" render-mode="Server" /> </app> with <app class="app"> <div class="container-fluid"> <component type="typeof(App)" render-mode="Server" /> </div> </app>
