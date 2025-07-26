# Possible error in the edit grid template

## Question

**Mar** asked on 31 Aug 2023

Blazor Grid - Popup Editing - Telerik UI for Blazor <GridSettings> <GridPopupEditSettings MaxWidth="600px" MaxHeight="300px" Class="custom-popup"> </GridPopupEditSettings> <GridPopupEditFormSettings Orientation="@FormOrientation.Horizontal" ButtonsLayout="FormButtonsLayout.Center" Columns="2"> </GridPopupEditFormSettings> </GridSettings> The button layout is always left no matter what you choose in FormButtonsLayout

## Answer

**Nadezhda Tacheva** answered on 05 Sep 2023

Hi Martin Herløv, Thank you for reaching out! You are correct, there seems to be a problem with the button layout in the popup edit form. While researching this matter, I found out this regression occurs as of version 4.3.0 of UI for Blazor - prior to that the buttons appear in the correct layout. Great catch! I logged a bug report for that on your behalf: Popup Edit Form: Buttons do not render in the correct layout as of version 4.3.0 I added your vote there but we are generally striving to fix the regressions as quickly as possible. As a creator, you will get an email notification when the status of the item changes. For the time being, possible workarounds are to position the buttons with CSS or use a Popup Buttons Template. Last but not least, I want to take a moment to thank you for pointing our attention to that behavior! As a small token of gratitude, I have rewarded your account with some Telerik points. Regards, Nadezhda Tacheva Progress Telerik

### Response

**Martin Herløv** commented on 05 Sep 2023

Thanks 😊Always great service from you For now, I am using CSS for the alignment
