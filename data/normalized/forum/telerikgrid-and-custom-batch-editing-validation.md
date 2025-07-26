# TelerikGrid and Custom Batch editing : validation

## Question

**Lou** asked on 20 Mar 2023

Hello. I use Custom Batch editing Grid and need to perform some validation when save all changes. I try in the view <ValidationMessage class="col-sm-12 text-danger" For="@(()=> CurrentlyEditing.tlkpLocalisationId)" /> with something like this in the razor.ca file public async Task SaveAllChanges()
{
...
messageStore?.Add(editContext.Field("tlkpLocalisationId"), "test");
....
} Not working. And more if user change/add some invalid data (multiple rows) so those rows must be validated too. Thanks for your time

## Answer

**Stamo Gochev** answered on 23 Mar 2023

Hi Louis, Can you send me a Telerik Blazor REPL example that demonstrates your scenario and configuration, so I can inspect it? In addition, can you provide more details on this part: " if user change/add some invalid data (multiple rows) so those rows must be validated too." How are these rows inserted - do you have something preconfigured or would like the user to be able to add multiple entries and validate them manually on some action, e.g. a button click? Regards, Stamo Gochev

### Response

**Louis** answered on 25 Mar 2023

Hello Stamo, Thanks to take time about my issue. User have on entrer data in one of 3 fields. At lease in one for 3 fields. If no value is entred at all I want to display a error message. See atachement.

### Response

**Nadezhda Tacheva** commented on 29 Mar 2023

Hi Louis, Thank you for sharing more details about the desired result! At this stage, it is not clear if you are struggling with generating the validation message or with its displaying. Based on the screenshot, it looks like you are successfully showing the message. Is it possible that you are not happy with the current option that you are using to show the message (ValidationMessage displayed only below a part of the three fields)? If so, you may consider another UI for notifying the user that the validation is not satisfied. For example, you may use Notification or Alert. In case the attached screenshot shows just the desired result (not the current progress of your application) and you are still facing difficulties with actually generating the validation message, please send us an isolated runnable sample that replicates your current configuration. This will allow us to revise it and see what might be missing. You may use our Custom Batch Editing demo as a base. If you select the "EDIT IN TELERIK REPL" option in the toolbar, you will generate a snippet in the REPL tool which you can easily modify to demonstrate your current setup. Thank you in advance!
