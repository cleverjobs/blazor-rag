# Problem with DropDownList data annotations

## Question

**Dav** asked on 13 Feb 2024

I have an issue with the DropDownList and Data Annotations. I have created a REPL instance that demonstrates the problem [https://blazorrepl.telerik.com/GyamPdlf37LXpPAW36](https://blazorrepl.telerik.com/GyamPdlf37LXpPAW36) Select the last item in the tree 7.Garden and change the value in the drop down list to Unsupported. The drop down list shows a red border. Select item 6.Garden from the tree. (Any item in the tree other than 1 will do) I expect the drop down to not have the red border, yet is does. The text box does not show the same behaviour. Select 7.Garden Edit the email address to start with unsupported The text box has the red border Select any other item in the tree, they will not have the red border. TBH I'm not sure if this is a Telerik/DropDownList issue or I'm doing something wrong. The REPL example replicates an issue in a larger piece of code that is more complex with regards to the validation which is why there are no data annotations on properties and the binding are not simple. Regards

## Answer

**Nadezhda Tacheva** answered on 16 Feb 2024

Hi David, Thank you for sharing a runnable sample! Looking at the TreeItem that you are using in the form, I see that none of its fields are decorated with DataAnnotations. That said, I would say the problem is not related to DataAnnotations and DropDownList but to how the EditContext created and is validated. I am not familiar with the complete scenario and the main purpose of the current configuration but I will share my observations. In the general case, the EditContext is created from a model while in the example I see that you are passing the whole FlatData collection to it. It is not clear to me why you need to validate the whole collection. If you only need to validate the selected item, you can use that as a model or EditContext for the form. In this case, it is not needed that the TreeView is placed in a form. In addition, the EditContext is not passed to the SelectedItem child component, so when you invoke EditContext.Validate() upon DropDownList value change, you are not essentially working with the same EditContext. My suggestion is to revise the specifics of the form, its EditContext and validation and alter the configuration to achieve the desired result. The complete implementation, however, is a custom solution that falls outside of the standard support scope. Should you face any difficulties with the Telerik for Blazor components' specifics, please let me know. Regards, Nadezhda Tacheva Progress Telerik

### Response

**David** commented on 23 Feb 2024

Thanks for the feedback, most useful. Unfortunately I've been put onto a different project for a little while but your feedback has been added to our ticket. Regards

### Response

**David** commented on 30 May 2024

Hi, I realise our validation method is probably not traditional but our dyamic model can't be validated with data annotations so we have to use a complex method. I had a burning question as to why this was happening on the DropDownList control and not on the TextInput. How could it be that our complex method of validation worked for one type of control but not another? I did some digging. With the help of your source code I was able to see that the SetParameterAsync method in the TelerikInputBase class sets the FieldIdentifier whereas the TelerikSelectBase does not. The SetParameterAsync method in TelerikSelectBase only sets the FieldIdentifier in the OnInitializedAsync method and not in SetParameterAsync the FieldIdentitier is therefore never updated. I tested this by making a change to the TelerikSelectBase SetParameterAsync method to set the FieldIdentifier. The validation now works as I would expect. Regards Dave

### Response

**Nadezhda Tacheva** commented on 04 Jun 2024

Hi David, Thank you for sharing your findings! I opened a discussion with our dev team to evaluate the difference in setting the FieldIdentifier in TelerikInputBase and in TelerikSelectBase. I will follow up with an update once I have more details.

### Response

**Nadezhda Tacheva** commented on 05 Jun 2024

Hi David, I've discussed the case with the team and we've agreed that we should unify the FieldIdentifier setting in the TelerikInputBase and in TelerikSelectBase. I opened a public item where you can track the progress of the changes: FieldIdentifier is set only on initialization.

### Response

**David** commented on 06 Jun 2024

Thanks. Much appreciated. Regards Dave
