# I want to add the x Close icon in the Confirmation modal

## Question

**Kis** asked on 06 Jan 2022

Hello there, I am using the Telerik confirmation dialog to delete the user functionality, during the delete the user open confirmation pop-up I want to add the x Close icon top of the Confirmation modal. here is my code for confirmation modal var isDelete=await Dialogs.ConfirmAsync("Are you sure you would like to delete this User?", "Confirmation!"); please check the attached image for reference I want to customize this Dialog as the attached image.

## Answer

**Dimo** answered on 10 Jan 2022

Hello Kishan, UI for Blazor 2.30 introduced a richer Dialog component. Now the component has a ShowCloseButton attribute, which is true by default. Check the online demos. Regards, Dimo
