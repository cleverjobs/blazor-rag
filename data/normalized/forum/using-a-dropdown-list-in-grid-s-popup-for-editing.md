# Using a Dropdown List in Grid's Popup for editing

## Question

**ele** asked on 21 Apr 2023

I'm using Telerik Blazor's Grid to show a table. Currently this table contains a column that uses an id that references to a string in another table. Currently the Grid is able to show the string using the following: <GridColumn Field=@nameof(EEOTrainingVM.TrainingType) Title="Testing"> <EditorTemplate> @{
if (context as EEOTrainingVM is not null)
{
Training=context as EEOTrainingVM; <TelerikDropDownList Data="@Trainings" @bind-Value="@Training.TrainingType" TextField="@nameof(LUTRAINING.desc)" ValueField="@nameof(LUTRAINING.code)" Width="100%"> </TelerikDropDownList> }
} </EditorTemplate> <Template> @{
int trainName=(context as EEOTrainingVM).TrainingType; <text> @GetTrainingValue(trainName) </text> } </Template> </GridColumn> I'm running into an issue where when clicking on the Edit button in a row, to show the Edit popup, an exception is thrown - stem.NullReferenceException: Object reference not set to an instance of an object.
at Telerik.Blazor.Extensions.ObjectExtensions.IsEqualTo[T](Object object1, T object2)
at Telerik.Blazor.Components.TelerikDropDownList`2. <MapSelectedItem> b__138_0(ListDataItem item)
at System.Linq.Enumerable.TryGetFirst[TSource](IEnumerable`1 source, Func`2 predicate, Boolean& found)
at System.Linq.Enumerable.FirstOrDefault[TSource](IEnumerable`1 source, Func`2 predicate)
at Telerik.Blazor.Components.TelerikDropDownList`2.MapSelectedItem()
at Telerik.Blazor.Components.TelerikDropDownList`2.OnParametersSetAsync()
at Microsoft.AspNetCore.Components.ComponentBase.CallStateHasChangedOnAsyncCompletion(Task task)
at Microsoft.AspNetCore.Components.ComponentBase.RunInitAndSetParametersAsync()
at Telerik.Blazor.Components.Common.TelerikSelectBase`2.SetParametersAsync(ParameterView parameters)
l and I'm not sure why. The GetTrainingValue helper method is as follows: public string GetTrainingValue(int trainingID) { LUTRAINING match=TrainingType.FirstOrDefault(t=> t.LUTRAINING.code==trainingID); return match !=null ? match.LUTRAINING.desc : "Unknown"; }

## Answer

**Svetoslav Dimitrov** answered on 26 Apr 2023

Hello Jenna, If I understood correctly, you would like to achieve a Foreign Key column in the Telerik UI for Blazor Grid. If I am correct, you can check the Foreign Key Column knowledge-based article where you can find a code snippet together with explanations. Can you take a look at that knowledge-based article and see if it helps you resolve the issue? Regards, Svetoslav Dimitrov Progress Telerik
