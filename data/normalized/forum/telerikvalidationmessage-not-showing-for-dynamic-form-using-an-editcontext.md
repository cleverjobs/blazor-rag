# TelerikValidationMessage not showing for dynamic form using an EditContext

## Question

**JimJim** asked on 29 Nov 2022

I have a question regarding the TelerikValidationMessage, which is showing in one form, but not in another. I am using data annotations on the properties of the User class. public class User
{
[Display(Name="Voornaam*")]
[Required(ErrorMessage="Voornaam ontbreekt.")]
[Placeholder(Description="Voer de voornaam in.")]
public string FirstName { get; set; }
... The first form is a non-dynamic form with fields for every property in the User class. It is using a Model with bind-Value instead of an EditContext with Value and ValueChanged. When I press the Submit button, the validation summary is shows as are the validationmessages below the textinputs. This is the desired situation. <TelerikForm Model="@TestUser" OnValidSubmit="@HandleValidSubmit" OnInvalidSubmit="@HandleInvalidSubmit"> <FormValidation> <DataAnnotationsValidator> </DataAnnotationsValidator> </FormValidation> <FormItems> <FormItem Field="@nameof(User.FirstName)"> <Template> <div class="mb-3 row"> <label for="firstName" class="k-label k-form-label col-sm-2"> Voornaam * </label> <div class="col-sm-10"> <TelerikTextBox Id="firstName" @bind-Value="@TestUser.FirstName" InputMode="text" PlaceHolder="Voornaam"> </TelerikTextBox> <TelerikValidationMessage For="@(()=> TestUser.FirstName)"> </TelerikValidationMessage> </div> </div> </Template> </FormItem>... Since I am trying to create a dynamic form which will work for all my classes, I have created a second form. This second form is a dynamic form using an EditContext. <TelerikForm EditContext="@MyEditContext" OnValidSubmit="@HandleValidSubmit" OnInvalidSubmit="@HandleInvalidSubmit" ValidationMessageType="@FormValidationMessageType.Inline"> <FormValidation> <DataAnnotationsValidator> </DataAnnotationsValidator> <ValidationSummary /> </FormValidation> <FormItems> @foreach (var propertyInfo in DataContext.GetType().GetProperties())
{ <FormItem Field="@propertyInfo.Name"> <Template> <div class="mb-1 row"> <label for="@(propertyInfo.Name)" class="k-label k-form-label col-sm-2"> @propertyInfo.DisplayName() </label> <div class="col-sm-10"> <TelerikTextBox Id="@(propertyInfo.Name)" Value="@propertyInfo.GetValue(DataContext)?.ToString()" ValueExpression="@(()=> propertyInfo.Name)" OnChange="OnChange" ValueChanged="@(value=> OnValueChanged(value, propertyInfo.Name))" InputMode="text" PlaceHolder="@propertyInfo.PlaceholderDescription()"> </TelerikTextBox> <TelerikValidationMessage For="@(()=> propertyInfo.Name)"> </TelerikValidationMessage> </div> </div> </Template> </FormItem> } </FormItems> </TelerikForm> And here's the imporant part of the code behind. This is proof of concept code and will be improved later. protected void OnValueChanged(object e, string prop)
{
var propertyInfo=DataContext.GetType().GetProperty(prop);
if (propertyInfo==null) return;

if (propertyInfo.PropertyType==typeof(int))
{
var intValue=Convert.ToInt32(e);
propertyInfo.SetValue(DataContext, intValue);
}

if (propertyInfo.PropertyType==typeof(string))
propertyInfo.SetValue(DataContext, e.ToString());

if (propertyInfo.PropertyType==typeof(DateTime) || propertyInfo.PropertyType==typeof(DateTime?))
propertyInfo.SetValue(DataContext, DateTime.Now);

if (propertyInfo.PropertyType==typeof(bool) || propertyInfo.PropertyType==typeof(bool))
propertyInfo.SetValue(DataContext, true);
}

protected void OnChange(object e)
{
MyEditContext.Validate();
} When I press the submit button, the validationsummary is correctly shown, the labels color red and the border of the textinput colors red (after adding some css). So the validation seems to be working fine. However, the validationmessage below the textinput isn't showing. It isn't even in the DOM, so I assume it's not generated. I have searched the Interwebs and this forum/documentation, but I can't find the reason why the validationmessage isn't showing. Any help would be highly appreciated. Btw; the second form shows the Inline messagetype, but that has no effect. ValidationMessageType="@FormValidationMessageType.Inline"

## Answer

**Dimo** answered on 01 Dec 2022

Hi Jim, The For parameter of the TelerikValidationMessage should point to a property of an object instance. Currently it points to a property name and that's why it doesn't work. If it's not possible or convenient to set the correct object instance in the TelerikValidationMessage declaration, then you will have to obtain the validation messages from the EditContext and render them manually. Regards, Dimo

### Response

**Jim** commented on 01 Dec 2022

That is what I suspected. How can I point it to the object instance? I'm not sure how to do this for my dynamic form. I'm not using fixed classes, so I am not sure how to proceed.

### Response

**Jim** commented on 01 Dec 2022

Thanks for your updated comment. Do you have a code example for the manual rendering solution? PS Since it's basic NET functionality I will probably be able to find some examples, but it you have any for a dynamic form, that would be great.

### Response

**Jim** commented on 01 Dec 2022

Probably something like this: [https://chrissainty.com/creating-a-custom-validation-message-component-for-blazor-forms/](https://chrissainty.com/creating-a-custom-validation-message-component-for-blazor-forms/)

### Response

**Dimo** commented on 01 Dec 2022

The For parameter of the ValidationMessage is defined in our source code like this: public Expression<Func<TValue>> For { get; set; } We have a generic ReflectionExtensions method, which provides expressions for unknown types: public static Expression <Func <TItem>> GetNestedExpression <TItem>( this object item, string field ) {
Expression expression=Expression.Constant(item); foreach ( var namePart in field.Split( '.' ))
{
expression=Expression.Property (
expression,
expression.Type.GetPropertyInfo(namePart)
);
} var convertedExp=Expression.Convert(expression, typeof (TItem)); return Expression.Lambda <Func<TItem>>(convertedExp);
} You can experiment and try to implement something similar that will create a lambda, based on a provided type.

### Response

**Jim** commented on 01 Dec 2022

I failed to create my own expression. I might try that one out later. In the meantime, I used this solution and created a custom validator. This is working like a charm. Check out the links below: [https://stackoverflow.com/questions/74252454/blazor-validationmessage-wont-show-after-manually-filling-validationmessagesto](https://stackoverflow.com/questions/74252454/blazor-validationmessage-wont-show-after-manually-filling-validationmessagesto) [https://chrissainty.com/creating-a-custom-validation-message-component-for-blazor-forms/](https://chrissainty.com/creating-a-custom-validation-message-component-for-blazor-forms/)
