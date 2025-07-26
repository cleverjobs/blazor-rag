# Dropdown in TelerikForm stops the popup from loading. (Page stops responding)

## Question

**DaDa** asked on 22 Nov 2023

Hello, I have a page where user could click a button to open a modal popup. Then create a name and state association. However, after clicking the button, popup doesn't show up and the page stops responding then I have to close the page. If remove the dropdown from the modal popup, everything works fine. Below is the sample razor code. I appreiate your help. <TelerikDialog @bind-Visible="@ShowDialog" @ref="@DialogRef" Title="MyTelerikDialogTitle" Width="400px"> <DialogContent> <TelerikForm Id="MyTelerikForm" Model="@MyModel" OnValidSubmit="@OnOkSubmit" OnUpdate="@OnFormUpdate" @ref="@FormRef"> <FormValidation> <DataAnnotationsValidator /> </FormValidation> <FormItems> <FormItem Field="@nameof(MyDto.Name)" LabelText="Name" /><FormItem Field="@nameof(MyDto.Address)" LabelText="Address" /> <FormItem Field="@nameof(MyDto.Zipcode)" LabelText="Zipcode" /> <FormItem Field="@nameof(MyDto.State)"> <Template> <label for="StateName">State Name:</label> <TelerikDropDownList @bind-Value="@MyItem" DefaultText="Choose a state" Data="@StateNameDropDown" Id="StateName"> <DropDownListSettings> <DropDownListPopupSettings Height="auto" /> </DropDownListSettings> </TelerikDropDownList> </Template> </FormItem> ...

### Response

**Georgi** commented on 24 Nov 2023

Hi, Da, Thank you for the provided code snippet! I do not see a problem with the configuration of any of the three components. It is hard to pinpoint the exact reason for this behaviour with the given information. I have prepared a REPL example based on the provided configuration. Can you modify it so the issue is reproducible and send it back to me? This will allow me to investigate the issue locally and come up with suggestions accordingly. I am looking forward to your reply.
