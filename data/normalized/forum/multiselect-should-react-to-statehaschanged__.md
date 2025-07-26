# MultiSelect should react to StateHasChanged()

## Question

**Edw** asked on 28 Oct 2020

I have a MultiSelect that is two-way bound to a List<Guid> selectedValues. If selectedValues changes, I expect the MultiSelect to properly reflect the change once StateHasChanged() is called. That is not the case, I have to do something like selectedValues=new List<Guid>(selectedValues) Apparently, creating a new reference triggers the notification and forces the component to redraw itself. This seems very hackish and counterintuitive. All components should check their state when StateHasChanged() is called and determine whether a UI update is necessary.

## Answer

**Marin Bratanov** answered on 29 Oct 2020

Hello Edward, In Blazor, the ParametersSet event of child components is called so they can react to changes in their parameters coming from their parent. The framework calls this event: when a primitive (value) type parameter gets a new value - this is the common case for strings and numbers when the reference to an object type parameter changes - this includes models and collections - and so the MultiSelect Value falls here. For a collection reference to change, you should generally do a "new List<T>(oldCollection)" Thus, this is not about StateHasChanged() - it does not provide a new hook to react to - it is about when and how the framework passes new parameter values to the child components. Regards, Marin Bratanov
