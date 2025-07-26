# Control column location of fields

## Question

**Mar** asked on 12 Mar 2021

If the form has more than one column, the fields are placed in columns based upon how they were laid out in the HTML. For example, field 1 is placed in column 1, field 2 in column 2, field 3 in column 1, etc. Is there a way, without using a form group, to to control which column is used to render the field? For example, fields 1 & 2 are placed in column 1, and field 3 is placed in column 2. If that is not possible, then the FormGroup element should be changed so that when the LabelText is not provided, the legend html element is not rendered.

## Answer

**Svetoslav Dimitrov** answered on 16 Mar 2021

Hello Marc, The way to group different editors in a custom manner is indeed to use the FormGroups. If you do not wish to have the legend rendered you could use some CSS to hide it. Below, I have made an example that showcases a way to achieve the desired UI. In it, I have used the Class parameter to place a custom CSS class on the topmost wrapping element of the Form and cascade styles from it. You can extend that example to provide a conditional CSS class to the Class parameter (checks if the LabelText is null or empty). <style>.my-telerik-form.k-form-legend { display: none;
}
</style> @using System.ComponentModel.DataAnnotations

<TelerikForm Model="@person" Columns="2" ColumnSpacing="25px" Class="my-telerik-form">
<FormValidation>
<DataAnnotationsValidator></DataAnnotationsValidator>
</FormValidation>
<FormItems>
<FormGroup LabelText="Personal Information" Columns="2" ColumnSpacing="15px">
<FormItem LabelText="First Name" Field="@nameof(Person.FirstName)"></FormItem>
<FormItem LabelText="Last Name" Field="@nameof(Person.LastName)"></FormItem>
<FormItem LabelText="Age" Field="@nameof(Person.Age)" ColSpan="2"></FormItem>
<FormItem LabelText="Email" Field="@nameof(Person.Email)" ColSpan="2"></FormItem>
</FormGroup>
<FormGroup LabelText="Employee Information" ColumnSpacing="25px">
<FormItem LabelText="Company Name" Field="@nameof(Person.CompanyName)"></FormItem>
<FormItem LabelText="Position" Field="@nameof(Person.Position)"></FormItem>
</FormGroup>
</FormItems>
</TelerikForm>

@code { public Person person { get; set; }=new Person (); public class Person {
[Required(ErrorMessage="The First name is required")]
public string FirstName { get; set; } [Required(ErrorMessage="The Last name is required" )] public string LastName { get; set; } [Range(18, 120, ErrorMessage="The age should be between 18 and 120" )] public int Age { get; set; } [Required] [EmailAddress(ErrorMessage="Enter a valid email" )] public string Email { get; set; } [Required] public string CompanyName { get; set; } [MaxLength(25, ErrorMessage="The position can be maximum 25 characters long" )] public string Position { get; set; }
}
} Let me know if this solution works as expected for you and if you need any further assistance. Regards, Svetoslav Dimitrov Progress Telerik
