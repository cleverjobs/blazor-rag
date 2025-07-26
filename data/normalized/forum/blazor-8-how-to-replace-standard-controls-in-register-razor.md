# Blazor 8: How to replace standard controls in Register.razor?

## Question

**Ste** asked on 29 Nov 2023

Hi, I tried to replace the standard controls in Register.razor (Identity page) with Telerik controls (TextBox). But the behaviour of your controls seems to be different. Working code with standard and Telerik controls: @page "/Account/Register" <PageTitle> @_IdentityLocalizer["TitleRegister"] </PageTitle> <h1> @_IdentityLocalizer["TitleRegister"] </h1> <div class="row"> <div class="col-md-4"> <StatusMessage Message="@Message" /> <EditForm Model="@Input" asp-route-returnUrl="@ReturnUrl" method="post" OnValidSubmit="RegisterUser" FormName="register"> <DataAnnotationsValidator /> <ValidationSummary /> <h2> Create a new account. </h2> <hr /> <div class="k-form-field"> <label id="textBoxEmail"> @_IdentityLocalizer["LabelEmail"] </label> <TelerikTextBox @bind-Value="@Input.Email" Id="textBoxEmail" /> <TelerikValidationMessage For="@(()=> Input.Email)" /> </div> <div class="k-form-field"> <label id="textBoxPassword"> @_IdentityLocalizer["LabelPassword"] </label> <TelerikTextBox @bind-Value="@Input.Password" Password Id="textBoxPassword" /> <TelerikValidationMessage For="@(()=> Input.Password)" /> </div> <div class="k-form-field"> <label id="textBoxConfirmPassword"> @_IdentityLocalizer["LabelConfirmPassword"] </label> <InputText id="textBoxConfirmPassword" type="password" @bind-Value="Input.ConfirmPassword" /> <TelerikValidationMessage For="@(()=> Input.ConfirmPassword)" /> </div> <div class="k-form-field"> <TelerikButton ButtonType="ButtonType.Submit"> @_IdentityLocalizer["ButtonRegister"] </TelerikButton> </div> </EditForm> </div> <div class="col-md-6 col-md-offset-2"> <section> </section> </div> </div> After clicking the submit button the result seems correct: After replacing the last input control with Telerik control the code looks like this: <div class="k-form-field"> <label id="textBoxConfirmPassword"> @_IdentityLocalizer["LabelConfirmPassword"] </label> <TelerikTextBox @bind-Value="@Input.ConfirmPassword" Password Id="textBoxConfirmPassword" /> <TelerikValidationMessage For="@(()=> Input.ConfirmPassword)" /> </div> Now I get the following exception when trying to submit (nothing entered): It seems that the model instance (Input) is null after trying to submit the (empty) form. For me it is not understandable why the behaviour of your controls are so different to standard controls. Is there a chance to use Telerik controls in Identity pages? Regards, Stefan

## Answer

**Stefan** answered on 29 Nov 2023

It seems that adding the rendermode to register page solves the problem: @rendermode RenderMode.InteractiveServer

### Response

**Stefan** answered on 30 Nov 2023

Sorry to say, but adding the rendermode is not a solution. So I started again with standard project template (Blazor Web App, individual accounts, auto render mode) and replaced the standard controls on register page with Telerik components. It is not working... For me it is not understandable why the behaviour is different, but currently I am not able to use Telerik for Blazor .NET 8 projects.

### Response

**Svetoslav Dimitrov** answered on 04 Dec 2023

Hello Stefan, Let me sum up my understanding of the issue you are facing: You are using the Telerik input components for Blazor in an EditForm. If you click the button the Model (Input) becomes null and subsequent button clicks throw an exception. I am not sure why this would be happening as I can confirm that the Telerik button does not execute any logic that would cause this exception. At that point, I would like to request a runnable code snippet where we can invest the scenario with your exact configuration. Regards, Svetoslav Dimitrov Progress Telerik
