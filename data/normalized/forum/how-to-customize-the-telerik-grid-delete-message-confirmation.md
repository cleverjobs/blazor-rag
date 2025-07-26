# How to customize the Telerik Grid delete message confirmation?

## Question

**Sat** asked on 17 Jun 2022

I need to add custom text to the delete message. Is there a way to do this? [https://docs.telerik.com/blazor-ui/components/grid/editing/built-in-dialogs/delete-confirmation](https://docs.telerik.com/blazor-ui/components/grid/editing/built-in-dialogs/delete-confirmation)

## Answer

**Benjamin** answered on 21 Jun 2022

Hey Satish, you can easily do this with customizing the localization ressources (For the grid the message can be found by key "Grid_ConfirmDeleteText"). It's not enabled by default, but you might already have set up localization in your project anyway - if not, it's just 1-2 minutes work: [https://docs.telerik.com/blazor-ui/globalization/localization](https://docs.telerik.com/blazor-ui/globalization/localization) You can change all language strings by modifying the ressource files. Regards

### Response

**Nadezhda Tacheva** answered on 22 Jun 2022

Hi Satish, As Benjamin mentioned, you can indeed customize the delete confirmation message through the localization resources. Please let us know if you face any difficulties in the process. Another approach would be to use a custom Dialog instead of the built-in one. We provide predefined and custom dialogs that will allow you to make the desired customization. The implementation will be different depending on the exact scenario. If you only need to modify the text in the popup and not add more complex content (additional components, for instance), the easier approach will be to use a predefined Confirm dialog. You can display the dialog in the OnDelete handler of the Grid. Based on the user confirmation, you can then either cancel the delete or proceed with it. Regards, Nadezhda Tacheva Progress Telerik

### Response

**Satish** commented on 30 Jun 2022

Thanks Benjamin and Nadezhda. For now, I am implementing Dialog, and it works great. I haven't enabled localization in my project. I need to do some studying on it.

### Response

**Nikhil** commented on 01 Oct 2022

In custom Dialog how to pass GridCommandEventArgs which is available in DeleteHandler for the Grid. If I use localization it will modify all Grids' Confirmation text. Is there any way to have custom delete confirmation title for different Grid objects?

### Response

**Nadezhda Tacheva** commented on 05 Oct 2022

Hi Nikhil, If you want to use a custom Dialog component, an option is to work with a saved local instance of the current item that the user tries to delete. You can get it from the GridCommandEventArgs of the OnDelete handler. Thus, you can also display the desired details for the current item in the dialog and then pass it for deletion if the user confirms. Additionally, you should cancel the built-in delete as you will actually be handling the deletion in the OnClick handler of the confirm button in the Dialog. I've prepared the following basic sample that demonstrates the approach: [https://blazorrepl.telerik.com/GQbYYfas45LJg1kO41.](https://blazorrepl.telerik.com/GQbYYfas45LJg1kO41.) See comments in the code for more details on the spot. The example also shows how to implement a custom title. I hope this information and example will help you move forward with your application. Please let us know if more questions are raised.
