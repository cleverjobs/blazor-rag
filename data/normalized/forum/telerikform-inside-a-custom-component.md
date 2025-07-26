# TelerikForm inside a custom component

## Question

**Akm** asked on 22 May 2024

I have a custom component which takes RenderFragment and displays it as ChildContent. I'm passing TelerikForm for ChildContent and getting such error: Unhandled exception rendering component: Specified cast is not valid. Here's the custom component: <div class="gg_wizard_step @(IndexInParent !=ParentSection.CurrentStep ? " hidden " : " ")">
<CascadingValue Value="this">
@ChildContent
</CascadingValue>
</div>

@code {
[ Parameter ] public RenderFragment ChildContent { get; set; }

[ CascadingParameter ] public NLWizardSection ParentSection { get; set; }

[ Parameter ] public int IndexInParent { get; set; } protected override void OnInitialized () { base.OnInitialized();

ParentSection.AddChild( this );
}
} Here's the form added to custom component: <NLWizardStep>
<h3>@L[ "What is the name of your resource?" ]</h3>
<TelerikForm Model="@((NameForm)_currentForm)" @ref="NameFormRef" ValidationMessageType="FormValidationMessageType.Inline">
<FormValidation>
<DataAnnotationsValidator></DataAnnotationsValidator>
<CustomValidation></CustomValidation>
</FormValidation>
<FormItems>
<FormItem Field="@nameof(NameForm.Name)"></FormItem>
</FormItems>
<FormButtons></FormButtons>
</TelerikForm>
</NLWizardStep>

## Answer

**Nadezhda Tacheva** answered on 27 May 2024

Hi Akmal, It seems like the error "Specified cast is not valid" might be occurring due to a casting issue with the Model property of the TelerikForm within your custom component. Here are a few things to check and try: Ensure the Model Type Matches: Double-check that _currentForm is indeed of type NameForm at runtime. This error can occur if _currentForm is not the expected type when the form tries to cast it. Cascading Parameters: Since you are using CascadingValue, ensure that all necessary parameters are correctly passed down to the TelerikForm. If there's a mismatch or an incorrect type being cascaded, it could lead to casting issues. Blazor Component Restrictions: Blazor sometimes has specific restrictions or behaviors around rendering fragments and component hierarchies. Make sure that the TelerikForm is compatible with being used within a CascadingValue component. You might want to try a simple test by placing the TelerikForm outside of any custom component to see if it renders without issues. You may also test with an EditForm instead of a TelerikForm to validate if you get the same behavior. If after checking these points the issue persists, I recommend isolating the problem by gradually reducing the complexity of the form or custom component until you identify the specific cause. Regards, Nadezhda Tacheva Progress Telerik
