# UI for Blazor Update Breaks Ability To Submit Form Using Enter Key

## Question

**bil** asked on 22 Aug 2024

We recently updated to Telerik.UI.for.Blazor 6.0.0 and now none of the forms on our website will submit using the "Enter" key on the keyboard. You must now either click or tab to the button and then hit enter. This was not an issue with the previous version that we had pulled in. Is there a fix for this or a new implementation pattern that needs to be used to support this?

### Response

**Dimo** commented on 27 Aug 2024

Hi Billy, I tested our online Form demos and all of them submit successfully on Enter. Can you show me a small example, which doesn't work in version 6.0, but works in earlier versions?

### Response

**billy** commented on 09 Oct 2024

This is my form. This used to work with the earlier (albiet much ealier) version, but now when I attempt to submit this form, it does nothing unless I tab down to the button and hit enter while the button has focus. <TelerikForm Model="@LoginModel" OnValidSubmit="@HandleSubmit"> <FormItems> <div class="input-wrapper"> <FVTextBox @bind-Value="@this.LoginModel.Username" TabIndex="1" @ref="@this.UserNameTextBoxRef" /> </div> <div class="input-wrapper"> <TelerikButton Class="login-action-btn forgot-password" ButtonType="ButtonType.Button" OnClick="@(()=> this.ShowForgotUsernamePassword=true)"> Forgot Username / Password </TelerikButton> <FVButton OnClick="@this.RevealPassword" ButtonType="Telerik.Blazor.ButtonType.Button" Icon="@FontIcon.Eye" Class="show-pw-icon" /> <FVTextBox @bind-Value="@this.LoginModel.Password" Password="this.HidePassword" TabIndex="2" /> </div> </FormItems> <FormButtons> <TelerikButton Class="login-btn" Enabled="@(this.LoginModel.IsValid && !this.LoggingIn)" ButtonType="@ButtonType.Submit" ThemeColor="@ThemeConstants.Button.ThemeColor.Primary" TabIndex="3"> <TelerikIcon Class="btn-icon" Icon="@FontIcon.CheckOutline" /> Login </TelerikButton> </FormButtons> </TelerikForm>

### Response

**Dimo** commented on 09 Oct 2024

Hi Billy, The Form markup needs some required and some optional updates: <FormItems> must not contain custom HTML or components. Use a <FormItemsTemplate> instead. The Eye button can be inside a TextBoxSuffixTemplate. This will simplify your markup and possibly improve the UI. Use this working snippet as a reference: @using System.ComponentModel.DataAnnotations <TelerikForm Model="@LoginModel" OnValidSubmit="@HandleSubmit"> <FormValidation> <DataAnnotationsValidator> </DataAnnotationsValidator> </FormValidation> <FormItems> <FormItem Field="@nameof(LoginFormModel.Username)" /> <FormItem Field="@nameof(LoginFormModel.Password)"> <Template> <label for="password-id" class="k-label k-form-label"> Password </label> <div class="k-form-item-wrap"> <div style="display:flex;gap:.4em"> <TelerikTextBox @bind-Value="@LoginModel.Password" Password="@(!RevealPassword)"> <TextBoxSuffixTemplate> <TelerikButton ButtonType="@ButtonType.Button" Icon="@FontIcon.Eye" OnClick="@( ()=> RevealPassword=!RevealPassword )"> </TelerikButton> </TextBoxSuffixTemplate> </TelerikTextBox> <TelerikButton ButtonType="ButtonType.Button"> Forgot Username / Password </TelerikButton> </div> <TelerikValidationMessage For="@( ()=> LoginModel.Password )" /> </div> </Template> </FormItem> </FormItems> <FormItemsTemplate Context="formContext"> @{
var formItems=formContext.Items.Cast <IFormItem> ().ToList();
} <div class="input-wrapper"> <TelerikFormItemRenderer Item="@( formItems.First(x=> x.Field==nameof(LoginFormModel.Username)) )" /> </div> <div class="input-wrapper"> <TelerikFormItemRenderer Item="@( formItems.First(x=> x.Field==nameof(LoginFormModel.Password)) )" /> </div> </FormItemsTemplate> <FormButtons> <TelerikButton ThemeColor="@ThemeConstants.Button.ThemeColor.Primary" Icon="@FontIcon.CheckOutline"> Login </TelerikButton> </FormButtons> </TelerikForm> <p> <strong style="color:green"> @SubmitLog </strong> </p> @code {
public LoginFormModel LoginModel { get; set; }=new();

private string SubmitLog { get; set; }=string.Empty;

private bool RevealPassword { get; set; }

private void HandleSubmit()
{
SubmitLog=$"Success at {DateTime.Now.ToString("HH:mm:ss.fff")} !";
}

public class LoginFormModel
{
[Required]
public string Username { get; set; }=string.Empty;

[Required]
public string Password { get; set; }=string.Empty;
}
}

### Response

**Mike** commented on 03 Jun 2025

I expect this is long solved, but having encountered possibly the same problem... (not as a result of a change in my case, so I don't know if this ever behaved differently) If the HandleSubmit method is defined as 'async void': private async void HandleSubmit () {
DoStuff();
} Then the enter Key press would submit the form, HandleSubmit() would fire, and DoStuff() would run. But any effect on the UI is not captured until something else notifies the component that it should re-render. So it appears as though nothing has happened. Both (void without async) private void HandleSubmit () and (async Task) private async Task HandleSubmit () complete properly, and have their changes reflected in the UI.

### Response

**Dimo** commented on 03 Jun 2025

@Mike - the observed behavior is expected and is not related to Telerik UI for Blazor. That's why async void is not recommended in Blazor unless you really want the UI to NOT update.

### Response

**Mike** commented on 03 Jun 2025

Yep, that's a good clarification! I didn't mean to suggest it was a problem with Telerik - just a possible cause of the behaviour they were seeing. :)
