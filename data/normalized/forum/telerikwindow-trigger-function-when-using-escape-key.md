# TelerikWindow trigger function when using escape key

## Question

**Mar** asked on 03 Feb 2022

I would like to call a function every time the window closes. No matter how the close was triggered. <TelerikWindow Width="900px" Height="fit-content" Centered="true" Visible="@(Details.BaseData.Id> 0)" Modal="true" CloseOnOverlayClick="true"> <WindowTitle> <strong> @Title </strong> </WindowTitle> <WindowActions> <WindowAction Name="Close" OnClick="OnFormClosed" /> </WindowActions>

## Answer

**Blazorist** answered on 03 Feb 2022

Hi Martin. Did you tried using VisibleChanged event? <TelerikWindow Width="900px" Height="fit-content" Centered="true" Visible="@(Details.BaseData.Id> 0)" Modal="true" CloseOnOverlayClick="true" VisibleChanged="@VisibleChangedHandler"> <WindowTitle> <strong> @Title </strong> </WindowTitle> <WindowActions> <WindowAction Name="Close" OnClick="OnFormClosed" /> </WindowActions> </TelerikWindow> @code{ public void VisibleChangedHandler ( bool visible ) {
IsVisible=visible; // set the window visibility /* Do whatever you want */ } Hope that will help. Blazorist

### Response

**Blazorist** commented on 03 Feb 2022

I'm not sure if the VisibleChanged event is fired when the close button is pressed. If this happend, you could use OnFormClosed and VisibleChangedHandler simultaneously.

### Response

**Hristian Stefanov** answered on 08 Feb 2022

Hi all, You are on the right path. There are a couple of options here: Use the VisibleChanged event Use the action click event and add visibility changing logic in its code as it is now a custom action Please test to see which one of the above will suit your app requirements best. Regards, Hristian Stefanov Progress Telerik
