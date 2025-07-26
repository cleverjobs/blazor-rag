# Modal Popup - Close button Click Event

## Question

**Vis** asked on 18 Sep 2020

I need customized Click event on clicking Modal popup close button. <WindowActions><WindowAction Name="Close" /></WindowActions> Instead of above code, I need as below <WindowActions> <WindowAction Icon="@IconName.Close" OnClick="@OnCloseClick" /> </WindowActions> async Task OnCloseClick() { }

## Answer

**Marin Bratanov** answered on 18 Sep 2020

Hello Vishnu, You have a couple of options: Use the VisibleChanged event: [https://docs.telerik.com/blazor-ui/components/window/events#visiblechanged](https://docs.telerik.com/blazor-ui/components/window/events#visiblechanged) Use the action click event and add visibility changing logic in its code as it is now a custom action: [https://docs.telerik.com/blazor-ui/components/window/events#action-click](https://docs.telerik.com/blazor-ui/components/window/events#action-click) Regards, Marin Bratanov

### Response

**Jim** answered on 15 Feb 2021

What is this component used for? Telerik.Blazor.Components.Popup.TelerikPopup

### Response

**Marin Bratanov** answered on 15 Feb 2021

Hi Jim, This is not a public component that you can use. It is part of the inner workings of our component suite. There simply is no provision in the framework to hide such components from the intellisense, and by definition they must have the public access modifier because they are a razor component. In a future version of the framework it will probably have the feature to mark element ancestry so that tags show up only when applicable and this might reduce the possible components you see in the intellisense. To add to the original question - you can Follow this item to know when OnClick can be used for the built-in actions of the window: [https://feedback.telerik.com/blazor/1505032-fire-onclick-for-built-in-actions-before-the-built-in-action](https://feedback.telerik.com/blazor/1505032-fire-onclick-for-built-in-actions-before-the-built-in-action) Regards, Marin Bratanov

### Response

**Hao** answered on 26 Oct 2022

HI, Can I close the Dialog box programatically. The document said Visible is two-way binding but with this snip code, it does not close programatically for me. I tried to set TriquestraProgressBarVisible from True to False. Does it needs users to click close? ProgressBarVisible=true; var id=await _stocktakeScheduleDetailService.SavingStateAsync(Model); ProgressBarVisible=false; <TelerikDialog @bind-Visible="@ViewModel.ProgressBarVisible"> <DialogContent> Are you sure you want to delete item with </DialogContent> <DialogButtons> </DialogButtons> </TelerikDialog> I did try Loading Container but It could not close programatically [https://docs.telerik.com/blazor-ui/components/loadercontainer/overview](https://docs.telerik.com/blazor-ui/components/loadercontainer/overview)

### Response

**Dimo** commented on 31 Oct 2022

@Hao - yes, you can close the Dialog programmatically. Our online demos show this approach in a Button OnClick handler. Here is a test page that uses your code. I assume that the problem may be related to incorrect Blazor life cycle usage or cross-component parameter values.
