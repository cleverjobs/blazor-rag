# Population of EditContext in TelerikForm

## Question

**Pet** asked on 15 Mar 2023

I've made a custom FormItem and I need access to the EditContext. This works, but - is there a simpler way to get access to the EditContext? The Form: <TelerikForm Model="@AWonderfullModel" OnSubmit="@OnSubmitHandler" @ref="@FormRef"> <FormItems> <CascadingValue Name="TheForm" Value="@FormRef"> @foreach (var row in RexFormItems)
{ <DynamicComponent Type="@row.Component" Parameters="@row.Parameter" /> } </CascadingValue> </FormItems>.... </TelerikForm> I populate the FormRef via the CascadingValue and in my CustomControl simple: [ CascadingParameter ] public TelerikForm TheForm { get; set; }

.... protected override void OnParametersSet () {
Model=TheForm.EditContext.Model;
...
} This works well, but we discussed this and there was the Idea, that the Form or the EditContext is reachable in an other way.

## Answer

**Dimo** answered on 16 Mar 2023

Hi Peter, Your approach is valid, however, if you need the Model and not the EditContext, you can pass AWonderfullModel as a cascading value instead of the Form reference. On the other hand, another option is to bind the Form to an EditContext that you create yourself (see online Form example ), and again, pass the EditContext directly instead of the Form reference. Regards, Dimo Progress Telerik

### Response

**Peter** commented on 16 Mar 2023

Thank you very much Dimo. You are right about the "EditContext". My above example is only a small excerpt. As part of the implementation, I not only need the EditContext, but the entire form element. In any case, you have kindly confirmed for me that we can do it this way. Thank you very much and best regards.. Peter
