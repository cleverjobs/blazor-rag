# Error with Multiselect looking for property "ChildContent" after component upgrade.

## Question

**Jst** asked on 28 Mar 2022

I'm getting the following error after upgrading from 2.x to 3.x of the Blazor library. Unhandled exception rendering component: Object of type 'Telerik.Blazor.Components.TelerikMultiSelect` does not have a property matching the name 'ChildContent'. This happens when this control attempts to load. <FormItem Field="@nameof(NoteVM.AssignedToUser)"> <Template> <TelerikMultiSelect Data="Users" AutoClose="false" Placeholder="Select Assign To Users" Width="100%" Filterable="true" TextField="@nameof(UserInfoVM.UserName)" ValueField="@nameof(UserInfoVM.UserName)" @bind-Value="@AssignedToUsers"> <MultiSelectPopupSettings> <DropDownListPopupSettings Height="200px" /> </MultiSelectPopupSettings> </TelerikMultiSelect> </Template> </FormItem>

## Answer

**Dimo** answered on 29 Mar 2022

Hi John, The error means that the <TelerikMultiSelect> tag has an invalid (not recognized) child tag: The <MultiSelectPopupSettings> tag has to be wrapped by <MultiSelectSettings>. <DropDownListPopupSettings> doesn't belong here at all. See Breaking Changes in the Popup Settings and MultiSelect Popup Settings for examples. Regards, Dimo Progress Telerik
