# Dropdowns are not working as they should

## Question

**Gle** asked on 18 Apr 2024

Start app that has the dropdown component click on the dropdown and select one of the options Note: only changes after 6+ clicks Actual result: The specific option isn't opened. <FilterComponent @ref="filterComponent" SelectedItem="selectedItem" SelectedItemChanged="UpdateSelectedItemAsync"> <TelerikStackLayout Orientation="StackLayoutOrientation.Horizontal" HorizontalAlign="StackLayoutHorizontalAlign.Right" VerticalAlign="StackLayoutVerticalAlign.Center" Spacing="5px"> <TelerikDropDownButton Icon="FontIcon.MoreHorizontal" ThemeColor="@ThemeConstants.Button.ThemeColor.Secondary"> <DropDownButtonContent> Reports </DropDownButtonContent> <DropDownButtonItems> <DropDownButtonItem Icon="FontIcon.Table" OnClick="NavigateToReport1Async">Report 1</DropDownButtonItem> <DropDownButtonItem Icon="FontIcon.Table" OnClick="NavigateToReport2Async">Report 2</DropDownButtonItem> <DropDownButtonItem Icon="FontIcon.Table" OnClick="NavigateToReport3Async">Report 3</DropDownButtonItem> </DropDownButtonItems> </TelerikDropDownButton> <TelerikButton Icon="FontIcon.ChangeManually" ThemeColor="@ThemeConstants.Button.ThemeColor.Secondary" OnClick="NavigateToCardAsync">Card</TelerikButton> </TelerikStackLayout> </FilterComponent>

## Answer

**Svetoslav Dimitrov** answered on 23 Apr 2024

Hello Glendys, It seems that I am missing important details from your scenario to fully understand the issue you are facing. Can you provide information on the following: Can you send us the definition of the FilterComponent? I believe that this is a custom component in your application and as it wraps the DropDownButton it might be connected to the issue. Can you send us a runnable code snippet where we can investigate? Regards, Svetoslav Dimitrov Progress Telerik

### Response

**MobileApps** answered on 26 Apr 2024

Hey Svetoslav, I just noticed we have a support account here is my ticket with supported information Ticket 1650162
