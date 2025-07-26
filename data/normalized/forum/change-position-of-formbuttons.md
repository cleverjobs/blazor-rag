# Change position of FormButtons

## Question

**Mar** asked on 21 Apr 2021

I'm would like to have the buttons on my form justified right. I tried various Bootstrap alignment styles, which have no effect. How can I justify the buttons to the right? Also, maybe the FormButtons component should support various justification: left, center, right, vertical. Thanks

## Answer

**Svetoslav Dimitrov** answered on 26 Apr 2021

Hello Marc, You can use the justify-content: flex-end; to justify the buttons to the right of the container that wraps the buttons. You can customize our components by using CSS. It is not a bad practice, it is the general way to modify the visual representation of the rendered HTML. Below, I have added a demo code snippet that might serve as a base: <style>.my-form.k-form.k-form-buttons { justify-content: flex-end;
}
</style> @using System.ComponentModel.DataAnnotations

<TelerikForm EditContext="@theEditContext" OnValidSubmit="@OnValidSubmitHandler" Width="200px" Class="my-form">

<FormButtons>
<TelerikButton ButtonType="@ButtonType.Submit" Primary="true">Submit</TelerikButton>
<TelerikButton ButtonType="ButtonType.Button" OnClick="@ClearButton">Clear</TelerikButton>
</FormButtons>

</TelerikForm>

@code { private void ClearButton ()
{
person=new Person();
CreatedEditContext(person);
} void CreatedEditContext ( Person model )
{
theEditContext=new EditContext(model);

// we add the validation like this instead of in the markup
// because changing the model and context does not otherwise attach the validator
// and using the Clear button to new-up the model will leave you without validation
theEditContext.AddDataAnnotationsValidation();
} Person person { get; set; }=new Person (); EditContext theEditContext { get; set; } protected override async Task OnInitializedAsync ()
{
person=new Person()
{
FirstName="John",
DOB=DateTime.Now.AddYears(-37)
}; CreatedEditContext ( person );
} async Task OnValidSubmitHandler ()
{
Console.WriteLine($"SAVING {person.FirstName} {person.LastName} who was born on {person.DOB}");
} public class Person {
[Required]
public string FirstName { get; set; } [Required] public string LastName { get; set; } public DateTime DOB { get; set; }
}
} Regards, Svetoslav Dimitrov

### Response

**Marc Simkin** answered on 26 Apr 2021

Hi Svetoslav: Thank you for the response. Before I posted the question, I had tried various bootstrap styles to get the buttons to position as I wanted. For example, I placed the buttons inside a div with the bootstrap justify-content-end style. <FormButtons> <div class="row justify-content-end"> <TelerikButton ButtonType="@ButtonType.Submit" Primary="true">Submit</TelerikButton> <TelerikButton ButtonType="ButtonType.Button" OnClick="@ClearButton">Clear</TelerikButton> </div> </FormButtons> That had no effect on the buttons. As an aside, it would be very helpful, if all the styles that are available for use are documented someplace. I don't think Telerik has published such a document. -marc

### Response

**Svetoslav Dimitrov** answered on 29 Apr 2021

Hello Marc, The bootstrap styles work for plain HTML elements. When our components render they use different CSS rules, via our CSS classes, that define the design and/or some functionality. That is the reason why bootstrap classes are not supported for our components. As the next steps, you could manually add the CSS rules that are carried from the bootstrap classes with a suitable CSS selector that targets the desired HTML element. Regards, Svetoslav Dimitrov Progress Telerik
