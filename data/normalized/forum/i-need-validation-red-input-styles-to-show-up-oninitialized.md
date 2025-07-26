# I Need Validation (Red Input Styles) To Show Up OnInitialized()

## Question

**bil** asked on 14 Oct 2021

When the component is intialized, I need the inputs to display with the red (invalid) classes and such. The validation is in place as when I start to enter, then backspace back to empty it TURNS red, but I need it to be red by default when the form initializes. How do I do this using <TerlerikForm>

## Answer

**Radko** answered on 18 Oct 2021

Hello Billy, You can trigger a validation through EditContext's Validate() method. You can check its API here - EditContext.Validate. For example, taking the demo from the Form Docs as a base, you can introduce an OnAfterRender lifecycle method and call the Validate() method within it(source also attached): protected override void OnAfterRender ( bool firstRender ) { if (firstRender)
{ MyEditContext.Validate(); } base.OnAfterRender(firstRender);
} Alternatively, the component reference provides you with access to the EditContext that the form will generate when you pass a model, thus calling its Validate() method will also work: <TelerikForm ... @ref="@FormReference">
</TelerikForm>

@code { public TelerikForm FormReference { get; set; } protected override void OnAfterRender ( bool firstRender ) { if (firstRender)
{ FormReference.EditContext.Validate(); } base.OnAfterRender(firstRender);
}
...
} Please do not hesitate to reach out in case of any more questions. Thank you! Regards, Radko Stanev
