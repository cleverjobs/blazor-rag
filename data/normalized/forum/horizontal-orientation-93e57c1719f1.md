# Horizontal Orientation

## Question

**Mar** asked on 24 Feb 2021

Hi: With the new Form component, when the orientation is set to horizontal, is that only for the FormItems? I would like to arrange my form so that FormItems and FormButtons are all laid out horizontally. The attached screen shot is what I am looking to achieve. Thanks -marc

## Answer

**Marc Simkin** answered on 24 Feb 2021

The attached image is what I am currently getting when I use a horizontal orientation. Here is the markup: <TelerikForm EditContext="_editContext" Orientation="FormOrientation.Horizontal" OnValidSubmit="OnValidSubmit" Width="50%"> <FormValidation> <FluentValidationValidator DisableAssemblyScanning="@true" /> </FormValidation> <FormItems> <FormItem Field="@nameof(ViewModel.Ean)" LabelText="EAN" /> </FormItems> <FormButtons> <TelerikButton ButtonType="ButtonType.Submit" Primary="true">@SubmitButtonText</TelerikButton> </FormButtons> </TelerikForm> I would also like to shift everything to the left to not leave so much white space. I looked for where the left padding/margin is being set for either the form or the form item. I didn't find it. Thanks -marc

### Response

**Marc Simkin** answered on 25 Feb 2021

I am looking to have the layout similar to the Bootstrap .form-inline.

### Response

**Svetoslav Dimitrov** answered on 25 Feb 2021

Hello Marc, You can achieve a similar layout by using the Columns parameter of the TelerikForm and pass a value that is equal to the number of properties you have in the model. To make it more automated I have added an example where this is done in a method. If you would like to reduce or increase the space between the columns you can use the ColumnSpacing parameter as shown in the example below. To place buttons next to the fields you can use the Template exposed for the FormItem. When you are creating an inline form I would suggest you use the Vertical Orientation of the Form. The Orientation parameter controls the positioning of the labels relative to the FormItems. If you are using the Vertical orientation you will save some additional horizontal space. Something else I did in the example is to add an empty <FormButtons> tag. It will inform the Form component that it should not render a Submit button by default and you can place it elsewhere. Code snippet: <TelerikForm Model="@person" Columns="@GetColumnsCount()" ColumnSpacing="10px" Orientation="@FormOrientation.Vertical">
<FormItems>
<FormItem Field="@nameof(Person.Id)" LabelText="Id"></FormItem>
<FormItem Field="@nameof(Person.FirstName)" LabelText="First name"></FormItem>
<FormItem Field="@nameof(Person.LastName)" LabelText="Last name"></FormItem>
<FormItem Field="@nameof(Person.DOB)" LabelText="Date of Birth"></FormItem>
<FormItem Field="@nameof(Person.CompanyName)" LabelText="Company name"></FormItem>
<FormItem Field="@nameof(Person.HireDate)" LabelText="Hire date"></FormItem>
<FormItem>
<Template>
<TelerikButton OnClick="@CustomButtonMethod">Custom Button in the Form</TelerikButton>
</Template>
</FormItem>
</FormItems>
<FormButtons></FormButtons>
</TelerikForm>

@code { private int GetColumnsCount ( ) {
Type t=typeof (Person); int propertiesCount=t.GetProperties().Count(); return propertiesCount;
} private void CustomButtonMethod ( ) { //some logic } public Person person=new Person(); public class Person { public int Id { get; set; } public string FirstName { get; set; } public string LastName { get; set; } public DateTime DOB { get; set; }=DateTime.Today.AddYears( -20 ); public string CompanyName { get; set; } public DateTime HireDate { get; set; }
}
} I hope this helps you move forward with your application. Let me know if I can be of further assistance! Regards, Svetoslav Dimitrov

### Response

**Marc Simkin** answered on 01 Mar 2021

Hi Svetoslav: My apologues for the delayed response. The example provided was almost what I wanted, except that I only have one field and the button in the form. Setting the properties count dynamically is just overkill. I provided example, gave me enough information that I was able to get something working the way I needed. I needed to leave the form in "Horizontal" orientation, otherwise the top of the input field and button are not aligned. Now I have the label, input field and button all aligned horizontally nicely. I know that the label has a style that included k-label and k-form-label. I am trying to figure out what style needs to be overridden in order to get everything inside the form to be flush to the left side area being rendered. Thank you. -marc

### Response

**Svetoslav Dimitrov** answered on 02 Mar 2021

Hello Marc, You can take advantage of the Class parameter exposed for the TelerikForm. It adds a custom CSS class to the topmost HTML element and you can use it to make the cascading of CSS rules easier. You are correct that our labels have both k-label and k-form-label classes. By using a suitable CSS selector you can reset the width CSS rule. Below, I have made an example. The form is wrapped in a div with a border to better showcase the effect of the CSS: <style>.custom-css-class.k-label.k-form-label { width: auto;
}
</style> <div style=" border: solid 0.5px black ">
<TelerikForm Model=" @person "
Columns="@GetColumnsCount()" ColumnSpacing="10px" Orientation="@FormOrientation.Horizontal" Class="custom-css-class">
<FormItems>
<FormItem Field="@nameof(Person.Id)" LabelText="Id"></FormItem>
<FormItem Field="@nameof(Person.FirstName)" LabelText="First name"></FormItem>
<FormItem>
<Template>
<TelerikButton OnClick="@CustomButtonMethod">Custom Button in the Form</TelerikButton>
</Template>
</FormItem>
</FormItems>
<FormButtons></FormButtons>
</TelerikForm>
</div>

@code { private int GetColumnsCount ()
{
Type t=typeof(Person);
int propertiesCount=t.GetProperties().Count();

return propertiesCount;
} private void CustomButtonMethod ()
{
//some logic
} public Person person=new Person (); public class Person {
public int Id { get; set; } public string FirstName { get; set; } public string LastName { get; set; } public DateTime DOB { get; set; }=DateTime.Today.AddYears ( -20 ); public string CompanyName { get; set; } public DateTime HireDate { get; set; }
}
} I hope I understood your question correctly. If I missed something let me know. Regards, Svetoslav Dimitrov

### Response

**Marc Simkin** answered on 04 Mar 2021

Hi Svetoslav. Thanks. All working now.

### Response

**Nadezhda Tacheva** answered on 22 Oct 2021

Hello Marc, I'm stepping in to provide an update that we now have a feature request for customizing the position of the Form Buttons. You can find it in our public
