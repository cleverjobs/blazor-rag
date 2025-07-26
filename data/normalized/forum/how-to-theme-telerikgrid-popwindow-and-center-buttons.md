# How to theme TelerikGrid popwindow and center buttons

## Question

**RobRob** asked on 27 Sep 2023

Seems like these 2 questions should have simple answers, but I cannot figure them out from trial-and-error or looking at the documentation or this forum so far... First item - how to format the title bar of a TelerikGrid popup window. In the attached screenshot and sample page, I know how to format the title bar in a TelerikWindow, but there is no ThemeColor property on either the GridPopupEditSettings or GridPopupEditFormSettings of the TelerikGrid that I can find. How can I format it? Second item - and this pertains to both the TelerikWindow component and the TelerikGrid popup window - how can I center or right-align buttons in the popup windows? Any insights appreciated. :) Rob

## Answer

**Dimo** answered on 02 Oct 2023

Hi Rob, Thanks for the provided runnable code. 1. Popup edit form theming Currently a ThemeColor is not exposed in GridPopupEditSettings. I will suggest to our devs to add it (update: the enhancement is already in testing and should make it for the coming release 4.6.0 next week). A possible workaround is to set the desired theme colors with custom CSS. You can use the custom CSS class that you already have: .custom-popup.k-window-titlebar { background: #0d6efd; color: #fff;
} 2. Popup edit form button layout The setting GridPopupEditFormSettings ButtonsLayout is relevant only if FormTemplate is not used. Otherwise the rendering and layout of the buttons depend entirely on the FormTemplate markup. For example, you can set ButtonsLayout="@FormButtonsLayout.Center" to the <TelerikForm>. Regards, Dimo Progress Telerik
