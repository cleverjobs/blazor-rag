# TelerikForm FormItem set focus

## Question

**Jef** asked on 03 Jan 2023

Is there a way to set the initial focus to an item on a TelerikForm?

## Answer

**Svetoslav Dimitrov** answered on 06 Jan 2023

Hello Jeff, The `<FormItem>` is an abstraction of the real editor that is rendered in the browser. To set a programmatic focus you must: Use the FormItem Template to provide the desired editor. Use the `FocusAsync()` method accessible through the `@ref` of the added editor. @using System.ComponentModel.DataAnnotations

<TelerikForm Model="@person">
<FormValidation>
<DataAnnotationsValidator></DataAnnotationsValidator>
</FormValidation>
<FormItems> <FormItem>
<Template>
<label for="first-name-textbox">First name:</label>
<TelerikTextBox @bind-Value="@person.FirstName" @ref="@TextBoxReference" Id="first-name-textbox">
</TelerikTextBox>
<TelerikValidationMessage For="(()=> person.FirstName)"></TelerikValidationMessage>
</Template>
</FormItem> <FormItem Field="@nameof(Person.LastName)" LabelText="Last name" Hint="Enter your last name" ColSpan="2"></FormItem>
<FormItem Field="@nameof(Person.DOB)" LabelText="Date of birth" Hint="Enter your Date of Birth"></FormItem>
</FormItems>
</TelerikForm>

@code { private TelerikTextBox TextBoxReference { get; set; } private Person person=new Person(); protected override async Task OnAfterRenderAsync ( bool firstRender ) { await Task.Delay( 20 ); await TextBoxReference.FocusAsync();
} public class Person {
[ Editable(false) ] public int Id { get; set; }

[ Required ]
[ MaxLength(20, ErrorMessage="The first name should be maximum 20 characters long" ) ]
[ Display(Name="First Name" ) ] public string FirstName { get; set; }

[ Required ]
[ MaxLength(25, ErrorMessage="The last name should be maximum 25 characters long" ) ]
[ Display(Name="Last Name" ) ] public string LastName { get; set; }

[ Required ]
[ Display(Name="Date of Birth" ) ] public DateTime? DOB { get; set; }
}
} Regards, Svetoslav Dimitrov

### Response

**Jeff** commented on 09 Jan 2023

Thanks!! that is a great explanation and example.
