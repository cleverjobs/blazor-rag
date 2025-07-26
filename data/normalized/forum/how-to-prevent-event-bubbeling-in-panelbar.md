# How to prevent Event Bubbeling in Panelbar

## Question

**Dom** asked on 09 Dec 2022

Hi, I have some additional Controls in a PanelBar-Header-Template. Anytime when I click on a Control the Event bubbles to the PanelbarHeader and opens the panel. How can I prevent this bubbeling? As you see, I tried to get rid of that with "stopPropagation". But you can imagine it doesn't work. <TelerikPanelBar Data="@item.ColorsWithArticles" @bind-ExpandedItems="@ExpandedItems" OnExpand="@OnPanelBarExpand"> <PanelBarBindings> <PanelBarBinding Level="0" ItemsField="Articles"> <HeaderTemplate> @{
var article=((ColorAndArticlesItemVm)context); <div class="d-flex flex-row flex-wrap"> <div class="p-1 border"> <img src="@article.Color.ColorImageUrl" alt="" style="width:28px; height:28px"> </div> <div onkeydown="stopPropagation(event)" onmousedown="stopPropagation(event)"> <TelerikTextBox @bind-Value="@StringValue" /> </div> </div> <script suppress-error="BL9992"> function stopPropagation ( e ) {
e.stopPropagation();
} </script> Thank you

## Answer

**Yanislav** answered on 13 Dec 2022

Hello Dominik, Thank you for the shared code snippet. I was able to reproduce the problem. The fix is to replace ' onmousedown ' with ' onclick ': [https://blazorrepl.telerik.com/GcPmPcld36ljDZ2M23](https://blazorrepl.telerik.com/GcPmPcld36ljDZ2M23) <div onkeydown="stopPropagation(event)" onclick="stopPropagation(event)"> <TelerikTextBox @bind-Value="@StringValue" /> </div> The idea is that stopPropagation should be set for the same events that we use internally for the component's keyboard navigation. I hope this helps. Regards, Yanislav
