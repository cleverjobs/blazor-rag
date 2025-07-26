# Refreshing Form Model Data Or Form Component

## Question

**Kol** asked on 28 Aug 2023

Hello, I am currently working on an application that includes a form which exposes certain business logic dependent on if the page the form is contained in was reached alongside an included route parameter or not; if so, the page queries for information that will populate the 'Model' attribute of the Form tag with pre-existing information for updating. If the page is reached without a route parameter, then the form simply displays as blank for the user to fill out a new form. In regards to the Telerik library, I had seen in the documentation for the Telerik Form tag that you can receive a reference for that particular component, which would then expose a "Refresh()" that, presumably, can be used for refreshing the Model data handled by the Form, in case of any changes. I had also assumed that this might work similarly to the TelerikGrid reference 'Rebind()' method in principle, where the data context for the component can be "recontextualized' whenever a change to such data is made. My question then is this; how does one go about calling this method after properly exposing the Form component's reference, and will this particular method work similarly to how the TelerikGrid 'Rebind()' method functions in that it can refresh the data context of the component (i.e, refresh the object that is used and, subsequently, the appropriate FormItems)? Is it possible that this is the wrong approach to accomplishing refreshing data on the Form component, or should I look into a different solution altogether? I have provided a very simple pseudo-code to help assist with explaining my desired question. Thank you in advance for the assistance, I have very much enjoyed using the Telerik library as a whole.

## Answer

**Svetoslav Dimitrov** answered on 31 Aug 2023

Hello Kolton, First of all, I would like to thank you for the kind words regarding our component suite. Now, let's focus on the questions that you have: When is the component reference populated? This is the statement from the Microsoft documentation: "A component reference is only populated after the component is rendered and its output includes ReferenceChild's element. Until the component is rendered, there's nothing to reference. To manipulate component references after the component has finished rendering, use the OnAfterRender or OnAfterRenderAsync methods." This means that the TelerikForm reference will be populated in the OnAfterRender lifecycle hook. I can see that you are using it in the OnParametersSet which is a bit early (this lifecycle hook fires before the OnAfterRender lifecycle event). In your code snippet, the FormRef must be null, thus an exception. If you want to make sure the Form reference is populated properly in the OnParametersSet event you can add a await Task.Delay(20); before using the reference. Now, let me paraphrase the next question: Do I need to call the Refresh method in the OnParametersSet lifecycle hook? In your case, I would say no. Why? - If you are loading the initial data in the OnInitialized lifecycle hook you can override it easily in the OnParametersSetAsync without calling the FormRef.Refresh() method. Below is a code snippet as a validation of the aforementioned. Note that the initial value of the Name property is "From OnInit event", however in the UI, it renders as "From Parameters Set" without calling the FormRef.Refresh() method. The reason is that the OnParametersSet fires after the OnInitialized lifecycle hook. @using System.ComponentModel.DataAnnotations

<TelerikForm Model="@TeamMate" @ref="@FormRef" Width="300px">
<FormValidation>
<DataAnnotationsValidator />
</FormValidation>
</TelerikForm>

@code { private TelerikForm FormRef { get; set; } private Employee TeamMate { get; set; } protected override void OnInitialized ( ) {
TeamMate=new Employee()
{
Name="From OnInit event" }; base.OnInitialized();
} protected override async Task OnParametersSetAsync ( ) { await Task.Delay( 20 );

TeamMate.Name="From Parameters Set";

FormRef.EditContext.Validate();
} public class Employee {
[ Display(AutoGenerateField=false) ] public int Id { get; set; }
[ Required ]
[ MinLength(2, ErrorMessage="{0} should be at least {1} characters." ) ] public string Name { get; set; }
[ Required ] public DateTime? BirthDate { get; set; }
}
} Now, let's focus on the difference between the Form's Refresh and Grid's Rebind methods: Refresh vs Rebind The Form's refresh method will, behind the scenes, call the StateHasChanged() method only for the TelerikForm component, and not for the entire razor page the Form is in. Now the Rebind() - It does a lot more. Calling rebind will: If the OnRead event is manually added to the Grid: Calling Rebind() will execute the entire business logic in the OnRead event handler which leads to refreshing the data and re-rendering the component. If the OnRead is not manually defined: The Rebind() method will execute our internal event that reads the data for the Grid and will, again, refresh the data which leads to the re-rendering of the component. So, the Rebind() method is directly connected to the data operations in the Grid component. On the other hand, the Refresh() method just re-renders the component and is not directly connected to the Model/EditContext of the Form. Conclusion There is not a single "correct approach", however, there are subtle nuances in how the Blazor framework operates when it populates the component references, and in the Refresh and Rebind methods. Let me know if this information helps you move forward and if you have any follow-up questions. Regards, Svetoslav Dimitrov Progress Telerik

### Response

**Kolton** commented on 11 Sep 2023

Dimitrov, This is exactly what I was looking for! I originally had some difficulties with getting the Form resources to populate accordingly as a direct result of not having as much of a grasp on the Blazor lifecycle and how re-rendering works in general in a Blazor context. I have since developed a solution using the mentioned "OnParametersSetAsync" method in the code response. Thank you for taking the time to answer this, it is appreciated.
