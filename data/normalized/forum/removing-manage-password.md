# Removing Manage Password

## Question

**Vis** asked on 23 Mar 2021

Hi, When I entering the password, the password is stored in chrome browser. So I need to remove the manage password and I have attached the image below Please see below code <EditForm Model="@resetPasswordModel" OnValidSubmit="@SaveChanges" autocomplete="off"> <FluentValidator TValidator="ResetPasswordValidator" /> <p>@Model.Name</p> <EFormRowGroup LabelText="New Password" Id="Password"> <TelerikTextBox Id="Password" @bind-Value="@resetPasswordModel.Password" Password="true" AutoComplete="off"/> </EFormRowGroup> <EFormRowGroup LabelText="Confirm Password" Id="ConfirmPassword"> <TelerikTextBox Id="ConfirmPassword" @bind-Value="@resetPasswordModel.ConfirmPassword" Password="true" AutoComplete="off"/> </EFormRowGroup> <EValidationSummary /> <EDialogActions> <TelerikButton Icon="save" Primary="true" ButtonType="@ButtonType.Submit">Save</TelerikButton> <TelerikButton Icon="cancel" ButtonType="@ButtonType.Button" OnClick="@CancelClick">Cancel</TelerikButton> </EDialogActions> </EditForm> Could you please advise on this. Thanks, Vishnu Vardhanan.

## Answer

**Vishnu** answered on 24 Mar 2021

Hi, Could you please help on this.

### Response

**Svetoslav Dimitrov** answered on 26 Mar 2021

Hello Vishnu, The Manage Password is part of the AutoFill feature of Google Chrome. At the time of writing this, there are lots of reports that this feature cannot be disabled. It does not originate from our components or the Blazor framework itself and is outside of our control. We are aware that it creates some other issues and we created the Chrome autofills the Form and the floating label overlaps the values KB article to provide more information. The same behavior can be reproduced if you use the <input type="password"> HTML element. Regards, Svetoslav Dimitrov

### Response

**Lawrence** answered on 31 Mar 2022

This works for me. Enter "new-password" in the AutoComplete Property. <TelerikTextBox AutoComplete="new-password" Password="this.HidePassword" PlaceHolder="Enter Password..." @bind-Value="this.Model.Password" />
