# Popup behaving badly

## Question

**Ran** asked on 20 Oct 2019

Hi, Check the attached screen shot. The markup is shown below. Is this a bug on your side or am I doing something wrong? Thanks ... Ed <TelerikWindow Visible="@(selectedUser !=null)" Modal="true"> <WindowTitle> @{ if (selectedUser.Id <0 ) { <strong>Add Employee</strong> } else { <strong>Edit Employee</strong> } } </WindowTitle> <WindowContent> <EditForm Model="@selectedUser" OnValidSubmit="@Save"> <DataAnnotationsValidator /> <div class="form-row"> <div class="col"> <TelerikTextBox @bind-Value="@selectedUser.FirstName" Label="First Name"></TelerikTextBox> </div> <div class="col"> <TelerikTextBox @bind-Value="@selectedUser.LastName" Label="Last Name"></TelerikTextBox> </div> </div> @*<div class="form-row"> <div class="col"> <TelerikDropDownList Data="@lstRoles" @bind-Value=@SelectedRole PopupHeight="170px" ValueField="Id" TextField="RoleName"> </TelerikDropDownList> </div> </div>*@<div class="form-row"> <div class="col"> <TelerikTextBox @bind-Value="@selectedUser.Email" Label="Email"></TelerikTextBox> </div> <div class="col"> <TelerikTextBox @bind-Value="@selectedUser.PhoneNumber" Label="Phone"></TelerikTextBox> </div> </div> <div class="form-row"> <div class="col"> <TelerikTextBox @bind-Value="@selectedUser.Address1" Label="Address 1"></TelerikTextBox> </div> <div class="col"> <TelerikTextBox @bind-Value="@selectedUser.Address2" Label="Address 2"></TelerikTextBox> </div> </div> <div class="form-row"> <div class="col"> <TelerikTextBox @bind-Value="@selectedUser.City" Label="City"></TelerikTextBox> </div> <div class="col"> <TelerikTextBox @bind-Value="@selectedUser.PostCode" Label="Post Code"></TelerikTextBox> </div> </div> <div class="form-row"> <div class="col"> <div style="margin-top:20px;"> Is Active <InputCheckbox @bind-Value="@selectedUser.IsActive" /> </div> </div> <div class="col"> <span class="k-label" style="font-size:7pt">Role</span> <TelerikDropDownList Data="@lstRoles" TextField="Name" ValueField="Id" @bind-Value="selectedRole" Width="100"> </TelerikDropDownList> </div> </div> <div class="form-row"> <br /> <ValidationSummary /> <TelerikButton Class="mt-2" Icon="save" Primary="true" ButtonType="@ButtonType.Submit">Save</TelerikButton> <TelerikButton Class="mt-2" Icon="cancel" OnClick="@ClearSelection" ButtonType="@ButtonType.Button">Cancel</TelerikButton> </div> </EditForm> </WindowContent> </TelerikWindow>

## Answer

**Marin Bratanov** answered on 21 Oct 2019

Hello Ed, The most common problems related to popups are explained here: [https://docs.telerik.com/blazor-ui/troubleshooting/general-issues#popups-do-not-work](https://docs.telerik.com/blazor-ui/troubleshooting/general-issues#popups-do-not-work) so you can see if this matches your case. In case you are referring to the two window components being available for user interaction - please Vote for and Follow this feature request: [https://feedback.telerik.com/blazor/1407791-support-for-multiple-nested-modal-windows.](https://feedback.telerik.com/blazor/1407791-support-for-multiple-nested-modal-windows.) In case you are referring to something else - I do not see all the components from the screenshot on the code snippet and so I can't say if something in the code is off. If the two links above do not answer your question, please post the relevant code or a link to a fork of the custom popup edit form repo sample. Regards, Marin Bratanov

### Response

**Randy Hompesch** answered on 21 Oct 2019

That did it! I don't understand it, but it did it. If you look at the original screenshot I uploaded, the dropdownlist's dropdown was positioned incorrectly. Now, thank to your tweek life is good again. Thanks ... Ed

### Response

**Randy Hompesch** answered on 21 Oct 2019

Not quite. I did as you suggested and removed teh styling, but now, when the dropdown is shown, if I click on an item to select it, nothing happens. I'm dead in the water. THanks ... Ed

### Response

**Marin Bratanov** answered on 21 Oct 2019

Hi Ed, Please post here the code I can use to reproduce this. If you find it easier, open a support ticket and attach a runnable sample project I can debug. Doing either of these will let me investigate and offer a concrete answer, as opposed to guessing. Regards, Marin Bratanov

### Response

**Randy Hompesch** answered on 21 Oct 2019

I just created a ticket. Feel free to call me at teh phone number I listed there. Thanks ... Ed

### Response

**Marin Bratanov** answered on 21 Oct 2019

Let's work on this in the ticket and post a solution here once found. What I can say at the moment is that in the sample in the ticket there are some issues with the DOM structure (things from the <head> rendering inside the <app>) which is quite odd and is likely an indicator that something in the app itself is broken. Regards, Marin Bratanov
