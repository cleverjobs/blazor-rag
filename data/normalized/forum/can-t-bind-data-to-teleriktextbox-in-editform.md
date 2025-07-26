# Can't bind data to TelerikTextBox in EditForm

## Question

**Kyl** asked on 18 Nov 2024

I'm trying to get Telerik working in a simple login form and I can't get the binding to work. This is a .NET 8 Blazor Web Assembly app. To narrow it down, I followed the instructions outlined here. I selected "Individual Accounts" for authentication and WebAssembly for Interactive render mode (and Global for Interactivity location as suggested in the article). I also included the sample pages and changed the email field in the login page to: <TelerikTextBox @bind-Value="Input.Email" class="form-control" placeholder="name@example.com" /> When I submit the form, it says the Email field is required. It works fine with a standard InputText. I thought maybe it has to do with the control in an EditForm on the server since the click event works fine on a client page but I've seen other examples where it's supposed to work in an EditForm as well.

### Response

**Kyle** commented on 19 Nov 2024

I added a reproduction here.

## Answer

**Dimo** answered on 20 Nov 2024

Hello Kyle, Our components require interactive render mode, while the Account section of the Blazor identity project template uses static render mode. Please see the yellow note in this documentation section. In this case, you can use a regular <InputText /> or plain HTML <input /> which looks like our TextBox. However, the FloatingLabel is designed to integrate with our components only. @using System.ComponentModel.DataAnnotations <p> TelerikTextBox: </p> <TelerikTextBox @bind-Value="Input.Email" class="form-control" placeholder="name@example.com" /> <p> HTML: </p> <span class="k-textbox k-input form-control k-input-solid k-rounded-md k-input-md"> <input @bind="Input.Email" role="textbox" placeholder="name@example.com" class="k-input-inner" dir="ltr" aria-readonly="false" tabindex="0" /> </span> <p> InputText with HTML: </p> <span class="k-textbox k-input form-control k-input-solid k-rounded-md k-input-md"> <InputText class="k-input-inner" @bind-Value="Input.Email" autocomplete="username" aria-required="true" placeholder="name@example.com" /> </span> @code {
private InputModel Input { get; set; }=new();

private sealed class InputModel
{
[Required]
[EmailAddress]
public string Email { get; set; }="";

[Required]
[DataType(DataType.Password)]
public string Password { get; set; }="";

[Display(Name="Remember me?")]
public bool RememberMe { get; set; }
}
} Regards, Dimo Progress Telerik

### Response

**Kyle** commented on 20 Nov 2024

Thank you, Dimo. I'll give that a try. In the meantime, I did get it to work also by adding Name="Input.Email" to the TelerikTextBox. The FloatingLabel still doesn't work but I'm able to submit the data at least.
